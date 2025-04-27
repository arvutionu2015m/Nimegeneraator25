## 🏷️ Projekti nimi:  
**Nimegeneraator**

---

## 🎯 Projekti eesmärk:  
Luua veebipõhine rakendus, kus kasutaja saab sisestada märksõna ja seejärel:

- Genereerida loomingulisi nimeideid OpenAI abil  
- Salvestada genereeritud nimed andmebaasi  
- Märkida parimad nimed ⭐ lemmikute hulka  
- Allalaadida lemmiknimed `.txt` või `.csv` failina  
- Kustutada kõik salvestatud nimed vajadusel  
- Näha soovitatud parimat nime põhinedes nutikal reeglil  
- Kasutada modernset ja kasutajasõbralikku UX-i koos hele/tume režiimi toetusega  
- Saada koheseid Toast-teavitusi tegevuste õnnestumise kohta

---

## ⚙️ Tehnilised detailid:

- **Backend**: Python, Django 5.x
- **Frontend**: HTML5, Bootstrap 5.3
- **AI Integratsioon**: OpenAI API (`gpt-4`)
- **Andmebaas**: SQLite (arenduses) või PostgreSQL (soovi korral)
- **Teema tugi**: Automaatne hele/tume režiimi tuvastus + manuaalne teemavahetus (🌞 ↔ 🌙)
- **Kohandatud CSS**: Pehmed animatsioonid ja pulse efektid
- **Kohandatud UX parendused**:
  - Pulse efekt teemalülitil
  - Spinner laadimisel ja nupul
  - Bootstrap Toast teavitused Django `messages` abil

---

## 📈 Peamised funktsioonid:

| Funktsioon | Kirjeldus |
|:-----------|:----------|
| Märksõna sisestamine | Kasutaja sisestab märksõna, mille põhjal nimed genereeritakse |
| OpenAI integratsioon | Genereeritakse 5 loomingulist nime GPT-4 mudeliga |
| Nimede salvestamine | Iga genereeritud nimi salvestatakse koos märksõnaga |
| Lemmikute süsteem | Kasutaja saab nimed tähistada lemmikuteks või eemaldada |
| Parima nime soovitus | Nutikas algoritm pakub lühikese ja märksõnaga seotud parima nime |
| Nimede allalaadimine | Lemmikud nimed saab alla laadida `.txt` või `.csv` formaadis |
| Toastid ja eduteavitused | Iga tegevus annab kohese visuaalse kinnituse (nt "lisatud lemmikutesse") |
| Hele/Tume režiim | Toetab automaatset ja manuaalset teemavahetust |
| Kustuta kõik nimed | Ühe klikiga saab andmebaasi tühjendada |
| Statistika kuvamine | Kuvab salvestatud nimede ja lemmikute arvu

---

## 🌟 Erilised tugevused:

- **Väga kiire ja intuitiivne kasutuskogemus**
- **Professionaalsed Toast-teavitused**  
- **Kerge ja puhas Bootstrap 5 disain**  
- **Hele ja tume režiimi täielik tugi (automaatne + käsitsi)**  
- **Modulaarne ja skaleeritav kood** — valmis hilisemaks edasiarenduseks (nt kasutajakontod, otsing jne)

---

## 📚 Kaustastruktuuri näide:

```
nimegeneraator/
├── generaator/
│   ├── migrations/
│   ├── static/
│   │   └── images/
│   │       ├── logo_light.png
│   │       └── logo_dark.png
│   ├── templates/
│   │   └── generaator/
│   │       └── generate_name.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

## ✅ Projekti staatus:
**Täielikult töötav ja testitud MVP!**  
Valmis ka hilisemate laienduste jaoks:  
(nt kasutajakontod, oma teemade salvestamine, automaatne parimate nimede valik, genereeritud nimede põhjal statistika jms.)

---

# 🚀 Mis võiksid olla järgmised arendussuunad?

| Idee | Kirjeldus |
|:-----|:----------|
| Kasutajakontod | Iga kasutaja saaks oma salvestatud nimed |
| Märksõna põhine otsing | Filtreeri salvestatud nimesid kiiremini |
| Populariseeritud nimed | Kuvada enim salvestatud või lemmikuks märgitud nimed |
| Kategooriate toetus | Nimede jagamine ärinimedeks, bloginimedeks, appi nimedeks jne |
| Generatsiooniajaloost eksportimine | Kõik genereeritud nimed ühte suurde allalaadimisse |
