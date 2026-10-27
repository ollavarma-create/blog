---
title: "LLM-aikakauden tiedekriisi: konfabulaatio, toistettavuus ja tieteen rapautuminen"
translation-key: "tieteen-eroosio-llm"
date: 2026-05-25
draft: false
tags:
  - tekoäly
  - tiede
  - konfabulaatio
  - LLM
  - toistettavuuskriisi
  - avoin tiede
categories:
  - tekoäly
  - tutkimus
  - tulevaisuus
description: "Miten tieteellinen toistokriisi ja suurten kielimallien konfabulaatio kietoutuvat yhteen, ja millä uusilla menetelmillä tieteen luotettavuus voidaan palauttaa?"
summary: "Tiede on murroksessa: toistokriisi ja LLM-konfabulaatio uhkaavat tiedon luotettavuutta. Tutustumme ongelman juurisyihin ja esittelemme ratkaisuja kuten Proof-Carrying Papers ja Schrödinger’s Machine."
---

Raportin AI-avustaja: Qwen3.6-Plus Deep Research.


# **1. Johdanto**

Tämä raportti tarkastelee tieteellisen tiedon luotettavuuden heikkenemistä, ilmiötä, jota kutsutaan yhä useammin *toistokriisiksi (replication crisis)*. Analyysi käsittelee kriisin keskeisiä juurisyitä menetelmällisiä ongelmia, tutkimusvinoumia (bias) ja akateemisia kannustinjärjestelmiä sekä uutta, nopeasti kasvavaa uhkaa: suurten kielimallien (**large language models, LLM**) tuottamaa **konfabulaatiota (hallucination)**.

Raportin tavoitteena on esittää selkeä ja jäsennelty kokonaiskuva siitä, miten nämä kaksi ilmiötä kietoutuvat toisiinsa ja muodostavat yhdessä merkittävän haasteen modernille tieteelle. Teksti esittelee myös uusia ratkaisumalleja, kuten *Proof-Carrying Papers* -lähestymistavan ja *Schrödinger's Machine* -konseptin, jotka pyrkivät palauttamaan tieteellisen tiedon läpinäkyvyyden ja replikoitavuuden.

Kokonaisuutena raportti tarjoaa analyyttisen, tasapainoisen ja helposti lähestyttävän katsauksen tieteellisten menetelmien nykytilaan ja tulevaisuuden haasteisiin.

# 2. Toistokriisin juurisyyt ja tutkimusvinoumat

Tieteellinen toistokriisi ei ole yksittäisten tutkimusten epäonnistumisten summa, vaan laaja ja syvälle juurtunut ongelma, joka koskee tieteellisen tiedon perusteita. Monilla aloilla aiemmin julkaistuja tuloksia ei pystytä toistamaan, mikä heikentää luottamusta koko tutkimusjärjestelmään. Taustalla vaikuttaa monimutkainen kokonaisuus menetelmällisiä käytäntöjä, organisaatiokulttuureja ja inhimillisiä vinoumia.

## 2.1 Kyseenalaiset tutkimuskäytännöt (QRPs)

Yksi keskeinen toistokriisin taustatekijä on *kyseenalaisten tutkimuskäytäntöjen (questionable research practices, QRP)* laaja käyttö. Näitä ovat esimerkiksi:

- **p-arvojen manipulointi (p-hacking)**: tutkija muokkaa analyysia tai dataa niin kauan, että tulos muuttuu tilastollisesti merkitseväksi (p \< 0,05).

- **hypoteesien muotoilu jälkikäteen (HARKing)**: hypoteesi kirjoitetaan vasta tulosten näkemisen jälkeen, jolloin tutkimus esitetään virheellisesti ennustavana eikä selittävänä.

Nämä käytännöt tekevät tutkimustuloksista näennäisen vakuuttavia, mutta metodologisesti epäluotettavia. 

Vaikka bayesilaiset menetelmät voivat vähentää joitakin tilastollisen päättelyn ongelmia, ne eivät estä HARKingia tai bayesilaista "p-hackingia": myös posteriorijakaumia voidaan manipuloida.

