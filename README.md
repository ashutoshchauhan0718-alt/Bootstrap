# KALAGNI Integrated Projects – Website (UI)

Static, multi-page website for **KALAGNI Integrated Projects Private Limited** (Hyderabad EPC company),
built with **Bootstrap 5.3.9**. Content comes from the company profile PDF (`assets/docs/kalagni-profile.pdf`).

Plain HTML + CSS + a little JavaScript. No build step, no npm, no internet needed (except the Google Map
on the Contact page). Bootstrap, Bootstrap Icons and the fonts are stored locally.

## Run it

Any static server works, for example from the project folder:

```bash
python -m http.server 5500
```

Then open <http://127.0.0.1:5500/index.html>. (VS Code "Live Server" works too.)

## Project structure

```
index.html              Home
pages/                  services, clients, about, contact
css/style.css           ALL custom styles (brand colors as --kg-* variables at the top)
js/main.js              Hover menus, image loader, enquiry form, carousel pause, back-to-top
assets/images/          Logo, favicon, photos (see "Images" below)
assets/fonts/           Montserrat (headings) + Poppins (body), woff2
assets/docs/            Company profile PDF (the "Company Profile" download button)
vendor/                 Bootstrap 5.3.9 + Bootstrap Icons 1.13.2 (do not edit)
tools/gen_site.py       Generates the 5 HTML pages (see below)
_reference/             Planning notes: build plan, design audit of the reference site (not part of the site)
```

## ⚠️ How the pages are built: read before editing HTML

The 5 HTML pages are **generated** by `tools/gen_site.py`. It holds all page content (services,
leadership, clients, etc.) and the shared parts (header, mega menu, footer, enquiry popup), so a change
to the menu or footer happens in one place instead of five.

```bash
python tools/gen_site.py          # rewrites index.html and pages/*.html
```

- **Text / content / header / footer / popup changes**: edit `tools/gen_site.py`, then run it.
- **Styling**: edit `css/style.css` directly (not generated).
- **Behaviour**: edit `js/main.js` directly (not generated).
- If you edit an HTML file by hand, a later run of the generator **overwrites** it. Either stick to the
  generator, or stop using it and edit the HTML files directly from then on.

## Design tokens

Colors were measured from the PDF and live at the top of `css/style.css`:

| Variable | Value | Use |
|---|---|---|
| `--kg-navy-900` | `#011C3A` | Main navy: bands, footer, card headers |
| `--kg-navy-800` → `--kg-navy-700` | `#012B55` → `#013666` | Navbar gradient |
| `--kg-gold-500` | `#EBA40B` | Accent: logo flame, icons, buttons, lines |
| `--kg-gold-600` | `#D19506` | Gold words in big headings on white (large text only) |
| `--kg-text` | `#2E3452` | Body text |

Custom buttons: `.btn-gold`, `.btn-outline-gold` (on navy), `.btn-outline-navy` (on white).
Breakpoint for the full menu: `navbar-expand-xl` (≥ 1200px); below that the menu is an offcanvas.

## Images

Photos are not in the repo yet. Each image area is a placeholder like:

```html
<div class="media media-4x3" data-img="assets/images/service-hvac.jpg">…</div>
```

`js/main.js` checks whether the file exists; if it does, it becomes the background automatically.
So: **save a photo under the expected name in `assets/images/` and it appears. No code change.**
The placeholder shows the expected file name. Full list with sizes: `_reference/BUILD-PLAN.md`, section 8.

## Open items before going live

- **Enquiry forms are UI only.** Validation and the thank-you message work; nothing is sent yet.
  Connect a backend / form service at the `TODO (backend)` line in `js/main.js`.
- **Content to confirm with the client** (search the HTML for `CONFIRM`):
  - Name spelling: "Vinod Duram" vs "Dr. Vinod Durgam"; "Busikem Indian Construction" vs "BrickCem Construction".
  - Organization names on Home/Clients come from the profile's "associated with the leadership team" slide,
    which says references must be confirmed before publication. Shown as text, no logos.
  - PAN number: card is prepared but commented out on the Contact page.
- Replace `assets/docs/kalagni-profile.pdf` with the final approved profile.
- Original logo as SVG (current `logo-white.png` is a background-removed export).
- Website address is "to be updated" in the profile.

## Delivering as a zip

Zip everything **except** `_reference/`, `tools/`, `README.md` and `.git/`.
