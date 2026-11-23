# KALAGNI website: build plan

Sources:
- **Content**: "KALAGNI profile 01.pdf" (15-page company profile; page numbers inside the slides are out of order).
- **Layout and behaviour**: reference audit of the labotemp.com homepage (see FILTERED-NOTES.md).

Rule: the **document decides WHAT** we show; the **reference decides HOW** it is laid out.
We never copy the reference's logo, images, text or colors.

---

## 1. What the document contains (sorted into a logical order)

| # | Topic | Slide title in the PDF | Used on |
|---|---|---|---|
| 1 | Cover: "Integrated EPC Solutions", "From concept to commissioning" | Company Profile | Home hero |
| 2 | Who we are, 5 highlights, 4 strengths, 6 values | 02 Who We Are | Home intro, About |
| 3 | Leadership team (5 people) | 03 Leadership Team | About |
| 4 | Electrical Power Infrastructure: 6 capabilities | 04 | Service page |
| 5 | Electrical: delivery workflow (8 steps), approach (4), statutory approvals | 05 | Service page + Home workflow |
| 6 | Solar & BESS: 6 capabilities, regulatory support, standards | 06 | Service page |
| 7 | Infrastructure & Construction: 5 capabilities, approach | 07 | Service page |
| 8 | MEPF Engineering: 5 capabilities, approach | 08 | Service page |
| 9 | HVAC Systems: 6 capabilities, sectors served | 09 | Service page |
| 10 | Railway & Metro Infrastructure: 5 capabilities | "08" (duplicate number) | Service page |
| 11 | Engineering & Digital Solutions: 6 capabilities | 10 | Service page |
| 12 | Approvals & Project Delivery: 6 capabilities | 11 | Service page |
| 13 | Operations & Maintenance: 6 services | 12 | Service page |
| 14 | Clientele & project experience (organizations + government bodies) | 13 | Clients page |
| 15 | Contact, location map, legal (CIN, GSTIN), certifications (ISO 9001/14001/45001, MSME) | 14 | Contact page, footer |

**9 services in total.** Every service slide follows the same template:
title + tagline → intro text → hero image → numbered capability cards (image + bullets) →
approach → "Our value proposition" strip. → **One HTML template, reused 9 times.**

---

## 2. Brand (colors MEASURED from the PDF by pixel sampling, 23 Nov 2026)

Defined as CSS variables in `css/style.css` (`:root`, prefix `--kg-`).

| Variable | Value | Where it appears in the PDF |
|---|---|---|
| `--kg-navy-950` | `#021734` | Heading text: "WHO", "ELECTRICAL POWER", "LEADERSHIP" |
| `--kg-navy-900` | `#011C3A` | Dark bands, footer strip, cover panel, card headers, icon circles |
| `--kg-navy-800` → `--kg-navy-700` | `#012B55` → `#013666` | Top header bar (left-to-right gradient) |
| `--kg-navy-600` | `#03458D` | Brighter navy highlights (links) |
| `--kg-gold-500` | `#EBA40B` | Logo flame, gold text on navy, card numbers "01", icons, thin lines |
| `--kg-gold-600` | `#D19506` | Gold heading words on white: "WE ARE", "INFRASTRUCTURE", "VALUES" |
| `--kg-gold-300` | `#FCC04C` | Light gold highlight |
| `--kg-text-strong` | `#212649` | Card titles ("SAFETY FIRST") |
| `--kg-text` | `#2E3452` | Body paragraphs, letter-spaced taglines (dark slate-navy) |
| `--kg-text-muted` | `#62677A` | Bullet lists in capability cards |
| `--kg-bg` / `--kg-bg-soft` / `--kg-card` | `#FFFFFF` / `#F7FBFE` / `#FBFBFB` | Page / light sections / light cards |

Overall look: about 1/3 of each slide is deep navy (header bar, bands, footer strip),
the rest white or near-white, with gold used sparingly for accents, lines, icons and
the second word of every big heading.

Contrast check:
- Gold `#EBA40B` on navy `#011C3A`: about 8:1. Excellent; use freely.
- Gold `#D19506` on white: about 2.6:1. Matches the PDF, but only use it for big display
  headings (like the PDF does), never for small or body text.
- Body text `#2E3452` on white: about 12:1. Good.

- **Headings**: very bold geometric sans in the slides (two-tone: navy word + gold word,
  e.g. "WHO **WE ARE**"). → **Montserrat 800**.
- **Body**: clean sans → **Poppins 400/500/600** (same as the reference).
- **Taglines**: uppercase, wide letter-spacing (e.g. "INTEGRATED SOLUTIONS | RELIABLE EXECUTION").
- **Shapes**: diagonal gold "slash" lines between images, gold left border on intro text,
  numbered cards ("01", "02") with a navy header, round gold-outlined icon badges.
