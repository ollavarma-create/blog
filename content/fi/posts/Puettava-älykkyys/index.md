---
title: "Puettava älykkyys"
date: 2023-09-25
tags: ["tens-laitteet", "kivunlievitys", "älykkyys", "wearables", "lääketiede", "lääkkeetön hoito", "innovointi", "Omron TENS", "CE0197", "terveyshoito"]
summary: "Tarkastelen Omron TENS-laitetta ja sen käyttömahdollisuuksia kivun lievittämiseen lääkkeetön tavalla. Artikkelissa selvitän laitteen toimintaperiaatteita, patentteja, käyttövaatimuksia ja mahdollisuuksia sen integroinnille tietokoneeseen tai älypuhelimelle."
---

# Johdanto

Tarkastelen tässä projektiraportissa yleisesti myynnissä olevaa Omron
TENS-laitetta, jolla on myös CE0197 hyväksyntä. Aluksi selvitän
lyhenteitä, direktiivejä, mitä CE0197 tarkoittaa ja sitten perehdyn
laitteen toimintaperiaatteeseen, laitteelle myönnettyihin patentteihin,
kokeilen laitetta itseeni, pohdin voisiko lääkkeiden käyttöä vähentää
TENS:n avulla ja lopuksi pohdin voisiko laitetta jollain tavoin kehittää
tai integroida esimerkiksi tietokoneeseen ja/tai älypuhelimeen.

Laitteen ja ihmisen välisen toiminnan tarkastelun kannalta tuon esille
keskeisimmät hermoston ja lihaksiston toimintaan liittyvät tekijät.
Oletan lukijalla olevan perustietämyksen ihmisen perusfysiologiasta,
biologiasta, hermojärjestelmistä ja sen verran sähkötekniikan osaamista,
että lukija ymmärtää vaihto- ja tasajännitteen, virran, vastuksen ja
impedanssin käsitteet.

# Projektin rajauksesta

Koronapandemiasta ja etäopinnoista johtuen on luontevaa tarkastella
sellaista terveysalan teknologiaa, joka on helposti saatavilla,
turvallisesti testattavissa ja testaaminen ei edellytä rahoitusta.
Minulla on kaksi kappaletta Omron E2 Elite TENS elektronista
hermostimulaattoria, joissa molemmissa on CE0197 merkintä. Laitetta
käytetään pääosin kivun lievitykseen, mutta sillä on myös muita
käyttökohteita, joita en tässä yhteydessä tarkastele lähemmin.

# Lyhenteistä, direktiiveistä ja laeista

Raportin selkeyttämiseksi käytän yleisesti hyväksyttyjä lyhenteitä ja
määritelmiä, mutta jotkin määritelmät, kuten CE-hyväksyntä, vaatii
tarkempaa asian käsittelyä.

## CE eli Conformité Européenne 

 CE-merkintä kertoo, että tuote on EU:n vaatimusten mukainen, ja
 merkintä on oltava tietyissä tuoteryhmissä, jotta niitä voidaan myydä
 EU:n talousalueella. CE-merkintä on valmistajan vakuutus siitä, että
 tuote täyttää sille määritellyt vaatimukset, kuten turvallisuuteen,
 terveyteen, ympäristösuojeluun ja kuluttajansuojaan liittyvät
 vaatimukset. Vaatimustenmukaisuuden täyttymistä valvovat viranomaiset
 eri ministeriöidenhallinnonaloilla riippuen tuotteesta.

### Lääkinnälliset (MDD) CE merkityt laitteet

 Lääkintälaitteiden CE-vaatimustenmukaisuutta Suomessa valvoo Sosiaali-
 ja terveysalan lupa- ja valvontavirasto Valvira. MDD on
 lääkinnällisistä laitteista annetun Euroopan neuvoston direktiivi
 93/42/ETY, Medical Device Directive, joka määrittelee lääkinnällisen
 mahdollisten lisälaitteiden kanssa, mukaan luettuna valmistajansa
 erityisesti diagnosointi- ja/tai ho
 laitteen Linnavuori (2015) mukaan seuraavasti:

 "Lääkinnällisellä laitteella tarkoitetaan kaikkia instrumentteja, laitteistoja, välineitä, ohjelmistoja, materiaaleja tai muita yksinään  tai yhdistelmänä käytettäviä laitteita tai tarvikkeita, yhdessä
 mahdollisten lisälaitteiden kanssa, mukaan luettuna valmistajansa  erityisesti diagnosointi- ja/tai hoitotarkoituksiin tarkoittamat ja  niiden asianmukaiseentoimintaan tarvittavat ohjelmistot, ja joita  valmistaja on tarkoittanut ihmisten:

 - sairauden diagnosointiin, ehkäisyyn, tarkkailuun, hoitoon tai
 lievitykseen;
 - vamman tai vajavuuden diagnosointiin, tarkkailuun, hoitoon,
 lievitykseen tai kompensointiin;
 - anatomian tai fysiologisen toiminnon tutkimiseen, korvaamiseen tai
 muunteluun;
 - hedelmöittymisen säätelyyn;

 Ja joiden pääasiallista aiottua vaikutusta ihmiskehossa tai ihmiskehoon ei saavuteta farmakologisin, immunologisin tai metabolisin
 keinoin, mutta joiden toimintaa voidaan tällaisilla keinoilla edistää."

### Lääkinnällisten laitteiden CE-luokitus ja Omron Elite E2 CE0197

 Suomessa 93/42/ETY direktiivi on saatettu voimaan Laki
 terveydenhuollon laitteista ja tarvikkeista 629/2010, minkä avulla
 Valvira voi antaa sitovia määräyksiä. Laitevalmistajat osoittavat
 CE-vaatimuksenmukaisuuden merkitsemällä CE-merkinnän tuotteeseensa ja
 riippuen riskiluokasta arvion voi tehdä joko valmistaja itse, tai
 mikäli tarvitaan ulkopuolinen taho, NB = Notified Body evaluoi
 tuotteen. Mikäli tuote on ulkopuolisen tahon evaluoima, käy se ilmi
 numerokoodista, esimerkiksi CE0197. Lääkintätuotteilla on neljä eri
 luokkaa: luokka I (Is - steriili, Im - mittaustoiminto) (matalin
 riski), IIa, IIb ja III (korkein riski). Tuotteet luokitellaan sen
 mukaan, miten suuri riski niiden käytöstä aiheutuu käyttäjälle. Luokan
 määrittämisessä käytetään MD-direktiivin (93/42/ETY) liitteen IX
 luokittelusääntöjä. Lisäksi valmistajan tai valtuutetun edustajan on
 allekirjoitettava vaatimuksenmukaisuusvaatimus, jolla vakuutetaan
 tuotteen olevan vaatimusten mukainen. (Linnavuori 2015.)

 EUDAMED (2022) - European Database on Medical Devices on tietokanta,
 josta voi hakea laitteen valmistajan, tyyppikoodin tai esimerkiksi
 edellä mainitun NB:n eli CE-kirjaimen jälkeen olevan numerosarjan
 perusteella evaluoijaa. Esimerkiksi CE0197 tarkoittaa sitä, että 0197
 NB on TÜV Rheinland LGA Products GmbH, joka on toiminut laitteen
 evaluoijana tai tahona, jolle valmistaja ilmoittaa laitteensa
 täyttävän kyseisen artiklan vaatimukset.

 CERTIPEDIA (2022) sisältää kaikki TÜV Rheinland LGA Products GmbH
 myöntämät sertifikaatit. Esimerkiksi Omron E2 Elite ei tietokannasta
 löydy, mutta Omron Healthcare Co. Ltd löytyy useammankin MDD-luokan
 järjestelmäsertifikaateista.

 Mikäli CE-sertifikaatteja haluaa tarkastella, löytyvät ne
 valmistajalta ja tässä tapauksessa myös maahantuojalta, Berner Oy:ltä
 (Liite 1 on muuten sama mutta uudempi malli). Kaikki Omron
 TENS-laitteet ovat lääkinnällisiä laitteita. Laite on luokan IIa (MDD
 artikla 9 liite IX sääntö 9) mukainen.

 EUR-LEX (1993) liitteen IX sääntö 9 (kohta 3.1) on kirjoitettu
 seuraavasti: "Aktiiviset terapeuttiset laitteet, jotka on tarkoitettu
 tuottamaan tai vaihtamaan energiaa kuuluvat II a luokkaan, jolleivat
 niillä ole sellaisia ominaisuuksia, jotka voivat tuottaa energiaa
 ihmiskehoon tai suorittaa energiansiirtoja sen kanssa mahdollisesti
 vaarallisella tavalla, ottaen huomioon tämän energian luonteen,
 tiheyden ja kohdistuspaikan, jolloin ne kuuluvat II b luokkaan.
 Aktiiviset laitteet, jotka on tarkoitettu II b luokan aktiivisten
 terapeuttisten laitteiden tehon tarkastukseen ja valvontaan tai
 tarkoitettu vaikuttamaan suoraan näiden laitteiden suorituskykyyn
 kuuluvat II b luokkaan." Tarkemmin tämä jaottelu on avattu MDR-b
 (2022) linkissä löytyvässä artikkelissa.

 MDD artikla 9 liite IX mukaan lääkinnällisten laitteiden tuottaminen
 on MDD:n ytimessä, sillä valmistajalta vaaditaan tällöin myös
 auditoitua laatujärjestelmää Artiklan 10 mukaisesti. Tämä on se miksi
 CERTIPEDIA (2022) listaa Omron Healthcaren vain
 järjestelmäsertifikaateissa. Liittyen CE0197 ja IIa luokitukseen,
 liite IX mukaan NB:lle eli tässä tapauksessa 0197 = TÜV Rheinland LGA
 Products GmbH on annettava mahdollisuus vähintään kerran vuodessa
 tarkistaa edellä mainittu laatujärjestelmä, siinä oleva dokumentaatio,
 jälkimarkkinaselvitykset ja muut tiedot. Luokan IIa osalta
 auditoijalle pitää antaa mahdollisuus tarkistaa myös tekninen
 dokumentaatio ja mallikappaleet. Lisäksi auditoija, eli TÜV Rheinland
 LGA Products GmbH pitää vähintään kerran viidessä vuodessa tehdä
 ennalta ilmoittamaton tarkistus tehtaaseen, jossa tuotetta
 valmistetaan. (MDR 2022.)

## Depolarisaatio ja polarisaatio 

 Depolarisaatio tarkoittaa jännitteen purkautumista ja varauksen
 jakautumista. Depolarisaatio tapahtuu hermosolussa. Lepotilassa olevan
 hermosolun lepojännite pienenee depolarisaatiossa. Depolarisaation
 etenemistä hermosolujen välillä kutsutaan toimintajännitteeksi,
 hermoimpulssiksi tai aktiopotentiaaliksi. Jännitteen purkautumisessa
 hermosolun kalvon normaali polarisoituminen muuttuu, sillä
 positiivisesti varautuneita natriumioneja pääsee virtaamaan soluun
 tasoittamaan varauseroa solun ja ympäröivän aineen välillä.

## Endorfiinit

 Endorfiinejä kutstutaan sisäsyntyisiksi morfiineiksi, koska ne ovat
 keskushermostossa esiintyviä hormoneita, eli elimistön itse tuottamia
 välittäjäaineita, jotka sitoutuvat opioidireseptoreihin ja saavat
 aikaan mielihyvän tunteita samalla kivun tuntemuksia vähentäen.
 Esimerkiksi beta-endorfiini on 18--33 kertaa voimakkaampaa kuin
 morfiini. (Loh, H., Tseng, L., Wei, E. & Li C. 1976.)

