# 🔐 Encryptie App

## 📘 Overzicht

Deze applicatie is een eenvoudige **command-line tool** waarmee gebruikers tekst kunnen **versleutelen** en **ontsleutelen** met behulp van **symmetrische encryptie**.
De implementatie is gebaseerd op het **AES-256-algoritme** in combinatie met **PBKDF2** voor veilige sleutelafleiding uit een wachtwoord.

De applicatie is geschreven in **Python** en maakt gebruik van de betrouwbare en goed geteste `cryptography`-library.

---

## ⚙️ Functionaliteit

De applicatie biedt twee hoofdopties:

1. **Encryptie**
   De gebruiker voert een tekst en een wachtwoord in.

   * Er wordt een willekeurige `salt` en `iv` (initialization vector) gegenereerd.
   * Met behulp van PBKDF2 wordt uit het wachtwoord een 256-bits sleutel afgeleid.
   * De tekst wordt versleuteld met AES-256 in **CFB-modus**.
   * De uitvoer (versleutelde data) wordt als **base64-string** weergegeven.

2. **Decryptie**
   De gebruiker voert de versleutelde tekst en hetzelfde wachtwoord in.

   * De applicatie haalt `salt`, `iv` en de ciphertext uit de versleutelde data.
   * De sleutel wordt opnieuw gegenereerd met PBKDF2 en hetzelfde wachtwoord.
   * De originele tekst wordt succesvol teruggezet.

---

## 🧠 Symmetrische vs. Asymmetrische encryptie

Bij **symmetrische encryptie** wordt **dezelfde sleutel** gebruikt voor zowel versleutelen als ontsleutelen.
Dit maakt het proces **snel en efficiënt**, maar stelt hogere eisen aan **veilig sleutelbeheer** — de sleutel moet immers veilig gedeeld worden tussen partijen.

Bij **asymmetrische encryptie** worden daarentegen **twee sleutels** gebruikt:

* een **publieke sleutel** voor versleutelen,
* en een **privésleutel** voor ontsleutelen.
  Dit maakt sleuteluitwisseling veiliger, maar de berekeningen zijn trager en complexer.

In deze applicatie is bewust gekozen voor **symmetrische encryptie met AES-256**, omdat dit een modern, betrouwbaar en breed ondersteund algoritme is dat uitstekend geschikt is voor het veilig versleutelen van tekst met één wachtwoord.

---

## 🧩 Gebruikte encryptiemethode

* **Algoritme:** AES-256 (Advanced Encryption Standard met 256-bits sleutel)
* **Modus:** CFB (Cipher Feedback Mode)
* **Sleutelafleiding:** PBKDF2 met HMAC-SHA256 (100.000 iteraties)
* **Bibliotheek:** [cryptography](https://cryptography.io/en/latest/)

### 🔎 Waarom AES-256?

AES is de moderne industriestandaard voor symmetrische encryptie.
Het is **veilig, efficiënt en wijdverspreid getest**. AES-256 gebruikt een sleutel van 256 bits, waardoor brute-force aanvallen praktisch onmogelijk zijn met huidige technologie.
De keuze voor **CFB-modus** biedt flexibiliteit omdat het met tekststrings kan werken zonder dat padding nodig is.

---

## 🔑 Sleutelbeheer

De sleutel wordt **niet opgeslagen** en **niet hard-coded** in de applicatie.
In plaats daarvan:

* De gebruiker kiest een **wachtwoord**.
* Er wordt een willekeurige **salt** gegenereerd (16 bytes).
* Uit dat wachtwoord en de salt wordt met **PBKDF2-HMAC-SHA256** een sterke sleutel afgeleid.
* De salt wordt samen met de ciphertext opgeslagen in de uitvoer, zodat dezelfde sleutel later opnieuw kan worden afgeleid bij decryptie.

### Beveiligingsimplicaties

Deze aanpak voorkomt dat sleutels in platte tekst worden bewaard.
Zonder het juiste wachtwoord kan de originele tekst niet worden hersteld.
De enige zwakte blijft de **sterkte van het wachtwoord** — een zwak wachtwoord verlaagt de totale veiligheid van het systeem. Daarom is het belangrijk dat gebruikers een sterk wachtwoord kiezen.

---

## 🧩 Kerckhoffs’s Principe

Kerckhoffs’s Principe stelt dat:

> “Een versleutelingssysteem moet veilig blijven, zelfs als alle details van het systeem, behalve de sleutel, publiek bekend zijn.” — *Auguste Kerckhoffs (1883)*

Mijn applicatie voldoet hieraan:

* De **code**, **library** en **methode (AES)** mogen publiek zijn.
* De **veiligheid** hangt enkel af van het **geheimhouden van de sleutel** (het wachtwoord).
  Zelfs als een aanvaller toegang heeft tot de broncode of weet dat AES-256 wordt gebruikt, blijft de data onleesbaar zonder het juiste wachtwoord.

---

## 🧰 Installatie & gebruik

### 1️⃣ Vereisten installeren

```bash
pip install cryptography
```

### 2️⃣ Start de applicatie

```bash
python encryptie_app.py
```

### 3️⃣ Gebruik

* Typ `e` om tekst te versleutelen.
* Typ `d` om tekst te ontsleutelen.
* Volg de instructies in de terminal.

---

## 🧾 Voorbeeld

**Encryptie:**

![encrypt.png](images%2Fencrypt.png)

**Decryptie:**

![decrypt.png](images%2Fdecrypt.png)

---

## 🧩 Conclusie

Deze applicatie toont een veilige implementatie van **symmetrische encryptie** met **AES-256**.
Door het gebruik van **PBKDF2** voor sleutelafleiding en het volgen van **Kerckhoffs’s Principe** blijft de beveiliging robuust, ook als de broncode openbaar is.

De eenvoud en betrouwbaarheid van deze aanpak maken de tool geschikt voor educatieve doeleinden en kleine beveiligde teksttransacties.

---

## 📚 Bronnen

* GeeksforGeeks. (2025, August 7). Cryptography and its Types. GeeksforGeeks. https://www.geeksforgeeks.org/computer-networks/cryptography-and-its-types/
* GeeksforGeeks. (2025, August 8). Advanced Encryption Standard (AES). GeeksforGeeks. https://www.geeksforgeeks.org/computer-networks/advanced-encryption-standard-aes/
* A note about Kerckhoff’s Principle. (2025, October 24). The Cloudflare Blog. https://blog.cloudflare.com/a-note-about-kerckhoffs-principle/
* Cryptographic Storage - OWASP Cheat Sheet Series. (n.d.). https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
