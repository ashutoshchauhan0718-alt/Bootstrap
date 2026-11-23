Copy everything below the line into Claude in Chrome (with the reference website open in the current tab).

---

You are helping me analyse this website as a DESIGN REFERENCE. I will rebuild a site
with Bootstrap 5.3 inspired by it (not a copy). Do a complete, very detailed audit and
write ALL findings into ONE Google Doc.

=== HOW TO WORK ===
1. Open a new tab at https://docs.new and name the document "Reference Site Audit".
   Keep the reference website open in its own tab and switch between the two.
2. Work through PARTS 1-7 below in order. After finishing EACH part, immediately write
   that part into the Google Doc under a heading "PART X – <name>" before moving on.
   Don't keep everything in memory until the end. Don't stop to ask me between parts.
3. Rules for every part:
   - Use real DOM / computed styles, not guesses. Exact values (px, hex, rgba, font names).
   - Hover over / click elements to reveal hidden states (dropdowns, hover effects, menus).
   - Describe text content (e.g. "heading about fast delivery"), don't copy it word for word.
   - Use tables where possible.
   - Before inspecting, check window.innerWidth. PARTS 1-6 must be done in the DESKTOP
     layout (innerWidth ≥ 1200). If the page is narrower (e.g. because of your side
     panel), zoom out with Ctrl+minus until innerWidth ≥ 1200. Zoom does not change
     computed px values. Note the zoom level used at the top of each part.
4. At the very end, reset zoom with Ctrl+0 and give me a short summary in chat with the
   Google Doc link.

=== PART 1 – TECH & GLOBAL DESIGN TOKENS ===
- Is Bootstrap used (version)? Other frameworks/libraries (jQuery, Swiper, Slick, AOS,
  GSAP, Tailwind...)? Icon library? List CSS/JS files loaded.
- Fonts: every font-family, where loaded from (exact Google Fonts URL if any), weights.
- Typography table: font-size / weight / line-height / letter-spacing / color for
  h1, h2, h3, h4, body, small text, nav links, buttons.
- Color palette table: every distinct color (hex/rgba) and where it's used: primary,
  secondary, accent, text, muted, backgrounds, borders, links, hover states.
  Full CSS of any gradients.
- Container max-width, section top/bottom padding, common gaps.
- Border radius values, box shadows, transitions (duration/easing).
- Buttons: every variant: padding, font, radius, colors, border, hover/focus, icons.
- All CSS variables defined in :root.

=== PART 2 – HEADER, LOGO & NAVIGATION (very detailed) ===
A. Top bar above navbar (if any): contents, height, colors, hidden on mobile/scroll?
B. Logo: file type (SVG/PNG/text) and its URL, rendered width/height (desktop and mobile),
   position, spacing, links to home? Variants: on scroll, on dark bg, in footer,
   favicon, mobile. Also any client/partner LOGO STRIP on the page: layout,
   grayscale or color, hover effect, slider or static.
C. Navbar: height, background (solid/transparent/blur), shadow, border.
   Sticky/fixed? Transparent over hero then solid on scroll? Shrinks on scroll?
   All menu items in order and which ones have sub-menus. Alignment.
   Link styles: font, spacing, normal/hover/active state (underline, color, animation).
   Right-side extras: CTA button, search, cart, login, language, icons.
D. Sub-nav / dropdowns (hover over EVERY item that has one):
   Type: simple dropdown / multi-level nested / mega menu. Opens on hover or click?
   Open animation. Indicator arrow (does it rotate?). Dropdown box: width, padding,
   background, radius, shadow, border, offset. Items: font, padding, hover, icons,
   descriptions, images. Mega menu: columns, headings, featured image/card.
   Simplified HTML skeleton of one nav item with its sub-menu (structure + classes only).

=== PART 3 – HERO SECTION (very detailed) ===
- Height (100vh? px?), full-width or contained.
- Background: image / video / gradient / solid / pattern; overlay color + opacity;
  position/size; parallax?
- Layout (text left + image right? centered?), columns.
- Content in order: badge/label, heading, highlighted words (color/underline/gradient),
  sub-text, buttons (count + styles), stats, trust badges, logos, form, search,
  scroll-down indicator.
- Exact typography for heading and sub-text; max-width of text block.
- Images/illustrations: type, size, position, decorative shapes, floating cards.
- Slider? Number of slides, autoplay, arrows/dots style, transition.
- Animations on load / scroll / hover; library if detectable.
- Simplified HTML skeleton (structure + classes only).

=== PART 4 – ALL OTHER SECTIONS (between hero and footer), top to bottom ===
For EACH section: name/purpose; background; padding; heading block style (label above
title? centered? divider?); layout columns; card styles (padding, radius, shadow,
border, image, icon size/background, hover effect); sliders/tabs/accordions and their
controls; scroll animations; best Bootstrap 5 component/grid to rebuild it.

=== PART 5 – FOOTER, FORMS & MISC ===
- Footer: background, column layout, contents of each column, link hover style,
  social icons, newsletter form, bottom bar.
- Forms anywhere: input height, padding, border, radius, placeholder color, focus style,
  label style (above/floating/none), validation style, submit button.
- Misc: back-to-top button, cookie banner, chat widget, preloader, custom scrollbar,
  cursor effects, page transitions.
- Accessibility: contrast problems, focus outlines visible or removed.

=== PART 6 – OTHER PAGES ===
Find the main nav pages similar to: About, Services, Contact, Login (or closest
equivalents). For each one, open it and briefly note: page header/banner style,
sections used (reuse PART 4 format but shorter), and anything unique to that page.

=== PART 7 – RESPONSIVE SWEEP (using zoom) ===
STEP 1: Read document.styleSheets and list every @media width breakpoint used.
  If some stylesheets are blocked (cross-origin), say so. Identify the exact media
  query that switches the navbar between hamburger and full menu.
STEP 2: For target widths ~375, ~768, ~992, ~1280, ~1440:
  Ctrl+0, read innerWidth at 100%, then pick the Chrome zoom level (25, 33, 50, 67,
  75, 80, 90, 100, 110, 125, 150, 175, 200, 250, 300%) that gets innerWidth closest
  to the target. Report the ACTUAL innerWidth reached. Then scroll the whole page and
  record: navbar (hamburger or full? logo size? CTA/top bar visible?), how sub-menus
  open at that width, hero layout + heading size, columns per section, anything
  hidden/shown, footer layout. If a mobile menu exists, OPEN it and describe it
  (dropdown / full-screen overlay / side drawer, hamburger animation, how sub-menus
  expand inside it).
STEP 3: Write in the doc:
  1. Table of CSS breakpoints and what each controls.
  2. Comparison table: rows = page parts (navbar, sub-nav, hero, each section, footer),
     columns = each tested width.
  3. Exact width where the hamburger appears.
  4. Anything odd or broken at any size.
STEP 4: Ctrl+0 to reset zoom.
