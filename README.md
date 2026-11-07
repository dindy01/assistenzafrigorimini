# Lead Gen sites

Siti one-page per la lead generation locale, generati da un template unico.

- `template/`: `index.html`, `grazie.html` e `privacy.html` con placeholder `{{...}}`
- `sites/*.json`: un file per ogni nicchia o città (testi, telefono, webhook, Google Ads)
- `build.py`: genera `dist/<slug>/`. Il config con `"root": true` viene scritto anche nella root del repo (il sito servito da questo repo con il CNAME `assistenzafrigorimini.it`).

```bash
python3 build.py                  # tutti i siti
python3 build.py caldaie-bologna  # uno solo
```

Il build segnala i valori `DA_INSERIRE` ancora da completare.
Piano operativo e ricerca di mercato: vedi [PIANO.md](PIANO.md).