## NNT, NNH ja lumevaikutus

 Tutkimuksissa eräs lähtökohta on verrata hoitoa placeboon. Placebolla
 tarkoitetaan lumevaikutusta, eli esimerkiksi lääkettä ilman
 vaikuttavaa ainetta, tai leikkausta ilman todellisia toimenpiteitä tai
 TENS-hoitoa ilman sähköimpulsseja.

 NNT on arvo, joka kertoo montako potilasta tulee hoitaa, jotta yksi
 potilas saa hyödyn. Esimerkiksi vortioksetiini (Brintellix)
 masennuslääkkeen NNT on 7. Tämä tarkoittaa sitä, että hoitovasteen saa
 46--49 % vorttioksetiinia ja 34 % lumetta saaneista ihmisistä. Eli kun
 vortioksetiinilla hoidetaan seitsemää potilasta, saadaan yksi
 hoitovaste enemmän kuin lumeella. Vastaavasti 11:tä potilasta
 hoidettaessa vortioksetiinilla saavutetaan yksi remissio enemmän. NNH
 kertoo vastaavasti siitä moniko hoidetuista potilaista saa haittoja
 hoidosta ja keskeyttää hoidon. Vortioksetiinihoidon keskeyttää yksi
 potilas 36 hoidetusta, jolloin number needed to harm, NNH=36. (Fimea
 2014.)

## Ääreishermosto eli perifeerinen hermosto 

 Ääreishermosto on hermoston osa, johon kuuluvat selkäydinhermot ja
 aivohermot. Ääreishermosto sisältää autonomisen eli tahdosta
 riippumattoman hermoston ja somaattisen eli tahdonalaisen hermoston

## Taajuudet TENS-laitteissa

 Taajuus kertoo kuinka monta kertaa sekunnissa sähköistä stimulaatiota
 kohdistetaan iholle ja se esitetään yksikössä hertsi (Hz). 30
 stimulaatiota sekunnissa tarkoittaa 30 Hz.

## TENS eli transcutaneous electroneural stimulation 

 Transkutaaninen elektroneuraalinen stimulaatio, tunnetaan myös
 elektroterapiana.

# Ihmisen hermoston ja lihaksiston toiminnasta

Koska TENS-laitteen toiminta liittyy ihmisen sähkökemiallisiin
toimintoihin, on järkevää tarkastella aluksi ihmisen hermoston ja
lihaksiston toimintaa. Kokonaiskuvan ymmärtämisen helpottamiseksi
yksinkertaistan hermoston toiminnan analogiseksi ja binääriseksi, vaikka
todellisuudessa tilanne on monimutkaisempi.

## Hermosolujen ja synapsien kehittymisestä ja toiminnasta

 Hermosolut jaetaan kolmeen eri luokkaan, joita ovat 1) sensory neurons
 eli aistinhermosolut, jotka keräävät tietoa ulkoisesta ja sisäisestä
 tilasta ja kuuluvat ääreishermostoon, 2) interneuronit, jotka
 yhdistävät aistintoiminnot motorisiin toimintoihin ja ne tekevät
 synaptisia kontakteja muihin hermosoluihin, mutta ei lihaksiin tai
 aistinhermosoluihin sekä 3) motorneuronit, jotka kuljettavat
 impulsseja keskushermostosta effektorisoluihin lihaksiin ja erittäviin
 rauhassoluihin. Hermoston toiminta koostuu miljoonien hermosolujen
 koordinoidusta yhteistoiminnasta, mutta yksinkertaisimmillaan lenkkiin
 kuuluu vain aistinneuroni, joka on synaptisessa yhteydessä motoriseen
 neuroniin, joka edelleen lähettää signaalin effektorille, esimerkiksi
 lihaksen ja refleksin välisessä tilanteessa. Sensoristen neuronien
 solukeskukset sijaitsevat keskushermoston ulkopuolella ja muodostavat
 ganglioita, joissa on useita samantyyppisten hermosolujen
 solukeskuksia. Keskushermostossa samanlaisia toiminnallisia rakenteita
 kutsutaan tumakkeiksi. Tumakkeet ja gangliot mahdollistavat
 yksinkertaisten toimintojen, kuten refleksien käsittelemisen aivojen
 ulkopuolella, säästäen aivojen kapasiteettia monimutkaisempien
 toimintojen suorittamiseen. (Campbell 2011, 1131--1136.)

 Erilaisia hermoston ja lihasten toimintoja toteuttavat
 hermosoluliitokset syntyvät kehityksemme eri aikoina. Ensimmäisenä
 kehittyivät tietojen vastaanottoon liittyvät solut ja liikehermosolut.
 Geenit tuottavat hermosolujen ja aivoalueidensisäiset ja niiden
 väliset yhteydet. Vaikka voisi olettaa synapsien määrän lisääntyvän
 koko loppuelämän, todellisuudessa toimintojen kehityttyä synapsien
 määrä vähenee, koska aivorata optimoituu ja turhat solut kuolevat pois
 solukuolemalla, apoptoosilla. Solukuolema tapahtuu tunnistamalla
 kohdesolun troofisia kasvutekijöitä ja mikäli niitä ei ole, tekee solu
 itsemurhan käynnistämällä apoptoosimekanismit ja lyysautuu pois
 verenkiertoon. Mikäli troofisia kasvutekijöitä kuitenkin on,
 välittäjäainetta vastaanottanut solu kiittää sitä antanutta solua
 erittämällä lisää kasvutekijää ja soluliitos syntyy. Arviolta noin 70
 % hermosoluliitoksista muuttuu päivittäin, eli mikäli haluaa säilyttää
 hermoverkossa yhteydet, tulee yhteyksiä käyttää, muuten yhteydet
 häviävät. Use it or loose it toimii siis myös hermoverkkoon. Tällaiset
 rakenteelliset muutokset mahdollistavat tarkemman viestinvälityksen.
 Mikäli yhteydet pysyvät, hermosolut alkavat kypsyä, eli rasvatupet
 kehittyvät johtokimpuiksi, jolloin yhteyksien määrä kasvaa ja niiden
 nopeus ja teho kasvaa. Huomaa, että erityisesti harmaan aineen määrä
 aivoissa ei ole merkityksellistä, sillä harmaa aines vähenee
 ikääntyessä kokemusten karttuessa edellä mainituista syistä. Mikäli
 esimerkiksi peitämme toisen silmämme, alkaa silmämme hermo hävittää
 yhteyksiään. Silmän peittämistä voidaan käyttää myös
 tarkoituksellisesti esimerkiksi lapsen karsastuksen hoitamisessa ja
 antaa kehittymättömän silmän ottaa kehittynyttä silmää kiinni.
 (Penttonen 2017.) Hermosolut kasvattavat siis tuoja- ja
 viejähaarakkeita ja soluliitoksia. Viejähaarakkeen kasvun ohjaus
 tapahtuu kasvukartiolla, kontakti- ja kemotaksiaohjauksella,
 houkuttelulla ja karkottamisella. Synaptinen soluliitos syntyy, jos
 tuojahaarakkeen eli dendriitin ulokkeiden ja kasvavan aksonin
 filopodiumin avulla suoritettu yhteistyötunnustelu tuntuu
 mahdolliselta. Tätä tapahtumaa kutsutaan synaptogeneesiksi. (Penttonen
 2017; Paavilainen 2016, 55--68.)

## Ääreishermosto, sympatikus ja parasympatikus

 Ääreishermosto jakautuu raajoin ja aistinelimin vievään eli
 efferenttiin ja tuovaan eli afferenttiin somaattiseen hermostoon ja
 ei-tahdonalaisia sisäelintoimintoja ohjaavaan autonomiseen hermostoon.
 Autonominen, eli vegetatiivinen hermosto jakautuu aktiivisessa tilassa
 toimivaan sympaattiseen ja lepotilassa toimivaan parasympaattiseen
 hermostoon. Välittäjäaineista asetyylikoliini on parasympatikuksen
 tärkein välittäjäaine. Tunteisiin ja niiden kokemiseen liittyy
 sympatikuksessa tärkeimpänä noradrenaliini. Aivoissa samankaltaisten
 hermosolujen rypästä kutsutaan tumakkeeksi ja aksonikimppuja radoiksi.
 Ääreishermostossa aksonikimppuja kutsutaan hermoiksi ja hermosolujen
 soomaosien kasautumaa ganglioksi. Keskushermosto ja ääreishermosto
 kytkeytyvät toisiinsa selkäytimessä ja aivorungossa. Aivorunko
 sisältää väliaivot, keskiaivot, aivosillan ja ydinjatkeen. Aivorunko
 säätelee esimerkiksi vireystilaa ja univalverytmiä suprakiasmaattisen
 tumakkeen avulla. Aivorunko kytkeytyy kahdestatoista aivohermoparista
 yhteentoista, sillä näköhermo menee suoraan väliaivoihin. Aivohermot
 liittyvät pään alueen aistielinten, lihasten sekä joidenkin
 sisäelinten toimintoihin. Niitä on sekä sensorisia ja motorisia.
 Selkäydinhermo jakautuu segmentteihin, kuten tunnon kannalta
 tärkeisiin dermatomeihin. Bell-Magendien laki määrittää
 selkäydinhermojen toiminnan siten, että sisään tulevat dorsaaliset
 hermojuuret tuovat aistitietoa iholta, ulos menevät ventraaliset
 hermojuuret vievät motorisia käskyjä lihaksiin. (Paavilainen 2016,
 44--47; Hämäläinen 2017.)

