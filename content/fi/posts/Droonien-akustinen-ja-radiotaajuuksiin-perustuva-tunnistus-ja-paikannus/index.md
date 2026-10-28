---
title: "Droonien akustinen ja radiotaajuuksiin perustuva tunnistus ja paikannus"
date: 2025-09-25
tags: ["ai", "droonit", "maanpuolustus", "passiivinen paikannus", "tekoäly", "koneoppiminen", "hamradio", "radioamatöörit", "säteilytutkimus", "turvallisuus"]
summary: "Tässä teknisessä selvityksessä käsitellään droonien tunnistamista ja paikantamista akustisilla ja radiotaajuuksilla perustuen, erityisesti passiivisten koherenttien paikannusjärjestelmien (PCL) avulla. Artikkelissa korostetaan teknologian salaisuutta, kansalaistiedeen soveltamista ja tekoälyn roolia tulevaisuuden turvallisuusjärjestelmissä."
---

# Droonien akustinen ja radiotaajuuksiin perustuva tunnistus ja paikannus

## Executive Summary

Tämä raportti tarjoaa perusteellisen analyysin monikerroksisen passiivisen valvontaverkoston toteutettavuudesta, strategisesta arvosta ja teknisestä arkkitehtuurista vapaaehtoisen maanpuolustuksen tueksi. Raportti syntetisoi kahden erillisen tekstin "Droonien akustinen ja radiotaajuuksiin perustuva tunnistus ja paikannus" ja Passive Radar Systems for Voluntary National Defense: Leveraging Civilian Infrastructure for Enhanced Situational Awareness käsitteitä ja ehdottaa järjestelmää, joka hyödyntää olemassa olevaa siviili-infrastruktuuria – mukaan lukien radioamatööriverkostoja, matkapuhelinverkon signaaleja ja mobiililaitteita – passiiviseen havaitsemiseen ja ilmassa olevien uhkien, erityisesti miehittämättömien ilmailulaitteiden (UAV) ja drooniparvien, jäljittämiseen. Analyysi kuvaa passiivisen koherentin paikannuksen (PCL) yhdistämistä akustiseen ja radiotaajuus (RF)-pohjaiseen havainnointiin, mikä luo kestävän, resilientin ja salaisen havaitsemiskyvyn. Raportti arvioi radioamatööriyhteisön kriittistä roolia ja soveltuvimpia digitaalisia viestintäprotokollia vapaaehtoisverkoston tiedonvaihtoon. Lopuksi se vertailee tätä puolustuslähtöistä paradigmaa siviili-ilmailun Unmanned Traffic Management (UTM) ja Remote ID -järjestelmiin ja korostaa ei-yhteistyöhaluisen valvontakerroksen täydentävää ja välttämätöntä roolia. Raportti antaa suosituksia strategisista, teknisistä ja oikeudellisista puitteista, joita tällaisen hankkeen tehokas ja eettinen toteuttaminen edellyttää.

* * *

## 1. Johdanto: Ilmauhkien muuttuva haaste ja siviilien resilienssi

### 1.1. Droonien asymmetrinen uhka

Edullisten, kaupallisesti saatavilla olevien ja helposti modifioitavien miehittämättömien ilma-alusten (UAV) yleistyminen on luonut merkittävän asymmetrisen uhan kriittiselle kansalliselle infrastruktuurille ja yleiselle turvallisuudelle. Näitä laitteita voidaan käyttää tiedusteluun, valvontaan ja hyökkäyksiin, ja ne muodostavat haasteen, johon perinteiset puolustusjärjestelmät eivät aina ole optimoituja vastaamaan. Tässä kontekstissa tarvitaan innovatiivisia, kustannustehokkaita ja passiivisia havaitsemisratkaisuja, jotka täydentävät perinteisiä sotilaallisia kykyjä ja laajentavat tilannekuvaa.1

### 1.2. Kansalaislähtöisen varautumisen perintö

Kansalaislähtöisen puolustusverkoston ajatus ei ole uusi. Suomen radioamatööriyhteisöllä on rikas historia resilienttinä viestintä- ja tiedusteluverkkona "poikkeusoloissa".1 Minun radioamatööriaikani kutsumerkillä OH4BC henkilökohtainen kokemus Neuvostoliiton "The Buzzer" (UVB-76) -aseman voimakkaista lähetyksistä kylmän sodan aikana korostaa radiotaajuuksien strategista merkitystä ja sopeutumiskyvyn tarvetta.1 Jo tuolloin radioamatöörit pystyivät keräämään ja levittämään tietoa maailmalta tehokkaammin kuin perinteiset viralliset kanavat. Tämä historiallinen ennakkotapaus todistaa, että yhteisöllä on syvällinen valmius ja kyky osallistua kansalliseen resilienssiin.1 Esimerkiksi HF-pohjaisten TCP/IP-solmujen käyttö 1990-luvun alussa työskennellessäni poliisilaitoksella "poikkeusolojen" aikana vahvistaa tätä historiallista yhteyttä.1

### 1.3. Uusi paradigma maanpuolustukselle

