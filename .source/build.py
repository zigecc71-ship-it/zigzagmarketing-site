"""Builds the ZigZag Marketing site into ../dist from shared partials + page fragments."""
import os, shutil, html, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "..", "dist")
BASE = "https://zigzagmarketing.net"
PHONE = "+386 41 306 629"
PHONE_TEL = "+38641306629"
EMAIL = "info@zigzagmarketing.net"


def ver(rel):
    """Short content hash so browsers re-download an asset whenever it changes."""
    with open(os.path.join(HERE, "assets", rel), "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:8]

URLS = {
    "hub":   {"sl": "/",                "en": "/en/"},
    "meta":  {"sl": "/meta-oglasi/",    "en": "/en/meta-ads/"},
    "web":   {"sl": "/spletne-strani/", "en": "/en/web-design/"},
    "ghost": {"sl": "/ghostwriting/",   "en": "/en/ghostwriting/"},
}

T = {
    "sl": {
        "nav": [("meta", "Meta oglasi"), ("web", "Spletne strani"), ("ghost", "Ghostwriting")],
        "lang_label": "Jezik", "cta": "Pogovorimo se →", "contact_id": "posvet",
        "services": "STORITVE", "company": "PODJETJE", "home": "Domov", "contact": "Kontakt", "call": "POKLIČITE", "write": "PIŠITE",
        "tagline": "Meta oglasi, spletne strani in besedila za znamke, ki želijo rasti.",
        "rights": "© 2026 ZigZag Marketing. Vse pravice pridržane.",
        "meta_tm": "Meta, Facebook in Instagram so blagovne znamke družbe Meta Platforms, Inc.",
        "form": {
            "title": "Pustite kontakt", "sub": "Odgovorimo v 1 delovnem dnevu.",
            "name": "Ime in priimek", "name_ph": "Janez Novak",
            "email": "E-pošta", "email_ph": "janez@znamka.si",
            "phone": "Telefon", "optional": "(neobvezno)", "phone_ph": "+386 40 123 456",
            "company": "Podjetje ali spletna stran", "company_ph": "www.vasaznamka.si",
            "service": "Kaj vas zanima?", "choose": "Izberite …",
            "svc": [("meta", "Meta oglasi"), ("web", "Spletna stran"), ("ghost", "Ghostwriting / besedila"), ("other", "Še ne vem, svetujte mi")],
            "budget": "Mesečni proračun za Meta oglase",
            "budget_opts": ["Še ne oglašujemo", "Do 2.000 €", "2.000–10.000 €", "10.000–50.000 €", "Nad 50.000 €"],
            "msg": "Kaj potrebujete?", "msg_ph": "Na kratko opišite, kaj bi radi dosegli …",
            "consent": "Strinjam se, da me ZigZag Marketing kontaktira glede mojega povpraševanja. Podatkov ne delimo s tretjimi osebami.",
            "send": "Pošlji povpraševanje →",
            "ok_h": "Hvala, prejeli smo vaše podatke!", "ok_p": "Oglasimo se vam v 1 delovnem dnevu.",
            "m_required": "Prosimo, izpolnite vsa obvezna polja in potrdite soglasje.",
            "m_sending": "Pošiljam …",
            "m_failed": "Pošiljanje ni uspelo. Poskusite znova ali nam pišite na info@zigzagmarketing.net.",
        },
    },
    "en": {
        "nav": [("meta", "Meta ads"), ("web", "Web design"), ("ghost", "Ghostwriting")],
        "lang_label": "Language", "cta": "Let's talk →", "contact_id": "contact",
        "services": "SERVICES", "company": "COMPANY", "home": "Home", "contact": "Contact", "call": "CALL", "write": "EMAIL",
        "tagline": "Meta ads, websites and writing for brands ready to grow.",
        "rights": "© 2026 ZigZag Marketing. All rights reserved.",
        "meta_tm": "Meta, Facebook and Instagram are trademarks of Meta Platforms, Inc.",
        "form": {
            "title": "Get in touch", "sub": "We reply within 1 business day.",
            "name": "Full name", "name_ph": "Jane Smith",
            "email": "Email", "email_ph": "jane@brand.com",
            "phone": "Phone", "optional": "(optional)", "phone_ph": "+44 7700 900123",
            "company": "Company or website", "company_ph": "www.yourbrand.com",
            "service": "What are you interested in?", "choose": "Select …",
            "svc": [("meta", "Meta ads"), ("web", "A website"), ("ghost", "Ghostwriting / copy"), ("other", "Not sure yet, advise me")],
            "budget": "Monthly Meta ads budget",
            "budget_opts": ["Not advertising yet", "Up to €2,000", "€2,000–10,000", "€10,000–50,000", "Over €50,000"],
            "msg": "What do you need?", "msg_ph": "Briefly describe what you'd like to achieve …",
            "consent": "I agree that ZigZag Marketing may contact me about my enquiry. We never share your details with third parties.",
            "send": "Send enquiry →",
            "ok_h": "Thanks, we've got your details!", "ok_p": "We'll get back to you within 1 business day.",
            "m_required": "Please fill in all required fields and tick the consent box.",
            "m_sending": "Sending …",
            "m_failed": "Sending failed. Please try again or email us at info@zigzagmarketing.net.",
        },
    },
}


def head(p):
    alts = URLS[p["key"]]
    return f"""<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<link rel="canonical" href="{BASE}{alts[p['lang']]}">
<link rel="alternate" hreflang="sl" href="{BASE}{alts['sl']}">
<link rel="alternate" hreflang="en" href="{BASE}{alts['en']}">
<link rel="alternate" hreflang="x-default" href="{BASE}{alts['sl']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/zigzag.css?v={ver('zigzag.css')}">
</head>
<body>
"""


def nav(p):
    t, lang, key = T[p["lang"]], p["lang"], p["key"]
    out = ""
    if p.get("topbar"):
        text, href, label = p["topbar"]
        out += f'<div class="topbar"><span>{text}</span><a href="{href}">{label}</a></div>\n\n'
    links = "".join(
        f'<a href="{URLS[k][lang]}"{" class=\"on\" aria-current=\"page\"" if k == key else ""}>{label}</a>'
        for k, label in t["nav"]
    )
    sl_on = ' class="on"' if lang == "sl" else ""
    en_on = ' class="on"' if lang == "en" else ""
    out += f"""<nav><div class="wrap">
  <a href="{URLS['hub'][lang]}" class="logo">ZIGZAG<span>/</span>MARKETING</a>
  <div class="links">{links}</div>
  <div class="nav-r"><div class="lang" aria-label="{t['lang_label']}"><a href="{URLS[key]['sl']}"{sl_on} hreflang="sl" lang="sl">SL</a><a href="{URLS[key]['en']}"{en_on} hreflang="en" lang="en">EN</a></div><a href="#{t['contact_id']}" class="btn-sm">{t['cta']}</a></div>
</div></nav>
"""
    return out


def contact(p):
    t = T[p["lang"]]
    f = t["form"]
    c = p["contact"]
    bullets = "\n".join(f'      <li><span class="tick">✓</span><span>{b}</span></li>' for b in c["bullets"])
    opts = "\n".join(
        f'        <option value="{v}"{" selected" if v == p["service"] else ""}>{label}</option>'
        for v, label in f["svc"]
    )
    placeholder_sel = "" if p["service"] else " selected"
    budget = ""
    if p["key"] == "meta":
        bopts = "\n".join(f"        <option>{o}</option>" for o in f["budget_opts"])
        budget = f"""      <label for="f-budget">{f['budget']} <small>{f['optional']}</small></label>
      <select id="f-budget" name="proracun">
        <option value="" selected>{f['choose']}</option>
{bopts}
      </select>
"""
    return f"""
<!-- CONTACT -->
<section class="dark final" id="{t['contact_id']}"><div class="wrap contact">
  <div class="contact-text">
    <div class="eyebrow">{c['eyebrow']}</div>
    <h2>{c['h2']}</h2>
    <p>{c['p']}</p>
    <ul>
{bullets}
    </ul>
    <div class="direct"><a href="tel:{PHONE_TEL}"><small>{t['call']}</small><b>{PHONE}</b></a><a href="mailto:{EMAIL}"><small>{t['write']}</small><b>{EMAIL}</b></a></div>
  </div>

  <div class="form-card">
    <form id="contact-form" action="/contact.php" method="post" novalidate data-msg-required="{html.escape(f['m_required'])}" data-msg-sending="{html.escape(f['m_sending'])}" data-msg-failed="{html.escape(f['m_failed'])}">
      <h3>{f['title']}</h3>
      <p class="fsub">{f['sub']}</p>
      <div class="frow">
        <div><label for="f-ime">{f['name']}</label><input id="f-ime" name="ime" required autocomplete="name" placeholder="{f['name_ph']}"></div>
        <div><label for="f-email">{f['email']}</label><input id="f-email" name="email" type="email" required autocomplete="email" placeholder="{f['email_ph']}"></div>
      </div>
      <div class="frow">
        <div><label for="f-tel">{f['phone']} <small>{f['optional']}</small></label><input id="f-tel" name="telefon" type="tel" autocomplete="tel" placeholder="{f['phone_ph']}"></div>
        <div><label for="f-web">{f['company']}</label><input id="f-web" name="podjetje" required placeholder="{f['company_ph']}"></div>
      </div>
      <label for="f-svc">{f['service']}</label>
      <select id="f-svc" name="storitev" required>
        <option value="" disabled{placeholder_sel}>{f['choose']}</option>
{opts}
      </select>
{budget}      <label for="f-msg">{f['msg']} <small>{f['optional']}</small></label>
      <textarea id="f-msg" name="sporocilo" rows="3" placeholder="{p.get('msg_ph', f['msg_ph'])}"></textarea>
      <input type="hidden" name="jezik" value="{p['lang'].upper()}">
      <input type="hidden" name="stran" value="{URLS[p['key']][p['lang']]}">
      <input type="text" name="website_hp" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label class="consent"><input type="checkbox" name="soglasje" required> <span>{f['consent']}</span></label>
      <p class="ferr" id="f-err" role="alert"></p>
      <button class="btn" type="submit" id="f-btn">{f['send']}</button>
    </form>
    <div class="fok" id="f-ok" hidden>
      <div class="okicon">✓</div>
      <h3>{f['ok_h']}</h3>
      <p class="fsub">{f['ok_p']}</p>
    </div>
  </div>
</div></section>
"""


def footer(p):
    t, lang = T[p["lang"]], p["lang"]
    svc = "".join(f'<a href="{URLS[k][lang]}">{label}</a>' for k, label in t["nav"])
    tm = f'<span>{t["meta_tm"]}</span>'
    return f"""
<footer><div class="wrap">
  <div class="foot">
    <div><a href="{URLS['hub'][lang]}" class="logo">ZIGZAG<span>/</span>MARKETING</a><p>{t['tagline']}</p></div>
    <div><h5>{t['services']}</h5>{svc}</div>
    <div><h5>{t['company']}</h5><a href="{URLS['hub'][lang]}">{t['home']}</a><a href="#{t['contact_id']}">{t['contact']}</a><a href="mailto:info@zigzagmarketing.net">info@zigzagmarketing.net</a></div>
  </div>
  <div class="legal"><span>{t['rights']}</span>{tm}</div>
</div></footer>

<script src="/assets/form.js?v={ver('form.js')}" defer></script>
</body>
</html>
"""


def build(pages):
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(DIST, "assets"))
    shutil.copy(os.path.join(HERE, "contact.php"), os.path.join(DIST, "contact.php"))
    for p in pages:
        with open(os.path.join(HERE, "pages", p["frag"]), encoding="utf-8") as fh:
            body = fh.read()
        doc = head(p) + "\n" + nav(p) + "\n" + body.strip() + "\n" + contact(p) + footer(p)
        rel = URLS[p["key"]][p["lang"]].strip("/")
        out_dir = os.path.join(DIST, rel)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(doc)
        print("built", "/" + rel + ("/" if rel else ""), len(doc), "bytes")


if __name__ == "__main__":
    from pages_config import PAGES
    build(PAGES)
