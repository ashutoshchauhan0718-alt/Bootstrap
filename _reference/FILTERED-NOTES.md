# Filtered notes from the reference audit

Source: "Reference Site Audit.pdf" (Claude in Chrome, 22 Nov 2026).
Only what matters for our Bootstrap 5.3 build. The requirements document still decides the final scope.

---

## 1. Design tokens (simplified)

| Token | Value | Use |
|---|---|---|
| Font | Poppins 400/500/600/700, fallback `system-ui, sans-serif` | Everything |
| Primary | `#145da0` (hover `#0f4d85`) | Buttons, pills, footer headings |
| Heading blue | `#155baf` | h1, card titles |
| Section title blue | `#0f5991` | h2 |
| Accent orange | `#ff6600` / `#f76c0f` | Search button, card stripe, icons |
| Text | `#212529` body, `#555` card text | |
| Card border | `rgba(18,93,173,.28)` | Category cards |
| Card shadow | `0 8px 24px rgba(149,157,165,.2)` | Category cards |
| Radius | 3px cards, 6px inputs/feature cards, 999px pills | |
| Brand gradient | `linear-gradient(90deg,#145da0,#ff6600)` | Footer heading underline |

Section headings: 29px / 600, centered. Body 16px / 24px.

---

## 2. Page structure (homepage)

1. **Header**, 3 bands
   - Announcement bar (soft peach to blue gradient, 3 trust claims)
   - Logo (left) + main menu (right)
   - Catalog pill | search with orange button | language pill + Request Quote button
2. **Navbar**: 4 items with full-width mega menus (product image + label) and 3 plain links
3. **Hero**: 4 slides that fade into each other every 4s, plus an H1 and intro text below
4. **Category sections** (repeated): centered h2, description, 2-column card grid
   (text + sub-links on the left, product image on the right, image zooms on hover)
5. **"Fast selling"**: row of round icons (110px light-blue circles), icon zooms on hover
6. **"Why choose us"**: 6 cards, orange left border, icon + title + text, card lifts on hover
7. **Footer**: 4 columns (brand + social, links, products, contact), slanted blue panel
   behind column 1, orange scrolling strip, copyright bar
8. **Extras**: floating WhatsApp and quote buttons (bottom right), Request Quote modal form

---

## 3. Bootstrap mapping

| Part | Bootstrap |
|---|---|
| Navbar switching at 1200px | `navbar-expand-xl` |
| Mobile menu | Offcanvas (`offcanvas-start`) + Accordion sub-menus |
| Mega menu | Dropdown + grid inside, opens on hover (desktop) and click |
| Hero | Carousel `carousel-fade`, `data-bs-interval="4000"` |
| Category cards | `row row-cols-1 row-cols-md-2 g-3` + `card` |
| Feature cards | `row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4` + `card border-start border-4` |
| Footer | `row row-cols-1 row-cols-xl-4` |
| Quote form | Modal + `row g-3` + `col-md-6` + `form-control` |

---

## 4. Do better than the reference

- No broken header between 992 and 1200px, and no horizontal scroll
- Mega menu usable by click and keyboard, not hover only
- Mobile sub-menus collapsible (accordion), with a backdrop behind the menu
- Hero text in real HTML (not baked into images), and the hero shown on mobile
- Visible hamburger icon, visible focus states, left-aligned paragraphs
- Respect `prefers-reduced-motion` for the fading, marquee and scrolling animations
- Use our own logo, images and text, never theirs

## 5. Skip unless the requirements document asks for it

Cookie banner, Google Translate (UI-only language pill is fine), tracking scripts,
SweetAlert2, intl-tel-input, Cloudflare Turnstile, AJAX search.

---

## 6. Header & navbar details (from the full Part 2 audit)

### Desktop header, 3 bands (~154px total, not sticky)
| Band | Height | Look | Contents |
|---|---|---|---|
| Announcement bar | 28px | Peach to blue gradient `linear-gradient(90deg,#f6b28a 0,#f3caa7 25%,#d1e6f8 65%,#9fc7f4 100%)`, text 15px/600 `#333`, centered | 3 trust claims separated by "•" |
| Logo + nav row | ~71px | White, **1px solid `#ff6600` bottom border**, side padding ~19px | Logo left (col-xl-2), nav centered (col-xl-10) |
| Utility row | 54px | White, shadow `0 2px 5px rgba(0,0,0,.1)`, side padding 48px | Catalog pill, search (wide, center), language pill + divider + Request Quote (right) |