Tässä raportissa ehdotettu passiivinen valvontaverkosto nähdään loogisena jatkumona tälle historialliselle perinteelle. Soveltamalla nykyaikaisia passiivisia teknologioita jo hyväksi todettuun organisaatiomalliin voidaan luoda kustannustehokas ja salainen havaitsemisratkaisu. Tämä lähestymistapa siirtää painopistettä kalliista, keskitetyistä ja aktiivisista sotilaallisista järjestelmistä hajautettuun, edulliseen ja passiiviseen kansalaisjohtoiseen verkostoon, mikä parantaa tilannekuvaa ja resilienssiä monenlaisia moderneja ilmauhkia vastaan.1 Erityisesti kun Morse-koodin osaamista ei enää vaadita radioamatöörilupaa varten, harrastuksen esteet madaltuvat, mikä avaa arvokkaan tilaisuuden laajentaa osallistumista.1

* * *

## 2. Passiivisen ilmatilan valvontajärjestelmän yhtenäisteoria

Tämä luku syntetisoi kaksi edellä mainittua ensisijaista lähdetekstiä ja osoittaa, kuinka tekstin 1 strateginen visio voidaan toteuttaa tekstissä 2 kuvattujen teknisten menetelmien avulla luomalla monitasoinen sensorijärjestelmä.

### 2.1. Passiivisen koherentin paikannuksen (PCL) periaatteet

PCL-järjestelmät, jotka tunnetaan myös passiivisina valvonta-, koherentteina tai lois-tutkajärjestelminä, havaitsevat ja jäljittävät kohteita käsittelemällä heijastuksia ympäristön olemassa olevista, ei-yhteistyöhaluisista radiolähteistä.1 Toisin kuin tavanomaiset "aktiiviset" tutkajärjestelmät, jotka lähettävät omia signaalejaan, passiivinen tutka toimii ilman omaa lähetintä, mikä tekee siitä luonnostaan salaisen. Tämä perusero tarjoaa merkittäviä etuja. Koska järjestelmä ei lähetä signaaleja, se on havaitsematon viholliselle ja tarjoaa vahvan salailukyvyn.1 Tämä on erityisen tärkeää kansalaislähtöisessä hankkeessa, koska se pienentää merkittävästi yksittäisten osallistujien altistumista mahdollisille uhkille.1

PCL on myös immuuni tutkasäteilyä vastaan kohdennetuille ohjuksille ja sitä on erittäin vaikea häiritä. Koska järjestelmällä ei ole aktiivista lähetintä, sitä ei voida hyökätä tutkasäteilyä vastaan suojatuilla ohjuksilla, ja koska vastustajat eivät tiedä, mitä ulkoisia signaaleja passiivinen tutka hyödyntää, kohdennettu häirintä on erittäin vaikeaa.1 Tämän lisäksi onboard-lähettimien ja suuritehoisten vahvistimien puuttuminen vähentää merkittävästi laitteistokustannuksia verrattuna tavanomaisiin aktiivisiin tutkajärjestelmiin.1 Tämä kustannustehokkuus sopii täydellisesti strategiaan, jossa hyödynnetään olemassa olevaa, edullista siviililaitteistoa ja infrastruktuuria puolustustarkoituksiin.

Raportti laajentaa tätä käsitettä alkuperäisen kysymyksen pohjalta. Se tarkastelee myös, kuinka matkapuhelimet ja niiden tukiasemat, jotka mittaavat jatkuvasti signaalin voimakkuutta, voisivat toimia "absorbanssimittareina" ja paljastaa drooniparvien tai lentokoneiden läsnäolon signaalin vaimenemisen tai absorboitumisen kautta.1 On tutkittu, että liikkeen ja fyysisten esteiden aiheuttamia Received Signal Strength Indicator (RSSI) -arvojen vaihteluita voidaan hyödyntää passiiviseen liikkeentunnistukseen, sillä fyysiset esteet voivat aiheuttaa signaalin tehon laskun vaimenemisen, varjostuksen ja absorption vuoksi.1 Tämä lähestymistapa laajentaa passiivisen havaitsemisen soveltamisalaa perinteisen heijastuspohjaisen tutkan ulkopuolelle.

### 2.2. Monianturifuusio parantaa havaitsemista

Tässä osiossa yhdistetään kaksi ensisijaista tutkimusmateriaalia, mikä osoittaa, kuinka passiivinen tutka on täydennetty muilla passiivisilla havaitsemismenetelmillä, erityisesti akustisella ja RF-pohjaisella valvonnalla. Tällä tavalla kaksi lähdetekstiä sulautuvat yhteen muodostaen entistä vahvemman havainnointijärjestelmän.

### 2.2.1. Akustinen allekirjoitusanalyysi

