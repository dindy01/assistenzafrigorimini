#!/usr/bin/env python3
"""Genera i siti lead-gen dai config in sites/*.json usando i template in template/.

Uso:
    python3 build.py              # genera tutti i siti in dist/<slug>/
    python3 build.py caldaie-bologna

Un config con "root": true viene scritto anche nella root del repo
(è il sito servito da GitHub Pages con il CNAME di questo repo).
"""
import html
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATES = ["index.html", "grazie.html", "privacy.html"]
REQUIRED = ["slug", "domain", "site_name", "color", "meta_title", "meta_description",
            "badge", "h1", "subtitle", "phone_display", "phone_tel", "hours", "webhook",
            "issues", "zones", "brands", "faq", "operator_line"]
PLACEHOLDER_MARK = "DA_INSERIRE"

e = html.escape


def gads_snippets(cfg):
    gid = cfg.get("gads_id", "")
    if not gid or PLACEHOLDER_MARK in gid:
        return "", "", ""
    head = f"""<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied'}});
try{{if(localStorage.getItem('cc')==='1')gtag('consent','update',{{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'denied',analytics_storage:'granted'}});}}catch(_){{}}
gtag('js',new Date());gtag('config','{e(gid)}');
document.addEventListener('DOMContentLoaded',function(){{var s;try{{s=localStorage.getItem('cc');}}catch(_){{}}if(s)return;
var b=document.createElement('div');b.style.cssText='position:fixed;left:8px;right:8px;bottom:84px;background:#1a202c;color:#fff;padding:12px;border-radius:8px;font-size:13px;z-index:9;max-width:520px;margin:0 auto';
b.innerHTML='Usiamo cookie di Google Ads solo per misurare le richieste generate dagli annunci. <a href="privacy.html" style="color:#fff">Info</a><div style="margin-top:8px;display:flex;gap:8px"><button id="ccy" style="padding:8px">Accetta</button><button id="ccn" style="padding:8px;background:#4a5568">Rifiuta</button></div>';
document.body.appendChild(b);
function set(v){{try{{localStorage.setItem('cc',v);}}catch(_){{}}if(v==='1')gtag('consent','update',{{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'denied',analytics_storage:'granted'}});b.remove();}}
document.getElementById('ccy').onclick=function(){{set('1')}};document.getElementById('ccn').onclick=function(){{set('0')}};}});
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={e(gid)}"></script>"""
    call_label = cfg.get("gads_call_label", "")
    form_label = cfg.get("gads_form_label", "")
    call_conv = (f"track('conversion', {{send_to: '{e(gid)}/{e(call_label)}'}});"
                 if call_label and PLACEHOLDER_MARK not in call_label else "")
    form_conv = (f"<script>gtag('event','conversion',{{send_to:'{e(gid)}/{e(form_label)}'}});</script>"
                 if form_label and PLACEHOLDER_MARK not in form_label else "")
    return head, call_conv, form_conv


def render(cfg):
    missing = [k for k in REQUIRED if k not in cfg]
    if missing:
        sys.exit(f"[{cfg.get('slug', '?')}] campi mancanti: {missing}")

    gads_head, gads_call, gads_form = gads_snippets(cfg)
    issues = cfg["issues"]
    warning = cfg.get("warning", "")
    values = {
        **{k: e(str(v)) for k, v in cfg.items() if isinstance(v, (str, int, float))},
        "issues_title": e(cfg.get("issues_title", "Problemi che gestiamo")),
        "brands_title": e(cfg.get("brands_title", "Marchi trattati")),
        "name_placeholder": e(cfg.get("name_placeholder", "Es. Mario Rossi")),
        "zone_example": e(cfg["zones"][0]),
        "issue_options": "\n          ".join(
            f'<option value="{e(i["label"])}">{e(i["label"])}</option>' for i in issues),
        "issue_list": "\n      ".join(
            f'<li><strong>{e(i["label"])}</strong>: {e(i["desc"])}</li>' for i in issues),
        "warning": f'<p class="warn">{e(warning)}</p>' if warning else "",
        "zones": "".join(f"<span>{e(z)}</span>" for z in cfg["zones"]),
        "brands": "".join(f"<span>{e(b)}</span>" for b in cfg["brands"]),
        "faq": "\n    ".join(
            f"<details><summary>{e(f['q'])}</summary><p>{e(f['a'])}</p></details>" for f in cfg["faq"]),
        "webhook_json": json.dumps(cfg["webhook"]),
        "slug_json": json.dumps(cfg["slug"]),
        "gads_head": gads_head,
        "gads_call_conv": gads_call,
        "gads_form_conv": gads_form,
    }

    out = {}
    for name in TEMPLATES:
        text = (ROOT / "template" / name).read_text(encoding="utf-8")
        for k, v in values.items():
            text = text.replace("{{" + k + "}}", v)
        leftover = [seg.split("}}")[0] for seg in text.split("{{")[1:]]
        if leftover:
            sys.exit(f"[{cfg['slug']}] placeholder non risolti in {name}: {leftover}")
        out[name] = text
    return out


def main():
    only = set(sys.argv[1:])
    configs = sorted((ROOT / "sites").glob("*.json"))
    warnings = []
    for path in configs:
        cfg = json.loads(path.read_text(encoding="utf-8"))
        if only and cfg["slug"] not in only:
            continue
        pages = render(cfg)
        dest = ROOT / "dist" / cfg["slug"]
        if dest.exists():
            shutil.rmtree(dest)
        dest.mkdir(parents=True)
        for name, text in pages.items():
            (dest / name).write_text(text, encoding="utf-8")
        (dest / "CNAME").write_text(cfg["domain"] + "\n", encoding="utf-8")
        if cfg.get("root"):
            for name, text in pages.items():
                (ROOT / name).write_text(text, encoding="utf-8")
        todo = sorted({k for k, v in cfg.items() if isinstance(v, str) and PLACEHOLDER_MARK in v})
        if todo:
            warnings.append(f"  {cfg['slug']}: da completare -> {', '.join(todo)}")
        print(f"OK  {cfg['slug']:<26} -> dist/{cfg['slug']}/" + ("  (+ root)" if cfg.get("root") else ""))
    if warnings:
        print("\nATTENZIONE, valori segnaposto ancora presenti:")
        print("\n".join(warnings))


if __name__ == "__main__":
    main()