## Tiedonkulku hermosolussa

 Hermosoluissa on sekä sensorisia, eli aistimiseen liittyviä soluja,
 että motorisia, eli liikkumiseen liittyviä soluja. Näiden väliin on
 kytkeytyneenä välineuroneita, joita on eniten hermosoluista.
 Välineuronit muodostavat monimutkaisia verkostoja, joissa
 tiedonkäsittely tapahtuu. Hermosolujen solukeskuksessa eli soomassa
 sijaitsee tuma, jonka sisältämät kromosomit ohjaavat solun toimintaa
 geneettisen koodin mukaisesti. Solukeskuksessa kytkeytyvät toisista
 hermosoluista tietoa vastaanottavat haarakkeet eli dendriitit. Yhdestä
 solusta voi olla yhteyksiä jopa kymmeniin tuhansiin muihin soluihin.
 Solukeskuksessa on aksonikeko, josta lähtee yksi tietoa vievä haarake
 eli aksoni. Aksoni voi haarautua loppupäästään useiksi
 päätehaarakkeiksi. Tiedon vastaanottoa yhteen hermosoluun useista eri
 hermosoluista kutsutaan konvergenssiksi ja tiedon lähettämistä yhteen
 tai useampiin hermosoluihin kutsutaan divergenssiksi. Raajoihin
 menevät aksonit ovat pisimpiä ja aivoissa lyhyimpiä. Hermosolujen
 välissä sijaitsee synaptinen liitos, jossa tietoa tuovaa hermosolua
 kutsutaan presynaptiseksi ja vastaanottavaa hermosolua
 postsynaptiseksi soluksi. Hermostossa on lisäksi monen tyyppisiä
 tukisoluja, joiden tehtävä on huoltaa hermostoa välittämällä niille
 ravintoaineita ja poistamalla kuona-aineita ja ohjaamalla uusia
 hermosoluja oikeille paikoilleen ja poistamalla kuolleita hermosoluja.
 Tukisolut muodostavat myös aksoneiden ympärille tiedonvälitystä
 nopeuttavaa myeliinituppea Ranvierin kuroumineen. (Paavilainen 2016,
 34--38; Hämäläinen 2017.)

 Hermoston tiedonvälitys toimii sekä binäärisesti että analogisesti.
 Tietokoneista tuttua binääristä tiedonvälitystä tapahtuu
 hermosoluissa, jotka voivat olla joko lepotilassa (0) tai lauenneena
 (1). Lepotilassa (0) hermosolun varaus on noin miinus 70 mV ja
 lauenneena (1) noin plus 50 mV. Depolarisaatiolla tarkoitetaan solun
 ja ympäröivän tilan jännite-eron vähenemistä ja hyperpolarisaatiolla
 jännite-eron kasvamista. Depolarisoitunut solukalvon kohta depolarisoi
 myös viereistä hermosolua ja tämä jännitemuutos eli hermoimpulssi
 lähtee etenemään aksonia pitkin 1--10 m/s riippuen aksonin
 paksuudesta. Mikäli hermosolua ympäröi eristävä myeliinituppi ja
 Ranvierin kuroumat, voi hermoimpulssi kulkea jopa 120 m/s hyppimällä
 kuroumasta toiseen. Hermosolu ei voi kuitenkaan laueta määrättömän
 nopeasti, vaan jännitepotentiaalia ylläpitävien solun
 natrium-kaliumionipumppujen pitää palauttaa solun negatiivinen varaus
 aina ennen seuraavaa laukeamista. Tämä estää myös hermoimpulssin
 kulkemisen väärään suuntaan. Palautumiseen ja uuteen valmiuteen kuluu
 aikaa noin 2 ms, jota kutsutaan refraktääriajaksi. Näin ollen
 hermosolun voi enimmillään tuottaa noin 500 hermoimpulssia sekunnissa.
 Hermoimpulssit ovat aina suuruudeltaan samanlaisia ja tästä syystä
 sensoristen hermosolujen ärsyke on koodattava hermoston kielelle
 esimerkiksi taajuuskoodauksella. (Paavilainen 2016, 38--40.)

 Tarkemmin depolarisaatiota ja hyperpolarisaatiota voi tarkastella
 membraanipotentiaalin avulla, joka syntyy silloin, kun solun
 puoliläpäisevän solukalvon eri puolilla on erilainen pitoisuus
 varauksellisia ioneja. Tyypillisesti solun sisäpuolella on runsaasti
 K+ (kalium) -ioneja ja jonkin verran Na+ (natrium) -ioneja. Solun
 ulkopuolella K+ ja Na+ kationien pitoisuudet ovat suurin piirtein
 päinvastaiset. Solun sisällä anioneina, eli negatiivisina
 partikkeleina, toimivat proteiinit, aminohapot, sulfaatti ja
 fosfaatti. Ionit pääsevät kulkeutumaan kalvon puolelta toiselle
 passiivisesti ionikanavien avulla ja aktiivisesti ionipumppujen
 avulla. Nämä kanavat päästävät lävitseen valikoivasti vain kaliumia,
 natriumia tai klooria. Proteiinit ja muut suurikokoiset solun sisäiset
 anionit eivät läpäise solukalvoa ja näin ollen ne ylläpitävät
 negatiivista varausta solun sisällä. Kalium pyrkii
 konsentraatiogradienttinsa mukaisesti ulos solusta, jolloin solun
 sisäpuolen negatiivinen varaus kasvaa ja sähköinen gradientti on
 vastakkainen konsentraatiogradientille. Mikäli kalium olisi ainoa
 kationi, joka voi siirtyä solukalvon puolelta toiselle, syntyisi
 tasapainotila, jossa kaliumia virtaisi ulos ja sisään yhtä paljon.
 Tällöin membraanipotentiaali olisi kaliumionien
 tasapainopotentiaalissa, mutta kalium ei kuitenkaan ole ainoa kationi,
 joka voi ylittää solukalvon, vaan myös natrium voi siirtyä solukalvon
 läpi. Sekä ionien konsentraatio- että sähköinen gradientti pyrkivät
 siirtämään natriumia solun ulkopuolelta soluun sisään, jolloin
 natriumin vähäinen virtaus soluun nostaa membraanipotentiaalin
 kaliumionien tasapainopotentiaalista ylöspäin. Natriumin vähäinenkin
 virtaus johtaisi lopulta tasapainotilaan, mutta tämän estää Na+/K+
 -pumppu, eli proteiini, joka käyttää ATP:tä energialähteenään, joka
 siirtää natriumia ulos solusta ja kaliumia solun sisään ylläpitäen
 konsentraatiogradienttia. (Campbell 2011, 1091--1097.)

 Esimerkiksi verensokeri on glukoosia (monosakkaridi), joka
 mitokondriossa tapahtuvassa hapetuksessa vapauttaa energiaa, joka
 taltioidaan ATP:na. ATP on mukana myös silloin, kun solu valmistaa
 rakennusosista uusia molekyylejä. Fosfaatin siirtäminen ATP:sta
 aktivoitavalle molekyylille on tärkeä mutta ei ainoa tapa, jolla ATP
 toimii välittäjänä. (Heino & Vuento 2008.)

 Vaikka kaikilla soluilla onkin membraanipotentiaali, vain hermo- ja
 lihassoluilla on kyky muuttaa kalvopotentiaaliaan. Solun normaalia
 kalvopotentiaalia kutsutaan lepopotentiaaliksi. Hermosoluilla on
 ionikanavia, jotka mahdollistavat solun muuttaa kalvopotentiaaliaan
 vasteena solun stimuloinnille. Sensoristen neuronien tapauksessa
 ärsyke tulee tyypillisesti elimistön ulkopuolelta. Ärsykkeen vaikutus
 hermosolussa riippuu avautuvan ionikanavan tyypistä ja ärsykkeen
 seurauksena solussa saattaa syntyä hyperpolarisaatio tai
 depolarisaatio. Tällaisia jännitteen muutoksia kutsutaan
 asteittaisiksi potentiaaleiksi, sillä vasteen suuruus riippuu
 ärsykkeen voimakkuudesta. Mikäli depolarisaatio ylittää laukeamiseen
 liittyvän kynnysarvon, seuraa aktiopotentiaali, eli hermoimpulssi,
 jossa voimakas natriumkanavien avautuminen nostaa potentiaalin
 positiiviseksi. Hyperpolarisaatiot eivät aiheuta aktiopotentiaaleja,
 vaan tekevät niiden syntymisen epätodennäköisemmäksi. Ei-asteittainen,
 kaikki-tai-ei-mitään --tapahtuma eli hermoimpulssin voimakkuus on
 riippumaton stimuluksen suuruudesta. Ärsykkeen suuruus vaikuttaa
 siihen kuinka tiheään hermoimpulsseja syntyy. Hermoimpulssin
 aiheuttajana toimivat jänniteherkät ionikanavat, jotka avautuvat ja
 sulkeutuvat vasteena kalvopotentiaalin muutoksiin. Hermoimpulssin
 depolarisaatiovaiheessa membraanipotentiaali on hetkellisesti
 käänteinen, sillä solun ulkopuoli on negatiivinen sisäpuoleen
 verrattuna, koska natrium virtaa sisään soluihin. Tämä on
 epätasapainoinen tila, jossa positiivisen palautevaikutuksen
 seurauksena kanavien avautuminen stimuloi yhä useampien
 natriumkanavien aukeamista, eli kynnysarvon saavuttava depolarisaatio
 lisää depolarisaatiota, joka on peruuttamaton tila. (Campbell 2011,
 1098--1100)

 Synapseissa tiedonvälitys on kemiallista eli analogista. Tiedon
 välitys hermosolusta toiseen tapahtuu välittäjäaineiden avulla.
 Synapsirako on noin 20--30 nanometriä paksu sisältäen nestettä, joka
 erottaa pre- ja postsynaptiset hermosolut toisistaan. Kun
 hermoimpulssi saapuu presynaptisen aksonin päätelevyihin, alkaa se
 vapauttaa synapsikuiluun välittäjäainetta. Välittäjäaine siirtyy
 synapsikuilun yli postsynaptisen hermosolun dendriiteissä oleviin
 välittäjäainereseptoreihin. Hermostosta on löydetty yli 100 erilaista
 välittäjäainetta. Välittäjäaineita tuotetaan tyypillisesti
 hermosolussa itsessään ja niitä varastoidaan aksonin presynaptisissa
 päätteissä oleviin rakkuloihin. Ravintoaineet välittäjäaineiden
 tekemiseksi tulevat ruoan mukana, esimerkiksi serotoniinia eli
 5-hydroksi-tryptamiini (5HT) tuotetaan tryptofaanista. Serotoniini on
 myös kudoshormoni. Välittäjäaineet kierrätetään tyypillisesti takaisin
 rakkuloihin tai ne pilkotaan entsymaattisesti osatekijöiksi ja
 syntetisoidaan uudelleen. (Paavilainen 2016, 43.) 

## Hermoston kiihdytys ja hidastaminen

 Edellä käsitellyt välittäjäaineet voivat olla joko kiihdyttäviä eli
 eksitatorisia tai estäviä eli inhibitorisia. Eksitatoriset
 välittäjäaineet muuttavat postsynaptisen solun lepojännitettä
 positiiviseen suuntaan kohti miinus 50mV laukeamiskynnystä,
 inhibitoriset negatiiviseen poispäin laukeamiskynnyksestä.
 Lepojännitettä depolarisoivaa muutosta kutsutaan EPSP:ksi eli
 eksitatoriseksi postsynaptiseksi potentiaaliksi ja vastaavasti
 hyperpolarisoivaa IPSP:ksi eli inhibitatoriseksi postsynaptiseksi
 potentiaaliksi. Yleisin inhibitorinen välittäjäaine on gaba, eli
 gamma-aminovoihappo ja yleisin eksitatorinen välittäjäaine on
 glutamaatti. Muita keskeisimpiä välittäjäaineita ovat asetyylikoliini,
 serotoniini, dopamiini ja noradrenaliini. (Hämäläinen 2017.)

 Usein samaa välittäjäainetta käyttävät aivojen alueet muodostavat
 toisiinsa kytkeytyneitä alueita säädellen tietynlaisia erikoistuneita
 toimintoja, kuten asetyylikoliini kolienergisen järjestelmän, joka
 liittyy vireystilaan ja oppimiseen, dopaminerginen järjestelmä
 liikkeiden säätelyyn ja mielihyvän kokemiseen, adrenaliinia käyttävä
 adreginen järjestelmä tunteiden säätelyyn ja serotonerginen
 järjestelmä vireystilaan ja mielialaan. Välittäjäaineiden muutokset
 ovat portaattomia ja kestävät vain sen aikaa, kun välittäjäaine
 poistuu tai entsymaattisesti hajotetaan synapsiraosta. Koska samaan
 hermosoluun voi kytkeytyä suuri määrä presynaptisia hermosoluja ja osa
 hermosoluista voi olla inhibitorisia ja osa eksitatorisia, niiden
 tuottama IPSP/EPSP:n summa määrittelee sen mihin suuntaan ja miten
 paljon sooman lepojännite muuttuu. Kuten edellä käsiteltiin, mikäli
 hermosolun laukeamiskynnys ylitetään, laukeaa hermoimpulssi. Mikäli
 hermosoluja olisi vain eksitatorisia, aivot ajautuisivat kierteeseen,
 jossa hermosolut kiihdyttäisivät aina vain lisää tosiaan laukomaan
 lisää hermoimpulsseja. Esimerkiksi tarkkaavaisuutta edellyttämissä
 tilanteissa pitää pystyä vaimentamaan IPSP:llä ei-tarkkailtua kohdetta
 ja vahvistamaan EPSP:llä tarkkaavaisuuden kohdetta, kuten esimerkiksi
 lukemaan keskittymisessä. Monissa hermosoluissa on myös itsesyntyistä
 spontaania aktiivisuutta, joiden tuottamia hermoimpulssien taajuutta
 säädellään IPSP:n ja EPSP:n avulla. (Paavilainen 2016, 41--42 &
 134--137.)

 Sensoristen ja motoristen hermosolujen välillä toimiva monimutkainen
 välineuroniverkosto voi myös tuottaa hermoimpulsseja spontaanisti.
 Synapsit sijaitsevat tyypillisesti presynaptisen solun aksonin ja
 postsynaptisen solun dendriittien välillä, mutta esimerkiksi motorisen
 hermosolun aksonin ja lihassolun välisessä synapsissa hermosolu
 vapauttaa välittäjäainetta, joka saa lihassäikeet supistumaan.
 (Paavilainen 2016, 42.)