## 2.2 Inhimilliset vinoumat (bias)

Menetelmälliset ongelmat kietoutuvat tiiviisti psykologisiin vinoumiin. Keskeisin näistä on **vahvistusvinouma (confirmation bias)**, eli taipumus etsiä ja tulkita tietoa tavalla, joka tukee omia ennakkokäsityksiä.

Vahvistusvinouma vaikuttaa tutkimusprosessin kaikkiin vaiheisiin, tutkimuskysymyksen valinnasta analyysiin ja tulosten tulkintaan. Myös vertaisarvioijat ja lukijat ovat sille alttiita, mikä vahvistaa vinoutuneiden tulosten päätymistä julkaisuiksi.

Toinen merkittävä vinouma on **julkaisuvinouma (publication bias)**: positiiviset ja "uutisarvoiset" tulokset julkaistaan huomattavasti todennäköisemmin kuin negatiiviset tai neutraalit tulokset.

Tämä johtaa systemaattisesti optimistisempaan kuvaan todellisuudesta ja vääristää meta-analyysejä, jotka perustuvat jo valmiiksi vinoutuneeseen aineistoon.

## 2.3 Akateeminen kannustinjärjestelmä

"Julkaise tai kuole" -kulttuuri ohjaa tutkijoita tuottamaan nopeasti julkaistavia tuloksia, mikä kannustaa riskialttiisiin menetelmävalintoihin ja QRPs-käytäntöihin. Urakehitys, rahoitus ja maine sidotaan usein julkaisujen määrään, ei niiden laatuun tai replikoitavuuteen.

Tämä kannustinjärjestelmä on havaittu ongelmalliseksi useilla aloilla, kuten psykologiassa, sosiaalitieteissä ja tietojenkäsittelytieteessä.

## 2.4 Seuraukset: epistemologinen eroosio

Kun tutkimusmenetelmät ovat joustavia, vinoumat vahvoja ja kannustimet vääristyneitä, tieteellinen tieto alkaa rapautua. Toistettavuus, tieteellisen menetelmän peruspilari, heikkenee, ja tieteellinen prosessi alkaa muistuttaa rituaalia, ei luotettavaa tiedonhankintaa.

Tätä kehitystä on kuvattu käsitteillä:

-   **epistemologinen katoaminen (epistemic decay)**

-   **luottamuksen romahtaminen (collapse of trust)**

Vaikka avoimen tieteen käytännöt ja esirekisteröinnit ovat parantaneet tilannetta, ongelma on syvä ja vaatii kulttuurista muutosta, painopisteen siirtämistä määrästä laatuun.

# 3. Suurten kielimallien konfabulaatio: järjestelmätason uhka tieteelle

Vaikka toistokriisi on syntynyt pitkän ajan kuluessa ja juontaa juurensa ihmisten tekemiin menetelmällisiin ja kulttuurisiin valintoihin, viime vuosien nopein ja voimakkain kiihdyttäjä on ollut suurten kielimallien (*large language models, LLM*) laaja käyttöönotto tieteellisessä työssä. LLM-malleja käytetään kirjoittamisen tukena, tiivistämisessä, koodin tuottamisessa ja jopa tutkimusideoiden generoinnissa. Samalla ne ovat tuoneet mukanaan uuden, rakenteellisen ongelman: *konfabulaation (hallucination)*.

## 3.1 Konfabulaation luonne

Konfabulaatio tarkoittaa tilannetta, jossa LLM tuottaa kielellisesti sujuvaa, loogiselta vaikuttavaa mutta tosiasiatasolla virheellistä tai täysin keksittyä sisältöä. Malli voi esimerkiksi:

-   kuvata yksityiskohtaisesti kokeita, joita ei ole koskaan tehty

-   viitata tutkimuksiin, joita ei ole olemassa

-   esittää tieteellisiä tuloksia, joilla ei ole todellista lähdettä

