---
title: "Artikkelien tuonti Hugoon — muistiinpanot"
---

# HTML → Hugo Markdown -konversio

## 1. Konvertoi Pandocilla

```bash
pandoc -f html -t markdown artikkeli.html -o artikkeli.md
```

## 2. Lisää front matter tiedoston alkuun

```yaml
---
title: "Artikkelin otsikko"
date: 2025-09-25
tags: ["ai", "filosofia", "innovointi"]
summary: "Lyhyt kuvaus artikkelilistaa varten."
translationKey: "artikkelin-tunniste"
---
```

Jos artikkelista on sekä fi- että en-versio, käytä samaa
`translationKey`-arvoa molemmissa.

## 3. Pandoc-jäämien siivous (sed)

Aja nämä konvertoituun tiedostoon:

```bash
# Poista {target="_blank"} linkeistä
sed -i 's/{target="_blank"}//g' artikkeli.md

# Poista {target=_blank} (ilman lainausmerkkejä, variaatio)
sed -i 's/{target=_blank}//g' artikkeli.md

# Escaped lainausmerkit \" → "
sed -i 's/\\""/"/g' artikkeli.md

# Escaped heittomerkki \' → '
sed -i "s/\\\\'/'/g" artikkeli.md

# Escaped putki \| → |
sed -i 's/\\|/|/g' artikkeli.md

# Escaped kolme pistettä \... → …
sed -i 's/\\\.\.\./…/g' artikkeli.md
```

Tai kaikki kerralla yhdellä komennolla:

```bash
sed -i \
  -e 's/{target="_blank"}//g' \
  -e 's/{target=_blank}//g' \
  -e 's/\\""/"/g' \
  -e "s/\\\\'/'/g" \
  -e 's/\\|/|/g' \
  -e 's/\\\.\.\./…/g' \
  artikkeli.md
```

## 4. Otsikkotasot

Hugo renderöi `title`-kentän h1:nä, joten artikkelin sisällä:

- Pääotsikot: `##` (h2)
- Alaotsikot: `###` (h3)
- Ala-alaotsikot: `####` (h4)

Jos Pandoc tuotti `###`-pääotsikot, nosta ne:

```bash
# Muuta ### → ## (pääotsikot, esim. "### I. Johdanto")
# HUOM: tee käsin tai varovasti, älä muuta alaotsikoita
sed -i 's/^### \([IVX]\)/## \1/g' artikkeli.md
```

## 5. Kuvat

1. Kopioi kuvat kansioon `static/images/`
2. Päivitä polut artikkelissa:

```markdown
![Kuvateksti](/images/kuvan-nimi.png)
```

## 6. Erityismuotoilut

Blockquote (esim. lainaukset, runot):

```markdown
> *Kursivoitu lainaus tähän...*
```

Horisontaalinen viiva (osioiden välissä):

```markdown
---
```

Huom: Pandoc tuottaa usein pitkän viivan `--------...--------`,
joka toimii Hugossa, mutta `---` on siistimpi.

## 7. Sijoita valmis tiedosto

```bash
# Suomenkielinen artikkeli
cp artikkeli.md content/fi/posts/

# Englanninkielinen artikkeli
cp artikkeli.md content/en/posts/
```

## 8. Tarkista ja julkaise

```bash
# Esikatselu
hugo server -D

# Julkaise
./deploy.sh
```

## Pikaohje: uusi artikkeli tyhjästä

```bash
hugo new fi/posts/uusi-artikkeli.md
```

Tämä luo valmiin pohjan `archetypes/default.md`-mallista.
Poista `draft: true` kun artikkeli on valmis julkaistavaksi.