## Lihaksiston toiminnasta

 Liike aikaansaadaan lihaksia supistamalla, lihaksen jännityksen
 laukeaminen tapahtuu sen sijaan passiivisesti. Mahdollisuus liikuttaa
 ruumiinosia vastakkaisiin suuntiin vaatii pareittain toimivat
 lihakset, koukistajan ja ojentajan. Lihasten nimityksissä esimerkiksi
 abductor ja extensor. Lihaksen kyky supistua perustuu rakenteeseen,
 jossa yksittäiset lihassolut ovat järjestäytyneet lihassyy- eli
 lihassolukimpuiksi, jotka edelleen yhdessä muodostavat lihaksen.
 Kunkin lihassyyn muodostavat ohuet säikeet, myofibrillit, jotka
 edelleen ovat muodostuneet myofilamenteista, eli paksuista
 myosiinifilamenteista ja ohuista aktiinifilamenteista. Filamenttien
 järjestäytyminen saa aikaan lihaksen poikkijuovaisen ulkoasun.
 Lihaksen supistuvaa, säikeissä toistuvaa jaksoa kutsutaan
 sarkomeeriksi, joka on samalla lihaksen toiminnallinen yksikkö.
 Sarkomeeri koostuu Z-vyöhykkeestä, joka muodostuu sarkomeerin
 rajoista, kalvoista, joihin kahden sarkomeerin aktiinit kiinnittyvät.
 Myosiini sijaitsee sarkomeerin keskellä H-vyöhykkeenä, jossa ei ole
 aktiinia. Sarkomeerin molemminpuolista aluetta, jolla on vain
 aktiinia, kutsutaan I-vyöhykkeeksi. Vyöhykettä, jolla aktiini ja
 myosiini ovat päällekkäin, kutsutaan A-vyöhykkeeksi. (Campbell 2011,
 1153--1161)

 Poikkijuovaisessa lihaskudoksessa lihassyytä eli solua ympäröi
 endomysium, lihassyykimppua perimysium ja lihassyykimppujen
 muodostamaa lihasta epimysium. Lihaksen solut ovat monitumaisia.
 Lihassolun sisällä on lihassäikeitä, myofibrillejä, joiden välissä on
 solulimaa eli sarkoplasmaa. Lihassäikeet koostuvat edelleen
 myofilamenteistä, jotka voidaan jakaa ohuiksi aktiinifilamenteiksi ja
 paksuiksi myosiinifilamenteiksi, joiden järjestäytyneisyydestä johtuu
 lihaksen poikkijuovaisuus. (Yanagisawa 2011, 902--904.)

 Luustolihas supistuu vain motorisen neuronin stimuloimana. Neuronin
 toiminta on käsitelty ylempänä tässä tekstissä. Levossa myosiinin
 sitoutumiskohdat ovat peitettynä säätelyproteiini tropomyosiinilla,
 jonka asemaa toinen säätelyproteiini, troponiinikompleksi, säätelee.
 Lihaksen supistumiseksi aktiinin pinnalla olevien myosiinin
 sitoutumispaikkojen täytyy olla vapaita. Sitoutumispaikat vapautuvat
 kalsiumionien sitoutuessa troponiiniin ja täten muuttaen troponiinin
 ja tropomyosiinin välistä sidosta, jolloin sitoutumispaikat
 paljastuvat. Kalsiumin ollessa läsnä lihas voi supistua. Sisäisen
 kalsiumpitoisuuden laskiessa, aktiinin sitoutumispaikat ovat peitossa,
 eikä lihas voi supistua. Kalsiumin pitoisuutta solulimassa säätelee
 sarkoplasmakalvosto, joka aktiivisesti kuljettaa kalsiumia solulimasta
 kalvostoon varastoitavaksi. Lihaksen supistumiskäsky saapuu motorista
 neuronia pitkin hermo-lihasliitokseen, jossa asetyylikoliinin
 vapautuminen synaptiseen rakoon aikaansaa postsynaptisen lihassolun
 depolarisaation ja aktiopotentiaalin synnyn. Aktiopotentiaali leviää
 lihassolun sisään kaikkiin sarkomeereihin plasmamembraanin eli
 sarkolemman painaumia myöten, joita kutsutaan T-putkijärjestelmäksi.
 T-putkien koskettaessa sarkoplasmista kalvostoa sen kalsiumläpäisevyys
 kasvaa. Lihaksen supistus päättyy, kun kalsium on pumpattu
 sytoplasmasta takaisin talteen ja troponiinitropomyosiinikompleksi
 peittää myosiinin sitoutumispaikat aktiinin pinnalta. (Campbell 2011,
 1152--1153.)

 Lihaksen toiminta on asteittaista, eli voimme jännittää esimerkiksi
 hauistamme vähän tai täysin, jolloin yhden lihaksen kaikki
 lihassyykimput eivät supistu samanaikaisesti, vaan lihas toimii
 motorisina yksiköinä. Lihaksissa yhteen lihassoluun tulee vain yksi
 synapsi, mutta sama motorinen hermosolu voi muodostaa synapsin
 useamman lihassolun kanssa. Saman neuronin hermottamat lihassolut
 muodostavat siis motorisen yksikön. Yksittäisen lihassolun
 supistuminen on kaikki-tai-ei-mitään -tapahtuma, jonka laukaisee
 motorista neuronia pitkin saapuva hermoimpulssi. Koko lihaksen
 asteittainen supistuminen on mahdollista myös aktiopotentiaalien
 tiheyttä säätelemällä, sillä yhden hermoimpulssin aikaansaama supistus
 kestää korkeintaan 100 millisekuntia. Mikäli seuraava aktiopotentiaali
 saapuu ennen edellisen lakkaamista, vaikutus summautuu ja lihas
 supistuu enemmän. Yhtenäinen nopea aktiopotentiaalien virta saa aikaan
 tetanuksen, kouristuksenomaisen supistuksen. Lihassolut voidaan jakaa
 nopeisiin eli valkeisiin ja hitaisiin eli punaisiin lihassoluihin sen
 mukaan kauanko sarkoplasmisen kalvoston kalsiumkanavat pysyvät auki,
 eli kauanko lihaksen supistustila kestää. Nopeita lihassoluja
 tarvitaan äkkinäisiin, voimakkaisiin supistuksiin kuten sprinttiin,
 kun taas hitaiden solujen tonus saattaa olla hieman heikompi, mutta
 selvästi pitkäkestoisempi, esimerkiksi kestävyyslajit ja asentoa
 ylläpitävät lihakset. Hitaissa soluissa sarkoplasmista kalvostoa on
 vähemmän, joten kalsiumin sisäänotto on noin viisi kertaa hitaampaa
 kuin nopeassa lihaksessa. Punaiset lihakset sisältävät runsaan
 verisuonituksen ja paljon mitokondrioita sekä happea varastoivaa
 myoglobiini-proteiinia. (Campbell 2011, 1150--1161.)

 Nyt ymmärrämme hieman, miten hermosto ja lihaksisto toimii. Evoluution
 näkökulmasta voi hieman hupaisasti todeta sen, että jos näyttää
 keskisormea mielenosoituksena toisille, aivoista ei lähde keskisormea
 hallinnoiville lihaksille käskyä näyttää keskisormea, vaan aivoista
 lähtee ensin käsky avata koko käsi, sitten heti perään käsky älä avaa
 koko kättä, vaan ainoastaan keskisormi. Evoluutiossa olemme siis
 roikkuneet puissa ja tarvinneet vain kämmenotetta, mutta myöhemmin
 hienomotoriikkaa, joka on edellyttänyt hermoston koodauksen muutosta.

 Tästä pääsemmekin siihen, miten saadaan lihakset ja vaikka se
 keskisormi pystyyn ulkoisesti tuotetun sähkövirran avulla.

# TENS-laitteen toimintaperiaatteesta ja käyttökohteista yleisesti

Toin edellä esille ionipumput solujen toiminnassa ja yhdessä veden
kanssa johteet, kuten natrium, vähentävät kehon vastusta. Elämää ei
olisi ilman jatkuvaa ionipumppujen toimintaa. Ionipumppujen toiminta voi
häiriintyä ulkoisista sähkövirroista, kuten sähköiskusta.

Silloin kun puhutaan sähköiskuista, tarkoitetaan sillä usein
sähkölaitteiden käyttämää sähköä, joka EU:ssa on 50 Hz ja 240 V
vaihtovirtaa. Se miten vaarallista sähköisku on, riippuu kehon läpi
menevästä virrasta, eli ampeereista. Mikäli ottaa esimerkiksi 240 V
vaihejohtimesta kiinni paljain sormin, mutta muut osat kehosta ei ole
maadoitettuna, tai osu nollajohtimeen tai suojamaadoitukseen, ts. on
eristävät vaatteet ja jalkineet, ei kosketus tunnu missään. Mutta jos
jokin osa kehosta on maadoitettu, tai lähes maadoitettu, kuten paljaat
jalat betonisella lattialla, sähköisku on hengenvaarallinen. Tasavirran
suhteen tilanne on kuitenkin eri, eli on tärkeää erottaa tasajännitteen
ja vaihtojännitteen aiheuttamat reaktiot toisistaan.

Artikkelissa Conduction of Electrical Current to and Through the Human
Body: A Review Fish, R. ja Geddes, L. (2009) tuo esille muutamia arvoja
liittyen sähkön siirtymiseen eri kehon osissa. Artikkelissa käsitelty
jännite on Yhdysvalloissa tyypillinen 120 V ja taajuus 60 Hz.
Esimerkiksi 99 % sähkövastuksesta on iholla. Kuivan käden ihon
resistanssi voi olla yli 100 000 Ω (100 kΩ), sillä käden iho on paksua.
Kehon sisäinen resistanssi on noin 300 Ω. Ihoon kohdistuneet haavat ja
muut tekijät voivat vähentää ihon vastusta merkittävästi. Yli 500 voltin
vaihtojännite aiheuttaa ihon pintakerroksen vioittumisen, mutta
tasajännitteen kohdalla tilanne on eri, sillä suurikaan tasajännite ei
välttämättä tunnu missään.

Ulkoisen sähkövirran lisäksi kehomme tuottaa heikkoa sähkövirtaa, kuten
hermoimpulsseja, monissa ruumiinosissa, kuten sydämessä, aivoissa,
lihaksissa ja hermoissa. Keho myös reagoi ulkoa tuleviin sähköisiin
ärsykkeisiin ja saa aikaan muutoksia kehon toiminnoissa. Kehon
sisäisessä sähkössä esiintyviä poikkeuksia, kuten jäykkyyttä tai kipua,
hoidetaan käyttämällä elektroterapialla, josta pientaajuusterapia on
tyyppiesimerkki. (Omron 2022.)

Elektroterapeuttisesta TENS-laitteesta kytketään iholle elektrodit,
joiden välille laite tuottaa potentiaalieron, jossa muuttujina ovat
jännite (U) ja virta (I). Virta (I), eli elekronit, menevät elektrodien
välillä kudoksissa, joissa se saa aikaan aktiopotentiaaleja, eli
hermoimpulsseja. Jännite voidaan laskea käyttämällä Ohmin lakia kaavalla
jännite = virta x resistanssi. Jännitettä (U) mitataan volteissa (V),
virtaa (I) ampeereissa (A) ja resistanssia (R) ohmeissa (Ω) silloin kun
kyse on tasajännitteestä. Ihon resistanssi muuttuu sen mukaan, miten
kostea iho on, tai minkä verran ihon soluissa on johtavia ioneita, kuten
natriumsuoloja. Ihmisillä kivunlievitykseen tarvitaan tyypillisesti
15--50 milliampeeria virtaa tuottamaan hyvä kivunlievitys. Mikäli hyvin
kosteutettu iho olisi 1000 Ω ja haluttaisiin saada 25 mA virtaa kudoksen
läpi, tarvittaisiin 1000 Ω x 0,025A eli 25 volttia jännitettä.
Tyypilliset TENS-laitteet voivat tuottaa 40--60 volttia ja jotkin jopa
100 volttia jännitettä. (Quell 2020.)