Akustinen havainnointi toimii monianturijärjestelmän kriittisenä, ei-RF-perusteisena kerroksena. Pienet moniroottoridrooneiden potkurit ja moottorit tuottavat tyypillisen "surisevan" tai "pörisevän" äänen, joka sisältää tunnistettavia taajuuskomponentteja.1 Herkkiä tai parabolisia mikrofoneja käyttämällä droonin ääntä voidaan kerätä jopa useiden satojen metrien etäisyydeltä, kunhan ympäristön melu ei ole liian voimakasta.1 Koneoppimisalgoritmeja voidaan kouluttaa tunnistamaan nämä ainutlaatuiset akustiset allekirjoitukset, ja tietyissä kokeissa on saavutettu jopa 98 prosentin tunnistustarkkuus vaihtelevissa olosuhteissa.1 Tämä menetelmä on elintärkeä erityisesti "hiljaisten" droonien havaitsemisessa, jotka lentävät radiohiljaisuudessa ilman aktiivista radiolinkkiä ohjaajaan.1

### 2.2.2. RF-spektrin seuranta ja kolmiomittaus

Vaikka akustista havainnointia rajoittavat ympäristön melu ja kantama (yleensä 300–500 metriä), RF-seuranta tarjoaa huomattavasti pidemmän kantaman.1 Droonit käyttävät usein tunnettuja taajuuskaistoja (esim. 2,4 GHz, 5,8 GHz, 433 MHz) ohjaukseen, telemetriaan ja videolinkeihin.1 Tarkkailemalla laajaa spektrin aluetta RF-sensoriverkosto voi havaita droonikohtaisia signaaleja ja jopa tunnistaa droonin tyypin sen ainutlaatuisen "radiosormenjäljen" perusteella. Droonin ohjaussignaalit voivat näkyä spektrissä purskeina tai jatkuvina kantoaaltoina.1 Modernit RF-analysaattorit ja -sensorit voivat nopeasti skannata laajoja kaistanleveyksiä ja tunnistaa signaaleja, jotka viittaavat drooniin. Nykyaikainen lähestymistapa yhdistää tunnettuihin signaaleihin perustuvan analyysin ja poikkeamien etsintään perustuvan analyysin tekoälyn avulla, mikä mahdollistaa myös ennestään tuntemattomien droonityyppien havaitsemisen.1

Kaksi lähdetekstiä käsittelevät siis erillisiä passiivisia havaitsemismenetelmiä: toinen keskittyy PCL-järjestelmiin, jotka hyödyntävät siviilisignaaleja, kun taas toinen kuvaa akustisia ja RF-pohjaisia menetelmiä. Syvempi tarkastelu paljastaa, etteivät ne ole erillisiä, vaan ne ovat toisiaan täydentäviä kerroksia yhdessä, kestävässä järjestelmässä. Tämä monitasoinen lähestymistapa, joka on todellista antureiden "fuusiota", luo järjestelmän, jota on paljon vaikeampi ohittaa kuin mitään yksittäistä menetelmää. Esimerkiksi autonomisesti ja radiohiljaisuudessa lentävää droonia ei RF-ilmaisin havaitsisi, mutta PCL- ja akustiset sensorit saattaisivat tunnistaa sen. Häiritty drooni havaittaisiin PCL- ja akustisilla sensoreilla. Vastaavasti RF-ilmaisin saattaisi havaita lennokin, jolla on pieni tutkaheijastus, mutta aktiivinen RF-linkki. Vaikka drooni olisi vaimentanut kaikenlaista RF-liikennettä, sen ääni on lähes mahdoton vaimentaa täysin, joten akustinen sensoriverkosto voisi silti havaita sen.1 Tämä kerroksellinen havainnointi, jossa jokainen kerros kattaa toisen heikkoudet, on äärimmäisen tärkeää uhkien havaitsemiseksi monimutkaisissa tilanteissa.

### 2.3. Uhkan paikantaminen: kolmiomittaus ja ohjaajan tunnistaminen

Monianturijärjestelmän etu ulottuu pelkkää havaitsemista pidemmälle kohteiden tarkkaan paikantamiseen. Useista RF-antureista koostuva verkosto voi kolmiomittauksella paikantaa droonin tarkan sijainnin, sekä, mikä vielä tärkeämpää, sen ohjaajan sijainnin. Koska droonin ohjain lähettää voimakasta signaalia, sen lähde voidaan kolmiomittauksella paikantaa maasta käsin.1 Tämä kyky on ratkaisevan tärkeä, koska uhka voidaan usein neutralisoida tehokkaimmin kiinnittämällä huomio itse ohjaajaan. Akateeminen tutkimus on osoittanut, että useita ohjelmistopohjaisia radiovastaanottimia (SDR) hyödyntämällä droonin sijainti voidaan paikantaa noin ±12 metrin tarkkuudella ja ohjaajan sijainti noin ±11 metrin tarkkuudella.1 Tämä mahdollistaa esimerkiksi kenttäpoliisin ohjaamisen oikealle alueelle epäillyn etsintään.1

* * *

## 3. Radioamatööriyhteisön hyödyntäminen: strateginen viitekehys

### 3.1. Yhteisö, joka on rakennettu viestinnän ja resilienssin varaan