Ilmiö muistuttaa neurologista konfabulaatiota, jossa ihminen täydentää muistinsa aukkoja uskottavalta kuulostavalla fiktiolla. LLM:lle tämä ei ole virhe vaan seuraus sen rakenteesta: malli ei *tiedä*, mitä se ei tiedä. Se tuottaa todennäköisintä jatkoa tekstille, ei varmennettua tietoa.

Konfabulaatio ei ole satunnaista. Tutkimukset osoittavat, että:

-   epäselvät tai huonosti muotoillut ohjeet lisäävät hallusinaatioita

-   mallit eivät kykene arvioimaan omaa tietämystään

-   mallit täydentävät puuttuvaa tietoa "uskottavalla fiktiolla"

Tämä tekee konfabulaatiosta järjestelmätason riskin, ei yksittäisen käyttäjän virheen.

## 3.2 LLM:t perivät ja vahvistavat ihmisen vinoumia

Koska LLM:t koulutetaan valtavilla tekstikorpuksilla, ne perivät kaikki ihmisen tuottaman tiedon vinoumat (bias). Näitä ovat esimerkiksi:

-   **vahvistusvinouma (confirmation bias)**

-   **positiivisuusharha (positivity bias)**

-   **julkaisuvinouma (publication bias)**

Jos koulutusdata koostuu pääosin positiivisista tuloksista, malli oppii "maailman", jossa kokeet onnistuvat lähes aina. Tämän seurauksena LLM voi tuottaa:

-   yleistettyjä, liian optimistisia tulkintoja

-   vääristyneitä tiivistelmiä

-   keksittyjä positiivisia tuloksia

Tämä luo itseään vahvistavan kierteen: vinoutunut kirjallisuus → vinoutunut malli → vielä vinoutuneempi uusi sisältö.

## 3.3 Mallin omat vinoumat

LLM:t eivät ainoastaan peri vinoumia, niillä on myös omia, rakenteesta syntyviä vinoumia:

- **yligeneralointi (overgeneralization)**: malli esittää rajalliset tulokset yleispätevinä

- **viittausvinouma (citation bias)**: malli suosii tunnettuja, paljon viitattuja lähteitä

- **lähdevinouma (source bias)**: LLM‑tuotettu teksti saa hakujärjestelmissä etulyöntiaseman ihmisen kirjoittamaan verrattuna

Nämä vinoumat vahvistavat jo olemassa olevia ongelmia ja vaikeuttavat uusien, epäsuosittujen tai haastavien tutkimuslinjojen esiin pääsyä.

## 3.4 Järjestelmätason vaikutus tieteeseen

LLM‑konfabulaatio ei ole vain yksittäisten virheiden lähde, se uhkaa tieteellisen tiedon koko rakennetta. Kun tutkijat käyttävät LLM:iä:

- kirjallisuuden tiivistämiseen → malli voi vääristää alkuperäisiä tuloksia

- artikkelien kirjoittamiseen → malli voi keksiä väitteitä ja viittauksia

- tutkimusideoiden generointiin → malli voi tuottaa "tieteelliseltä kuulostavaa" fiktiota

Tämä vaarantaa tieteellisen menetelmän perusperiaatteet:

-   **replikoitavuus**

-   **tarkistettavuus**

-   **läpinäkyvyys**

Kun tieteellisen työn loppuvaiheita automatisoidaan työkalulla, joka tuottaa uskottavaa mutta epäluotettavaa sisältöä, koko tutkimusketju altistuu virheille.

LLM:t voivat siis toimia *kriisin moottoreina*: ne eivät ainoastaan lisää virheitä, vaan vahvistavat ja kiihdyttävät jo olemassa olevia rakenteellisia ongelmia.

# 4. Valheellisten viittausten leviäminen: konfabulaation vakavin muoto

Konfabulaatio (*hallucination*) on suurten kielimallien (*large language models, LLM*) tunnettu ongelma, mutta sen vaarallisin ja pitkäkestoisin muoto on valheellisten *viittausten generointi*. Tämä tarkoittaa, että malli tuottaa tieteellisiä viitteitä, jotka näyttävät täysin aidoilta, mutta joita ei ole koskaan julkaistu. Ilmiö ei ole marginaalinen, vaan järjestelmätason uhka tieteellisen tiedon luotettavuudelle ja pitkäaikaiselle säilyvyydelle.