### Logo
- Width 231px desktop, 212px at ~1200, 194px at 768, 173px at 375 (height auto).
- Links to home. Same logo in the footer (~200–232px wide).
- Ours: SVG or 2× PNG, plus a proper favicon.

### Main nav
- 7 items: 4 with mega menus (Cooling, Heating, Testing, Laboratory Equipment) + 3 plain links (Data Sheets, About Us, Contact Us).
- Links: Poppins 15px / 600, `#000`, padding 11px 9px (≈18px between labels), link height 48px.
- Plain-link hover: text turns amber `#d97706` + a 2px underline grows from 0 to 100% width (`transition: width .25s`).
- Reference has NO caret icon, NO hover on mega parents, NO active-page state.

### Mega menu panel (same for all 4)
- Full width, white, padding 15px 0, shadow `0 4px 10px rgba(0,0,0,.1)`, no radius, ~160px tall.
- Inner content max-width 1200px, items in one centered row, gap 40px.
- Item: 97×97px product image (object-fit contain, mb 10px) + label 15px / 600 `#155baf`, min-width 130px.
- Item hover: image `scale(1.05)` over .3s.
- Items per menu: Cooling 3, Heating 1, Testing 1, Laboratory Equipment 4.

### Search
- Input 42px tall, padding 8px 16px, 15px text, bg `#f9fafb` (white on focus), border `1px solid rgba(20,93,160,.56)`, radius 6px, shadow `0 4px 12px rgba(0,0,0,.1)`.
- Orange `#ff6600` icon button inside the input on the right (36×33, radius 4px, search icon).
- Suggestion box (UI only for us): directly under the input, white, 1px border, max-height 200px, scrolls.

### Utility buttons
| Element | Style |
|---|---|
| Catalog pill | 8px 16px, 12px / 600 uppercase, letter-spacing .3px, bg `#145da0`, radius 30px, book icon; hover bg `#0f4d85` + lift 1px + bigger shadow |
| Language pill | ~108×29, 6px 12px, 13px, transparent bg, border `1px solid rgba(0,0,0,.12)`, radius 999px, translate icon + label + ▾; hover bg `rgba(0,0,0,.05)` |
| Language dropdown | 220px wide, radius 14px, shadow `0 18px 45px rgba(15,40,80,.18)`, items 13.5px with flag, active item bold with light-blue bg |
| Divider | 1px × 24px, `rgba(181,174,174,.53)` |
| Request Quote | 8px padding, 15px / 500 uppercase, bg `#145da0`, radius 3px, file icon; animated coral border running around it; opens the quote modal |

### Mobile (reference)
- Blue bar `#145cac` on top (catalog pill, full-width search, language pill), then white logo row below.
- Hamburger sits on the blue bar in dark blue, which makes it nearly invisible (don't copy).
- Menu: panel slides in from the left, 250px wide, bg `#0d70b9`, white text 15–16px, sub-items indented ~41px, all sub-menus always open, no backdrop.

### Our navbar decisions
- `navbar-expand-xl`: full menu at ≥1200px, hamburger below. No broken 992–1200 range.
- Mega parents get a small chevron and the same amber hover/underline as plain links.
- Mega menu opens on hover (desktop) AND click/keyboard; panel anchored under the header, short fade-in.
- Show the active page (amber text + underline).
- Mobile: logo + white/visible hamburger row, full-width search below; menu = **offcanvas-start** with **accordion** sub-menus, backdrop and scroll lock. Catalog, language and Request Quote go inside the offcanvas.
- Mobile menu lists ALL items (the reference misses "Centrifuge" on mobile).

---

## 7. Still missing

- [x] Part 2 audit (header and navbar in detail, all 4 mega menus)
- [ ] Screenshots: desktop header, each mega menu open, mobile header, mobile menu open
- [ ] Save the latest audit PDF into `_reference/`
- [ ] Requirements document