Radioamatööriyhteisön historiaa leimaa sen kyky innovoida ja tarjota kriittisiä viestintäpalveluita hätätilanteissa.1 Kuten oma henkilökohtainen kokemukseni osoittaa: leikkisästä uteliaisuudesta etäasemien kuunteluun (DX-kuuntelu) ja morsetuksen hallinnasta modernien digitaalisten teknologioiden hyödyntämiseen poikkeusoloissa poliisilaitoksella.1 Tämä historia luo perustan sille, että tällä yhteisöllä on sisäänrakennettu luottamus ja kyky osallistua kansalaisjohtoiseen tiedonkeruuseen, mikä on merkittävä etu mille tahansa vapaaehtoiselle puolustushankkeelle.1

### 3.2. WSPRnet: suunnitelma globaalille passiiviselle sensoriverkostolle

Weak Signal Propagation Reporter (WSPR) -verkosto toimii vankkana, jo olemassa olevana mallina ehdotetulle vapaaehtoiselle maanpuolustusjärjestelmälle.1 WSPRnet on globaali radioamatööriharrastajien verkosto, joka käyttää pienen tehon digitaalisia lähetyksiä radiopilvien kulkureittien testaamiseen valtavien etäisyyksien yli.1 Järjestelmän menestys MH370-lentokoneen jäljittämisessä tarjoaa vakuuttavia todisteita siitä, että hajautettu, laajalle levinnyt verkosto edullisia, kuluttajatason sensoreita voi tuottaa kriittistä, laajamittaista dataa poikkeamien havaitsemiseksi, kun data kerätään ja analysoidaan tilastollisesti.1 WSPRnet-vastaanottimet voivat toimia jopa erittäin alhaisilla signaali-kohinasuhteilla, jopa noin -27 dB:n tasolla.1 Vaikka yksittäiset sensorit voivat olla "meluisia", miljoonien datapisteiden kerääminen maailmanlaajuisesta verkostosta tekee tilastollisista poikkeamista, kuten lentokoneen aiheuttamasta signaalin heikkenemisestä, havaittavissa ja merkityksellisiä.1 Tämä osoittaa, että kansalaispohjainen passiivinen tutkajärjestelmä ei vaadi jokaisen sensorin olevan täydellisesti kalibroitu tai erittäin tarkka. Sen sijaan sen vahvuus piilee kollektiivisessa datassa ja kehittyneiden tilastollisten ja tekoäly-pohjaisten tekniikoiden soveltamisessa merkityksellisten kuvioiden poimimiseksi.

### 3.3. Digitaalisten verkostojen arviointi vapaaehtoisten tiedonvaihtoon

Hajautetun vapaaehtoisverkoston kriittinen komponentti on vankka, luotettava ja käyttäjäystävällinen digitaalinen viestintäalusta. Radioamatööriyhteisö tarjoaa useita vaihtoehtoja, joilla kaikilla on omat etunsa ja haittansa.

-   **Digital Mobile Radio (DMR):** DMR on avoin standardi, mutta se kehitettiin alun perin kaupalliseen käyttöön, ei radioamatööreille.2 Se on suosittu matalien hankintakustannusten vuoksi, ja edullisia laitteita on saatavilla.2 Järjestelmää pidetään kuitenkin "tiukasti kontrolloituna" ja sen ohjelmointi on monimutkaista, sillä se vaatii yksilöllisiä käyttäjätunnuksia ja ulkoisia tietokantoja.2 Sen kaupallinen alkuperä saattaa olla ristiriidassa monien radioamatöörien avoimen lähdekoodin eettisten periaatteiden kanssa.
    
-   **D-Star:** Icomin kehittämä D-Star on radioamatööreille tarkoitettu digitaalinen tila.2 Vaikka se on käyttäjäystävällinen, sen protokolla on osittain avoin, ja laitteet ovat yleensä kalliimpia, mikä rajoittaa sen laajaa käyttöönottoa.2
    
-   **System Fusion (YSF):** Yaesun kehittämä YSF tunnetaan yksinkertaisuudestaan ja helppokäyttöisyydestään, mikä tekee siitä erittäin saavutettavan uusille käyttäjille.3 Se on kuitenkin kaupallinen, suljettu järjestelmä, mikä rajoittaa sen yhteentoimivuutta ja estää kolmannen osapuolen laitteistokehitystä.3
    
-   **M17:** M17 erottuu joukosta, koska se on aidosti avoimen lähdekoodin ja yhteisön vetämä digitaalinen protokolla, joka on kehitetty erityisesti radioamatöörikäyttöön.4 Se hyödyntää avoimen lähdekoodin Codec 2 -koodekkia, mikä varmistaa, että koko protokolla on vapaasti saatavilla kaikille käytettäväksi, muokattavaksi ja parannettavaksi.4 Tämä filosofia on täysin linjassa radioamatööriyhteisön hengen kanssa. M17 tarjoaa myös täyden tuen mielivaltaiseen tiedonsiirtoon ja salaukseen 5, mikä ei ole ominaisuus DMR:ssä tai D-Starissa.
    