- **Icons**: Bootstrap Icons only (one library, stored locally).
- **Fonts**: downloaded into `assets/fonts/` so the zip works offline.

Accessibility note: bright gold on white is too low-contrast for normal text. Use gold on navy
(high contrast), or the darker gold for large headings on white.

---

## 3. Site map

```
index.html            Home
pages/about.html      About: who we are, values, leadership, strengths, certifications
pages/services.html   ONE long page: overview cards at the top, then all 9 services as sections
pages/clients.html    Clientele & project experience
pages/contact.html    Contact details, map, enquiry form, legal info
```
(No login page: the document has no login feature. Decided 22 Nov 2026.)

**Services page anchors** (the mega menu links jump to these):
`#electrical`, `#solar-bess`, `#infrastructure`, `#mepf`, `#hvac`, `#railway-metro`,
`#digital`, `#approvals`, `#om`
e.g. from the home page: `pages/services.html#hvac`; from another page in `pages/`: `services.html#hvac`.

Each service section uses the same block layout (see "Service template" below), with
alternating light/white backgrounds so the long page stays readable, and a small
"Back to all services" link.

---

## 4. Header & navigation (reference pattern, KALAGNI content)

| Reference element | KALAGNI version |
|---|---|
| Announcement bar (gradient, 3 trust claims) | Navy bar, white/gold text: "ISO 9001 · 14001 · 45001 Certified • From Concept to Commissioning • Hyderabad, India" |
| Logo + nav row (orange line below) | **Navy** bar (like the PDF header bars, because the official logo has white text), logo left, nav centre, buttons right, **gold** line below. Sticky. |
| Mega menus (product images) | **Services** mega menu, 3 columns with icons (below) |
| Catalog pill | "Company Profile" pill (downloads the PDF) |
| Search bar | Left out (decided: no product catalog) |
| Language pill | Left out (decided) |
| Request Quote (opens modal) | "Get a Quote" button (opens enquiry modal) |

**Nav items**: Home · About ▾ (Who We Are, Leadership, Values) · Services ▾ (mega) · Clients · Contact · [Get a Quote]

