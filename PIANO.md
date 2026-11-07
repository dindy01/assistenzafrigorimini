# Piano Lead Gen: novembre 2026 – febbraio 2027

Vincoli: **5 ore a settimana**, **€50 di budget iniziale**. Obiettivo: €1000/mese, il prima possibile (target 3 mesi).

---

## 1. Decisione sulla nicchia

**Nicchia principale: riparazione caldaie a Bologna.**
**Riserva, già pronta: riparazione elettrodomestici a domicilio a Bologna.**
Frigo industriali a Rimini: in pausa fino ad aprile.

| Criterio | Frigo industriali Rimini | **Caldaie Bologna** | Elettrodomestici Bologna |
|---|---|---|---|
| Domanda nov–feb | Bassa (riviera chiusa) | **Picco** (stagione di riscaldamento) | Stabile tutto l'anno |
| Urgenza | Alta (B2B) | **Alta** (casa senza riscaldamento) | Media |
| Valore dell'intervento | Alto | €40–100 piccoli guasti, €150–450 scheda elettronica | Uscita ~€55–89 + ricambi |
| Bacino | ~150k abitanti, stagionale | ~1M (area metropolitana) | ~1M |
| Valore stimato di un lead per il tecnico* | €30–50 | **€20–35** | €15–25 |
| Rischio | 10 pitch, 0 risposte | Tecnici già pieni in inverno, CPC più alti | Ticket basso, rischio "non conviene riparare" |

\* Le stime sul valore di un lead sono mie, ricavate dai prezzi degli interventi. Non sono un dato di mercato.

**Perché caldaie, adesso:**
- A Bologna l'accensione dei riscaldamenti 2026–27 è stata **rinviata al 1° novembre** per l'aria. Il periodo di guasti alla prima accensione è *adesso* e dura fino a metà aprile, cioè coincide con l'orizzonte di 3 mesi.
- Un guasto in inverno è un'emergenza per cui si paga e si chiama subito, quindi la conversione dagli annunci è buona.
- Bologna ha un bacino ~6 volte più grande di Rimini e non dipende dal turismo.

**Contro-argomento principale:** in inverno i tecnici caldaie bravi hanno già troppo lavoro e potrebbero non volere lead a pagamento. Mitigazione: punta ai **tecnici singoli o alle ditte di 1–3 persone** con poche recensioni, non ai centri autorizzati. Se non funziona entro il primo controllo (fine settimana 4), passa al sito elettrodomestici, che è già generato.

**Cosa non ho potuto verificare:** volumi di ricerca reali e CPC per Bologna (serve Keyword Planner dal tuo account Google Ads) e disponibilità dei domini.

---

## 2. Due cambiamenti rispetto al vecchio piano in Notion

1. **Gli annunci "Call-Only" non esistono più.** Da febbraio 2026 Google Ads non permette di crearne di nuovi, e quelli esistenti si spengono a febbraio 2027. Si usa una **campagna Search con asset di chiamata**.
2. **Numeri di telefono:** Google vuole che il numero appartenga all'attività promossa, e sta restringendo l'uso dei numeri virtuali. Usa un **numero mobile reale** (il tuo, con segreteria attiva) e pubblicalo sul sito. Quando arrivano i primi incassi, passa a una seconda SIM dedicata.

E un cambio di approccio:

3. **Non vendere un "audit del sito". Offri un cliente.** La nuova richiesta al tecnico costa poco: *"Ti mando gratis 1–2 clienti che mi chiamano per caldaie in zona tua. Se ti piacciono, parliamo."* È un sì facile, a differenza del vecchio pitch.

---

## 3. Budget da €50

| Voce | € |
|---|---|
| Dominio `.it` per il sito caldaie (1° anno) | ~5–12 (verifica sul registrar) |
| Google Ads (~8 giorni a €5/giorno) | ~38–45 |
| Hosting (GitHub Pages) | 0 |
| Make.com (piano gratuito) | 0 |
| Telefono (la tua SIM) | 0 |