Kaupallisten, oletusarvoisesti suljettujen protokollien (DMR, D-Star, YSF) varaan rakennettu maanpuolustusverkosto on altis yhden pisteen epäonnistumiselle: valmistajalle tai sitä kontrolloivalle taholle. Jos valmistaja lopettaa tuotelinjan tai muuttaa protokollaa, verkosto on vaarassa. M17:n avoimen lähdekoodin luonne poistaa tämän riskin. Yhteisön vetämä kehitys varmistaa protokollan jatkuvan parantamisen ja sopeutumisen, ja laitteita voi rakentaa kuka tahansa, mikä edistää hajautettua ja erittäin resilienttiä toimitusketjua. Se, että M17 tukee salausta 5, mikä on usein radioamatöörimääräysten vastaista, mutta ratkaisevan tärkeää turvallisen tiedonsiirron kannalta puolustuskontekstissa, on monimutkainen oikeudellinen ja sääntelyyn liittyvä haaste, joka olisi ratkaistava ennakoivasti.

* * *

## 4. Tekninen toteutus: kaikkialla olevista signaaleista toimintakelpoiseen tiedusteluun

### 4.1. Älypuhelin hajautettuna sensorina

Vaikka mobiililaitteet ovat kaikkialla, niiden suora käyttö passiivisina tutkavastaanottimina on teknisesti haastavaa. Älypuhelimien käyttöjärjestelmät (esim. Android) rajoittavat tiukasti suoraa pääsyä matalan tason RF-signaaleihin ja raakaan matkapuhelimen signaalin datamassaan.1 Rajoitetut ohjelmointirajapinnat, kuten Androidin CellInfo API, tarjoavat vain korkeamman tason ja usein sensuroitua tietoa.1

Käytännöllisin ratkaisu tähän rajoitukseen on käyttää ulkoisia ohjelmistopohjaisia radiovastaanottimia (SDR), kuten RTL-SDR-sovittimia, jotka liitetään älypuhelimeen OTG-sovittimen kautta.1 Nämä sovittimet ovat edullisia (20–70 dollaria) ja kykenevät vastaanottamaan laajaa taajuusaluetta, mikä mahdollistaa korkealaatuisen tiedonkeruun, joka ohittaa puhelimen sisäiset ohjelmistorajoitukset.1 Olemassa olevat sovellukset, jotka on suunniteltu lentokoneiden jäljittämiseen (ADS-B) ja yleisiin passiivisen tutkan periaatteisiin, osoittavat tämän lähestymistavan toteutettavuuden.1

Lisäksi raportti syventyy käyttäjän kysymykseen signaalin absorptioilmiöstä. Tutkimukset vahvistavat, että fyysiset esteet, kuten signaalireitin läpi kulkeva drooni, voivat aiheuttaa mitattavissa olevia laskuja signaalin tehon indikaattoreissa (RSSI).1 Tiheä matkapuhelinverkon laitteiden verkosto, joka seuraa jatkuvasti RSSI-arvoja useista tukiasemista, voisi luoda ilmatilasta "radiopuutteellisen läpinäkyvyyskartan". Tämän kartan poikkeamat voisivat osoittaa ilmakappaleiden läsnäolon, jopa varkaissa olevien kohteiden, jotka eivät tuota voimakkaita tutkaheijastuksia.1

### 4.2. Korkealla sijaitseva havainnointi: sidottujen droonien rooli

Maanpäällisten passiivisten vastaanottimien suurin rajoitus on niiden vaatima näköyhteys (LoS), jonka maastomelu, maasto ja rakennukset helposti estävät.1 Passiivisen vastaanottimen nostaminen korkeammalle parantaa merkittävästi sen toimintakykyä, erityisesti matalalla lentävien kohteiden havaitsemisessa.1 Sidotut droonit ovat moniroottorilennokkeja, jotka on fyysisesti yhdistetty maassa olevaan asemaan kaapelin välityksellä. Tämä sidontakaapeli tarjoaa useita kriittisiä etuja, jotka tekevät niistä ihanteellisia tähän käyttöön.1

-   **Rajoittamaton lentoaika:** Sidontakaapeli syöttää jatkuvasti virtaa maasta käsin, mikä mahdollistaa loputtoman lennon keston ja potentiaalisesti 24/7-valvonnan.1
    
-   **Suuri kaistanleveys tiedonsiirtoon:** Sidontakaapeliin on usein integroitu valokuitu, joka tarjoaa turvallisen, häiriösuojatun ja pienen viiveen tiedonsiirtoyhteyden.1 Tämä on välttämätöntä suuren RF-datamassan reaaliaikaiseen siirtämiseen keskusprosessorille.
    
-   **Suurempi hyötykuorman kantokyky:** Raskaiden akkujen puuttuminen kasvattaa droonin kantokykyä, mikä mahdollistaa entistä kehittyneempien sensorilaitteiden, kuten passiivisiin tutkasovelluksiin suunniteltujen SDR-vastaanottimien, kuljettamisen.1
    