**Services mega menu (grouped, improves on the reference's single row):**
| Power & Energy | Buildings & Infrastructure | Engineering & Support |
|---|---|---|
| Electrical Power Infrastructure | Infrastructure & Construction | Engineering & Digital Solutions |
| Solar & BESS | MEPF Engineering | Approvals & Project Delivery |
| | HVAC Systems | Operations & Maintenance |
| | Railway & Metro | |

Behaviour: `navbar-expand-xl`; hover + click + keyboard; chevron on dropdown items;
active page highlighted; mobile = offcanvas-start + accordion sub-menus, white hamburger.

---

## 5. Home page sections (top to bottom)

| # | Section | Content from PDF | Reference pattern | Bootstrap |
|---|---|---|---|---|
| 1 | Hero carousel | 4 slides: Integrated EPC Solutions / Power Infrastructure / Solar & BESS / Infrastructure & Construction; tagline + "Explore Services" + "Get a Quote" | Fading banner (but with real HTML text, shown on mobile) | Carousel `carousel-fade` |
| 2 | Who we are (short) | Intro paragraph + 5 highlights (Integrated EPC, Quality & Safety, Experienced Leadership, Client-Focused, Sustainable Growth) | H1 + intro block | `row` 2 cols: text / icon list |
| 3 | Strengths band | 4 items: Multi-disciplinary Expertise, End-to-End Delivery, Client-Centric, Sustainability | — (from PDF navy strip) | Navy band, `row-cols-2 row-cols-lg-4` |
| 4 | Our services | 9 service cards: title, 3 bullets, image, "Learn more" | Category showcase cards (text left, image right, image zoom on hover) | `row-cols-1 row-cols-md-2 row-cols-xl-3` + `card` |
| 5 | Sectors we serve | Power, Renewable, Buildings, MEPF & HVAC, Railway & Metro, Digital, O&M | "Fast selling" round icon strip | `d-flex flex-wrap justify-content-center` + round badges |
| 6 | How we deliver | 8-step workflow: Concept Design → … → AMC & Lifecycle Support | — (from PDF arrow steps) | `row-cols-2 row-cols-md-4 row-cols-xl-8` numbered steps |
| 7 | Our values | 6 values: Safety First, Quality Driven, Integrity, Innovation, Sustainability, Client Success | "Why choose us" cards with colored left border (gold) + lift on hover | `row-cols-1 row-cols-md-2 row-cols-lg-3` |
| 8 | Experience | Organization names by sector (text or placeholder logos until approved) | Logo strip | Grid / scrolling strip |
| 9 | Certifications | ISO 9001:2015, ISO 14001:2015, ISO 45001:2018, MSME | — | small icon row |
| 10 | CTA band | "Let's build a stronger tomorrow together" + Get a Quote | — | Navy band with gold button |
| 11 | Footer | 4 cols: brand+about+social / quick links / services / contact; marquee tagline; bottom bar with © + CIN + GSTIN | Reference footer (slanted panel → navy diagonal) | `row-cols-1 row-cols-md-2 row-cols-xl-4` |
| + | Floating buttons | WhatsApp + Call / Enquiry | Reference floating buttons | fixed position |
| + | Enquiry modal | Name, Email, Phone, Company, Service (select of 9), Message | Reference quote modal | Modal + `row g-3` form |

---

## 6. Other pages

- **About**: page banner → who we are (full text) → 5 highlights → strengths band → values (6) →
  **leadership** (5 cards: icon, name, role, "leader" tag, education / experience / at KALAGNI;
  3 + 2 layout like the PDF) → certifications → CTA.
- **Services (one page)**: banner → 9 overview cards linking to the sections below →
  9 service sections → workflow (8 steps) → CTA.
- **Service section template** (used 9 times on services.html): title + tagline → intro with
  gold left border + image → numbered capability cards (navy header with "01" + icon, image,
  bullet list) → approach (where present) → value proposition strip → "Back to all services".
- **Clients**: banner → intro → organization groups by sector (EPC & Power, Data Centers & IT,
  Industrial, Commercial Real Estate, Renewable, Healthcare) → government organizations →
  "Our strength through experience" (4 points).
- **Contact**: banner → 4 contact cards (address, phone, email, website) → map (Hyderabad) →
  enquiry form → legal & regulatory (company name, CIN, GSTIN, PAN) → certifications.

---

## 7. Things in the document to confirm before publishing

- **Website**: "To be updated". **PAN**: "To be inserted".
- **Name inconsistencies**: "Vinod Duram" (leadership slide) vs "Dr. Vinod Durgam" (infrastructure slide);
  "Busikem Indian Construction" vs "BrickCem Construction Private Limited"; map label says "KALAAGNI".
- **Client logos**: the slide says these are organizations associated with the *leadership team*,
  and "specific team members, contracts and project references must be confirmed before publication".
  Logos are trademarks; use them only with permission. Until then: names as text or placeholders.
- **Typos in slides** (fix silently in the site): "mixed-uss", "multidiscipllinary", "preperation",
  "KALAGNI integrated" (lowercase i).
- **Duplicate slide number** "08" (MEPF and Railway & Metro).

---

## 8. Assets needed (the real files will be provided)

Put them in `assets/images/` with these names so they drop straight into the code:

| File | What | Ideal size |
|---|---|---|
| `logo-white.png` | ✅ DONE: from the logo you provided (white text, for navy backgrounds), trimmed | (original SVG / high-res still welcome: current edges are slightly soft) |
| `logo-dark.png` | ✅ DONE: navy-text copy made from it, for white backgrounds | replace with an official dark version if one exists |
| `favicon.png`, `apple-touch-icon.png` | ✅ DONE: flame cut out of the logo (64px, 180px) | |
| `hero-1.jpg` … `hero-4.jpg` | Hero slides: EPC overview, power substation, solar, buildings | 1920×800, landscape |
| `about.jpg` | Office building (Who We Are) | 1200×800 |
| `service-electrical.jpg`, `service-solar-bess.jpg`, `service-infrastructure.jpg`, `service-mepf.jpg`, `service-hvac.jpg`, `service-railway-metro.jpg`, `service-digital.jpg`, `service-approvals.jpg`, `service-om.jpg` | One main image per service | 1200×800 |
| `banner-about.jpg`, `banner-services.jpg`, `banner-clients.jpg`, `banner-contact.jpg` | Page header banners | 1920×500 |
| (optional) capability images | Small images for each capability card | 600×400 |
| `assets/docs/kalagni-profile.pdf` | Company profile for the "Company Profile" download pill | — |

Also needed: social media links (none in the document).

Until a file arrives, the page uses a neutral grey placeholder of the same size, so the layout
can be built and checked now.

---

## 9. Build order

1. Global setup: fonts (local), Bootstrap Icons (local), design tokens in `style.css`
2. Header + navbar + mega menu + mobile offcanvas
3. Footer + floating buttons + enquiry modal
4. Home page sections 1–10
5. Service page template → duplicate for 9 services
6. About, Services overview, Clients, Contact
7. Responsive pass (375 / 768 / 992 / 1200 / 1440), accessibility pass, final zip