Käytettävät TENS-tekniikat voidaan jakaa perinteiseen, akupunktuurin
kaltaiseen ja intensiiviseen TENS:n. Näitä erottaa taajuus, voimakkuus
ja pulssin leveys. Perinteisessä TENS:ssä taajuudet ovat välillä 50--100
Hz, voimakkuudet kipua tuottamattomassa ihoaistimuksesta ja
pulssinleveys 50--220 mikrosekuntia. Akupunktuurin kaltaisessa TENS:ssä
käytetään lisäksi matalia taajuuksia välillä 2--4 Hz, korkeampaa
voimakkuutta aina maksimikivun tuntemukseen saakka ja pulssinleveys voi
olla 100--400 mikrosekuntia. Intensiivisessä TENS:ssä käytetään 200 Hz
taajuutta ja kivunsiedon maksimin voimakkuutta. Keskeiset kipua estävät
vaikutukset TENS: n aikana tapahtuvat monimutkaisen vuorovaikutuksen
kautta kiihottavien ja estävien välittäjäaineiden ja
neuromodulaattoreiden välillä, joihin vaikuttaa osittain pulssivirran
taajuus. Vaikutusmekanismit kohdistuvat ensisijaisesti kipuärsykkeitä
johtaviin hermoihin, jotka vievät aistimuksia aivoihin, ääreishermojen
antidromiseen aktivointiin ja moniin välittäjäaineisiin.
Välittäjäaineista vaikutus ääreishermostossa liittyy esimerkiksi
opioideihin, serotoniiniin, asetyylikoliiniin, noradrenaliiniin,
gammavoihappoon (GABA) sekä reseptoreihin kuten 5-HT2 ja 5-HT3 ja myös
selkäytimen deltaopioidi reseptoreihin ja aspartaatin ja glutamaatin
tasoihin. (Johnsson 2007; Johnsson 2021.) Välittäjäaineiden merkitystä
hermoston toiminnassa olen avannut aiemmin hermoston toimintaan
liittyvässä kappaleessa, mutta olen jättänyt pois pohdinnat
reseptoreiden ja välittäjäaineiden välisen affiniteetin merkityksestä.
Toisin sanoen, välittäjäaineen ja hormonin ja niitä lukevien
reseptoreiden välillä vallitseva tasapainotila voi olla toimiva, vaikka
välittäjäainetta olisi vähän ja reseptoreita paljon, tai
välittäjäainetta paljon ja reseptoreita vähän.

Pientaajuusstimulointi on tehokasta kroonisen kivun, jäykkyyden ja
turtumuksen lievittämisessä. Sillä on vaikutusta kipua lievittävien
aineiden eritykseen sekä verenkierron vilkastumiseen. Lihakset
supistuvat ja rentoutuvat pientaajuusvirtauksen mukaisesti. Silloin kun
lihas rentoutuu, suuri määrä verta virtaa lihaksen sisään ja kun lihas
supistuu, kuona-aineita sisältävä veri virtaa lihaksesta ulos. Tätä
toistettaessa veri virtaa sujuvammin ja verenkierto paranee
käsiteltävällä alueella. Kun pientaajuussähkövirta kulkeutuu
kipualueelle, vaikuttaa se kivunvälitysmekanismeihin.
Pientaajuussähkövirta vähentää muun muassa kiputuntemusten välitystä
aivoihin. Suurtaajuusstimulointi on sen sijaan tehokasta akuutin
hermokivun lievityksessä ja se on erityisen tehokasta kiputuntemusten
pikaisessa estämisessä pientaajuusstimulaatioon verrattuna. (Omron
2022.)

Nykyiset TENS-laitteet vaikuttavat perustuvan vanhoille patenteille.
Esimerkiksi Omronin TENS-laitteelle on myönnetty useita patentteja ja se
hyödyntää myös muiden tuottamia patentteja. Järkevintä on tässä
yhteydessä tarkastella EspaceNet (1994) patenttia, jossa käsitellään
mikroprosessoriohjattua hermo ja lihas- stimulaattoria. Patentti on
myönnetty yhdysvaltalaiselle keksijälle Paul T. Kolenille vuonna 1993.
Patentin mukaan laite lähettää moduloitua pulssitaajuutta, jonka
aaltomuodon voimakkuus, taajuus ja amplitudi voidaan säädellä
mikroprosessoriohjatusti. Tämä mahdollistaa erilaisten ohjelmien
tallentamisen pysyväismuistiin eri käyttötarkoituksia varten, kuten
esimerkiksi kivun lievitykseen tai turvotuksen laskemiseen
kohdealueella, joihin elekrodit on kytketty. Prosessorilla voidaan myös
vähentää polttavuuden tunnetta kohdealueella. Patentin taustatietojen
mukaan kivunlievityksessä sähköimpulssien vaikutus on tiedetty pitkään,
mutta vaikutusmekanismeja ei täysin tunneta, vaikka erilaisia
hypoteeseja onkin esitetty alkaen vuodesta 1965. EspaceNet (1994.)
Keskeistä on tieto siitä, että kiputuntemukseen liittyy hermoimpulssin
aaltomuoto, pulssin toistotaajuus, pulssin kesto, pulssin amplitudi ja
pulssin modulaatio.

Yleisesti ottaen, TENS-laitteen hyödyksi voi laskea sen, ettei kivun
lievitykseen tarvita lääkkeitä, leikkausta tai psykiatrisia menetelmiä.
Taustatietojen mukaan TENS-hoitoon ei tiedetä liittyvän
haittavaikutuksia.

# Tutkimuksia TENS-hoidoista

TENS elektroterapiaa on tutkittu vuosikymmeniä moneen eri
käyttökohteeseen. Artikkelissa Resolving Long-Standing Uncertainty about
the Clinical Efficacy of Transcutaneous Electrical Nerve Stimulation
(TENS) to Relieve Pain: A Comprehensive Review of Factors Influencing
Outcome Johnsson (2021) tuo esille sen, että TENS-hoidon tehokkuudesta
on tehty 50 vuotta tutkimuksia, mutta kliininen tehokkuus on edelleen
epävarmaa johtuen osittain tutkimusasetelmista. Kipua voidaan lievittää
farmakologisilla ja ei-farmakologisilla lähtökohdilla.
Elektroterapeuttinen hermostimulaatio, TENS, on kuitenkin suositeltu
kivunlievitysmenetelmä lääketieteessä, hoitotyössä ja fysioterapiassa.
TENS:ä käytetään pääosin oireenmukaiseen helpotukseen erilaisissa
kivuissa kivun alkuperästä riippumatta, kuten neuropaattisessa kivussa
ja neoplastisessa kivussa. TENS:ä käytetään myös virtsan ja ulosteen
pidätysongelmissa, ummetuksessa, pahoinvoinnissa ja oksentelussa,
kserostomiassa, perifeerisessä iskemiassa ja Reynaudin oireyhtymässä,
dementiassa, aivohalvauksessa, turvotuksessa, haavojen parantamisessa,
kudosten uusiutumisessa, kudosten nekroosien vähentämisessä, unessa,
masennuksessa ja koomassa. (Johnsson 2021.)

Käypähoito-c (2015) artikkelissa transkutaaninen sähköinen
hermostimulaatio (TENS) kuukautiskipujen hoidossa todetaan, että TENS
saattaa lievittää kuukautiskipuja ja erityisesti korkeataajuinen TENS
vaikuttaisi tehoavan hyvin. Käypähoito-d (2012) artikkelissa
TENS-sähkövirran vaikutus polven nivelrikon aiheuttamaan kipuun
todetaan, että meta-analyysin perusteella kipu lievittyy merkitsevästi
enemmän TENS-hoitoa saaneilla (SMD -0.85, 95 % luottamusväli -1.36 --
-0.34) kuin verrokeilla.

Tutkimuksessa Effect of transcutaneous electrical nerve stimulation on
human blood beta-endorphin levels Brien, W., Rutan, F. Sanborn, C. ja
Omer, G. (1984) testasivat 42 koehenkilön avulla 80 Hz ja 2 Hz TENS
hoitoa ja mittasivat beta-endorfiinitasoja verenkierrossa ennen hoitoa,
hoidon aikana ja heti hoidon jälkeen. Hoito ei vaikuttanut merkittävästi
beta-endorfiinitasoihin, eikä opiaattiagonisti naloksiini hydrokloridin
injektoiminen vaikuttanut kiputuntemukseen. Tutkimuksessa ei siis
löydetty todisteita siitä, että TENS vaikuttaisi kipukynnykseen tai
verenkierron beta-endorfiinitasoihin.

Tutkimuksessa Acute Effects of Acu-TENS on FEV1 and Blood Β-endorphin
Level in Chronic Obstructive Pulmonary Disease Jones, A., Ngai, S.,
Hui-Chan, C. ja Yu H. (2011) testasivat kaksoissokkomenetelmällä
keuhkoahtaumataudin (COPD) hoitoa siten, että he mittasivat hengen
ahdistusta (FEV), pakotettua uloshengityskapasiteettia (FVC),
hengenahdistuksen visuaalista pistemäärää (DVAS), hengitysnopeutta (RR)
ja veren beta-endorfiinitasoja ennen ja jälkeen hoidon. Placeboon
verrattuna hoito oli 24,2 % tehokkaampi FEV suhteen, DWAS ja RR olivat
14,2 % pienempiä ja hoidon jälkeinen beta-endorfiinitaso merkittävästi
korkeampi kuin placeboryhmällä.

Tutkimuksia on siis tehty paljon ja TENS-hoidosta on hyötyjä ja vähän
haittoja. Tässä vaiheessa on hyvä paneutua testattuun laitteeseen.

# Omron E2 Elite

Omron Healthcare tekee monenlaisia TENS-laitteita. Hintaa laitteilla on
noin 60--120 € riippuen ostopaikasta ja laitteen ominaisuuksista.
Laiteet ovat terveysteknologiaa, koska ne täyttävät CE MDD vaatimukset.
Testaamani Omron E2 Elite on jo vanhentunut malli ja se on maksanut
aikoinaan noin 100 €. Omron E2 ELITE on elektroninen TENS
hermostimulaattori, joka auttaa kiputilojen lieventämisessä ja
vähentämisessä. Aktiivisille ihmisille OMRON E2 ELITE tarjoaa lihaksia
rentouttavaa tai niska-/hartiakipua lievittävää hierontaa. Se helpottaa
myös fyysistä väsymystä ja vilkastuttaa verenkiertoa hoidetuilla
alueilla. (Omron 2022.)

Laitteessa Omron (2022) mukaan on 9 eri ohjelmaa ja niitä valitaan eri
painikkeiden avulla:

1.  Sininen nappula käynnistää nopean lievityksen lihaskipuun. Toiminto
    lievittää akuuttia kipua nopeasti 1200 Hz:n suurtaajuudella. Se
    sopii kivunlievitykseen alaselässä ja nivelissä.

2.  Aluepainikkeella voidaan valita 4 ohjelmaa hartioille,
    jalkapohjille, pohkeille ja alaselälle.

3.  Hierontapainikkeella voidaan valita 4 ohjelmaa: naputus, hieronta,
    painelu ja hankaus.