Sidotun droonin rajaton virtalähde ja turvallinen, suuren kaistanleveyden datayhteys vastaavat suoraan hajautetun verkoston kahteen merkittävimpään tekniseen haasteeseen: jatkuvaan toimintaan ja reaaliaikaiseen tiedonsiirtoon. Nostamalla edullinen SDR-vastaanotin sidotulla droonilla ilmaan, vapaaehtoinen voi tehokkaasti luoda jatkuvan "RF-aidan" tai valvontakuplan kriittisen alueen ylle. Tämä parantaa järjestelmän tehokkuutta merkittävästi ja muuttaa sen teoreettisesta konseptista käytännölliseksi ja käyttöön otettavissa olevaksi ratkaisuksi.

### 4.3. Matkapuhelinverkkojen hyödyntäminen

Matkapuhelinverkon tukiasemat tarjoavat kaikkialla läsnä olevia "valaisijoita" passiivisille tutkajärjestelmille.1 4G LTE-signaalit ovat vahvoja kandidaatteja passiivisen tutkan käyttöön niiden suuren kaistanleveyden ja laajan kattavuuden vuoksi.1 Erityisesti 5G-verkot ovat lupaava kehityssuunta. 5G:n synkronointisignaalilohko (SSB) on "aina päällä" oleva, hyvin määritelty signaali, joka tarjoaa johdonmukaisen ja luotettavan valaisulähteen, vaikka verkossa ei tapahtuisi tiedonsiirtoa.1 Siirtyminen 5G:hen tarjoaa sekä haasteita (vähemmän jatkuvaa suuritehoista valaistusta datakaistoilta) että merkittävän mahdollisuuden (luotettava, jaksollinen SSB-valaistus) passiivisiin tutkasovelluksiin.1

* * *

## 5. Järjestelmät laillista droonitoimintaa varten

### 5.1. Unmanned Traffic Management (UTM): yhteistyöhön perustuva ekosysteemi

UTM on yhteistyöhön perustuva ekosysteemi, jonka tarkoituksena on hallita turvallisesti matalalla lentäviä drooneja.1 Se on erillinen perinteisestä lennonjohdosta, mutta se on suunniteltu täydentämään sitä.6 Järjestelmä mahdollistaa kriittisiä toimintoja, kuten lennonsuunnittelun, lupien myöntämisen, valvonnan ja törmäysten estämisen.6 Keskeiset organisaatiot, kuten FAA, NASA ja yritykset kuten Airbus, kehittävät tätä ekosysteemiä, joka perustuu teollisuuden konsensuksella luotuihin standardeihin yhteentoimivuuden varmistamiseksi.7 UTM perustuu skaalautuvuuden, turvallisuuden ja yhteentoimivuuden periaatteille.7 Se on "liittoutunut verkosto", joka perustuu yhteistyöhön, jossa droonioperaattorit, palveluntarjoajat ja viranomaiset jakavat reaaliaikaisen tilannekuvan ilmatilasta.6 Järjestelmä on suunniteltu laillisille, luvanvaraisille droonioperaatioille, kaupallisista tarkastuksista toimituspalveluihin.1

### 5.2. Pakollinen etätunnistus (Remote ID): elektroninen rekisterikilpi

Etätunnistus (Remote ID) on sääntelyvaatimus, joka velvoittaa suurimman osan drooneista lähettämään tunnistus- ja sijaintitietoja lennon aikana.1 Se on kuin "elektroninen rekisterikilpi" drooneille.1 Järjestelmä lähettää droonin sarjanumeron, sijainnin, korkeuden ja nopeuden sekä kauko-ohjausaseman sijainnin.11 Tämä tieto on muiden ihmisten tai viranomaisten vastaanotettavissa maassa.10 Eri kansainvälisillä standardeilla on omat vaatimuksensa, ja esimerkiksi FAA:lla ja EASA:lla on omat erityiset sääntönsä.1

### 5.3. Kaksi vastakkaista paradigmaa: yhteistyöhön perustuva vs. ei-yhteistyöhön perustuva

Vaikka UTM/Remote ID -järjestelmät ja ehdotettu puolustusjärjestelmä vaikuttavat pinnallisesti samankaltaisilta, ne eroavat toisistaan perimmäiseltä filosofialtaan. Toinen on suunniteltu yhteistyöhaluiselle, sanktioitulle käytölle, kun taas toinen on tarkoitettu ei-yhteistyöhaluisten, mahdollisesti vihamielisten uhkien havaitsemiseen.

UTM/Remote ID -viitekehys toimii yhteistyön ja sääntöjen noudattamisen perustalla. Se olettaa, että lailliset drooniohjaajat rekisteröivät laitteensa ja lähettävät lentotietonsa. Sen sijaan droonintorjuntajärjestelmä on luonnostaan suunniteltu täysin vastakkaista skenaariota varten: uhka on ei-yhteistyöhaluinen, rekisteröimätön tai ilkeämielinen toimija. Vihamielinen drooni ei lähetä etätunnistesignaalia. Siksi passiivinen puolustusverkosto ei ole redundantti järjestelmä; se on välttämätön, täydentävä kerros, joka on luotu uhkia varten, joita siviili-ilmailun yhteistyöhön perustuva viitekehys ei ole suunniteltu käsittelemään. Puolustusjärjestelmä toimii ilmatilan ekosysteemin vastatiedustelu- ja turvallisuusosastona, toimien kriittisenä ei-yhteistyöhaluisena valvontakerroksena, joka suojaa uhkilta, jotka kiertävät tai jättävät siviilisäännökset huomiotta.