## 4.1 Miksi viittaukset ovat erityisen vaarallisia

Valheellisten viittausten ongelma ei rajoitu yksittäisiin virheisiin. Se vaikuttaa suoraan tieteellisen menetelmän ytimeen:

- **replikoitavuuteen**: tutkimusta ei voi tarkistaa, jos lähde ei ole olemassa

- **tiedon kumuloitumiseen**: virheelliset viitteet jäävät osaksi kirjallisuutta

- **tieteelliseen synkronointiin**: myöhemmät tutkimukset rakentuvat fiktiivisen tiedon varaan

Kun tällaiset viittaukset päätyvät julkaistuihin artikkeleihin, ne "saastuttavat" tieteellistä tietokantaa pysyvästi. Tämä eroaa tavallisista virheistä: konfabuloitu viite ei ole vain väärä, se on *keksitty*, eikä sitä voi jäljittää tai korjata ilman manuaalista auditointia.

## 4.2 Ilmiön laajuus: miljoonia valheellisia viitteitä

Useat laajat auditoinnit ovat osoittaneet, että ongelma on kasvanut nopeasti LLM‑mallien yleistymisen myötä:

- arXiv-auditoinneissa on löydetty **miljoonia** valheellisia viittauksia

- yhdessä tutkimuksessa 2,5 miljoonan paperin ja 111 miljoonan viittauksen analyysi paljasti **146 000** täysin olematonta viitettä

- PubMed-auditoinneissa arvioitiin, että **1/200** vuoden 2026 julkaisuista sisälsi konfabuloituja viitteitä

- yli **98 %** valheellisia viitteistä jäi pysyvästi tietokantoihin ilman korjausta

Nämä luvut osoittavat, että kyse ei ole yksittäisistä lipsahduksista vaan rakenteellisesta ongelmasta, joka leviää nopeasti.

## 4.3 Miksi viitteet ovat niin uskottavia

LLM-mallit osaavat tuottaa viitteitä, jotka näyttävät täysin aidoilta:

-   oikeanlaiset tekijälistat

-   uskottavat vuosiluvut

-   olemassa olevien lehtien nimet

-   jopa realistiset DOI-tunnukset

Ongelma on, että nämä viitteet *eivät johda mihinkään*. Ne voivat sisältää:

-   URL-osoitteita, joita ei löydy arkistoista

-   olemassa olevien artikkelien nimiä, mutta väärillä sivunumeroilla

-   yhdistelmiä oikeista tekijöistä ja keksityistä otsikoista

Tämä tekee niiden tunnistamisesta vaikeaa, etenkin, kun ne on upotettu muuten hyvin kirjoitettuun tekstiin.

Tunnettu tapaus oli Springer Naturen julkaisema koneoppimisen kirja, joka jouduttiin vetämään pois markkinoilta, koska se sisälsi suuren määrän täysin keksittyjä viitteitä.

## 4.4 Mistä ongelma syntyy

Valheellisten viittausten syntyyn vaikuttavat kolme keskeistä tekijää:

### 1. Koulutusdata on vinoutunutta

LLM oppii viittausten muodon ja rakenteen, mutta ei niiden todellista olemassaoloa. Jos koulutusdata sisältää vinoumia (esim. positiivisuusharhaa), malli oppii tuottamaan samanlaisia vinoutuneita viitteitä.

### 2. Käyttöohjeet ovat usein huonosti muotoiltuja

Pyynnöt tyyliin "lisää viitteet" tai "anna lähteet" johtavat mallin täydentämään aukot fiktiolla, koska se ei voi tarkistaa viitteiden todellisuutta.

### 3. LLM ei pysty verifioimaan viitteitä

Malli ei tarkista:

-   onko artikkeli olemassa

-   onko DOI oikea

-   vastaako viite todellista julkaisua

Se tuottaa vain todennäköisimmän näköisen viitteen.

Tämä luo itseään vahvistavan verkoston: LLM oppii valheellisia viitteitä → tuottaa uusia → nämä päätyvät koulutusdataan → malli oppii ne uudelleen.