4.  Neljällä erikoistoimintopainikkeilla voi muokata automaattisia
    ohjelmia ja valita pehmeän, toiston, kohdistetun ja laajan toiminnon
    sekä tasapainosäätimillä vaihtaa hieronnan tasapainoa.

 Tutkimuksiin reflektoiden, Omron TENS:ssä on varsin korkea 1200 Hz
 taajuus, joka tarkoittaisi tällöin hyvää lähtökohtaa esimerkiksi
 kuukautiskivun hoitoon, jota on käsitelty mm. Käypähoito-c (2015)
 artikkelissa.

## Vaarat ja varoitukset

 Laitetta ei saa käyttää, jos ihmisellä on sisäisiä lääketieteellisiä
 siirrännäisiä, kuten sydämentahdistin, tai elämää ylläpitäviä
 laitteita kuten hengityskone tai kehoon kiinnitettyjä laitteita kuten
 EKG. Ennen laitteen käyttöä tulee kysyä lääkärin mielipidettä, jos
 käyttäjällä on akuutti sairaus, pahanlaatuinen kasvain, tartuntatauti,
 raskaus, sydämen vajaatoiminta, korkea kuume, epänormaali verenpaine,
 ihotauti- tai iho-ongelma tai saa lääketieteellistä hoitoa ja olo on
 epämukava. Laitetta ei saa käyttää sydämen lähellä, niskan
 yläpuolella, päässä, suun ympärillä tai sairaalla iholla. Lisäksi
 laitetta ei saa käyttää yhtä aikaa muiden terapeuttisten laitteiden
 kanssa, eikä iholla, jossa on voidetta. (Omron 2022.)

# Laitteen testaus omalla lihaksistollani

Minulla oli sopivasti kipuja molemmissa käsivarsissa lumimyrskyn ja
siihen liittyvän kolmen tunnin kolaamisen jäljiltä. Koska Omron E2
Eliten keskeisin toimintatarkoitus on vähentää kipua, tulee
kivunlievitys testatuksi ja verratuksi siten, että kokeilen vähentää
kipua vain toisesta käsivarrestani.

## Testiasetelma

Aluksi testasin millaisia jännitteitä ja virtoja laite tuottaa
normaalissa käytössä. Minulla ei ole kunnon mittalaitteita
käytettävissä, joten tukeudun Fluke 73III yleismittariin ja sen
näyttämiin. Mittakaapeleiden resistanssi on noin 0,3 ohmia riippuen
kontaktin puhtaudesta. Lisäksi tulee OmronE2 Elite elektrodeihin
menevien kaapeleiden resistanssi, joka vaikuttaisi olevan samaa luokkaa.
Kunnollinen mittaus edellyttäisi oskilloskooppia, kapasitanssimittaria
ja parempaa virtamittaria. Iholle tulevina elektrodeina käytin laitteen
mukana tulleita Omron Eleplus Long Life Pad, jotka olivat juuri pesty
parhaan kontaktin saavuttamiseksi. Laitteessa oli uudet 2 x AAA
paristot.

Aluksi mittasin mitä ihon tasavirtavastus oli silloin kun elektrodit oli
kytketty 20 cm etäisyydellä käsivarren kyynärnivelen ja ranteen välille,
jossa tunsin myös rasituskipua. Tälle kohtaa jää lihaksistossa
radiaalisella (peukalon puoleisella) ja dorsaalisella (kehoon päin)
puolella yhteensä 12 lihasta, jotka ovat jakautuneet kolmeen eri ryhmään
siten, että 3 on radiaalisella puolella, 4 dorsaalisella puolella ja 5
syvällä käden sisällä. Nämä lihakset liikuttavat sormia ja kääntävät
kättä. Lihasten nimissä extensor on ojentaja ja abductor lähentäjä.

Radiaalisella puolella suurin lihas on brachioradialis, muut ovat
extensor radialis longus ja extensor radialis brevis. Brachioralis jää
käsivarressa ylöspäin, jos kämmen osoittaa kasvoihin ja peukalo osoittaa
ylöspäin. Syvällä käsivarressa olevia lihaksia ovat abductor pollicis
longus, supinator, extensor pollicis brevis, extensor pollicis longus ja
extensor indicis. Dorsaalisella puolella, eli pikkurillin puolella
lihaksia ovat anconeus, extensor carpi ulnaris, extensor digiti minimi
ja extensor digitorum.

Hermoimpulssit ja käskyt lihaksistolle voivat tulla aivoista, mutta
muistetaan myös se, että kuten reflekseissä, osa voi olla myös suorien
soluliitosten väliltä tulleita hermoimpulsseja tai heijastua esimerkiksi
selkäydinhermojen kautta.

## Testin tulokset

Mittasin aluksi elektrodien välille syntyvän resistanssin (R) Omron E2
Elite laitteen elektrodijohdon 3,5 mm monoplugin päästä. Resistanssi on
aluksi noin 200 kΩ, mutta alkaa hiljalleen nousta päätyen noin 300 kΩ
arvoihin. Tämä johtunee joko siitä, että elektrodin ja ihon väli kuivuu,
tai sitten jotkin muut kontaktiin vaikuttavat tekijät muuttuvat.
Useamman testikerran jälkeen päättelen siten, että noin 220 kΩ vastus
voisi olla luontevin keinokuorma mittaukseen. Ihmettelen tässä vaiheessa
hieman tutkimuksissa kerrottuja arvoja 100 kΩ ja 1000 Ω, mutta koska
elektrodien etäisyys, eli ihon määrä elektrodien välillä, on merkitsevin
tekijä, oletan 200 kΩ olevan järkevä tulos.

Laitteen tuottamaa jännitettä mittasin käyttämällä selälle tarkoitettua
ohjelmaa ja elektrodien asetusta, joka jakaa pulssin tasaisesti koko
elektrodin alueelle. Valitsin selkäohjelman siksi, että se vaikuttaisi
antavan amplitudiltaan korkeimpia ja tiheimpiä pulsseja heti alusta
saakka, jolloin hidas Fluken yleismittari kerkeäisi mitata niitä.
Rentoutusohjelmassa on erilainen ohjelma ja oletettavasti vaikeammin
mitattavissa.

Keinokuormaksi ihoa korvaamaan laitoin 0,5W 220 kΩ vastuksen (punainen,
punainen, keltainen, ruskea). Yleismittarilla mitattuna vastuksen arvo
näyttää 224 kΩ, jossa on tällöin mukana myös mittajohdon ja kontaktin
resistanssi. Silloin kun keinokuormana oli 220 kΩ vastus, jännite
vastuksen yli liikkui muutamissa millivolteissa. Tasavirtaa kovimpien ja
pitkäkestoisimpien pulssien aikana näkyi mittarissa noin 0,01 mA. Tämä
kertoisi siitä, ettei pulssimaisia jännite- tai virtapiikkejä voi oikein
mitata tavallisella yleismittarilla.

Mikäli yleismittarin mittapäät ovat ihon alla kohdissa, joissa
elektrodit ovat kiinni, jännite vaikuttaa liikkuvan samoissa lukemissa
kuin keinokuormavastuksen yli. Virtaa tasavirta-alueella mitattuna meni
saman verran, mutta vaihtovirta-alueella mitattuna virtaa meni välillä
0,01--0,038 A. Omron E2 TENS-laitteessa oli asetus 8/10 voimakkuutena,
joka on mielestäni erittäin voimakas asetus.

Omron (2022) käyttöohjekirjan mukaan suurin virrankulutus on 40 mA,
jolloin 2 x AAA paristoa riittävät noin kolme kuukautta. Ottaen huomioon
laitteen käyttämän energian, josta osa muuttuu lämmöksi, mittaamani
virta 0,038 A on todennäköisesti lähellä maksimia, vaikka energiaa
varattaisiinkin esimerkiksi kondensaattoriin ennen purkausta
elektrodeihin.

Kokeilin mitata virtaa myös kytkemällä elektrodeille menevät johdot
suoraan yleismittariin ampeerimittauksen alueella, jolloin resistanssi
on käytännössä mittajohtojen ja laitteen omien johtojen resistanssi,
ehkä noin ohmin luokkaa. Laite näyttä tuolloin samoja virtoja kuin
keinokuormaankin. Jännitettä mitatessa ilman keinokuormaa laite
sulkeutui, eli ilmeisesti Omron E2 mittaa kuormaa ennen kuin alkaa
syöttämään jännitettä elektrodeille. Voisi myös olettaa syöttöjännitteen
vaihtelevan havaitun kuorman, eli ihon aiheuttaman vastuksen mukaisesti,
mutta testini oikosuljetulla ampeerimittauksella ei oikein antanut tähän
vastausta.

Mikäli pohtii Quell (2020) artikkelia siitä, että kipua lieventävä
virtamäärä (I) olisi 15-50 mA, niin 220 kΩ vastuksella (R) tarvittaisiin
U = I \* R kaavan mukaan 3300--11 000 volttia jännitettä! Voitaneen
todeta, että joko testiasetelmani oli täysin tuhoon tuomittu, tai sitten
Quell (2020) arvioitu 1000 Ω vastus ja artikkelissa mainitut jännitteet
40--120 V perustuvat väärille olettamille.

Oli syy arvojen epäloogisuudelle mikä tahansa, niin ihon impedanssilla,
eli vaihtovirtavastuksella ei ole merkitystä, vaikka niin voisi olettaa.
Asetelmassa, jossa käteen kytketään elektrodit optimaalisiin (OSS) ja
epäoptimaalisiin (SSS) kohtiin ja sokkoistettuna tutkittiin
kahtakymmentä neljää koehenkilöä käyttämällä 30 minuutin aja 100 Hz
taajuutta ja 100 mikrosekunnin pulssin leveyttä kovalla, mutta ei
kivuliaalla amplitudilla, impedanssit vaihtelivat epäoptimaalisen kohdan
impedanssista 17.69±1.24 Ω optimaalisen kohdan impedanssiin 3.53±0.57 Ω
(P=0.007). Eroja testihenkilöt eivät tehossa kuitenkaan havainneet.
(Vance, C, Rakel, B, Dailey, D & Sluka, K. 2015.)

Loppujen lopuksi tärkeintä oli testata se, väheneekö kipu TENS-hoidolla.
Testasin kivun vähentymistä rentoutusohjelmalla vasempaan käteeni.
Käytin tällä kertaa ohjelmana rentoutusohjelmaa viiden minuutin ajan.
Testin jälkeen kipu oli selvästi lievittynyt ja kipu ei palannut
iltapäivän aikana. Oikeassa kädessäni kipu tuntui aluksi entiseen
malliin ja väheni pikkuhiljaa iltapäivän aikana.

# TENS-laite kivunlievityksessä ja farmakologiset lääkkeet

Ottaen huomioon TENS:n potentiaalin ei-farmakologisena
kivunlievittäjänä, jonka käyttöön ei liity juurikaan haittavaikutuksia,
luulisi sen olevan ensimmäinen vaihtoehto kivunlievitykseen. Johnsson
(2021) mukaan näyttöön perustuvassa hoidossa laite on osoittautunut
hyväksi ja joidenkin metatutkimusten mukaan TENS:n teho on akuutissa
kivussa noin 26,5 % (vaihteluväli −6 -- 51 %) enemmän kuin lumeella.
Hänen mukaansa erilaisiin kroonisiin kiputiloihin TENS:stä löytyy
tieteellisesti vakuuttavaa näyttöä moneen eri kiputilaan.

Tutkimusten metakatsauksessa Literature Review and Meta-Analysis of
Transcutaneous Electrical Nerve Stimulation in Treating Chronic Back
Pain Wu, L., Weng, P, Chen, C., Huang, Y., Tsuang, Y. & Chiang, C.
(2018) vertailevat TENS-hoitoa ja muita hermostimulaatiomenetelmiä (NST)
kroonisessa alaselkäkivussa ja toteavat, että TENS ei vaikuttaisi
parantavan alaselkäkipua, mutta TENS voi tuottaa lyhytkestoista hyötyä
liikuntakykyyn. Toisaalta kuitenkin Käypähoito (2014) artikkelissa TENS
kroonisessa alaselkäkivussa tulos kroonisen selkäkivun osalta on
päinvastainen, eli TENS saattaa hieman lievittää kroonista alaselkäkipua
lumehoitoon verrattuna mutta ei vaikuta toimintakykyyn. Tämä on ainakin
yksi näkökulma verrattaessa TENS-hoitoa esimerkiksi parasetamoliin, jota
käsittelen myöhemmin.

