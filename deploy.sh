#!/bin/bash
##
## deploy.sh — Commit source changes to main, build, and push to Codeberg Pages
##
## Usage: ./deploy.sh [commit message]
##
## What this does:
##   1. Commits any uncommitted source changes to the main branch
##   2. Builds the site with Hugo
##   3. Pushes the built output to the `pages` branch (Codeberg Pages)
##

set -euo pipefail

REMOTE="origin"
if [ -n "${CODEBERG_TOKEN:-}" ]; then
    REMOTE_URL="https://${CODEBERG_TOKEN}@codeberg.org/hiltsu/pages.git"
else
    # Fallback: kysy token interaktiivisesti jos ei ole env-varia
    read -rsp "🔑 Syötä Codeberg-token: " CODEBERG_TOKEN
    echo
    REMOTE_URL="https://${CODEBERG_TOKEN}@codeberg.org/hiltsu/pages.git"
fi
PAGES_BRANCH="pages"
BUILD_DIR="public"

MSG="${1:-Deploy $(date +%Y-%m-%d\ %H:%M)}"

# ---------------------------------------------------------------------------
# Step 1: Save source changes to main first
# ---------------------------------------------------------------------------

echo "==> Checking for uncommitted source changes..."

if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "==> Committing source changes to main..."
    git add -A
    git commit -m "$MSG"
    git push "$REMOTE" main
    echo "==> Source pushed to main."
else
    echo "    Nothing to commit on main — working tree is clean."
fi

# ---------------------------------------------------------------------------
# Step 2: Build
# ---------------------------------------------------------------------------

echo "==> Building site..."
hugo --minify

# ---------------------------------------------------------------------------
# Step 3: Push built output to pages branch
#
# The build dir is a separate orphan repo pointing at the same remote.
# We re-initialise it each time so there is no stale state.
# ---------------------------------------------------------------------------

echo "==> Deploying to pages branch: $MSG"

REMOTE_URL="$(git remote get-url "$REMOTE")"

cd "$BUILD_DIR"

# Initialise (or re-use) the embedded git repo.
if [ ! -d ".git" ]; then
    git init
    git remote add "$REMOTE" "$REMOTE_URL"
else
    # Make sure the remote URL is still correct (e.g. after a repo rename).
    git remote set-url "$REMOTE" "$REMOTE_URL"
fi

git checkout -b "$PAGES_BRANCH" 2>/dev/null || git checkout "$PAGES_BRANCH"

git add -A
if git commit -m "$MSG" 2>/dev/null; then
    echo "    Committed changes for deploy."
else
    echo "    No new changes to commit, but continuing to ensure remote sync..."
fi

# Korvaa retry-silmukka tällä (exponential backoff):
MAX_RETRIES=5
RETRY_COUNT=0
while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if git push "$REMOTE" "$PAGES_BRANCH"; then
        break
    fi
    RETRY_COUNT=$((RETRY_COUNT + 1))
    if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
        WAIT_TIME=$((2 ** RETRY_COUNT))  # 2s, 4s, 8s, 16s...
        echo "⚠️ Push epäonnistui, odotetaan ${WAIT_TIME}s ja yritetään uudelleen ($RETRY_COUNT/$MAX_RETRIES)..."
        sleep $WAIT_TIME
    else
        echo "❌ Push epäonnistui $MAX_RETRIES kertaa. Tarkista yhteys tai Codebergin status."
        exit 1
    fi
done


echo "==> Done! Site live at: https://hiltsu.codeberg.page"