**Cosa aspettarsi con €40 di annunci** (stima mia): CPC di €1,5–3,5 → 11–27 click → con il 10–25% di contatti → **circa 1–6 lead, valore atteso intorno a 2–3**. Basta per rispondere a una sola domanda: *un tecnico è disposto a pagare un lead?* Non basta per guadagnare. I soldi veri arrivano reinvestendo il primo incasso.

Canale gratuito in parallelo: **un annuncio su Subito.it** nella categoria Servizi ("Riparazione caldaie Bologna – tecnico in zona", con lo stesso numero).
**Da non fare:** creare una scheda Google Business Profile per il sito. Le linee guida di Google vietano le schede di lead gen senza un'attività reale a quell'indirizzo, e rischi la sospensione.

---

## 4. Piano settimana per settimana (5 ore a settimana)

### Settimana 1 (9–15 nov): messa online, ~5h
- [ ] (30') Compra il dominio, per esempio `tecnicocaldaiebologna.it` o `caldaiaguastabologna.it`. Verifica che sia libero.
- [ ] (30') In `sites/caldaie-bologna.json` sostituisci tutti i `DA_INSERIRE`: dominio, telefono, nome ed email in `operator_line`. Poi lancia `python3 build.py`.
- [ ] (45') Pubblica: crea un nuovo repo GitHub `caldaie-bologna`, copia dentro `dist/caldaie-bologna/*`, attiva Pages e configura il DNS (come già fatto per assistenzafrigorimini).
- [ ] (30') Make.com: nello scenario esistente aggiungi un router sul campo `site` e una notifica immediata a te (Telegram o email) con nome, telefono, zona e problema. Ricarica la struttura dati del webhook, perché ora arrivano anche `lead_zone`, `site` e `page_url`.
- [ ] (60') Trova su Google Maps 10 tecnici caldaie, cercando "riparazione caldaie Bologna" e "assistenza caldaie San Lazzaro / Casalecchio". Prendi solo ditte piccole (1–3 persone, <50 recensioni) e mettile nel tracker Notion.
- [ ] (90') Chiama i primi 5 con lo script 5A. **Obiettivo: 1 tecnico che dice "sì, mandameli".**

### Settimana 2: annunci accesi, ~5h
- [ ] (60') Crea l'account Google Ads seguendo la sezione 6. Accendi gli annunci **solo dopo** che almeno un tecnico ha detto sì.
- [ ] (60') Annuncio gratuito su Subito.it.
- [ ] Gestione dei lead (~10' l'uno): rispondi, prendi i dati, mandali su WhatsApp al tecnico (script 5C) e segna tutto nel tracker.
- [ ] (60') Se nessun tecnico ha detto sì, chiama gli altri 5.

### Settimane 3–4: dal lead gratis al lead a pagamento
- [ ] Dopo 1–2 lead gratuiti consegnati, chiedi al tecnico com'è andata e proponi il pagamento (script 5D).
- [ ] **Primo controllo (fine settimana 4, ~6 dic):**
  - ≥1 tecnico paga **≥€20 a lead** → **continua**. Reinvesti tutto negli annunci.
  - Lead arrivati ma nessun tecnico paga → passa a **elettrodomestici Bologna** per 3 settimane (sito già pronto), con altri €30–40.
  - Nessun lead con €40 di annunci → il problema è il traffico, non la vendita. Controlla i termini di ricerca e il CPC prima di spendere altro.

### Mese 2 (dic): da lead singoli a canone
- Quando un tecnico riceve ≥6–8 lead al mese, proponi l'esclusiva: **"€250/mese di canone + il budget annunci lo paghi tu, e la zona è solo tua"**. Così i costi degli annunci passano a lui e il canone resta a te come margine.
- Accendi il secondo sito (elettrodomestici) con un secondo tecnico, solo se il primo paga.

### Mese 3 (gen–feb): replicare
- Formula: **3 tecnici a €250–350/mese ≈ €750–1050/mese**. Lavoro di mantenimento circa 2–3 ore a settimana.
- Ad aprile riaccendi frigo Rimini per la stagione, con lo stesso template e il dominio già tuo.

**Previsione onesta:** €1000/mese entro 3 mesi richiede 3 tecnici paganti. Mi aspetto **1–2 tecnici a 3 mesi (€250–600/mese)** e €1000 tra il mese 4 e il mese 6, se il primo controllo passa.

---

## 5. Script

### 5A: Prima telefonata al tecnico (60 secondi)
> "Buongiorno, sono [Nome]. Gestisco un sito che riceve richieste di persone a Bologna con la caldaia guasta. Non vendo pubblicità né siti: ho clienti che chiamano e mi serve un tecnico serio in zona [quartiere/comune] a cui passarli. I primi due te li mando gratis, così vedi se sono clienti veri. Ti interessa?"
>
> Se dice sì: "Perfetto. Ti scrivo su WhatsApp nome, numero e problema appena arriva una richiesta. Che zone copri e in che orari?"

Non parlare del suo sito o dei suoi difetti. Non nominare subito prezzi.

### 5B: Se chiede "quanto costa?"
> "Per ora niente. Se i clienti ti piacciono, poi ci accordiamo su una cifra fissa a contatto, molto meno di quello che spenderesti in pubblicità."

### 5C: WhatsApp per passare un lead
> "Nuova richiesta 🔧 Nome: ___ · Tel: ___ · Zona: ___ · Problema: ___ · Arrivata alle ___. Puoi richiamarlo entro un'ora? Fammi sapere com'è andata 🙏"

### 5D: Conversione a pagamento (dopo 1–2 lead)
> "Com'è andata con [cliente]? … Ottimo. Dalla prossima settimana ti propongo €25 a contatto. Paghi solo i contatti veri: se è un numero sbagliato o fuori zona non lo paghi. Va bene?"

### 5E: Proposta di canone (≥6–8 lead/mese)
> "Questo mese ti ho mandato [N] clienti, cioè €[N×25]. Ti propongo una cifra fissa: €250 al mese più il budget annunci, e la zona diventa esclusiva tua: i contatti vanno solo a te."

---

## 6. Impostazione Google Ads (campagna Search)

- **Account in modalità esperto.** Niente campagne Smart né Performance Max. Disattiva la Rete Display e i partner di ricerca.
- **Località:** Bologna più un raggio di 15 km, impostazione "Presenza: persone che si trovano nelle località".
- **Orari:** lun–sab 8–20, solo quando puoi rispondere.
- **Budget:** €5/giorno, CPC massimo manuale €2,50. Alza solo se le impressioni sono quasi zero.
- **Keyword** (corrispondenza a frase o esatta):
  `"riparazione caldaia bologna"`, `"tecnico caldaia bologna"`, `"assistenza caldaie bologna"`, `"caldaia in blocco"`, `"caldaia non parte"`, `"caldaia non fa acqua calda"`, `"caldaia perde pressione"`, `[caldaista bologna]`
- **Keyword negative:** lavoro, offerte, corso, manuale, pdf, come, fai da te, video, youtube, reset, nuova, prezzo caldaia, installazione, sostituzione, bonus, incentivi, usata, vendita, ricambi, amazon, plus i nomi dei marchi seguiti da "assistenza autorizzata".
- **Annuncio responsive (RSA):**
  - Titoli: *Caldaia Guasta a Bologna?* · *Tecnico Caldaie in Zona* · *Preventivo Senza Impegno* · *Chiama Ora* · *Servizio di Contatto Gratuito* · *Caldaia in Blocco?* · *Niente Acqua Calda?*
  - Descrizioni: *Ti mettiamo in contatto con un tecnico caldaie indipendente della tua zona. Preventivo prima dell'intervento.* · *Bologna e provincia. Chiamaci o lascia il numero: un tecnico ti richiama.*
  - Non scrivere "centro autorizzato", "H24" o "in 60 minuti" se non è vero. È il motivo più comune per cui Google rifiuta annunci di lead gen (norma "Misrepresentation").
- **Asset di chiamata:** il tuo numero, lo stesso pubblicato sul sito.
- **Conversioni:** (1) chiamate dagli annunci di durata ≥ 30 secondi; (2) pagina `grazie.html`. Inserisci l'ID `AW-…` e le etichette in `gads_id`, `gads_call_label` e `gads_form_label` nel JSON, poi rigenera il sito. Il banner cookie e Consent Mode si attivano da soli.
- **Il 3° giorno:** apri "Termini di ricerca" e aggiungi come negative tutto ciò che non è un guasto.

---

## 7. Aspetti legali e fiscali (da verificare, non sono un consulente)

- **Trasparenza:** il sito dice esplicitamente che è un servizio di intermediazione e che il tecnico fattura direttamente al cliente. Serve per il Codice del Consumo (pratiche ingannevoli) e per le norme di Google Ads.
- **Privacy:** ci sono la privacy policy e la casella di consenso. Completa nome ed email del titolare in `operator_line`.
- **Fisco:** i primi incassi sporadici si possono gestire come prestazione occasionale. Un canone mensile ricorrente è un'attività abituale e probabilmente richiede la **P.IVA in forfettario**. Chiedi a un CAF o a un commercialista **prima** di firmare il primo canone.

---

## 8. Cosa è stato fatto in questa sessione

- Rifatto il sito come **template unico + config JSON + `build.py`**, così ogni nuova nicchia o città si crea in 15 minuti.
- Generati 3 siti: `dist/caldaie-bologna`, `dist/elettrodomestici-bologna`, `dist/frigo-rimini`. Quest'ultimo è copiato anche nella root del repo, che è il dominio attuale.
- Miglioramenti rispetto al vecchio sito: copy trasparente da intermediario, barra "Chiama ora" fissa su mobile, pagina `grazie.html` per misurare le conversioni, privacy e consenso, honeypot anti-spam, campi `zona` e `site` nel webhook, tracciamento delle chiamate con Google Ads e Consent Mode. Nessuna recensione finta, nessun indirizzo inventato, nessuna promessa di tempi di intervento.
- Testato con Playwright (iPhone 13): nessuno scroll orizzontale, invio del form → webhook → redirect a `grazie.html`, nessun errore JS.

**Non fatto, perché richiede te o soldi:** acquisto del dominio, numero di telefono, account Google Ads, chiamate ai tecnici, pubblicazione su main.

---

## Fonti
- Accensione riscaldamenti 2026–27, rinvio al 1° novembre nell'agglomerato di Bologna: [QuiFinanza](https://quifinanza.it/info-utili/rinvio-riscaldamenti-accensione-2026/1019053/), [Open](https://www.open.online/2026/10/05/riscaldamento-quando-si-possono-accendere-termosifoni-mappa/)
- Prezzi delle riparazioni caldaie: [Money.it](https://www.money.it/quanto-costa-revisionare-la-caldaia-prezzi-medi-e-spese-di-manutenzione), [BusinessOnline](https://www.businessonline.it/articoli/costo-manutenzione-caldaia-prezzo-medio-richiesto-.html)
- Prezzi delle riparazioni elettrodomestici: [listino Vestel](https://vestelinternational.com/Content/files/uploads/4070/Diritto%20alla%20Riparazione.pdf), [Cronoshare](https://www.cronoshare.it/servizi/riparazione-lavatrice)
- CPC Google Ads in Italia 2026 (stime di terzi): [AddLab](https://www.addlab.it/quanto-costa-una-campagna-google-ads-in-italia-nel-2026/), [WebMarketingAziendale](https://www.webmarketingaziendale.it/google-ads-costi-budget-e-prezzi/), [Stefano Diversi, spurghi](https://www.stefanodiversi.it/google-ads-spurghi-autospurgo/)
- Dismissione degli annunci di chiamata: [Google Ads Help](https://support.google.com/google-ads/answer/6341403?hl=it)
- Policy sui numeri di telefono: [Google Ads Help](https://support.google.com/google-ads/answer/6099637), [CallRail](https://www.callrail.com/blog/google-unacceptable-phone-number-policy)
- Policy Google sui servizi locali: [Advertising Policies Help](https://support.google.com/adspolicy/answer/13527633?hl=en)
- Elenchi di tecnici caldaie a Bologna (da verificare): [Cylex](https://www.cylex-italia.it/bologna/assistenza%20caldaie.html), [Deltagas](https://www.reteimprese.it/98848), [GAS WEB](https://www.reteimprese.it/114036)