Artikkelissa Transcutaneous electrical nerve stimulation for acute pain
Johnson, M., Paley, C. Howe, T. ja Sluka K. (2015) on tuotu esille
Cochrane-instituutin hallinnoimista kontrolloitujen ja satunnaistettujen
kokeiden (RCT) tietokannasta (CENTRAL), Cochrane kirjastojen MEDLINE,
EMBASE, CINAHL ja AMED sitä miten TENS toimii akuuttiin kipuun.
Kriteriat täyttäviä tutkimuksia löytyi 19 kappaletta käsittäen 1346
potilasta ja näistä eri tavoin pääteltynä voidaan luotettavasti todeta,
että TENS-hoidosta on kivun lievitykseen merkittävää hyötyä.

Käypähoito-b (2019) artikkelissa Fysioterapia aistitoimintojen
häiriöihin ja kipuun MS-taudissa on todettu, että TENS-kipuhoito saattaa
vähentää MS-kuntoutujien selkäkipua, yläraajojen kipua tai
epämiellyttäviä tuntemuksia lumehoitoon verrattuna. Lisäksi se saattaa
vähentää yläraajojen kipua tai epämiellyttäviä tuntemuksia yhtä
tehokkaasti kuin nortriptyliinilääkitys.

Tutkimukset siis puoltavat ajatusta tarkastella akuutin kivun hoitoa
sekä farmakologisista että TENS-hoidon näkökulmista, vaikka vertailevaa
tutkimusta ei ole tehtykään.

## Number Needed to Treat ja Number Needed to Harm

Vertailtaessa TENS:ä farmakologisiin lääkkeisiin on hyvä tarkastella
lähemmin mitä tarkoittavat NNH ja NNT. Alussa toin esille NNH, NNT ja
placebon määrittelyt. Samaan päätyy professori Juhani Knuuti (2018),
joka avaa blogissaan näitä käsitteitä hyvin. Hänen mukaansa NNT ja NNH
kertovat suoraan hoitojen tehosta. NNT tarkoittaa sitä, miten montaa
potilasta tulee hoitaa, jotta yksi saisi hoidosta hyödyn. Paras luku on
1, joka tarkoittaa sitä, että kaikki hoidetut potilaat paranevat tai
saavat hyödyn lääkkeestä. Sama pätee NNH, eli kuinka monta potilasta saa
haittoja hoidosta. Tärkeää on myös havaita mitä ollaan hoitamassa, eli
NNT ja NNH arvoja ei saa vertailla suoraan keskenään.

Esimerkiksi TENS:llä annettu kivunlievitys vähentää kipua ja siirtää
myöhemmäksi tarvetta käyttää farmakologisia kipulääkkeitä asetelmassa,
jossa työelämässä raskaana olevat naiset ovat satunnaistetun tutkimuksen
kohteena. Tässä kokeessa TENS:n NNT-arvoksi saatiin 2, joka tässä
tutkimuksessa tarkoittaa sitä, että joka toinen nainen kertoi kivun
olevan kipuasteikolla alle 7 ja joka toinen kertoi kivun olevan yli 7.
Haittoja ei havaittu. (Santana, L. Gallo, R. Ferreira, C. Duartea, G.,
Quintana, S. & Marcolin, A. 2016.)

Vastaavasti farmakologisessa lähtökohdassa parasetamoli on täysin
tehoton esimerkiksi selkäkipuun, sillä Cochrane (2022) mukaan edes 4000
mg päiväannoksilla 12 viikon aikana lääke ei ole sen parempi kuin
lumelääke, mutta käytöstä voi seurata todella vakavia haittoja. Tässä
artikkelissa ei tuoda esille NNT tai NNH arvoja, mutta analgesian eli
kivunlievityksen suhteen yleisesti vaikuttaisi olevan siten, että
lääkeaineen vahvuudella on suuri merkitys. Esimerkiksi parasetamolin NNT
on yhdellä 600 mg annoksella 5,4 ja 1000 mg annoksella 3,7. Vastaavasti
aspiriini 600 mg annoksella NNT on 4,4 ja 100 mg annoksella 4,0 (McQuay,
H. & Moore, R. 2007.)

Ei voi olla pohtimatta sitä moniko selkäkipuinen, tai polvikipuiinen,
käyttää parasetamolia kivunlievitykseen ja moniko nainen syö
kuukautiskipuihin parasetamolia. Olisi todella mielenkiintoista testata
millaiset tutkimustulokset saataisiin parasetamolin ja TENS:n välillä
edellisissä kiputiloissa. Farmakologinen kipulääkitys vaikuttaisi
kuitenkin olevan ensisijainen lähtökohta hoitaa kipua ja se näkyy
lääkehoidon kustannuksista.

## Kipulääkkeistä ja kustannuksista

Kivunlievitykseen myydään reseptittömiä valmisteita, kuten parasetamoli
ja aspiriini. Näitä ja voimakkaampia kipulääkkeitä määrätään reseptillä.
Kipukynnystä nostamaan voidaan käyttää myös esimerkiksi vanhoja
mielialalääkkeitä. Tulehduskipulääkkeistä eniten käytetään ibuprofeenia,
parasetamoli on toiseksi yleisin käytetty kipulääke.

Parasetamoli eli asetaminofeeni, jonka molekulaarinen kaava on C8H9NO2
tai HOC6H4NHCOCH3, myydään todella monilla kauppanimillä kuten Panadoli,
Tylenol, Intensin jne. Biologinen puoliintumisaika parasetamolille on
laskimon sisäisesti annosteltuna 15 mg/painokilo konsentraatiolla 2,5
tuntia. Vaikutusmekanismia ei täysin tunneta, mutta se liittynee
syklo-oksigenaasin toimintareittien estymiseen siinä missä aspiriinin ja
muiden kipulääkkeiden suhteen. Erään hypoteesin mukaan parasetamoli
lisäisi kipukynnystä prostaglandiinien synteesiin liittyvien
syklo-oksigenaasin isoformien cox-1 ja cox-2 vähentymisen johdosta.
Parasetamoli tuottaa analgesian, eli kiputuntemuksen puuttumisen ja
antipyresian, eli kuumeen laskemisen samalla tavoin kuin salisylaatit,
eli kuten aspiriini, mutta parasetamoli ei lisää virtsahapon
lisääntymistä. Parasetamolilla voi olla lieviä tulehdusta vähentäviä
ominaisuuksia joissakin ei-reumaattisissa tapauksissa ja se vähentää
kuumetta vaikuttamalla hypotalamukseen siten, että verisuonet laajenevat
ja kudosten verenkierto lisääntyy, jolloin kehossa oleva lämpö haihtuu
nopeammin. (PubChem-a 2021.)

Parasetamolin ATC-luokka on N02BE01. Kirjain N tarkoittaa hermostoon
vaikuttavia lääkeaineita ja numero 02 tarkoittaa analgeenejä, eli
kiputuntemusten poistoon tarkoitettuja lääkeaineita. Parasetamolia on
myös yhdistelmälääkkeissä, kuten N02AJ06 kodeiinin kanssa yhdistettynä
(esim. Panacod) ja N02AJ13 Tramadoli parasetamoli.

KELA:n ylläpitämästä Kelasto-tietokannasta voimme ATC-luokan avulla
tarkastella minkä verran lääkärit ovat määränneet parasetamolia
reseptillä ja paljonko niistä on tullut kustannuksia. Vuonna 2020
parasetamolia N02BE01 kirjoitettiin 2 122 723 reseptiä 855 790 ihmiselle
ja tästä syntyi kustannuksia 17 873 858 euroa. N02AJ06 kodeiinin ja
parasetamolin yhdistelmää kirjoitettiin 214 812 ihmiselle ja 474363
reseptiä, josta syntyi 3 935 795 euron kustannukset. N02AJ13 tramadolin
ja parasetamolin yhdistelmää kirjoitettiin 6 904 reseptiä 18 557
ihmiselle ja tästä syntyi kustannuksia 202 682 euroa. Yhteensä
kustannuksia syntyi siis noin 22 miljoonaa euroa pelkästään resepteillä
määrätyistä parasetamolivalmisteista.

Mikäli tästä resepteillä määrätyistä lääkkeistä voitaisiin korvata 20 %
TENS-hoidolla, tarkoittaisi se silloin 4,4 miljoonan euron säästöjä
vuosittain ja todennäköisesti myös haitat olisivat pienemmät. Laitteen
investointi on monivuotinen, eikä se tuota jätevesiin minkäänlaisia
jäämiä, toisin kuin lääkeaineet, jotka poistuvat pääosin ulosteiden
mukana.

# Kehitysideoita

TENS-laitteen toimintajännite on 3 V ja sen tarvitsema virta hyvin
pieni. Laitteelle saisi USB-portista tarvittavan käyttöjännitteen ja
virran, jolloin laite voisi toimia esimerkiksi kännykän tai tietokoneen
lisälaitteena. Tällöin olisi myös helppo päivittää erilaisia
toimintamoodeja ja mikäli laite olisi osana etäsairaanhoitoa, voisi
laitteen ohjelmia päivittää etänä. Tietokone tai kännykkä toisi myös
mahdollisuuden potilaalle arvioida hoidon tehokkuutta, jolloin laitteen
toimintaa voitaisiin säätää paremmaksi ja toisaalta samalla saataisiin
tutkimuksiin kunnon aineistoa TENS-hoidon vaikuttavuudesta.

Markkinoilla vaikuttaa olevan jo nyt iTens (2022), jossa on hieman tähän
suuntaan toteutettua puettavaa TENS-hoitoteknologiaa. Laitteessa
ohjataan mobiilisovelluksella iholle kiinnitettäviä TENS-elektrodeja.
Fysioterapeuteille on myynnissä ammattikäyttöön tarkoitettuja
TENS-laitteita ja vaikuttaisi siltä, että he myös suosittelevat
kuluttajille suunnattuja TENS-laitteita. Ehkä fysioterapeutit voisivat
jalkauttaa iTens (2022) tyyppisiä ratkaisuita, mikäli lääkärit ja
terveydenhoitopalvelut eivät sitä tee.

Pikaisella katsauksella Kuntaliiton ODA-hankkeissa (2022) saati OmaOlo
(2022) selkäkivun oirearvion tuottamassa ei tuoda TENS:ä esille millään
tavoin. Vaikuttaisi siltä, että OmaOlo (2022) kysymyksissä kysytään
kyllä tuottaako kipulääkitys tarvittavaa kivunlievitystä. Tämä
oletettavasti myös tilastoidaan, jolloin bias lääkehoidon tehokkuudesta
vääristyy suhteessa muihin hoitoihin, joita ei tuoda lomakkeella esille.

# Yhteenveto

Tarkastelin tässä raportissa yleisesti myynnissä olevia
kivunlievitykseen tarkoitettuja TENS-laitteita ja testasin Omron E2
mallista laitetta itseeni. Omron E2 täyttää lääkinnällisten laitteiden
CE-hyväksynnän ja sitä voidaan käyttää virallisena hoitomuotona moneen
kiputilaan, mutta ilmeisesti yli 50 vuoden tutkimukset eivät ole
tuottaneet riittävää näyttöön perustuvaa tulosta, jolla hoitoa
voitaisiin perustella muihin kuin KäypäHoidossa mainittuihin
kuukautiskipuihin, alaselkäkipuihin ja polvikipuihin. Toisaalta on myös
ymmärrettävä kriittisesti lääketieteen lähtökohdan olevan pääosin
farmakologinen, jolloin tällaisten hoitomuotojen yleistyminen voi olla
vastoin farmakologian ideologiaa. Googlen hakutulosten perusteella
joissakin sairaanhoitopiireissä saa lainattua TENS-laitteita kotiin,
joka voisi olla merkki siitä, että TENS voisi olla tulossa laajempaan
käyttöön terveydenhoidossa. Ainakin sitä kannattaisi tarkastella uuden
SOTE:n näkökulmasta muun muassa säästöpotentiaalin ja itsehoidon
näkökulmista.

