// main.js: custom JavaScript for the KALAGNI site.
// Loads after Bootstrap's JS, so the global "bootstrap" object is available.

document.addEventListener('DOMContentLoaded', () => {
  // Desktop = navbar expanded (1200px+) AND a real mouse (not a touch screen)
  const desktop = window.matchMedia('(min-width: 1200px) and (hover: hover)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  // ---------------------------------------------------------------
  // 1. Navbar dropdowns open on hover (desktop).
  //    Click and keyboard (Enter / Space / Esc) still work, because we only
  //    call Bootstrap's own show() / hide() methods.
  // ---------------------------------------------------------------
  document.querySelectorAll('.site-navbar .dropdown').forEach((dropdown) => {
    const toggle = dropdown.querySelector('[data-bs-toggle="dropdown"]');
    const menu = bootstrap.Dropdown.getOrCreateInstance(toggle);
    let hovering = false;
    let closeTimer;

    dropdown.addEventListener('mouseenter', () => {
      if (!desktop.matches) return;
      hovering = true;
      clearTimeout(closeTimer);
      menu.show();
    });

    dropdown.addEventListener('mouseleave', () => {
      if (!desktop.matches) return;
      hovering = false;
      // Small delay, so moving the mouse across the gap into the menu doesn't close it
      closeTimer = setTimeout(() => menu.hide(), 200);
    });

    // If hover already opened the menu, a mouse click must not close it again
    toggle.addEventListener('click', (event) => {
      if (desktop.matches && hovering) {
        event.preventDefault();
        event.stopPropagation();
      }
    });
  });

  // ---------------------------------------------------------------
  // 2. Mobile menu (offcanvas): close it after tapping a link that jumps
  //    within a page, and before the enquiry popup opens.
  // ---------------------------------------------------------------
  const offcanvasEl = document.getElementById('mainNav');
  const hideMobileMenu = () => {
    if (!offcanvasEl) return;
    const instance = bootstrap.Offcanvas.getInstance(offcanvasEl);
    if (instance) instance.hide();
  };
  if (offcanvasEl) {
    offcanvasEl.querySelectorAll('a[href*="#"]:not([data-bs-toggle])').forEach((link) => {
      link.addEventListener('click', hideMobileMenu);
    });
  }

  // ---------------------------------------------------------------
  // 3. Images: <div class="media" data-img="assets/images/x.jpg">
  //    If the file exists it becomes the background; otherwise the navy
  //    placeholder stays. So adding photos later needs no code changes.
  // ---------------------------------------------------------------
  document.querySelectorAll('[data-img]').forEach((el) => {
    const src = el.getAttribute('data-img');
    const probe = new Image();
    probe.onload = () => {
      el.style.backgroundImage = `url("${src}")`;
      el.classList.add('has-img');
    };
    probe.src = src;
  });

  // ---------------------------------------------------------------
  // 4. Enquiry popup: pre-select the service of the button that opened it
  //    (buttons like <button data-service="HVAC Systems">).
  // ---------------------------------------------------------------
  const quoteModal = document.getElementById('quoteModal');
  if (quoteModal) {
    quoteModal.addEventListener('show.bs.modal', (event) => {
      hideMobileMenu();
      const service = event.relatedTarget ? event.relatedTarget.getAttribute('data-service') : null;
      const select = quoteModal.querySelector('select[name="service"]');
      if (select && service) select.value = service;
    });
    // Put the cursor in the first field once the popup is open
    quoteModal.addEventListener('shown.bs.modal', () => {
      const first = quoteModal.querySelector('input, select, textarea');
      if (first) first.focus();
    });
  }

  // ---------------------------------------------------------------
  // 5. Enquiry forms: Bootstrap validation styles + thank-you message.
  //    UI only: there is no server yet. A backend developer connects the
  //    form at the marked line (e.g. fetch() to an API or a form service).
  // ---------------------------------------------------------------
  document.querySelectorAll('.js-enquiry-form').forEach((form) => {
    const success = form.querySelector('.form-success');

    form.addEventListener('submit', (event) => {
      event.preventDefault();

      if (!form.checkValidity()) {
        form.classList.add('was-validated');
        const firstInvalid = form.querySelector(':invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      // TODO (backend): send the data here, e.g. fetch('/api/enquiry', { method: 'POST', body: new FormData(form) })

      form.reset();
      form.classList.remove('was-validated');
      if (success) {
        success.classList.add('is-visible');
        success.focus();
      }
    });

    // Hide the thank-you message again when the user starts a new enquiry
    form.addEventListener('input', () => {
      if (success) success.classList.remove('is-visible');
    });
  });

  // ---------------------------------------------------------------
  // 6. Floating "back to top" button: appears after scrolling down.
  // ---------------------------------------------------------------
  const backToTop = document.querySelector('.js-back-to-top');
  if (backToTop) {
    const toggleBackToTop = () => {
      backToTop.classList.toggle('is-visible', window.scrollY > 600);
    };
    window.addEventListener('scroll', toggleBackToTop, { passive: true });
    toggleBackToTop();
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
    });
  }

  // ---------------------------------------------------------------
  // 7. Hero carousel: pause / play button (moving content must be
  //    stoppable), and no auto-play for people who prefer less motion.
  // ---------------------------------------------------------------
  const heroEl = document.getElementById('heroCarousel');
  if (heroEl) {
    const carousel = bootstrap.Carousel.getOrCreateInstance(heroEl);
    const pauseBtn = heroEl.querySelector('.hero-pause');
    let paused = false;

    const setPaused = (value) => {
      paused = value;
      if (paused) carousel.pause(); else carousel.cycle();
      if (pauseBtn) {
        pauseBtn.innerHTML = paused
          ? '<i class="bi bi-play-fill" aria-hidden="true"></i>'
          : '<i class="bi bi-pause-fill" aria-hidden="true"></i>';
        pauseBtn.setAttribute('aria-label', paused ? 'Play slideshow' : 'Pause slideshow');
      }
    };

    if (pauseBtn) pauseBtn.addEventListener('click', () => setPaused(!paused));
    if (reducedMotion.matches) setPaused(true);

    // Bootstrap restarts the slideshow when the mouse leaves the carousel;
    // keep it stopped if the user pressed pause.
    heroEl.addEventListener('mouseleave', () => {
      if (paused) carousel.pause();
    });
  }

  // ---------------------------------------------------------------
  // 8. Footer: current year in the copyright line.
  // ---------------------------------------------------------------
  document.querySelectorAll('.js-year').forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
});