* * *

## 6. Haasteita

### 6.1. Teknisten ja operatiivisten haasteiden ratkaiseminen

-   **Tiedon fuusio:** Suurin tekninen haaste on yhdistää tehokkaasti dataa heterogeenisistä sensoreista (passiivinen tutka, akustiikka, RF) ja vapaaehtoisilta.1 Tämä vaatii kehittyneitä algoritmeja, jotka käsittelevät erilaisia datatyyppejä ja poistavat melua ja häiriöitä.1
    
-   **Datan hallinta:** Hajautettu verkosto tuottaa massiivisen määrän RF- ja muita sensoridataa reaaliajassa.1 Tämä edellyttää vankkaa ja skaalautuvaa taustajärjestelmää datan keräämiseen, tallentamiseen ja käsittelyyn, hyödyntäen luultavasti pilvilaskentaa tai tehokkaita reunalaitteita alkuperäistä käsittelyä varten.1
    
-   **Laadunvalvonta:** Datan laadun ylläpitäminen ja vapaaehtoisten lähettämien tietojen validointi on ensiarvoisen tärkeää, jotta vältetään väärät hälytykset tai havaitsematta jääneet uhat.1
    

### 6.2. Oikeudellisten ja eettisten puitteiden tärkeys

Kaikki kansalaisjohtoiset valvontahankkeet on rakennettava nimenomaan oikeudelliselle suojalle ja eettisille ohjeille. Tämä on kriittinen ei-tekninen haaste. Valvontateknologioiden käytön on noudatettava demokraattisia periaatteita ja ihmisoikeuksia, ja datan keräämiselle, käsittelylle ja luovuttamiselle on oltava vankat suojatoimet.1

Esimerkit, kuten Yhdysvaltain NSA:n PRISM-ohjelma 1, korostavat joukkovalvonnan potentiaalia ja julkisen luottamuksen rapautumista. Vapaaehtoisen puolustusverkoston on noudatettava "tietosuojasuoja suunnittelun ja toteutuksen lähtökohtana" -periaatteita alusta alkaen. Anonymisoidun datan, kuten RSSI-mittausten, käyttäminen, joka ei mahdollista yksilöllistä tunnistamista 1, sekä selkeiden, läpinäkyvien datan käyttöpolitiikkojen ja riippumattoman valvonnan perustaminen eivät ole vain hyviä käytäntöjä – ne ovat välttämättömiä hankkeen pitkän aikavälin elinkelpoisuuden ja yleisen hyväksynnän kannalta. Ilman näitä suojatoimia hanke uhkaa tulla koetuksi yksityisyyden loukkaukseksi pikemmin kuin isänmaalliseksi panokseksi, mikä heikentää sen alkuperäistä tarkoitusta. Olemassa olevat menestyksekkäät organisaatiomallit, kuten U.S. Army Military Auxiliary Radio System (AMARS) ja Radio Amateur Civil Emergency Service (RACES) 1, tarjoavat selkeän mallin vapaaehtoisten hallintaan ja kouluttamiseen jäsennellyllä ja vastuullisella tavalla.

### 6.3. Suosituksia toteutukselle

-   **Pilottiohjelmat:** Käynnistetään kohdennettuja pilottiohjelmia, joissa testataan mobiililaitteisiin perustuvien passiivisten tutkavastaanottimien (hyödyntäen ulkoisia SDR-sovittimia) ja sidottujen droonien alustojen käytännön toteutettavuutta tietyillä maantieteellisillä alueilla.
    
-   **Teknologian kehittäminen:** Investoidaan strategisesti kehittyneiden signaalinkäsittelyalgoritmien ja tekoäly- ja koneoppimisalgoritmien tutkimukseen ja kehittämiseen poikkeamien automaattista havaitsemista ja kohteiden tarkkaa luokittelua varten. Keskitytään matkapuhelinsignaalien, erityisesti 5G SSB-signaalien ja absorptioilmiöiden, hyödyntämiseen.
    
-   **Kansalaistiedealusta:** Kehitetään turvallinen, käyttäjäystävällinen kansalaistiedesovellus ja vankka taustajärjestelmä tehokasta datan keräämistä, käsittelyä ja visualisointia varten, varmistaen, että datan anonymisointi- ja tietosuojaperiaatteet toteutetaan tiukasti alusta alkaen.
    
-   **Viitekehys ja koulutus:** Perustetaan virallinen yhteistyökehys, jossa on selkeät operatiiviset protokollat, kattavat oikeudelliset ohjeet ja perusteelliset koulutusohjelmat kansalaisvapaaehtoisille. Mallina voidaan käyttää AMARS:n ja RACES:n onnistuneita organisaatiomalleja, jotta voidaan varmistaa sekä datan laatu että operatiivinen turvallisuus.
    