Laitteen hankintahinta voi olla joillekin yksittäisille ihmisille
liikaa, mutta jos on varaa esimerkiksi urheiluharrastukseen, voi noin
100 € hankintahinta olla aika vähän suhteessa siihen hyötypotentiaaliin,
mitä laitteella on akuuttien kiputilojen, kuten rasituskivun
lievityksessä. Yrityksissä voisi olla myös tällaisia laitteita
esimerkiksi taukohuoneissa tai muissa vastaavissa kohteissa ja
periaatteessa terveyspisteet, kuten Suomen Punaisen Ristin
terveyspisteet voisi hyötyä TENS-hoitomahdollisuudesta.

**Lähdeluettelo**

Brien, W., Rutan, F. Sanborn, C. & Omer, G. 1984. Effect of
transcutaneous electrical nerve stimulation on human blood
beta-endorphin levels. Viitattu 14.02.2022. Saatavilla: DOI:
10.1093/ptj/64.9.1367

Campbell. 2011. Teoksessa Jane B. Reece, Lisa A. Urry, Michael L. Cain,
Steven A. Wasserman, Peter V. Minorsky & Robert B. Jackson, Campbell
Biology (9. painos). Pearson. U.S.A.

CERTIPEDIA. 2022. Certipedia - Certificate Database from TÜV Rheinland.
Viitattu 25.01.2022. Saatavilla: <https://www.certipedia.com/>>

Cochrane. 2022. Paracetamol: widely used and largely ineffective.
Viitattu 01.02.2022. Saatavilla:
<https://uk.cochrane.org/news/paracetamol-widely-used-and-largely-ineffective>>

EspaceNet. 1994. Microprocessor-based nerve and muscle stimulator for
localized application. Viitattu 28.01.2022. Saatavilla:
<https://worldwide.espacenet.com/patent/search/family/025675962/publication/EP0620025A1?q=pn%3DEP0620025A1>>

EUDAMED. 2022. EUDAMED - European Database on Medical Devices. Viitattu
25.01.2022. Saatavilla:
<https://ec.europa.eu/tools/eudamed/#/screen/home>>

EUR-LEX. 1993. NEUVOSTON DIREKTIIVI 93/42/ETY. Viitattu 26.01.2022.
Saatavilla:
<https://eur-lex.europa.eu/legal-content/FI/TXT/HTML/?uri=CELEX:01993L0042-20071011&from=EN>>

Fimea. 2014. LÄÄKETIETOA FIMEASTA 2/2014. Viitattu 04.02.2022.
Saatavilla:
<https://sic.fimea.fi/documents/721167/862630/26268_2_14_44-45_Vortioksetiini.pdf>>

Fish, R. ja Geddes, L. 2009. Conduction of Electrical Current to and
Through the Human Body: A Review. Viitattu 01.02.2022. Saatavilla:
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2763825/>>

Heino & Vuento. 2018. Biokemian ja solubiologian perusteet. Sanoma Pro.

Hämäläinen, H. 2017. Luento Mielen toiminta ja mielen tasapaino:
Hermosolut, synapsit ja välittäjäaineet. Turun yliopisto, 16.11.2017.

iTens. 2022. Viitattu 14.02.2022. Saatavilla: <https://itens.com/>>

Kelasto. 2020. Dispensations by ATC class. Viitattu 27.01.2022.
Saatavilla:
[https://tilastot.kela.fi/ibmcognos/bi/?perspective=classicviewer&pathRef=.public_folders%2FRaportit%2F91%2BEtuudet%2F9105%2BL%25C3%25A4%25C3%25A4kkeet%2FSairausvakuutuksesta%2Bkorvattavat%2Bl%25C3%25A4%25C3%25A4ketoimitukset%2B%25289105RS001%2529&id=i1465D29B12B943909136FA98D42354D8&objRef=i1465D29B12B943909136FA98D42354D8&action=run&format=HTML&cmPropStr=%7B%22id%22%3A%22i1465D29B12B943909136FA98D42354D8%22%2C%22type%22%3A%22report%22%2C%22defaultName%22%3A%22Sairausvakuutuksesta%20korvattavat%20l%C3%A4%C3%A4ketoimitukset%20%289105RS001%29%22%2C%22permissions%22%3A%5B%22execute%22%2C%22read%22%2C%22traverse%22%5D%7D](https://tilastot.kela.fi/ibmcognos/bi/?perspective=classicviewer&pathRef=.public_folders%2FRaportit%2F91%2BEtuudet%2F9105%2BL%25C3%25A4%25C3%25A4kkeet%2FSairausvakuutuksesta%2Bkorvattavat%2Bl%25C3%25A4%25C3%25A4ketoimitukset%2B%25289105RS001%2529&id=i1465D29B12B943909136FA98D42354D8&objRef=i1465D29B12B943909136FA98D42354D8&action=run&format=HTML&cmPropStr=%7B%22id%22%3A%22i1465D29B12B943909136FA98D42354D8%22%2C%22type%22%3A%22report%22%2C%22defaultName%22%3A%22Sairausvakuutuksesta%20korvattavat%20lääketoimitukset%20%289105RS001%29%22%2C%22permissions%22%3A%5B%22execute%22%2C%22read%22%2C%22traverse%22%5D%7D)

Kuntaliitto. 2022. ODA-projektin kautta sosiaali- ja terveyspalvelut
loikkaavat digiaikaan. Viitattu 14.02.2022. Saatavilla:
<https://www.kuntaliitto.fi/sosiaali-ja-terveysasiat/oda-projektin-kautta-sosiaali-ja-terveyspalvelut-loikkaavat-digiaikaan>>

Käypähoito. 2014. TENS kroonisessa alaselkäkivussa. Viitattu 14.02.2022.
Saatavilla: <https://www.kaypahoito.fi/nak08252>>

Käypähoito-b. 2019. Fysioterapia aistitoimintojen häiriöihin ja kipuun
MS-taudissa. Viitattu 14.02.2022. Saatavilla:
<https://www.kaypahoito.fi/nak05367>>

Käypähoito-c. 2015. Transkutaaninen sähköinen hermostimulaatio (TENS)
kuukautiskipujen hoidossa. Viitattu 14.02.2022. Saatavilla:
<https://www.kaypahoito.fi/nak08495>>

Käypähoito-d. 2012. TENS-sähkövirran vaikutus polven nivelrikon
aiheuttamaan kipuun. Viitattu 14.02.2022. Saatavilla:
<https://www.kaypahoito.fi/nak07846>>

Linnavuori, K. 2015. Uusi lääkinnällisten laitteiden EU-asetus. Viitattu
25.01.2022. Saatavilla:
<https://www.fimea.fi/documents/160140/765540/28338_Linnavuori_ATMP_2015-02-04_2_.pdf>>

McQuay, H. & Moore, R. 2007. Dose--response in direct comparisons of
different doses of aspirin, ibuprofen and paracetamol (acetaminophen) in
analgesic studies. Viitattu 01.02.2022. Saatavilla:
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2000740/>>

MDR. 2022. Medical Device Regulation. Conformity assessment based on a
quality management system and on assessment of technical documentation.
Viitattu 27.01.2022. Saatavilla:
<https://www.medical-device-regulation.eu/2019/08/14/annex-ix/>>

MDR-b. 2022. Medical Device Regulation. Classification rules. Viitattu
27.01.2022. Saatavilla:
<https://www.medical-device-regulation.eu/2019/08/08/annex-viii/>>

Johnsson, M. 2007. Transcutaneous Electrical Nerve Stimulation:
Mechanisms, Clinical Application and Evidence. Viitattu 27.01.2022.
Saatavilla: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4589923/>>

Johnsson, M. 2021. Resolving Long-Standing Uncertainty about the
Clinical Efficacy of Transcutaneous Electrical Nerve Stimulation (TENS)
to Relieve Pain: A Comprehensive Review of Factors Influencing Outcome.
Viitattu 01.02.2022. Saatavilla:
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8070828/>>

Johnson, M., Paley, C. Howe, T. & Sluka K. 2015. Transcutaneous
electrical nerve stimulation for acute pain. Viitattu 14.02.2022.
Saatavilla: DOI: 10.1002/14651858.CD006142.pub3

Jones, A., Ngai, S., Hui-Chan, C. & Yu H. 2011. Acute Effects of
Acu-TENS on FEV1 and Blood Β-endorphin Level in Chronic Obstructive
Pulmonary Disease. Viitattu 14.02.2022. Saatavilla:
<https://pubmed.ncbi.nlm.nih.gov/22314671/>>

Knuuti, J. 2018. Ylidiagnostiikka ja ylihoito: Number needed to treat.
Blogista Terveys & Tiede. Viitattu 01.02.2022. Saatavilla:
<https://blogit.ts.fi/terveys-tiede/ylidiagnostiikka-ja-ylihoito-osa-2/>>

Loh, H., Tseng, L., Wei, E. & Li C. 1976. Beta-endorphin is a potent
analgesic agent. Viitattu 14.02.2022. Saatavilla: doi:
10.1073/pnas.73.8.2895

OmaOlo. 2022. Alaselkäkipu tai -vamma. Viitattu 14.02.2022. Saatavilla:
<https://www.omaolo.fi/palvelut/oirearviot/2>>

Omron. 2022. Elektroninen hermostimulaattori E2 Elite (HV-F127-E)
käyttöohje. Liite 2.

Paavilainen, P. 2016. Toimivat aivot. Teoksessa Paavilainen Petri,
Toimivat aivot. Kognitiivisen neurotieteen perusteita. Ensimmäinen
painos. Edita Publishing Oy, 1--368.

Penttonen, M. 2017. Luento Hermostonkehitys ja muovautuvuus. Jyväskylän
yliopisto, 21.11.2017.

PubChem. 2021. Acetaminophen. Viitattu 31.01.2022. Saatavilla:
<https://pubchem.ncbi.nlm.nih.gov/compound/1983>>

Quell. 2020. TENS Under the Hood: Maximum Voltage. Viitattu 27.01.2022.
Saatavilla:
<https://www.quellrelief.com/blog/tens-under-the-hood-maximum-voltage/>>

Santana, L. Gallo, R. Ferreira, C. Duartea, G., Quintana, S. & Marcolin,
A. 2016. Transcutaneous electrical nerve stimulation (TENS) reduces pain
and postpones the need for pharmacological analgesia during labour: a
randomised tria
<https://www.sciencedirect.com/science/article/pii/S1836955315001289>>

Vance, C, Rakel, B, Dailey, D & Sluka, K. 2015. Skin impedance is not a
factor in transcutaneous electrical nerve stimulation effectiveness.
Viitattu 01.02.2022. Saatavilla:
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4547643/>>

Yanagisawa, M. 2011. Teoksessa Jane B. Reece, Lisa A. Urry, Michael L.
Cain, Steven A. Wasserman, Peter V. Minorsky, Robert B. Jackson,
Campbell Biology (9. painos). Pearson. U.S.A.

Wu, L., Weng, P, Chen, C., Huang, Y., Tsuang, Y. ja Chiang, C. 2018.
Literature Review and Meta-Analysis of Transcutaneous Electrical Nerve
Stimulation in Treating Chronic Back Pain. Viitattu 14.02.2022.
Saatavilla: DOI: 10.1097/AAP.0000000000000740