## 4.5 Vaikutukset tieteeseen

Valheellisten viittausten leviäminen aiheuttaa useita vakavia seurauksia:

- **tieteellinen tarkistettavuus heikkenee**: lähteitä ei voi varmentaa

-   **tutkimus rakentuu fiktiiviselle perustalle**

- **nuoret tutkijat ovat erityisen haavoittuvia**: he luottavat LLM-työkaluihin ilman kokemusta tunnistaa virheitä

- **tieteellinen historia vääristyy**: fiktiiviset viitteet jäävät pysyviksi osiksi kirjallisuutta

Tämä on yksi vakavimmista uhista tieteellisen tiedon kumuloitumiselle.

## 4.6 Ensimmäiset ratkaisuyritykset

Tieteellinen yhteisö on alkanut kehittää työkaluja ongelman torjumiseksi:

- **CiteAudit**: tarkistaa viitteet verkkovälimuisteja ja tietokantoja vasten

-   **GPTZero**: tunnistaa LLM‑tuotettuja viitteitä

- **LLM**‑**käytön dokumentointi**: ehdotus, että jokaisen artikkelin metodiosiossa tulisi ilmoittaa, missä vaiheissa LLM:iä on käytetty

Nämä ovat kuitenkin korjaavia, eivät ennaltaehkäiseviä ratkaisuja. Todellinen ratkaisu vaatii:

-   avoimen datan ja koodin pakollista julkaisemista

-   läpinäkyviä työprosesseja

- uusia julkaisumalleja, jotka estävät konfabulaation pääsyn tieteelliseen kirjallisuuteen

# 5. Proof-Carrying Papers (PCP): replikoitavuuden uudelleenmäärittely

Tieteellisen tiedon rapautuminen ja LLM‑konfabulaation aiheuttamat riskit ovat synnyttäneet tarpeen uudelle julkaisumallille, joka palauttaa läpinäkyvyyden ja replikoitavuuden tieteellisen menetelmän ytimeen. Yksi lupaavimmista ratkaisuista on *Proof-Carrying Papers (PCP)* ‑malli. Se ehdottaa siirtymistä perinteisestä, staattisesta artikkelimuodosta kohti dynaamista, tarkistettavaa ja avoimesti todennettavaa julkaisuprosessia.

## 5.1 PCP:n perusidea

PCP-mallissa jokaisen tieteellisen artikkelin mukana julkaistaan automaattisesti tuotettu *todistus*,koneellisesti generoitu, täydellinen ja läpinäkyvä kuvaus siitä, miten tulokset on saatu. Todistus sisältää:

-   käytetyn datan versionumerot

-   käytetyn mallin tai LLM:n version ja hyperparametrit

-   koko analyysikoodin

-   kaikki parametrit, asetukset ja laskentapolut

Tämä tekee artikkelista *tarkistettavan järjestelmän*, ei pelkkää narratiivista tekstiä. Tutkija voi "ajaa artikkelin uudelleen" ja varmistaa, että tulokset ovat toistettavissa täsmälleen samoilla asetuksilla.

## 5.2 Miten PCP ratkaisee nykyiset ongelmat

### 1. Replikoitavuus ei ole enää vapaaehtoista

Nykyisessä järjestelmässä replikoitavuus riippuu tutkijoiden hyvästä tahdosta ja datan saatavuudesta. PCP tekee replikoitavuudesta sisäänrakennetun ominaisuuden: ilman täydellistä todistusta artikkelia ei voi julkaista.

### 2. QRPs-käytännöt paljastuvat automaattisesti

Koska kaikki analyysivaiheet ovat näkyvissä:

-   p-arvojen manipulointi (p-hacking)

-   hypoteesien muotoilu jälkikäteen (HARKing)

-   epäselvät analyysipolut

...eivät enää pysy piilossa narratiivin sisällä.

### 3. LLM**‑**konfabulaatio voidaan eristää

Jos LLM tuottaa virheellisen viittauksen tai väitteen, se näkyy todistuksessa:

-   virheellinen koodipolku

-   puuttuva data

-   epäyhteensopiva lähde

Virhe voidaan poistaa ilman, että koko tutkimus hylätään.

### 4. Avoin tiede toteutuu käytännössä

PCP tekee avoimesta datasta ja avoimesta koodista pakollisia. Ilman niitä todistusta ei voi muodostaa.

## 5.3 PCP käytännössä

PCP ei ole pelkkä teoreettinen idea. Useilla aloilla on jo kehitetty prototyyppejä:

- materiaalitieteessä LLM‑pohjaisia järjestelmiä käytetään mallien ennusteiden validointiin

- agenttipohjaisissa malleissa (ABM) PCP‑tyylinen lähestymistapa auttaa ratkaisemaan replikaatio-ongelmia

- laskennallisissa tieteissä on kehitetty järjestelmiä, jotka generoivat automaattisia todisteita analyysiputkista

Nämä esimerkit osoittavat, että PCP on toteutettavissa nykyisillä teknologioilla.

## 5.4 Haasteet ja vaatimukset

PCP vaatii merkittäviä muutoksia tieteelliseen infrastruktuuriin:

-   uusia työkaluja todistusten automaattiseen generointiin

-   julkaisujärjestelmien uudistamista

- arviointiprosessin laajentamista narratiivista todistuksen tarkastamiseen

- kulttuurista muutosta: prosessin laatu tärkeämmäksi kuin tuloksen "uutisarvo"

Silti PCP:n ydinajatus on voimakas: *tiede ei ole vain tuloksia, vaan prosessi*. PCP tekee tästä prosessista näkyvän, tarkistettavan ja luotettavan.

# 6. Schrödingerin kone: dynaaminen ja epävarmuutta mallintava tiedon tuottaminen

Proof-Carrying Papers (PCP) ‑malli tarjoaa konkreettisen ratkaisun replikoitavuuden ongelmaan, mutta se ei yksin riitä korjaamaan tieteellisen tiedon syvempää ongelmaa: *epävarmuuden* käsittelyä. Tiede ei koskaan tuota absoluuttisia totuuksia, vaan aina todennäköisyyksiä ja arvioita. Tästä lähtökohdasta nousee visio *Schrödingerin koneesta*, järjestelmästä, joka ei tuota yksittäisiä väitteitä, vaan eksplisiittisesti mallintaa epävarmuutta ja tiedon epätäydellisyyttä.

## 6.1 Epävarmuus tieteellisen tiedon ytimessä

Tieteellinen menetelmä ei koskaan tarjoa varmoja vastauksia. Jokainen tulos on:

-   ehdollinen

-   rajallinen

-   epävarma

-   altis päivittymiselle

Schrödingerin kone tekee tästä periaatteesta näkyvän. Sen sijaan, että järjestelmä antaisi yhden väitteen ("X on totta"), se tuottaa:

-   todennäköisyysarvion

-   epävarmuusvälin

-   perustelun epävarmuuden lähteille

Esimerkiksi:

"Tämä väite on todennäköisesti totta (80 %), mutta epävarmuus on korkea, koska koulutusdata on rajallista tässä aiheessa."

Tämä on lähempänä todellista tieteellistä päättelyä kuin nykyiset LLM‑mallit, jotka antavat varmoja vastauksia myös silloin, kun niiden pitäisi olla epävarmoja.

## 6.2 Miten Schrödingerin kone toimii

Schrödingerin kone ei ole vain LLM, vaan kokonainen arkkitehtuuri, joka sisältää:

-   **epävarmuuden kvantifioinnin (uncertainty quantification)**

- **mallin oman tietämyksen arvioinnin (self**‑**knowledge estimation)**

-   **todennäköisyysjakaumien tuottamisen**

-   **läpinäkyvät perustelut epävarmuudelle**

Tämä tarkoittaa, että järjestelmä:

-   tietää, milloin se ei tiedä

-   ei täytä aukkoja fiktiolla

-   ei vahvista väitteitä, joille ei ole riittävää evidenssiä

- ei konfabuloidu, koska se ei yritä olla varma silloin, kun varmuutta ei ole

