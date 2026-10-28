---
title: "Passiivinen Skywatcher: Droonihavainto siviili-infrastruktuurin, SDR:n ja tekoälyn avulla"
date: 2026-05-06
draft: false
language: fi
tags:
  - droonit
  - SDR
  - LoRaWAN
  - WiFi-CSI
  - passiivitutka
  - koneoppiminen
  - maanpuolustus
  - hamradio
  - innovaatiot
  - tutkimus
summary: "Tutkimusraportti passiivisesta droonien havainnointijärjestelmästä, joka yhdistää SDR-, WiFi CSI- ja LoRaWAN-teknologiat sensorifuusion ja koneoppimisen avulla."
---

Päivitys 15.7.2025 julkaistuun englanninkieliseen artikkeliini [Passive Radar Systems for Voluntary National Defense: Leveraging Civilian Infrastructure for Enhanced Situational Awareness](https://ollavarma-create.github.io/blog/en/posts/passive-radar-systems-for-voluntary-national-defense-leveraging-civilian-infrastructure-for-enhanced/) ja [artikkelin suomennokseen](https://ollavarma-create.github.io/blog/fi/posts/droonien-akustinen-ja-radiotaajuuksiin-perustuva-tunnistus-ja-paikannus/).


# Passiivinen Skywatcher: droonihavaintojärjestelmä siviili-infrastruktuurin, SDR:n ja tekoälyn avulla

Tämä tutkimusraportti esittelee tieteellisesti perustellun ja teknisesti yksityiskohtaisen arkkitehtuurin kehittyneelle droonien havainnointijärjestelmälle, joka perustuu kehittyneen infrastruktuurin hyödyntämiseen harrastajaympäristössä. Järjestelmän tavoitteena on luoda monikanavainen, avoimen lähdekoodin työkalujen pohjalta rakennettu sensorifuusiojärjestelmä, joka yhdistää kolmea eri teknologiaa – ohjelmistoradio (SDR), WiFi-kanavan tilatieto (CSI) ja LoRaWAN – käyttäen oppivaa algoritmia ja keskeistä fysikaalista perustaa, nimittäin mikro-Doppler-ilmiötä. Raportin tarkoituksena on tarjota syvällinen ymmärrys järjestelmän toimintaperiaatteista, arkkitehtuurin suunnittelusta, datavirroista, eettis-oikeudellisesta kontekstista sekä käytännön toteutusmahdollisuuksista. Painotus on asetettu passiiviseen ilmavalvontaan kansalaisten tekemän turvallisuuden tueksi, erityisesti vapaaehtoisessa maanpuolustuksessa. Tutkimus perustuu nykyisiin teknologiatekijöihin vuosien 2020–2026 väliltä ja korostaa lainsäädännön rajoitteiden kunnioittamista.

## Fyysisen perustan ja tunnistusmekanismien analyysi: mikro-doppler-ilmiön rooli

Droonien havainnoinnin perimmäinen haaste piilee pienien kohteiden, nopeissa nopeuksissa ja usein epäsuorassa näköyhteysalueessa liikkuessa. Tavanomaiset aktiiviset tutkasovellukset, jotka lähettävät signaaleja ja mittaavat heijastumia, ovat usein liian kalliita, energiavaativia tai ne paljastavat oman sijaintinsa, mikä tekee niistä huonon valinnan passiiviseen valvontaan [62]. Ratkaisu löytyy fysikaalisesta ilmiöstä, joka on nimensä mukaan **mikro-Doppler-ilmiö**, ja sen kyvystä muodostaa ainutlaatuisen "sormenjäljen" liikkuville objekteille. Tämä ilmiö muodostaa keskeisen tunnistusperustan ehdotetulle arkkitehtuurille, koska se mahdollistaa droonien erottelun muusta ympäristöllisestä liikkeestä, kuten lintujen lennosta tai tuulen aiheuttamasta puun heilumisesta. Ilmiön teoreettinen perusta on Doppler-effektiin perustuva ilmiö, jossa liikkuva kohde muuttaa vastaanottimen saaman signaalin taajuutta. Kun kohteella on lisäksi pieniä, nopeasti pyöriviä tai heilahtelevia osia, kuten droonin potkurit, syntyy signaalissa hienovaraisesti vaihtelevia, korkeamman frekvenssin osittaissignaaleja. Nämä pienet taajuusvärähtelyt muodostavat spektrogrammiin karakteristisen, monimutkaisen kuvion, joka eroaa merkittävästi yksinkertaisesta Doppler-shiftistä, joka syntyy esimerkiksi tasaisesti lentävästä linnusta [11,30]. Akateeminen kirjallisuus on pitkään tukenut tätä lähestymistapaa; tutkimuksia, kuten Chen (2011):n ja Fioranelli ym. (2016):n, on keskitytty mikro-Doppler-ilmiön hyödyntämiseen droonien havaitsemiseen ja tunnistamiseen erilaisissa radiolaitteistoissa [2,19].

Erityisesti uudemmissa tutkimuksissa on korostettu mikro-Doppler-signatuurien käyttöä droonien ja lintujen erottelemiseen. Esimerkiksi tutkimus, jossa vertaillaan droonien ja lintujen mikro-Doppler-signatuureja, osoittaa, että vaikka molemmilla olisikin pyörivät osat (potkurit ja siivet), niiden liikkeen dynamiikka ja frekvenssiprofiili eroavat selvästi toisistaan [13]. Droonien potkurit pyörivät usein tasaisemmassa ja ennalta-arvattavammassa tahdissa kuin lintujen siivet, mikä muodostaa spektrogrammiin tunnistettavan, usein symmetrisen ja jaksollisen kuvion. Tämä ero on keskeinen tunnistamisperuste, sillä väärät hälytykset lintujen lennon takia ovat yksi suurimmista haasteista droonien havaitsemisessa [32]. Monet tutkimukset ovat sittemmin vahvistaneet, että mikro-Doppler-analyysi on tehokas tapa luokitella erilaisia liikkeitä [17,72]. Uudempien tutkimusten, kuten Rahman & Robertsonin (2018) työn, mukaan erilaisten lentävien kohteiden mikro-Doppler-signatuurien vertailu mahdollistaa myös heidän luokitteluunsa [13].

Tekoälyn ja erityisesti konvoluutioneuroverkkojen (CNN) rooli on tässä prosessissa ratkaiseva. Koneoppimismenetelmät, erityisesti CNN-mallit, ovat todettu erittäin tehokkaiksi työkaluiksi näiden monimutkaisten mikro-Doppler-spektrogrammien automaattiseen luokitteluun. Mallit pystyvät oppimaan näiden kuvien monimutkaiset piirteet, kuten frekvenssin vaihtelun, keston ja amplitudin, ja erottamaan aidot droonisignaalin luotettavasti muista häiriöistä, kuten maanpinnan heijastumista tai liikenteestä [20,76]. Useat tutkimukset ovat osoittaneet CNN-mallien menestyksen droonien ja lintujen luokittelussa käyttäen radar-spektrogrammeja [51,79,100]. Esimerkiksi GoogLeNet-tyyppisiä syvät konvoluutiokoneet on käytetty luokittelemassa drooneja ja lintuja, ja tuloksia on myös esitetty RGB-väreinä muunnettujen spektrogrammien avulla [51]. Myös aikaan perustuvien neuroverkkojen (LSTM) kaltaisten syväverkkojen rakenteiden käyttö on osoittautunut hyväksi analysoimaan mikro-Doppler-signaalin aikakehitystä ja paremmin ymmärtämään liikkeen dynamiikkaa [80,81]. Tämä tekoälypohjainen analyysi mahdollistaa korkean tarkkuuden ja luotettavan tunnistuksen, mikä on välttämätöntä käytännön sovelluksessa, jossa halutaan minimoida virheellisiä hälytyksiä. Järjestelmä voi siis oppia tunnistamaan droonin potkurien liikkeen erottamalla sen muusta taustakohinasta, mikä perustuu akateemiseen kirjallisuuteen [2].

Tässä arkkitehtuurissa mikro-Doppler-ilmiötä hyödynnetään eri sensoreiden kautta. Ohjelmistoradiolla (SDR) analysoidaan ulkoisesta signaalilähteestä (esim. LTE, 5G) heijastuneen signaalin Doppler-siirtymää. WiFi CSI:stä puolestaan analysoidaan signaalin vaihe- ja amplitudihäiriöitä, jotka aiheutuvat potkurien pyörimisestä. Vaikka fysikaalinen perusta on sama, eri sensoreiden käyttämät taajuuskaistat ja anturitekniikat vaativat erilaisia signaalinkäsittelyalgoritmeja. Esimerkiksi mmWave-tutkat voivat antaa erittäin tarkat signaaliarviot, mutta ne ovat usein kalliita ja rajoittuneet lyhyelle matkalle [8,31]. Ehdotettu arkkitehtuuri pyrkii kuitenkin hyödyntämään halvempia ja yleisemmin saatavilla olevia teknologioita, kuten SDR:tä ja WiFi-reitittimiä, joiden kanssa mikro-Doppler-analyysi on osoittautunut tehokkaaksi [70,109]. Tämä tekee siitä erityisen sopivan harrastajapohjaiseen, resurssirajoitetuun ympäristöön. Lopulta, mikro-Doppler-ilmiön hyödyntäminen on keskeinen tekijä, joka mahdollistaa droonien havaitsemisen passiivisella tavalla ja tarjoaa uskottavan perustan koneoppimispohjaiselle luokittelualgoritmille, joka on järjestelmän älykkyyden ytimessä.

## Sensoriteknologioiden vahvuudet, rajat ja fuusioperiaate

Ehdotettu havainnointijärjestelmä perustuu kolmen eri sensoriteknologian yhdistämiseen: ohjelmistoradio (SDR) passiivitutkana, WiFi Channel State Information (CSI) liikkeentunnistimena ja Long Range Wide Area Network (LoRaWAN) infrastruktuuriverkkona. Jokaisella näistä teknologioista on omat vahvuutensa, rajansa ja roolinsa fuusiotyössä. Sensorifuusion perusideana on hyödyntää kunkin anturin vahvuuksia täydentämällä niiden heikkouksia, mikä johtaa kokonaisuutena luotettavampaan ja tarkkaampaan järjestelmään kuin mikään yksittäinen anturi voisi tarjota. Tämä monipuolinen lähestymistapa vähentää merkittävästi virheellisten hälytysten riskiä, sillä yksittäinen anturi voi helposti virheellisesti identifioida drooniksi esimerkiksi lentäväksi linnuksi tai ajoneuvoksi, kun taas useiden, riippumattomien antureiden yhdistetty havainto kasvattaa varmuutta huomattavasti [9,23].

Ohjelmistoradio (SDR) toimii tässä arkkitehtuurissa passiivitutkana. Sen perusperiaate on käyttää olemassa olevaa ulkoista siviili-infrastruktuurin signaalilähdettä, kuten FM-radiota, digitaalista televisiota (DVB-T), GSM/GPRS, ja erityisesti nykyisin yleisempiä LTE- ja 5G-verkkoja, valvontaa varten [2,21]. SDR-vastaanotin jakaa vastaanotettavan signaalin kahteen kanavaan: referenssikanavaan, johon signaali suuntautuu suoraan, ja valvontakanavaan, johon signaali saapuu heijastuen ympäristön kohteilta. Kun kohteelta, kuten droonilta, heijastuu signaalia, se aiheuttaa havaittavan viiveen ja Doppler-siirtymän signaaliin. Vertaamalla näitä kahta kanavaa voidaan laskea heijastuman ominaisuudet [109]. Tämän menetelmän vahvuutena on se, että se ei itsessään lähetä mitään signaalia, mikä tekee siitä passiivisen ja salakavalan valvontaratkaisun [61]. SDR-pohjaiset järjestelmät ovat osoittautuneet tehokkaiksi droonien havaitsemiseen, ja niiden kantamaa on testattu eri taajuusalueilla. Erityisesti LTE450-verkon hyödyntäminen on noussut esiin, koska sen signaalit peittävät laajoja alueita ja pystyvät läpäisemään esteitä hyvin [2,115]. Toisaalta, vaikka SDR on hyvä pitkän matkan valvontaan, se kärsii monitieheijastumisesta kaupunkiympäristöissä, missä signaalit heijastuvat useista rakennuksista samanaikaisesti, mikä synnyttää häiriöitä ja vaikeuttaa kohteiden paikantamista [61].

Toinen avainkomponentti on WiFi Channel State Information (CSI). WiFi-teknologia, joka on yleisesti saatavilla kotitalouksissa, tarjoaa yllättävän tarkkaa liikkeentunnistusta ilman erillisiä antureita. Jokainen WiFi-paketti sisältää tietoa kanavan tilasta, joka kuvaa signaalin heijastumista eri reittejä pitkin kuljettaessa. Liike, kuten droonin potkurien pyörimisestä tai henkilön liikkuminen, aiheuttaa hetkellisiä vaihe- ja amplitudimuutoksia tähän CSI-dataan [45,70]. Tätä dataa voidaan analysoida erottamaan liike staattisesta ympäristöstä. WiFi CSI:n erityisominaisuutena on se, että se pystyy havaitsemaan liikettä jopa seinien läpi, mikä antaa ainutlaatuisen mahdollisuuden sisätilavalvontaan tai rakennusten suojaamiseen [82,87]. Lisäksi WiFi CSI on energiatehokasta, mikä tekee siitä sopivan pienikokoisten, edge-laskentaa vaativien laitteiden, kuten ESP32:n, käyttöön [82]. Sen rajoituksena on kuitenkin rajoittunut kantama, joka on yleensä parhaimmillaan muutama kymmenen metriä sisätiloissa ja muutama sata metriä ulkona. Se on myös herkkää muita häiriölähteitä vastaan, kuten naapuriverkkojen signaaleilta tai muilta laitteilta, jotka aiheuttavat sähkömagneettista melua.

Kolmas komponentti, LoRaWAN, ei itsessään tunnista drooneja, vaan se tarjoaa arkkitehtuurille keskeisen infrastruktuurin ja viestintäverkon. LoRaWAN on matalatehoinen, pitkän matkan langattoman verkkoteknologia, joka on suunniteltu IoT-sovelluksille, kuten maatalous- ja vesihuoltotarkoituksiin [27,28]. Sen rooli tässä järjestelmässä on kaksiosainen. Ensinnäkin se toimii halpana, laajana "kuunteluverkkona", joka mahdollistaa sensoreiden keskinäisen kommunikoinnin tai tiedon siirtämisen ulkopuolisille vastaanottimille, jos muut yhteydet katkeavat [24]. Toiseksi, se toimii kriittisen tärkeänä "varmistusverkkona". Jos esimerkiksi sähkökatkos tai tahallinen sähkömagneettinen häirintä katkaistaan muut sensoriverkot, LoRaWAN-moduuli voi vielä lähettää kriittisen "hälytys"-viestin pitkän matkan päässä olevalle vastaanottimelle [25]. Tämä tekee järjestelmästä erittäin robustin ja jatkuvuutta tukeneen. LoRaWAN ei kerää tarkkaa sijaintidataa, mutta se tarjoaa luotettavan tiedonsiirtomahdollisuuden, mikä on välttämätöntä tehokkaassa yhteistyössä, esimerkiksi viranomaisten kanssa.

Seuraavassa taulukossa on yhteenveto näiden kolmen sensoriteknologian ominaisuuksista ja niiden roolista fuusioprosessissa.

| Ominaisuus | Ohjelmistoradio (SDR) - Passiivitutka | WiFi Channel State Information (CSI) | LoRaWAN |
| :--- | :--- | :--- | :--- |
| **Perusperiaate** | Heijastuneen siviilisignaalin (esim. LTE) Doppler-siirtymän ja viiveen analyysi [21] | WiFi-paketin kanavan tilatietojen (CSI) vaihe- ja amplitudihäiriöiden analyysi liikkeen havaitsemiseksi [70] | Pitkän matkan, matalatehoinen langaton viestintä IoT-sovelluksiin [28] |
| **Pääasiallinen tehtävä** | Pitemmän matkan droonien havaitseminen ja suuntapaikannus | Lyhyen matkan liikkeentunnistus, jopa seinien läpi; potentiaalisesti sisätilavalvonta [82] | Halvan, laajan ja energiatehokkaan verkon tarjoaminen järjestelmän ylläpitoon ja hälytyksen lähetykseen |
| **Vahvuudet** | Pitkä kantama, erottelu esteistä läpi (erityisesti alhailla taajuuksilla), passiivinen toiminta [2] | Korkea resoluutio lyhyellä etäisyydellä, energiatehokas, ei vaadi erillisiä antureita [82] | Laaja peitto, pitkä akkujen kesto, alhainen infrastruktuurikustannus, robusti yhteys [24] |
| **Rajat** | Herkkyyttä monitieheijastumiselle kaupunkiympäristöissä, ei suoraan paikantava ilman monikanavaisia systeemejä [61] | Rajoittunut kantama, herkkyyttä muita häiriölähteitä vastaan, ei tarkkaa paikantamista [84] | Ei itse tunnista drooneja, alhainen tiedonsiirtokapasiteetti, ei tarkkaa paikantamista |
| **Fuusioperiaate** | Tarjoaa ennakkohavaintoja pitkältä matkalta ja antaa yleisen suunnan, johon muut anturit voivat keskittyä | Vahvistaa havainnon, jos drooni on lähellä, ja tarjoaa lisätietoa liikkeen luonteesta | Varmistaa, että tärkeimmät tiedot kulkevat koko ajan ja mahdollistaa hälytyksen lähetyksen, vaikka muut järjestelmät olisivat pois käytöstä |

Tämä taulukko havainnollistaa, kuinka järjestelmä hyödyntää kunkin sensorin vahvuuksia. SDR auttaa löytämään droonin laajalta alueelta, WiFi CSI vahvistaa sen läsnäolon ja luonnehtii liikettä, ja LoRaWAN varmistaa, että tärkeimmät tiedot kulkevat turvallisesti. Tällä tavoin järjestelmä ylittää yksittäisten antureiden rajoitukset ja tarjoaa yhtenäisen, luotettavan ja monipuolisen valvontaratkaisun.

## Datakeskeinen arkkitehtuuri: MQTT, Telegraf ja InfluxDB -pohjainen datavirtaus

Ehdotetun droonien havainnointijärjestelmän tehokkuus perustuu moderniin, skaalautuvasti toimivaan ja avoimen lähdekoodin työkalujen pohjalta rakennettuun datakeskeiseen arkkitehtuuriin. Tämä arkkitehtuuri, jota käyttäjä on ehdottanut (`MQTT → Telegraf → InfluxDB`), on tarkoitettu ottamaan huomioon harrastajapohjaisen, resurssirajoitetun ympäristön tarpeet, samalla kun se mahdollistaa jatkuvan oppimisen ja anomalian havaitsemisen. Tämä putki muodostaa järjestelmän verkon ja aivojen, joka kerää, prosessoi ja tallentaa sensorien tuottamaa dataa, jonka perusteella oppiva algoritmi voi tehdä päätöksiä. Jokainen komponentti tässä putkessa on valittu sen ansiosta, että se on helppokäyttöinen, skaalautuva ja robusti.

Datavirtaus alkaa reunalaitteista, jossa sensorit ja edge-laskenta-asemat (kuten Raspberry Pi tai ESP32) sijaitsevat [54]. Tärkein periaate täällä on tehdä mahdollisimman paljon prosessointia mahdollisimman lähellä dataa. Esimerkiksi WiFi CSI -anturilla ESP32-S3:lla, mikä on ehdotettu, suoritetaan mikro-Doppler-analyysi raakadatasta [54]. Tämä analyysi tuottaa vain tietyt havainnot, kuten aikaleiman, luotettavuusarvon (luottamuskerroin) ja signaalin voimakkuuden (RSSI). Raakadataa, joka voi olla suurta ja käsiteltävää, ei lähetetä verkossa. Tämä pienentää merkittävästi verkon kuormitusta ja vähentää viiveitä. Samoin SDR-järjestelmä GNU Radio -virtassa (flowgraph) voi suorittaa koherentin signaalinkäsittelyn ja lähettää vain sellaiset havainnot, joissa on havaittu merkittävää liikettä tai Doppler-siirtymää. Tämä edge-laskenta on keskeistä, sillä se mahdollistaa nopean reagoinnin ja vähentää riippuvuutta keskitetystä pilvipalvelusta.

Kun reunoilla on käsitelty data ja generoitu "havainto", se lähetetään seuraavaan kerrokseen, viestinvälitysprotokollan eli MQTT:n (Message Queuing Telemetry Transport) kautta [54]. MQTT on kevyt, joustava ja yleisesti käytetty protokolla IoT-sovelluksissa. Sen toiminta perustuu julkaisija-tilaaja -malliin. Sensorit toimivat julkaisijoina, jotka lähettävät tietoa tiettyihin aiheisiin (esimerkiksi `sensors/drone_detection/esp32_wifi_csi`). Järjestelmän muut osat, kuten datakeräilijä, ovat kuulijoita, jotka ovat kiinnostuneita tietystä aiheesta. MQTT-brokerin, kuten Mosquitton, rooli on välittää nämä viestit tehokkaasti [54]. Tämä malli irrottaa sensorit ja tietokannan toisistaan täydellisesti. Uusia sensoreita voidaan lisätä järjestelmään helposti lisäämällä uusi julkaistava aihe ilman, että muuta järjestelmää tarvitsee muuttaa. Tämä tekee arkkitehtuurista erittäin joustavan ja helpon laajentaa. MQTT:n lisäksi se mahdollistaa myös väliaikaiset yhteyskatkot, sillä broker voi säilyttää jonoon lähettämättömät viestit, mikä lisää järjestelmän luotettavuutta.

Kun MQTT-brokeri välittää havainnot, ne saapuvat seuraavaan kerrokseen, joka koostuu Telegrafista ja InfluxDB:stä. Telegraf on datankeräilijä, joka on suunniteltu ottamaan vastaan tietoa eri lähteistä, kuten MQTT:stä [54]. Telegrafin tehtävä on ottaa vastaan MQTT:stä tulevat havainnot ja tehdä niistä kevyt esikäsittely. Tämä voi sisältää esimerkiksi suodattamisen pois niistä havainnoista, joilla on alhainen luotettavuus (esimerkiksi alle 80 %), jotta tietokantaan tallennetaan vain luotettava data [54]. Tämä lisää järjestelmän tehokkuutta ja vähentää tarvetta käsitellä jälkikäteen virheellisiä signaaleja. Telegraf muuntaa sitten saamansa datan muotoon, joka on optimoitu InfluxDB:tä varten, ja lähettää sen tallennettavaksi.

InfluxDB on erikoistunut aikasarjatietokanta, joka on suunniteltu optimoimaan nopean kirjoitustehon ja tehokkaaseen hakuun suuria määriä aikaleimattuja tietoja [54]. Tämä tekee siitä ideaalisen valinnan tähän sovellukseen, koska jokainen droonihavainto on aikaleimattu mittaus. InfluxDB mahdollistaa nopean historiadatan hakua ja trendianalyysiä, mikä on välttämätöntä sekä anomalian havaitsemiseen että koneoppimisen koulutukseen. Havainnot tallennetaan taulukoihin, joissa ne voidaan luokitella eri tunnuksilla, kuten `sensor_type=csi`, `location=garden` tai `confidence=0.95`. Tämä taggaus mahdollistaa erittäin tarkat ja nopeat kyselyt, esimerkiksi "etsi kaikki havainnot, joissa luotettavuus on yli 90 % ja ne ovat tulleet WiFi CSI -sensorista puutarhassa viimeisen tunnin aikana". Tämä nopea hakukyky on keskeinen komponentti järjestelmän "älyn" toiminnan tukemiseksi. Lopuksi, järjestelmän visualisointiin ja raportointiin voidaan käyttää työkalua kuten Grafanaa, joka voi suoraan liittyä InfluxDB:hen ja näyttää reaaliaikaisia karttapohjaisia havaintokuvioita, mikä parantaa käytettävyyttä ja nopeuttaa päätöksentekoa [54].

Yhteenvetona, tämä datakeskeinen arkkitehtuuri on erittäin vahva, koska se on rakennettu modulaarisesti ja avoimen lähdekoodin työkaluilla. Se on skaalautuva, koska uusia sensoreita voidaan lisätä helposti MQTT-aiheiden kautta. Se on robusti, koska MQTT selviää väliaikaisista yhteyskatkoista ja Telegraf suodattaa dataa. Ja lopuksi, se on älykäs, koska InfluxDB:n nopea tallennus- ja hakukyky mahdollistaa jatkuvan anomalian havaitsemisen ja koneoppimisen, mikä tekee järjestelmästä dynaamisen ja oppivamman.

## Oppiva algoritmi ja koneoppiminen: anomalian havaitseminen ja luokittelun parantaminen

Ehdotetun arkkitehtuurin ytimessä on oppiva algoritmi, joka muuttaa joukon sensorien raakaa dataa ja yksinkertaisia havaintoja yhdeksi koherentiksi ja tarkaksi ilmoitukseksi. Tämä algoritmi perustuu koneoppimiseen ja mahdollistaa järjestelmän "älyn" kehittymisen ajan myötä. Sen tehtäviä ovat kaksi keskeistä toimintoa: anomalian havaitseminen, joka perustuu yksinkertaisiin sääntöihin, ja tarkempi luokittelu, joka perustuu koneoppimismalleihin, jotta järjestelmä voi oppia erottamaan droonit muusta ympäristöllisestä häiriöstä. Tämä kaksivaiheinen lähestymistapa mahdollistaa sekä nopean reagoinnin että jatkuvan parannuksen tarkkuudessaan.

Ensimmäinen ja nopeampi vaihe on anomalian havaitseminen. Tämä perustuu siihen, että droonihavainto on poikkeus normaalissa ympäristössä. InfluxDB-tietokannan avulla voidaan kirjoittaa kyselyjä (esimerkiksi käyttäen Flux-kieltä), jotka etsivät poikkeavia tapahtumia. Esimerkiksi yksinkertainen sääntö voisi olla: "jos WiFi CSI -anturi raportoi liikettä puutarhassa ja SDR-passiivitutka raportoi Doppler-siirtymää samalta alueelta samanaikaisesti, merkitse se poikkeavaksi tapahtumaksi". Tämä logiikka perustuu sensorifuusioperiaatteeseen, jossa yhdistetään useita riippumattomia havaintoja [23]. Tämä lähestymistapa on tehokas, koska se vähentää merkittävästi virheellisiä hälytyksiä, joita yksittäinen anturi voi aiheuttaa. Esimerkiksi lintu voi aiheuttaa WiFi CSI:stä hälytyksen, mutta se ei todennäköisesti aiheuta SDR:stä merkittävää Doppler-siirtymää samalla tavalla. Vastaavasti, SDR voi havaita lentävän kohteen, mutta jos se on kaukana ja ei ole mitään muuta tukea, järjestelmä voi luokitella sen ensisijaisesti epävarmaksi havainnoksi. Tämä anomalian havaitseminen on järjestelmän ensimmäinen puolustusviiva ja se mahdollistaa nopean, peruspohjaisen reagoinnin ilman, että tarvitaan monimutkaisia koneoppimismalleja. Tekoälyn ja koneoppimisen integraatio on keskeinen innovaatio, joka mahdollistaa tarkan ja luotettavan droonien havainnoinnin [16,49].

Toinen, tarkempi vaihe on koneoppimisen käyttöönotto luokittelun tarkentamiseksi. Vaikka anomalian havaitseminen on hyvä aloitus, se ei vielä erota drooneja linnuista tai muita häiriötekijöitä vastaan. Tähän tarvitaan koulutettuja luokittelijamalleja. Tämä prosessi on iteratiivinen ja se koostuu neljästä vaiheesta:

1.  **Datan keruu:** Järjestelmä kerää havaintoja normaaleista olosuhteista. Tämä sisältää dataa, jossa on lentäviä lintuja, autoja, tuulen aiheuttamaa liikettä ja muita tavallisia häiriötekijöitä. Tämä data tallennetaan InfluxDB:hen samankaltaisilla tageilla kuin droonihavainnot, mutta eri luokitusmerkillä (esim. `class=bird`, `class=car`). Tämä on keskeistä, koska koneoppimismallit tarvitsevat laadukasta koulutusdataa.

2.  **Datamerkintä:** Kun käyttäjä tai operaattori on varma siitä, että drooni on havaittu, hän voi manuaalisesti merkitä kyseiset havainnot InfluxDB:ssä luokaksi `class=drone`. Tämä prosessi, jota kutsutaan ohjatuksi oppimiseksi, tarjoaa mallille positiivisia esimerkkejä. Tarkkuus on tässä vaiheessa ratkaisevan tärkeää, koska virheellisesti merkitty data heikentää mallin suorituskykyä.

3.  **Mallin koulutus:** Kerätty ja merkitty data siirretään koneoppimisalustalle, jossa käytetään työkaluja kuten scikit-learn tai TensorFlow/Keras. Tässä vaiheessa valitaan sopiva mallityyppi. Koska data perustuu monenlaisiin sensorien havaintoihin, mahdollista on käyttää useita eri lähteistä tulevaa dataa. Konvoluutioneuroverkko (CNN) -mallit ovat erityisen hyviä kuvien luokitteluun, ja ne voidaan soveltaa myös mikro-Doppler-spektrogrammeihin tai muuhun visuaaliseen dataan [20]. Toisaalta, jos data on enemmän aikasarjatyyliltään (esim. aikaleimat, signaalin voimakkuudet), aikariippuvat neuroniverkon (LSTM) kaltaiset synteettiset sydänverkon mallit voivat olla tehokkaampia [81]. Malli koulutetaan oppimaan eroja droonien ja häiriölähteiden välillä käyttäen kerättyä dataa.

4.  **Mallin käyttöönotto ja päivittäminen:** Kun malli on koulutettu ja sen suorituskyky on arvioitu, se voidaan käyttöön ottaa automatisoituun luokitteluun. Koulutettu malli voidaan tallentaa ja ladata takaisin reunoille (edge) esimerkiksi käyttäen TinyML-työkaluja. Tämä mahdollistaa reaaliaikaisen, reunoilla tapahtuvan luokittelun, jolloin järjestelmä voi antaa paljon tarkempia ja luotettavampia havaintoja ilman tarvetta lähettää dataa keskitetystä tietokannasta. Tämä prosessi on jatkuvaa; uutta dataa kerätään jatkuvasti, ja kun järjestelmä on kerännyt tarpeeksi uutta dataa tai kun sen suorituskyky heikkenee, mallia voidaan uudelleenkouluttaa ja päivittää, mikä mahdollistaa jatkuvan oppimisen ja parannuksen.

Tämä koneoppimisprosessi on keskeinen osa järjestelmää, koska se mahdollistaa droonien ja häiriölähteiden luotettavan erottelun, joka on yksi suurimmista haasteista tässä sovelluksessa [32]. Käyttämällä avoimen lähdekoodin työkaluja ja tarkkailemalla järjestelmän suorituskykyä, harrastajaryhmät voivat kehittää hyvin tarkkoja ja erikoistuneita luokittelijoita omalle ympäristölleen, jolloin järjestelmä oppii tunnistamaan esimerkiksi tietyn lintulajin tai ajoneuvon, joka aiheuttaa paljon häiriötä alueella. Tämä tekee järjestelmästä yhä arvokkaamman työkalun kansalaisten tekemässä ilmavalvonnassa.

## Eettis-oikeudellinen viitekehys: passiivisuus, privaattisuus ja radioamatöörien lainsäädännöllinen asema

Tässä tutkimuksessa esitellyn droonien havainnointijärjestelmän kehittäminen ja käyttöönotto edellyttää syvällistä huomiota eettisiin ja oikeudellisiin näkökulmiin, erityisesti kun kyseessä on kansalaisten tekemä turvallisuustoiminta. Järjestelmän arkkitehtuuri perustuu ydinperiaatteeseen, joka on juridisesti ja eettisesti eduksi: passiivisuuteen. Järjestelmä ei itse lähetä mitään signaaleja, vaan se vain kuuntelee ja analysoi olemassa olevia siviili-infrastruktuurin signaaleja, kuten radio-, TV-, LTE- tai WiFi-signaaleja [61]. Tämä eroaa merkittävästi aktiivisista tutkasovelluksista, jotka lähettävät signaaleja ja voivat paljastaa omaa sijaintiaan sekä aiheuttaa sähkömagneettista häiriötä muulle liikenteelle. EU:n ja monet kansalliset lait sallivat yleensä passiivisen signaalikuuntelun, kunhan se ei riko salauksia tai häiritse lainmukaista radioliikennettä [1,3]. Tämä passiivisuus on avainasemassa, sillä se mahdollistaa järjestelmän käytön laillisesti ja vähentää merkittävästi yksityisyysriskejä.

Yksityisyyden suojelu on keskeinen huolenaihe. Järjestelmän käyttämät teknologiat, eli passiivitutka ja WiFi CSI, eivät kerää henkilökohtaista dataa, kuten MAC-osoitteita, viestien sisältöä tai muita tunnistettavia tietoja. Sen sijaan ne analysoivat vain signaalin fysikaalisia ominaisuuksia, kuten amplitudia, vaihetta ja taajuusmuutoksia, joita liike aiheuttaa [70]. Tämä on merkittävä ero aktiiviseen skannaukseen, jossa laite lähettää signaaleja ja mittaavat niiden heijastuksia, mikä voi sisältää tunnistettavia tietoja. Euroopan unionin yleisen tietosuoja-asetuksen (GDPR) periaatteet, kuten tietojen keruun minimointi ja tietojen käytön selkeys, sopivat hyvin tähän menetelmään. Koska järjestelmä ei kerää henkilötietoja, se ei kuulu suoraan GDPR:n soveltamisalaan, mikä helpottaa lainsäädännöllistä asemaa merkittävästi. Legal certainty, eli lainsäädännön selkeys ja ennustettavuus, on keskeinen periaate, ja tämä passiivinen menetelmä on helpompi sijoittaa olemassa olevan lainsäädännön viitekehykseen kuin uudet, aktiiviset valvontatekniikat [42].

Radioamatööriharrastajien asema tässä kontekstissa on erityisen relevantti ja mahdollistava. Radioamatöörit ovat yleensä laillisesti rekisteröityneitä käyttäjiä, joilla on oikeus käyttää ohjelmistoradioita (SDR) ja testata erilaisia radiolaitteita ja -protokollia. Heidän toimintansa on yleensä sallittua, kunhan se ei häiritse kauppaa tai muita lainmukaisia radioliikennevälineitä. Tämä tekee heistä luonnollisia kehittäjiä ja käyttäjiä tällaisesta järjestelmästä. Heillä on jo olemassa oleva lupa ja asiantuntemus, joka ei vaadi lisälupia passiivisen signaalikuuntelun harjoittamiseksi. Tämä tekee radioamatööreistä tärkeän resurssin kansalaisten tekemässä ilmavalvonnassa. He voivat aktivoida harrastusryhmiään tai yksittäisiä jäseniään osallistumaan järjestelmän rakentamiseen, testaukseen ja käyttöön. Tällainen yhteistyö voisi olla erityisen arvokasta alueilla, joilla viranomaiset eivät tarjoa aktiivista ilmavalvontaa. Lainsäädännön rajoitukset, kuten laki droonien torjunnasta, ovat usein tiukkoja siviileille, mutta tämä järjestelmä on suunniteltu pelkäksi havaintojärjestelmäksi, ei fyysiseksi torjuntajärjestelmäksi, mikä pysyy lainsäädännöllisten rajoitteiden sisällä [5].

Kuitenkin, vaikka järjestelmä on passiivinen, sen käytön tulisi olla selkeästi rajattu ja sen tulokset tulisi käsitellä vastuullisesti. Esimerkiksi havaintojen raportointi viranomaisille tulisi tapahtua selvien ohjeiden mukaan, ja järjestelmän käyttäjien tulisi ymmärtää vastuunsa. EU on jo ryhtynyt tekemään toimia droonien ja niitä vastustavien järjestelmien turvallisuudesta, ja pyrkii varmistamaan, että laillisten viranomaisten kapasiteetit ja koulutus ovat olemassa uhan vastaisen toiminnan varmistamiseksi [1,3]. Tällainen kansalaisyhteistyö voi täydentää viranomaisten toimintaa, mutta sen tulisi tapahtua yhteistyössä ja kunnioittaen toisiaan. Lopulta, tämän arkkitehtuurin eettis-oikeudellinen viitekehys perustuu siihen, että se on passiivinen, ei kerää henkilötietoja, ja se hyödyntää jo olemassa olevaa lupausta, kuten radioamatöörien toimintaa, jolloin se pysyy laillisesti ja moraalisesti hyväksyttävällä pohjalla kansalaisten tekemänä turvallisuuden tueksi.

## Yhteenveto ja strateginen näkökulma: harrastajapohjaisen ilmavalvonnan mahdollisuudet

Tämä tutkimusraportti on esittänyt ja analysoinut tieteellisesti perustellun arkkitehtuurin kehittyneelle droonien havainnointijärjestelmälle, joka yhdistää LoRaWAN-, SDR- ja WiFi CSI -sensoriteknologiat oppivan algoritmin avulla. Järjestelmä perustuu keskeiseen fysikaaliseen periaatteeseen, mikro-Doppler-ilmiöön, joka mahdollistaa droonien potkurien liikkeen erottamisen muusta ympäristöllisestä liikkeestä. Tämä teoreettinen perusta, yhdistettynä moderniin datakeskeiseen arkkitehtuuriin (`MQTT → Telegraf → InfluxDB`) ja koneoppimiseen, muodostaa vahvan ja monipuolisen pohjan kansalaisten tekemään ilmavalvontaan, erityisesti harrastajapohjaisessa ympäristössä. Raportin keskeinen johtopäätös on, että tällainen järjestelmä on teknisesti ja taloudellisesti mahdollista rakentaa käyttäen avoimen lähdekoodin työkaluja ja on juridisesti ja eettisesti mahdollistava, kun se suunnitellaan passiiviseksi havaintojärjestelmäksi.

Arkkitehtuurin vahvuus piilee sen monipuolisuudessa. Yksittäinen anturi ei ole täydellinen, mutta niiden yhdistäminen sensorifuusiolla luodaan yhteensä robusti ja luotettava järjestelmä. Ohjelmistoradio (SDR) tarjoaa pitkän matkan valvontakuvauksen hyödyntämällä olemassa olevia LTE- tai 5G-signaaleja, mikä mahdollistaa ajoissa varoituksen [2]. WiFi Channel State Information (CSI) toimii tarkkana, lyhyen matkan anturina, joka vahvistaa havainnon ja tarjoaa lisätietoa liikkeen luonteesta, jopa seinien läpi [82]. LoRaWAN puolestaan toimii luotettavana "verkon ylläpitäjänä", joka varmistaa, että kriittiset tiedot kulkevat koko ajan, vaikka muut järjestelmät olisivat pois käytöstä [24]. Tämä kolmiportainen lähestymistapa vähentää merkittävästi virheellisten hälytysten riskiä, joka on yksi suurimmista haasteista droonien havaitsemisessa [32]. Datakeskeinen arkkitehtuuri on erittäin skaalautuva ja joustava, mikä mahdollistaa jatkuvan kehityksen ja oppimisen. Koneoppiminen on keskeinen tekijä, joka mahdollistaa droonien ja häiriölähteiden erottelun, ja järjestelmä voi "oppia" paremmin ajan myötä keräämällä dataa ja uudelleenkouluttamalla mallejaan [49].

Strategisesti ottaen tämä arkkitehtuuri tarjoaa merkittävän mahdollisuuden täyttää aukko kansalaisten tekemässä ilmavalvonnassa. Kaupunkialueilla ja suojeltavilla alueilla droonien uhka on kasvanut, ja viranomaisten resurssit ovat usein rajalliset. Tällainen harrastajapohjainen, kehittyneen infrastruktuurin hyödyntävä järjestelmä voi tarjota lisäkapasiteettia ja laajempaa kattavuutta. Se on erityisen hyvä valinta vapaaehtoisten maanpuolustusryhmien käyttöön, koska se on passiivinen, ei vaadi lupaa aktiiviseen aseistoon, ja se sopii hyvin radioamatööriharrastajien lakisääteiseen toimintaan [1]. Projektin menestyksekäs toteutus edellyttää kuitenkin systemaattista kenttätestausta, jossa järjestelmää testataan eri ympäristöissä ja erilaisilla häiriölähteillä, jotta koneoppimismallit voidaan kouluttaa oikein [9]. Aloitusvirityksen kannattaa tehdä pienellä ja halvalla komponentilla, kuten WiFi CSI -anturilla ESP32:lla, jolloin perusdata-arkkitehtuuri voidaan vahvistaa ennen kuin siirrytään monimutkaisempiin ja kalliimpiin SDR-järjestelmiin [84].

Haasteita on kuitenkin myös. Järjestelmän tarkkuus riippuu suuresti koneoppimismallien laadusta, ja niiden kouluttaminen vaatii runsaasti ja laadukasta koulutusdataa. Järjestelmä on myös alttiina uusille häiriötekijöille, kuten uusille radiolaitteille tai WiFi-standardien muutoksille. Lopulta, vaikka järjestelmä on suunniteltu pelkäksi havaintojärjestelmäksi, sen käytön tulisi olla selkeästi rajattu ja vastuullinen, ja sen tulokset tulisi käsitellä yhteistyössä oikeudellisten viranomaisten kanssa. 

Yhteenvetona, ehdotettu arkkitehtuuri edustaa konkreettista ja realistista askelta kohti kansalaisten tekemää, teknologisesti perusteltua ilmavalvontaa. Se yhdistää nykyisin saatavilla olevat teknologiat yhdeksi koherentiksi, monipuoliseksi ja luotettavaksi kokonaisuudeksi, joka voi merkittävästi lisätä kansallista turvallisuutta harrastajapohjaisessa ympäristössä.

## Käytetty tekoäly
Artikkelin luomisessa on käytetty Qwen3.6-Plus tekoälyä.

## Käytetyt lähteet


1. Action Plan on Drone and Counter Drone Security - EUR-Lex https://eur- lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52026DC0081
2. A Survey on Detection, Classification, and Tracking of UAVs using ... https://arxiv.org/ html/2402.05909v2
3. [PDF] C-UAS detection, tracking and identification technology https://publications.jrc.ec.europa.eu/repository/bitstream/JRC140692/JRC140692_01.pdf
4. Secure Communication in Drone Networks: A Comprehensive ... https://www.mdpi.com/2504-446X/9/8/583
5. Mini/Micro UAV detection in the presence of ISM or spurious signals ... https://www.sciencedirect.com/science/article/pii/S2215098623002690
6. Detection and Identification of Non-cooperative UAV Using a COTS ... https://dl.acm.org/doi/full/10.1145/3638767
7. (PDF) A Survey on Detection, Classification, and Tracking of Aerial ... https://www.researchgate.net/publication/ 377741982_A_Survey_on_Detection_Classification_and_Tracking_of_Aerial_Threats_u   sing_Radar_and_Communications_Systems
8. ARTICLE IN PRESS - Nature https://www.nature.com/articles/ s41598-026-48925-1_reference.pdf
9. On the Detection of Unauthorized Drones-Techniques and Future ... https://ieeexplore.ieee.org/iel7/7361/9795939/09765451.pdf
10. State-of-the-Art Mobile Radiation Detection Systems for Different ... https://www.mdpi.com/1424-8220/21/4/1051
11. [PDF] RadarConf'24 - 2024 IEEE RADAR CONFERENCE https://confcats- siteplex.s3.us-east-1.amazonaws.com/radar24/ Radar_Conf_24_Program_V5_6a27fe72bd.pdf
12. [PDF] RF-Based Low-SNR Classification of UAVs Using Convolutional ... https://arxiv.org/pdf/2009.05519
13. (PDF) Recent Advances in mmWave-Radar-Based Sensing, Its ... https://www.researchgate.net/publication/375164853_Recent_Advances_in_mmWave-Radar-  Based_Sensing_Its_Applications_and_Machine_Learning_Techniques_A_Review
14. A Comprehensive Survey on Wi-Fi Sensing for Human Identity ... https://www.mdpi.com/2079-9292/12/23/4858

15. The Perception System of Intelligent Ground Vehicles in All Weather ... https://www.mdpi.com/1424-8220/20/22/6532
16. (PDF) A Comprehensive Survey on Artificial Intelligence for ... https://www.researchgate.net/publication/ 374021900_A_Comprehensive_Survey_on_Artificial_Intelligence_for_Unmanned_Aeri  al_Vehicles
17. Classification and Discrimination of Birds and Small Drones Using ... https://www.mdpi.com/2624-6120/4/2/18
18. Drone Detection and Classification Using Physical-Layer Protocol ... https://pmc.ncbi.nlm.nih.gov/articles/PMC9460464/
19. Detecting Fiber-Optic Drones with Micro-Doppler Signatures - LinkedIn https://www.linkedin.com/posts/samuel-
bendett-06996018_%D0%B2%D0%BE%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-
%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA% D0%B0-activity-7445198568975478786-dyP8
20. Radar-Spectrogram-Based UAV Classification Using Convolutional ... https://www.mdpi.com/1424-8220/21/1/210
21. Method for classification of UAV flight control RF signals based on ... https://www.nature.com/articles/s41598-025-25498-z
22. CNN-Based UAV Detection and Classification Using Sensor Fusion https://ieeexplore.ieee.org/iel7/6287639/10005208/10175389.pdf
23. Human Activity Recognition via Score Level Fusion of Wi-Fi CSI ... https://www.mdpi.com/1424-8220/23/16/7292
24. Adaptive Antenna for Maritime LoRaWAN: A Systematic Review on ... https://pmc.ncbi.nlm.nih.gov/articles/PMC12526727/
25. Recent Advances in LoRa: A Comprehensive Survey https://dl.acm.org/doi/full/ 10.1145/3543856
26. A systematic mapping and review on machine learning for non ... https://www.sciencedirect.com/science/article/pii/S2405959526000044
27. AI for UAV-Assisted IoT Applications: A Comprehensive Review https://ieeexplore.ieee.org/iel7/6488907/10210448/10113154.pdf
28. LoRa Communication for Agriculture 4.0: Opportunities, Challenges ... https://arxiv.org/html/2409.11200v1
29. Enhancing Human Activity Recognition with LoRa Wireless RF ... https://www.mdpi.com/2079-9292/13/2/264
30. UAV Recognition Based on Micro-Doppler Dynamic Attribute ... - MDPI https://www.mdpi.com/2072-4292/13/6/1205

31. [PDF] mmHawkeye: Passive UAV Detection with a COTS mmWave Radar https://arxiv.org/pdf/2308.06479
32. Detection and Identification of Non-cooperative UAV Using a COTS ... https://dl.acm.org/doi/10.1145/3638767
33. The use of unmanned aerial vehicles (UAVs) for engineering ... https://link.springer.com/article/10.1007/s10064-020-01766-2
34. Protect Your Sky: A Survey of Counter Unmanned Aerial Vehicle ... https://www.researchgate.net/publication/ 346287524_Protect_Your_Sky_A_Survey_of_Counter_Unmanned_Aerial_Vehicle_Syst  ems
35. RF/WiFi-based UAV surveillance systems: A systematic literature ... https://www.sciencedirect.com/science/article/pii/S2542660524001422
36. Software-Defined Radio Deployments in UAV-Driven Applications https://ieeexplore.ieee.org/iel8/8782711/10345397/10713191.pdf
37. A Survey of Modern Data Acquisition and Analysis Systems ... - PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC12986620/
38. [PDF] HUAWEI RESEARCH Issue 5 https://www-file.huawei.com/-/media/corp2020/ pdf/publications/huawei-research/2023/huawei-research-issue5-en-2.pdf
39. [PDF] The Logistics Trend Radar - DHL https://www.dhl.com/content/dam/dhl/ global/core/documents/pdf/glo-core-logistics-trend-radar-5thedition.pdf
40. Glo Core Logistics Trend Radar 5thedition | PDF - Scribd https://www.scribd.com/ document/492727199/Glo-Core-Logistics-Trend-Radar-5thedition-1
41. RTIMS: Real-Time Indoor Monitoring Systems - MDPI https://www.mdpi.com/ 2076-3417/15/24/13217
42. [PDF] Law and ICT - European Parliament https://www.europarl.europa.eu/RegData/ etudes/STUD/2024/762738/IPOL_STU(2024)762738_EN.pdf
43. Ctrl + Alt + Remedy? Child Rights, Access to Justice and Preventive ... https://www.mdpi.com/2075-4698/16/4/116
44. A lightweight FL-based UAV detection model using thermal images https://dl.acm.org/doi/pdf/10.1145/3659677.3659705
45. A Comparison of Machine Learning Algorithms for Wi-Fi Sensing ... https://www.mdpi.com/2079-9292/12/18/3935
46. Orientation-Independent Human Activity Recognition Using ... - MDPI https://www.mdpi.com/1424-8220/23/13/5810
47. Human Activity Recognition Based on Deep Learning and Micro ... https://www.mdpi.com/1424-8220/24/8/2530

48. A Time-Synchronized Multi-Sensor drone dataset acquired ... - Nature https://www.nature.com/articles/s41597-026-06802-6
49. [PDF] A Comprehensive Survey of Unmanned Aerial Vehicles Detection ... https://pdfs.semanticscholar.org/83ad/3a7e098355e1bf85945af8a92930afaccc6e.pdf
50. Advances and Challenges in Drone Detection and Classification ... https://www.researchgate.net/publication/ 376839468_Advances_and_Challenges_in_Drone_Detection_and_Classification_Techn   iques_A_State-of-the-Art_Review
51. Deep-Learning for Radar: A Survey - IEEE Xplore https://ieeexplore.ieee.org/ iel7/6287639/6514899/09568916.pdf
52. Advances and Challenges in Drone Detection and Classification ... https://www.mdpi.com/1424-8220/24/1/125
53. Integrated Sensing and Edge AI: Realizing Intelligent Perception in 6G https://arxiv.org/html/2501.06726v2
54. A Novel 5G PMN-Driven Approach for AI-Powered Irrigation and ... https://ieeexplore.ieee.org/iel8/6287639/10380310/10662981.pdf
55. Sensors, Volume 22, Issue 24 (December-2 2022) - 454 articles https://www.mdpi.com/1424-8220/22/24
56. State of the Art: Small Spacecraft Technology - Academia.edu https://www.academia.edu/127985821/State_of_the_Art_Small_Spacecraft_Technology
57. Design and Implementation of a Near Real-Time Human Detection ... https://ieeexplore.ieee.org/iel8/6287639/10820123/11194153.pdf
58. Utilization of Internet of Things and Wireless Sensor Networks for ... https://www.mdpi.com/1424-8220/22/9/3273
59. AIoT-informed digital twin communication for bridge maintenance https://www.sciencedirect.com/science/article/pii/S092658052300095X
60. IIoT Technologies - GAO Tek https://gaotek.com/category/iot/iot-systems/iiot- technologies/
61. (PDF) UAV Detection and Tracking in Urban Environments Using ... https://www.researchgate.net/publication/ 374749971_UAV_Detection_and_Tracking_in_Urban_Environments_Using_Passive_Se  nsors_A_Survey
62. Accessible Real-Time Surveillance Radar System for Object Detection https://pmc.ncbi.nlm.nih.gov/articles/PMC7218906/
63. A Comprehensive Survey on Artificial Intelligence for Unmanned ... https://ieeexplore.ieee.org/iel7/8782711/9932544/10254249.pdf

64. [PDF] LiDAR Technology for UAV Detection - Semantic Scholar https://pdfs.semanticscholar.org/5668/ec57e4308c403b6dd7b47d16d1c190b0b9bc.pdf
65. MicNest: Long-Range Instant Acoustic Localizat - ACM Digital Library https://dl.acm.org/doi/pdf/10.1145/3560905.3568515
66. Urban Aviation: The Future Aerospace Transportation System for ... https://www.mdpi.com/2413-8851/8/4/218
67. MACHINE LEARNING AND DEEP TEMPORAL NETWORKS FOR ... https://www.researchgate.net/publication/ 400495987_MACHINE_LEARNING_AND_DEEP_TEMPORAL_NETWORKS_FOR_UAV_  VELOCITY_CLASSIFICATION_USING_HIGH-DIMENSIONAL_CSI_AND_RSSI_DATA
68. Sensors, Volume 26, Issue 5 (March-1 2026) - 338 articles https://www.mdpi.com/ 1424-8220/26/5
69. Combined RF-Based Drone Detection and Classification https://www.researchgate.net/publication/353474236_Combined_RF- based_drone_detection_and_classification
70. Reconstructing Depth Images of Moving Objects from Wi-Fi CSI Data https://arxiv.org/html/2503.06458v1
71. EMind: A Foundation Model for Multi-task Electromagnetic Signals ... https://arxiv.org/html/2508.18785v1
72. Classification of Birds and UAVs Based on Radar Polarimetry https://www.researchgate.net/publication/ 305218087_Classification_of_Birds_and_UAVs_Based_on_Radar_Polarimetry
73. words-333333 - cs.Princeton https://www.cs.princeton.edu/courses/archive/ spring18/cos226/assignments/autocomplete/testing/words-333333.txt
74. (PDF) Classification of Bird and Drone Targets Based on Motion ... https://www.researchgate.net/publication/ 356476337_Classification_of_Bird_and_Drone_Targets_Based_on_Motion_Characteris   tics_and_Random_Forest_Model_Using_Surveillance_Radar_Data
75. (PDF) Channel Attention based CNN for Improving UAV ... https://www.researchgate.net/publication/ 401552112_Channel_Attention_based_CNN_for_Improving_UAV_Classification_using
_Micro_Doppler_Spectogram_Images
76. (PDF) Micro-Motion Classification of Flying Bird and Rotor Drones ... https://www.researchgate.net/publication/358856321_Micro- Motion_Classification_of_Flying_Bird_and_Rotor_Drones_via_Data_Augmentation_an  d_Modified_Multi-Scale_CNN
77. Classification of drones based on mikro-Doppler signatures with ... https://www.researchgate.net/publication/

323347774_Classification_of_drones_based_on_mikro-Doppler_signatures_with_dual-   band_radar_sensors
78. (PDF) Enhanced UAV Detection and Classification with Birds Using ... https://www.researchgate.net/publication/ 392005458_Enhanced_UAV_Detection_and_Classification_with_Birds_Using_NLFM_P  ulse-Doppler_Radar
79. Micro-Doppler Recognition of Small Unmanned Aerial Vehicles via ... https://www.researchgate.net/publication/401171088_Micro- Doppler_Recognition_of_Small_Unmanned_Aerial_Vehicles_via_Attention_Fusion_and
_Pruning
80. (PDF) Temporal Deep Learning for Drone Micro-Doppler Classification https://www.researchgate.net/publication/ 327075159_Temporal_Deep_Learning_for_Drone_Micro-Doppler_Classification
81. (PDF) Micro-Doppler Signature-Based Detection, Classification, and ... https://www.researchgate.net/publication/346358922_Micro-Doppler_Signature- Based_Detection_Classification_and_Localization_of_Small_UAV_With_Long_Short-  Term_Memory_Neural_Network
82. WiFi CSI Based Energy-Efficient Drone Detection | Request PDF https://www.researchgate.net/publication/402848730_WiFi_CSI_Based_Energy-  Efficient_Drone_Detection
83. Modelling, Analysis, and Simulation of the Micro-Doppler Effect in ... https://www.mdpi.com/1424-8220/20/4/1049
84. Low-cost UAV detection via WiFi traffic analysis and machine learning https://www.nature.com/articles/s41598-023-47453-6
85. [PDF] Intelligent World 2030 - Huawei https://www-file.huawei.com/admin/asset/ v1/pro/view/d2c1c28eeba24f4ca7bdf0022805a1dc.pdf
86. CSI-F: A Human Motion Recognition Method Based on Channel ... https://www.mdpi.com/1424-8220/24/3/862
87. Low Power Digital Array Radar for Drone Detection and Micro ... https://www.researchgate.net/publication/ 336792951_Low_Power_Digital_Array_Radar_for_Drone_Detection_and_Micro-  Doppler_Classification
88. Intelligent World 2030: Future Outlooks | PDF - Scribd https://www.scribd.com/ document/965036710/Huawei-Intelligent-World-2030
89. Research on Cross-Scene Human Activity Recognition Based on ... https://www.mdpi.com/2079-9292/14/8/1518

90. 5G Radar and Wi-Fi Based Machine Learning on Drone Detection ... https://www.researchgate.net/publication/352621224_5G_Radar_and_Wi- Fi_Based_Machine_Learning_on_Drone_Detection_and_Localization
91. Sensors, Volume 25, Issue 13 (July-1 2025) - 405 articles https://www.mdpi.com/ 1424-8220/25/13
92. [PDF] European Law Enforcement Research Bulletin Environmental crime https://www.cepol.europa.eu/api/assets/media/downloads/2025/ CEPOL_European_LE_Research_Bulletin_Thematic_Edition_No1_Environmental_Crim e.pdf
93. [PDF] B REGULATION (EU) 2021/821 OF THE EUROPEAN ... - EUR-Lex https://eur-
lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02021R0821-20231216
94. Sensors, Volume 25, Issue 21 (November-1 2025) - 306 articles https://www.mdpi.com/1424-8220/25/21
95. Sensors, Volume 22, Issue 17 (September-1 2022) - 401 articles https://www.mdpi.com/1424-8220/22/17
96. Ras Current Digest 2021 English 33 | PDF - Scribd https://www.scribd.com/ document/532614807/Ras-Current-Digest-2021-English-33
97. Frontier Progress of Unmanned Aerial Vehicles Optical Wireless ... https://www.mdpi.com/1424-8220/20/19/5476
98. [PDF] What Will the Future of UAV Cellular Communications Be? A ... - HAL https://hal.science/hal-03844004/file/%5B10%5D.pdf
99. CNN Based Radar | PDF - Scribd https://www.scribd.com/document/998655001/ CNN-Based-Radar
100. [PDF] Classification of drones and birds using convolutional neural ... https://www.semanticscholar.org/paper/Classification-of-drones-and-birds-using-neural-to- Rahman-Robertson/36036208428d5ca9607842f66de630649f0a53f6
101. Appl. Sci., Volume 15, Issue 4 (February-2 2025) - 573 articles - MDPI https://www.mdpi.com/2076-3417/15/4
102. Supporting Global Communications of 6G Networks Using AI, Digital ... https://www.mdpi.com/2673-4001/6/2/35
103. [PDF] Jamming Attacks and Anti-Jamming Strategies in Wireless Networks https://arxiv.org/pdf/2101.00292
104. Issue 4 - Volume 6 - Engineering Research Express - IOPscience https://iopscience.iop.org/issue/2631-8695/6/4
105. Appl. Sci., Volume 15, Issue 21 (November-1 2025) - 550 articles https://www.mdpi.com/2076-3417/15/21

106. Sensors, Volume 26, Issue 7 (April-1 2026) - 273 articles https://www.mdpi.com/ 1424-8220/26/7
107. (PDF) Extraction of Micro-Doppler Features from Unmanned Aerial ... https://www.researchgate.net/publication/383230231_Extraction_of_Micro- Doppler_Features_from_Unmanned_Aerial_Vehicles_Based_on_Electromagnetic_Simu  lation
108. Sensors, Volume 25, Issue 23 (December-1 2025) - 302 articles https://www.mdpi.com/1424-8220/25/23
109. Bird and Micro-Drone Doppler Spectral Width and Classification https://www.researchgate.net/publication/372296477_Bird_and_Micro- Drone_Doppler_Spectral_Width_and_Classification
110. Artificial Intelligence for Communications and Networks https://link.springer.com/ content/pdf/10.1007/978-3-030-22971-9.pdf
111. Course of Study of Various Branches For Registration 2021-2023 https://www.scribd.com/document/522206336/Course-of-Study-of-Various-Branches-for-  Registration-2021-2023
112. Sensors, Volume 25, Issue 17 (September-1 2025) - 392 articles https://www.mdpi.com/1424-8220/25/17
113. Sensors, Volume 25, Issue 5 (March-1 2025) - 359 articles - MDPI https://www.mdpi.com/1424-8220/25/5
114. Sensors, Volume 22, Issue 5 (March-1 2022) - 382 articles https://www.mdpi.com/ 1424-8220/22/5
115. Recent Advances in LoRa: A Comprehensive Survey https://dl.acm.org/doi/ 10.1145/3543856
116. On Indoor Localization Using WiFi, BLE, UWB, and IMU Technologies https://pmc.ncbi.nlm.nih.gov/articles/PMC10610672/
117. Internet of Things: Device Capabilities, Architectures, Protocols, and ... https://www.researchgate.net/publication/ 366238024_Internet_of_Things_Device_Capabilities_Architectures_Protocols_and_Sm   art_Applications_in_Healthcare_Domain
118. A Survey of Machine Learning Techniques for Indoor Localization ... https://link.springer.com/content/pdf/10.1007/s10846-021-01327-z.pdf
119. AI-Powered Building Ecosystems: A Narrative Mapping Review on ... https://www.mdpi.com/1424-8220/25/17/5265
120. [PDF] Civil liability regime for artificial intelligence - European Parliament https://www.europarl.europa.eu/RegData/etudes/STUD/2020/654178/ EPRS_STU(2020)654178_EN.pdf

121. [PDF] Product Liability in a More Circular Economy https://theses.hal.science/ tel-05421330v2/file/PhD%20Thesis%20EVG%20-
%20Product%20Liability%20in%20a%20More%20Circular%20Economy%20-
%20defended%20version_compressed.pdf