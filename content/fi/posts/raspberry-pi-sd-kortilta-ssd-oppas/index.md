---
title: "Raspberry Pi 4 SD-kortilta SSD:lle – Täydellinen opas ja vianmääritys"
date: 2026-05-26
description: "Vaiheittainen opas Raspberry Pi 4-järjestelmän siirtämiseksi SD-kortilta USB-liitäntäiselle SSD-levylle. Opas sisältää tiedostojen siirron (rsync), osioiden laajennuksen sekä ratkaisut yleisimpiin ongelmiin, kuten UAS-yhteensopivuuteen (JMicron vs. ASMedia) ja virtalähteiden aiheuttamiin epästabiliteetteihin."
tags: 
  - "Raspberry Pi"
  - "SSD"
  - "USB-Boot"
  - "Home Assistant"
  - "Linux"
  - "ORICO"
  - "Vianmääritys"
  - "DIY"
  - "Linux"
  - "Kotiautomaatio"
  - "Hardware"
slug: "raspberry-pi-sd-kortilta-ssd-oppas"
draft: false
---

# Opas: Raspberry Pi 4:n siirto SD-kortilta SSD-levylle (USB-boot)

Raspberry Pi on monikäyttöinen, mutta sen SD-kortti on usein järjestelmän pullonkaula. SD-kortit ovat hitaita satunnaislukemisessa ja niillä on rajallinen kirjoituskesto, mikä näkyy etenkin Home Assistant- tai tietokantakäytössä.

Siirtämällä käyttöjärjestelmä SSD-levylle saat:

- **Nopeamman käynnistyksen ja sovellusten latautumisen.**

- **Pitkän käyttöiän (SSD kestää huomattavasti enemmän kirjoitussyklejä).**

- **Vakauden (ei korruptoituneita tiedostoja sähkökatkojen jälkeen).**

Tässä ohjeessa siirretään Raspberry Pi 4 Model B:n järjestelmä SD-kortilta USB-liitäntäiselle SSD-levylle käyttäen luotettavaa **ORICO SATA to USB3.0 -koteloa**. Ohje toimii myös Raspberry Pi 3B+ alkaen myös uudemmille Raspberryille.

---

## ⚠️ Varoitus
Tämä ohje sisältää vaiheita, jotka tuhoavat kohdelevyn (SSD) sisällön. Varmista, että valitset oikean laitteen (`/dev/sdX`). Tekijä ei vastaa mahdollisista tietojen menetyksistä.

---

## 🛠️ Tarvikkeet
1. **Raspberry Pi 4 Model B** (Rev 1.1 tai uudempi).
2. **SSD-levy** (esim. 128GB–500GB SATA SSD).
3. **USB 3.0 -kotelo** (Suositus: **ORICO** tai vastaava, joka tukee **UASP**-protokollaa. Vältä halpoja tuntemattomia malleja).
4. **Virallinen Raspberry Pi -virtalähde** (5.1V / 3A USB-C). *Tämä on kriittinen.*
5. Toimiva SSH-yhteys tai näyttö + näppäimistö.

---

## Vaihe 1: Valmistelut ja levyn tunnistus

Kytke SSD-levy Raspin **siniseen USB 3.0 -porttiin**. Avaa terminaali ja tarkista, miten järjestelmä tunnistaa levyn:

```bash
lsblk
```
*Tulosteen pitäisi näyttää `sda`, `sdb` tai `sdc` (tässä ohjeessa käytetään esimerkkinä `sdc`). Huomaa, että `mmcblk0` on SD-kortti.*

### Ota SD-kortista varmuuskopio (suositus)
Ennen kuin teet mitään, on viisasta varmuuskopioida tärkeät tiedot tai ottaa täysi image SD-kortista `dd`-komennolla tai Win32 Disk Imagerilla tietokoneella.

---

## Vaihe 2: Osioinnin kopiointi (sfdisk)

