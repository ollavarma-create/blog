#!/usr/bin/env bash
##
## slug-check.sh — Detect content layout issues that produce nested
## or unintended URLs.
##
## Run from the project root:
##     ./tools/slug-check.sh
##
## Reports three classes of issue per leaf bundle (a directory that
## contains an index.md or _index.md):
##
##   1. SPACE        Directory name contains spaces. Hugo will slugify
##                   them to multiple hyphens (e.g. "Part 1" becomes
##                   "part---1"), producing ugly URLs.
##
##   2. SLUG/DIR     Front matter has an explicit `slug:` value that
##                   does NOT match the slugified directory name. This
##                   often produces TWO URLs for the same content, with
##                   the directory-derived path containing an empty
##                   index.html and the slug-derived path containing
##                   the real content. Either drop the `slug:` line or
##                   rename the directory to match it.
##
##   3. SPECIALS     Directory name contains characters Hugo will mangle
##                   (em dashes, smart quotes, parentheses). These
##                   render but produce inconsistent URLs across builds.
##
## No files are modified — this is a read-only audit tool.
##

set -euo pipefail

CONTENT_DIR="${CONTENT_DIR:-content}"

if [[ ! -d "$CONTENT_DIR" ]]; then
    echo "Error: $CONTENT_DIR not found. Run this from the project root." >&2
    exit 1
fi

# ANSI colours when stdout is a terminal.
if [[ -t 1 ]]; then
    BOLD=$'\033[1m'; RED=$'\033[31m'; YELLOW=$'\033[33m'
    GREEN=$'\033[32m'; DIM=$'\033[2m'; RESET=$'\033[0m'
else
    BOLD=''; RED=''; YELLOW=''; GREEN=''; DIM=''; RESET=''
fi

# Naive slugifier matching Hugo's default behaviour for ASCII inputs.
# - Lowercase
# - Strip a small set of punctuation
# - Collapse runs of non-alphanum/dash to single dashes
# Note: Hugo's Unicode handling is more nuanced; this is a best-effort.
slugify() {
    printf '%s' "$1" \
        | tr '[:upper:]' '[:lower:]' \
        | sed -E 's/[\(\)\[\]\.,!\?:;\"]+//g' \
        | sed -E 's/[^a-z0-9]+/-/g' \
        | sed -E 's/^-+|-+$//g'
}

# Extract a TOML/YAML scalar `slug:` (or `slug =`) from front matter.
# Strategy: look at the first 30 lines (front matter always lives at the
# very top), grep the first matching `slug` declaration, strip quoting.
# Portable across GNU and BSD utilities.
#
# IMPORTANT: We MUST swallow grep's "no match" exit code. Otherwise, with
# `set -o pipefail` enabled at the top of this script, a slug-less file
# would crash the whole loop on the very first lookup.
extract_slug() {
    local file="$1"
    {
        head -30 "$file" 2>/dev/null \
            | grep -E '^[[:space:]]*slug[[:space:]]*[:=]' \
            | head -1 \
            | sed -E 's/^[[:space:]]*slug[[:space:]]*[:=][[:space:]]*"?([^"#]*)"?[[:space:]]*$/\1/' \
            | sed -E 's/[[:space:]]+$//'
    } || true
}

# Counters
issues_space=0
issues_slug=0
issues_special=0
checked=0

echo "${BOLD}Scanning $CONTENT_DIR for slug/URL issues…${RESET}"
echo

# Iterate every leaf-bundle index.md (depth >= 3 keeps us inside posts/)
# Process substitution avoids losing variables in a subshell.
while IFS= read -r -d '' indexfile; do
    checked=$((checked + 1))
    dir=$(dirname "$indexfile")
    dirname=$(basename "$dir")
    relpath="${dir#./}"

    # 1. Spaces in directory name
    if [[ "$dirname" == *" "* ]]; then
        issues_space=$((issues_space + 1))
        echo "${YELLOW}SPACE${RESET}    ${BOLD}$relpath${RESET}"
        echo "         ${DIM}Directory name contains spaces — produces multi-hyphen URLs.${RESET}"
        echo "         ${DIM}Suggested rename: $(slugify "$dirname")${RESET}"
        echo
    fi

    # 2. Special characters Hugo will mangle.
    # Bash regex character classes are unreliable for multi-byte UTF-8;
    # case patterns with glob `*X*` work reliably across locales.
    case "$dirname" in
        *—*|*–*|*“*|*”*|*’*|*‘*|*\(*|*\)*)
            issues_special=$((issues_special + 1))
            echo "${YELLOW}SPECIALS${RESET} ${BOLD}$relpath${RESET}"
            echo "         ${DIM}Directory name has em-dashes, smart quotes, or parentheses.${RESET}"
            echo "         ${DIM}Suggested rename: $(slugify "$dirname")${RESET}"
            echo
            ;;
    esac

    # 3. Front-matter slug vs directory slug mismatch
    fm_slug=$(extract_slug "$indexfile")
    if [[ -n "$fm_slug" ]]; then
        dir_slug=$(slugify "$dirname")
        if [[ "$fm_slug" != "$dir_slug" ]]; then
            issues_slug=$((issues_slug + 1))
            echo "${RED}SLUG/DIR${RESET} ${BOLD}$relpath${RESET}"
            echo "         ${DIM}front-matter slug:${RESET} $fm_slug"
            echo "         ${DIM}directory slug   :${RESET} $dir_slug"
            echo "         ${DIM}Fix by removing the slug from front matter${RESET}"
            echo "         ${DIM}OR renaming the directory to match.${RESET}"
            echo
        fi
    fi

done < <(find "$CONTENT_DIR" -mindepth 3 -name 'index.md' -print0 2>/dev/null)

# Summary
total=$((issues_space + issues_slug + issues_special))
echo "${BOLD}─── Summary ───${RESET}"
printf "  Bundles scanned : %d\n" "$checked"
printf "  Spaces in name  : %d\n" "$issues_space"
printf "  Slug/dir mismatch: %d\n" "$issues_slug"
printf "  Special chars   : %d\n" "$issues_special"
echo

if [[ $total -eq 0 ]]; then
    echo "${GREEN}No issues found.${RESET}"
    exit 0
else
    echo "${YELLOW}$total issue(s) found.${RESET} See output above."
    exit 1
fi