Toisin sanoen Schrödingerin kone ratkaisee konfabulaation juurisyyn: mallin kyvyttömyyden arvioida omaa tietämystään.

## 6.3 Hyödyt tieteelliselle työlle

Schrödingerin koneen käyttöönotto toisi useita etuja:

### 1. Vinoumien vaikutus heikkenee

Koska järjestelmä ei vahvista väitteitä, joista se on epävarma, vahvistusvinouma (confirmation bias) ja positiivisuusharha (positivity bias) eivät pääse dominoimaan.

### 2. Konfabulaatio vähenee radikaalisti

Malli ei keksi lähteitä tai tuloksia, koska se ei yritä täyttää aukkoja varmuudella.

### 3. Tieteellinen vuorovaikutus muuttuu realistisemmaksi

Käyttäjä ei saa "totuutta", vaan:

-   todennäköisyysjakauman

-   epävarmuusvälin

-   perustelun epävarmuudelle

Tämä vastaa sitä, miten tutkijat oikeasti ajattelevat.

### 4. Parempi päätöksenteko

Epävarmuuden eksplisiittinen mallinnus on kriittistä esimerkiksi:

-   simulointitutkimuksessa

-   riskianalyyseissä

-   lääketieteellisessä päätöksenteossa

-   politiikkasuosituksissa

Schrödingerin kone tekee tämän automaattiseksi.

## 6.4 Suhde PCP‑malliin

PCP ja Schrödingerin kone täydentävät toisiaan:

-   **PCP** varmistaa *replikoitavuuden* ja *läpinäkyvyyden*

-   **Schrödingerin kone** varmistaa *epävarmuuden mallinnuksen* ja
    *konfabulaation minimoinnin*

Yhdessä ne muodostavat vision tulevaisuuden tieteestä:

-   avoin

-   tarkistettava

-   itsekorjaava

-   epävarmuutta kunnioittava

-   konfabulaatiolta suojattu

---

## Loppusanat: tiede ei ole totuutta, vaan prosessi

Tieteellinen menetelmä ei ole koskaan ollut täydellinen, mutta sen suurin vahvuus on aina ollut kyky korjata itseään. Toistokriisi ja LLM-aiheinen konfabulaatio eivät merkitse tieteen loppua, vaan ne ovat selkeä varoitusmerkki siitä, että vanhat julkaisu- ja tarkistuskäytännöt eivät enää kestä digitaalisen aikakauden tiedontuotannon vauhtia.

Ongelma ei ole tekoälyssä itsessään, vaan siinä, miten integroimme sen prosesseihin, jotka eivät ole vielä rakenteellisesti valmiita tarkistettavuuteen. Ratkaisu ei myöskään ole kieltää tekoälyä, vaan rakentaa sellainen infrastruktuuri, jossa läpinäkyvyys, replikoitavuus ja epävarmuuden rehellinen tunnistaminen ovat pakollisia, eivät valinnaisia.

Proof-Carrying Papers ja Schrödinger’s Machine eivät ole pelkkiä teknisiä kokeiluja. Ne ovat konkreettisia osoituksia siitä, että tieteellinen yhteisö on valmis ottamaan seuraavan askeleen. Ne muuttavat tiedon staattisesta väitteestä dynaamiseksi, koneellisesti tarkistettavaksi ja ihmisen kanssa yhteistyötä tekeväksi järjestelmäksi.

Tulevaisuuden tiede ei perustu siihen, että koneet tai ihmiset olisivat virheettömiä. Se perustuu siihen, että virheet näkyvät, epävarmuus merkitään selkeästi ja jokainen väite voidaan jäljittää sen lähteille. Jos onnistumme rakentamaan tämän kaltaisen ekosysteemin, emme pelkästään pysäytä tiedon rapautumista, teemme tieteellisestä menetelmästä luotettavamman kuin koskaan ennen.

**Tiede ei ole valmis totuus.** Se on tapa etsiä sitä. Ja nyt meillä on viimein työkalut, jotka auttavat meitä tekemään sen rehellisemmin.