Kopioidaan SD-kortin partitiorakenne (GPT/MBR) SSD:lle, jotta osiot vastaavat kooltaan alkuperäisiä.

```bash
# Tarkistetaan SD-kortin rakenne
sudo sfdisk -d /dev/mmcblk0 | sudo sfdisk /dev/sdc
```
*Komento varoittaa mahdollisista käytössä olevista levyistä. Varmista, että valitset oikean kohdelevyn, eli tässä tapauksessa `sdc`:n. Tämä luo SSD:lle vastaavan boot-osion ja root-osion.*

---

## Vaihe 3: Tiedostojärjestelmien alustus

Nyt luodaan tiedostojärjestelmät osioille. Koska `sfdisk` kopioi vain taulukon, itse osiot ovat vielä "raakoja".

```bash
# Tunnista uudet osiot
sudo partprobe /dev/sdc
lsblk -f /dev/sdc

# 1. Boot-osio (FAT32)
sudo mkfs.vfat -F 32 -n boot /dev/sdc1

# 2. Root-osio (ext4)
sudo mkfs.ext4 -L rootfs /dev/sdc2
```

---

## Vaihe 4: Liittäminen ja tietojen kopiointi

Liitetään sekä lähde- että kohdelevyt, jotta voimme siirtää tiedostot.

```bash
# Luo mount-pisteet
sudo mkdir -p /mnt/src /mnt/dst

# Liitä SSD-levy
sudo mount /dev/sdc2 /mnt/dst
sudo mkdir -p /mnt/dst/boot
sudo mount /dev/sdc1 /mnt/dst/boot

# Varmista tila: SSD:llä on oltava yhtä paljon tilaa kuin SD-kortilla on käytettyä
df -h /mnt/dst
df -h /dev/mmcblk0p2
```

### Tiedostojen siirto (rsync)
Käytämme `rsync`-komentoa, koska se on turvallisin tapa. Se säilyttää oikeudet, linkit ja jättää pois virtuaaliset järjestelmähakemistot.

```bash
sudo rsync -aHAXxv --info=progress2 /mnt/src/ /mnt/dst/
```
*Huom: `/mnt/src` viittaa SD-kortin juureen, `/mnt/dst` SSD:hen.*

---

## Vaihe 5: Boot-tiedostojen varmistaminen

Tämä on kriittinen vaihe. Koska formatoimme SSD:n boot-osion tyhjäksi, sille täytyy kopioida käynnistystiedostot (`cmdline.txt`, `config.txt` jne.).

```bash
# Kopioi boot-tiedostot SD-kortilta SSD:lle
sudo cp -a /mnt/src/boot/* /mnt/dst/boot/
sudo cp -a /mnt/src/boot/firmware/* /mnt/dst/boot/firmware/ 2>/dev/null
```

### Tarkista PARTUUID ja cmdline.txt
Huomaa, että `sfdisk` kopioidessaan osiotaulun säilytti levyn tunnisteen (MBR ID), joten SSD:n osioiden `PARTUUID`-tunnisteet ovat **samoin kuin SD-kortilla**.

Tarkista tämä varmuudeksi:
```bash
lsblk -o NAME,PARTUUID /dev/sdc
```
Jos `PARTUUID`-tunnisteet (esim. `00442c1c-01` ja `-02`) täsmäävät alkuperäiseen SD-korttiin, **et tarvitse muutoksia tiedostoihin `fstab` tai `cmdline.txt`**.

Varmista kuitenkin, että `cmdline.txt` on olemassa ja viittaa oikeaan osioon:
```bash
# Tarkista cmdline.txt (Bookworm-versiossa polku voi olla /boot/firmware/)
cat /mnt/dst/boot/cmdline.txt
# TAI
cat /mnt/dst/boot/firmware/cmdline.txt
```
Rivissä pitäisi lukea `root=PARTUUID=00442c1c-02` (tai vastaava tunniste).