## Yhteenveto

Passiivinen tutka, joka on saumattomasti integroitu akustiseen ja RF-pohjaiseen monianturifuusioon, tarjoaa houkuttelevan ja kustannustehokkaan ratkaisun kansallisen puolustuskyvyn parantamiseksi ilmauhkia vastaan. Tämä lähestymistapa ei ole vain tekninen uutuus, vaan strateginen ja filosofinen muutos, joka hyödyntää radioamatöörioperaattorien kaltaisten yhteisöjen luontaista teknistä osaamista ja sitoutumista yleiseen palveluun. WSPRnet-malli osoittaa, että laajamittainen, hajautettu verkosto edullisia sensoreita voi tuottaa arvokasta tiedustelutietoa. Vaikka siviilipuolen UTM- ja etätunnistusjärjestelmät tarjoavat viitekehyksen laillisen drooniliikenteen hallintaan, ehdotettu passiivinen puolustusverkosto tarjoaa kriittisen, ei-yhteistyöhaluisen vastatiedustelutason niitä uhkia vastaan, jotka jäävät tämän yhteistyöekosysteemin ulkopuolelle. Ratkaisemalla tekniset haasteet innovatiivisilla tavoilla, kuten ulkoisilla SDR-sovittimilla ja sidotuilla drooneilla, ja käsittelemällä ennakoivasti oikeudellisia ja eettisiä kysymyksiä vankoin tietosuojakeinoin, on mahdollista rakentaa vapaaehtoinen maanpuolustusverkosto. Tämä aloite ei ainoastaan vahvista kansallista turvallisuutta, vaan myös antaa kansalaisille mahdollisuuden osallistua merkitykselliseen rooliin oman resilienssinsä ja puolustuksensa eteen, mikä edustaa merkittävää ja tehokasta kehitystä pitkässä perinteessä.



### Lähdeartikkelit

1.  Droonien akustinen ja radiotaajuuksiin perustuva tunnistus ja paikannus.docx
    
2.  Dstar vs dmr : r/amateurradio - Reddit, avattu syyskuuta 25, 2025, [https://www.reddit.com/r/amateurradio/comments/1nk2a5j/dstar\_vs\_dmr/](https://www.reddit.com/r/amateurradio/comments/1nk2a5j/dstar_vs_dmr/)
    
3.  D-star, DMR, Fusion, Which is right for you? - Mike Myers (K3DO), avattu syyskuuta 25, 2025, [http://www.mikemyers.me/home/2016/2/19/d-star-dmr-fusion-which-is-right-for-you](http://www.mikemyers.me/home/2016/2/19/d-star-dmr-fusion-which-is-right-for-you)
    
4.  M17 Digital Voice Mode for Amateur Radio - Electronics Notes, avattu syyskuuta 25, 2025, [https://www.electronics-notes.com/articles/ham\_radio/voice-modes/m17-digital-voice.php](https://www.electronics-notes.com/articles/ham_radio/voice-modes/m17-digital-voice.php)
    
5.  M17 (amateur radio) - Wikipedia, avattu syyskuuta 25, 2025, [https://en.wikipedia.org/wiki/M17\_(amateur\_radio)](https://en.wikipedia.org/wiki/M17_(amateur_radio))
    
6.  Unmanned Aircraft System Traffic Management (UTM) | Federal Aviation Administration, avattu syyskuuta 25, 2025, [https://www.faa.gov/uas/advanced\_operations/traffic\_management](https://www.faa.gov/uas/advanced_operations/traffic_management)
    
7.  Airbus Unmanned Traffic Management, avattu syyskuuta 25, 2025, [https://www.airbus.com/en/innovation/future-aircraft-operations/airbus-unmanned-traffic-management](https://www.airbus.com/en/innovation/future-aircraft-operations/airbus-unmanned-traffic-management)
    
8.  Nationwide Drone Services | Aerial Imaging | FlyGuys | Nationwide Data Capture, avattu syyskuuta 25, 2025, [https://flyguys.com/](https://flyguys.com/)
    
9.  Arch Aerial | Commercial Drone Services Arch Aerial Drone Services, avattu syyskuuta 25, 2025, [https://archaerial.com/](https://archaerial.com/)
    
10.  Remote Identification of Drones | Federal Aviation Administration, avattu syyskuuta 25, 2025, [https://www.faa.gov/uas/getting\_started/remote\_id](https://www.faa.gov/uas/getting_started/remote_id)
    
11.  Remote identification (Remote ID) is coming. Are you ready? - FAA, avattu syyskuuta 25, 2025, [https://www.faa.gov/uas/getting\_started/remote\_id/Remote-ID-Toolkit-main.pdf](https://www.faa.gov/uas/getting_started/remote_id/Remote-ID-Toolkit-main.pdf)
    
12.  Remote ID Compliancy - Dronetag Help, avattu syyskuuta 25, 2025, [https://help.dronetag.cz/dronetag-dri/remote-id-compliancy](https://help.dronetag.cz/dronetag-dri/remote-id-compliancy)