⚠️ **HUOM:** `cmdline.txt`-tiedostossa ei saa olla rivinvaihtoa lopussa! Se on oltava yksi pitkä rivi.

---

## Vaihe 6: Käynnistys SSD:ltä

1. Siirrä välimuisti levylle: `sync`
2. Irrota osiot: `sudo umount /mnt/dst/boot && sudo umount /mnt/dst`
3. Sammuta Raspberry: `sudo shutdown now`
4. **Irrota virtajohto.**
5. **Poista SD-kortti.**
6. Varmista, että SSD on edelleen kiinni **sinisessä USB 3.0 -portissa**.
7. Kytke virta päälle.

Jos kaikki meni oikein, Raspberry boottaa nyt SSD:ltä.

---

## Vaihe 7: Tiedostojärjestelmän laajennus

SSD:llä on todennäköisesti enemmän tilaa kuin vanhalla SD-kortilla. Laajennetaan `root`-osio käyttämään koko levy.

```bash
sudo raspi-config --expand-rootfs
sudo reboot
```
Uudelleenkäynnistyksen jälkeen `df -h` näyttää koko levyn kapasiteetin.

---

## 🔍 Vianmääritys: Miksi bootti epäonnistui?

Jos ruutu jää mustaksi, värikkääksi tai verkko ei toimi, syynä on yleensä joko **virtalähde** tai **USB-kotelon ohjain**.

### 1. Virtalähdeongelma (keltainen ja vihreä ledi ethernet-portissa palaa tasaisesti, ei siis vilku)

Raspberry Pi 4 on nirso virran suhteen. Jos käytät vanhaa puhelimen laturia tai heikkolaatuista kaapelia:
*   **Oire:** Ethernet-portin LEDit palaa tasaisesti, mutta `ping` ei toimi. USB portissa oleva levy voi irrota ja liittyä uudelleen (`dmesg` näyttää I/O error).
*   **Ratkaisu:** Käytä aina **virallista 5.1V / 3-5A USB-C virtalähdettä**. Halvemmat laturit tiputtavat jännitettä kuormituksen noustessa (esim. kun SSD ja verkkokortti vetävät virtaa samaan aikaan).

### 2. USB-kotelon yhteensopivuus (JMicron vs. UASP)
Tämä on yleisin syy, miksi SSD ei käynnisty tai järjestelmä on hidas.

*   **Ongelma:** Monet halvat kotelot (esim. Temusta löytyvät "no-name" mallit) käyttävät **JMicron JMS578** -ohjainta. Raspberry Pi 4:n UAS-ajuri (USB Attached SCSI) ei aina tule toimeen tämän kanssa, mikä aiheuttaa `uas_eh_abort_handler` -virheitä ja I/O timeoutteja.
*   **Ratkaisu:**
    1.  **Osta oikea kotelo:** Suosittelen malleja, jotka tukevat natiivia **UASP**-protokollaa ja käyttävät **ASMedia ASM1153E** -piiriä. Hyvä esimerkki on **ORICO 2.5" SATA USB3.0 -kotelo**.
    2.  **Workaround (jos et voi vaihtaa koteloa):** Voit pakottaa kernelin käyttämään vanhempaa (mutta vakaampaa) USB Mass Storage -tilaa muokkaamalla `cmdline.txt`:tä ja lisäämällä rivin loppuun: `usb-storage.quirks=VID:PID:u`. (VID:PID löytyy `lsusb`-komennolla).

---

## ✅ Loppusanat
Siirrettyäsi järjestelmäsi SSD:lle huomaat eron välittömästi. Palvelut latautuvat nopeammin ja järjestelmä reagoi pirteämmin. Muista myös tarkistaa `fstab`-tiedosto, jos sinulla on muita liitettyjä levyjä, jotta niiden mount-pisteet eivät sekoitu laitenimien (`sda`, `sdb`) vaihtuessa.

Onnea matkaan! 🚀