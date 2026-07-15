/**
* Template Name: Landio
* Template URL: https://bootstrapmade.com/landio-bootstrap-landing-page-template/
* Updated: Sep 06 2025 with Bootstrap v5.3.8
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', toggleScrolled);
  } else {
    toggleScrolled();
  }

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  function renderSharedNavMenu() {
    const navmenu = document.querySelector('#navmenu');
    if (!navmenu) return;

    const currentPath = window.location.pathname || '/';
    const currentPage = currentPath.split('/').pop().toLowerCase() || 'index.html';
    const isBlogPage = currentPage === 'blog.html' || currentPath.includes('/blog/');
    const relPrefix = currentPath.includes('/blog/') ? '../' : '';
    const servicePages = [
      'layanan.html',
      'souvenir-kantor.html',
      'souvenir-custom.html',
      'merchandise-perusahaan.html',
      'seminar-kit.html',
      'botol-minum.html',
      'dining-set.html',
      'jam-dinding-custom.html',
      'mug-custom.html',
      'powerbank-custom.html',
      'pulpen-eksklusif.html',
      'tea-set.html',
      'tumbler-custom.html',
      'bantal-corporate.html',
      'humidifier-custom.html'
    ];
    const isServicePage = servicePages.includes(currentPage);
    const list = navmenu.querySelector('ul');

    if (!list) return;

    list.innerHTML = `
      <li><a href="${relPrefix}index.html"${currentPage === 'index.html' ? ' class="active"' : ''}>Beranda</a></li>
      <li><a href="${relPrefix}about.html"${currentPage === 'about.html' ? ' class="active"' : ''}>Tentang Kami</a></li>
      <li><a href="${relPrefix}katalog.html"${currentPage === 'katalog.html' ? ' class="active"' : ''}>Katalog</a></li>
      <li><a href="${relPrefix}blog.html"${isBlogPage ? ' class="active"' : ''}>Blog</a></li>
      <li class="dropdown"><a href="${relPrefix}layanan.html"${isServicePage ? ' class="active"' : ''}><span>Layanan</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="${relPrefix}souvenir-kantor.html">Souvenir Kantor</a></li>
          <li><a href="${relPrefix}souvenir-custom.html">Souvenir Custom</a></li>
          <li><a href="${relPrefix}merchandise-perusahaan.html">Merchandise Perusahaan</a></li>
          <li><a href="${relPrefix}seminar-kit.html">Seminar Kit</a></li>
        </ul>
      </li>
    `;
  }

  function bindNavMenuEvents() {
    document.querySelectorAll('#navmenu a').forEach(navmenu => {
      navmenu.addEventListener('click', () => {
        if (document.querySelector('.mobile-nav-active')) {
          mobileNavToogle();
        }
      });
    });

    document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
      navmenu.addEventListener('click', function(e) {
        e.preventDefault();
        this.parentNode.classList.toggle('active');
        this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
        e.stopImmediatePropagation();
      });
    });
  }

  function initSharedNavMenu() {
    renderSharedNavMenu();
    bindNavMenuEvents();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSharedNavMenu);
  } else {
    initSharedNavMenu();
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  // ensure initial state runs as soon as DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', toggleScrollTop);
  } else {
    toggleScrollTop();
  }
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    if (typeof AOS === 'undefined') return;
    var isSmall = (window.innerWidth || document.documentElement.clientWidth) <= 768;
    var duration = isSmall ? 350 : 600;
    AOS.init({
      duration: duration,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
    try { document.body.classList.add('aos-initialized'); } catch (e) { /* noop */ }
  }

  // Reduce or remove data-aos-delay on small screens to speed up perceived load
  function adjustAosForSmallScreens() {
    try {
      if ((window.innerWidth || document.documentElement.clientWidth) <= 768) {
        document.querySelectorAll('[data-aos-delay]').forEach(function(el) {
          el.setAttribute('data-aos-delay', '0');
        });
      }
    } catch (e) { /* noop */ }
  }

  // Initialize AOS as soon as the DOM is ready so elements with
  // data-aos don't stay hidden while waiting for all assets to load.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { adjustAosForSmallScreens(); aosInit(); });
  } else {
    adjustAosForSmallScreens();
    aosInit();
  }

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSwiper);
  } else {
    initSwiper();
  }

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle, .faq-item .faq-header').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function(e) {
      if (window.location.hash) {
        if (document.querySelector(window.location.hash)) {
          setTimeout(() => {
            let section = document.querySelector(window.location.hash);
            let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
            window.scrollTo({
              top: section.offsetTop - parseInt(scrollMarginTop),
              behavior: 'smooth'
            });
          }, 100);
        }
      }
    });
  } else {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  }

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', navmenuScrollspy);
  } else {
    navmenuScrollspy();
  }
  document.addEventListener('scroll', navmenuScrollspy);

  /**
   * Inject shared features strip on non-home pages that lack one.
   */
  function injectPageFeatures() {
    if (document.body.classList.contains('index-page')) return;
    if (window.location.pathname.endsWith('/about.html') || window.location.pathname.endsWith('about.html')) return;
    if (document.querySelector('.page-features, .features-2.section, .service-details-content, .features.section .features-grid')) return;

    const anchor = document.querySelector('.souvenir-bottom-cta') ||
      document.querySelector('.ad-banner-section') ||
      document.querySelector('#footer');
    if (!anchor) return;

    const section = document.createElement('section');
    section.className = 'page-features section light-background';
    section.setAttribute('data-aos', 'fade-up');
    section.innerHTML = `
      <div class="container">
        <div class="section-title">
          <h2>Keunggulan SouvenirPro</h2>
          <p>Partner terpercaya untuk souvenir kantor, merchandise custom, dan corporate gift dengan layanan end-to-end.</p>
        </div>
        <div class="features-mini-grid">
          <div class="mini-feature">
            <i class="bi bi-palette"></i>
            <h4>Desain & Mockup</h4>
            <p>Mockup logo dan proofing jelas sebelum produksi dimulai.</p>
          </div>
          <div class="mini-feature">
            <i class="bi bi-shield-check"></i>
            <h4>Quality Control</h4>
            <p>Setiap pesanan dicek jumlah, kondisi, dan hasil branding.</p>
          </div>
          <div class="mini-feature">
            <i class="bi bi-truck"></i>
            <h4>Pengiriman Fleksibel</h4>
            <p>Kirim ke kantor, venue acara, atau beberapa cabang sekaligus.</p>
          </div>
          <div class="mini-feature">
            <i class="bi bi-chat-dots"></i>
            <h4>Konsultasi Cepat</h4>
            <p>Tim admin siap bantu rekomendasi produk sesuai budget dan deadline.</p>
          </div>
        </div>
      </div>`;
    anchor.parentNode.insertBefore(section, anchor);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectPageFeatures);
  } else {
    injectPageFeatures();
  }

  /**
   * Load long-form layanan article on dropdown service pages.
   */
  function loadLayananArticle() {
    const mount = document.getElementById('layanan-article-mount');
    if (!mount || !window.LAYANAN_ARTICLE_TEMPLATE) return;

    const title = mount.dataset.title || 'Mengapa Souvenir Kantor Penting untuk Perusahaan';
    const intro = mount.dataset.intro || '';
    const introBlock = intro ? '<p class="article-lead">' + intro + '</p>' : '';

    mount.outerHTML = window.LAYANAN_ARTICLE_TEMPLATE
      .replace(/\{\{PAGE_TITLE\}\}/g, title)
      .replace(/\{\{PAGE_INTRO_BLOCK\}\}/g, introBlock);

    if (typeof AOS !== 'undefined') {
      AOS.refreshHard();
    }
  }

  // WhatsApp helpers used by the modal and widget
  var WA_NUMBER = '6288989643555';
  var DEFAULT_WA_MSG = 'Halo, saya ingin konsultasi souvenir dari website SouvenirPro';
  function waLink(message) {
    return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(message || DEFAULT_WA_MSG);
  }

  // Quick fallback: replace images using unsupported HEIC format
  function replaceHEICFallbacks() {
    try {
      document.querySelectorAll('img').forEach(function(img) {
        var src = img.getAttribute('src') || '';
        var lower = src.toLowerCase();
        if (!lower.endsWith('.heic')) return;
        // Keep testimonial profile HEIC images (profil*, profi*, profile*)
        // so devices that support HEIC (iOS Safari, newer browsers) can show them.
        var name = lower.split('/').pop() || '';
        if (/^(profil|profi|profile)/.test(name)) return;
        // otherwise replace with a small logo fallback to avoid broken images
        img.src = 'images/Logo.webp';
        img.setAttribute('data-fallback-heic', '1');
      });
    } catch (e) { /* noop */ }
  }

  // Run HEIC fallback immediately so images aren't left broken while other
  // inits (AOS, widgets) happen.
  try { replaceHEICFallbacks(); } catch (e) { /* noop */ }

  // Only adjust footer content: add short descriptive text under the "Layanan" column.
  function normalizeLayananLinks() {
    document.querySelectorAll('.nav-column').forEach(function(col) {
      try {
        var h6 = col.querySelector('h6');
        if (!h6 || h6.textContent.trim() !== 'Layanan') return;
        if (col.querySelector('.footer-layanan-text')) return;
        // Previously inserted a short descriptive paragraph here; removed per design request.
        // Remove the footer's "Ringkasan Layanan" link if present to avoid duplicate navigation.
        col.querySelectorAll('a[href="layanan.html"]').forEach(function(a) {
          try { a.remove(); } catch (e) { /* noop */ }
        });
      } catch (e) {}
    });

    // Disable header/nav anchors that point directly to layanan.html (keep dropdown toggle icon functional)
    try {
      document.querySelectorAll('#navmenu a[href="layanan.html"]').forEach(function(a) {
        // remove href so clicking the label doesn't navigate; keep the toggle icon ('.toggle-dropdown') functional
        a.removeAttribute('href');
        a.setAttribute('aria-disabled', 'true');
        a.classList.add('nav-disabled');
      });
    } catch (e) { /* noop */ }
  }

  // Inject Blog link into header nav and footer (runtime safe)
  function injectBlogLinks() {
    try {
      var navUl = document.querySelector('#navmenu ul');
      // Check for blog.html link with OR without relative prefix (../blog.html)
      if (navUl && !navUl.querySelector('a[href$="blog.html"]')) {
        var layananLi = navUl.querySelector('li.dropdown');
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = 'blog.html';
        a.textContent = 'Blog';
        li.appendChild(a);
        if (layananLi && layananLi.parentNode) {
          layananLi.parentNode.insertBefore(li, layananLi);
        } else {
          var berandaA = navUl.querySelector('a[href$="index.html"]');
          var insertAfter = berandaA ? berandaA.closest('li') : null;
          if (insertAfter && insertAfter.parentNode) insertAfter.parentNode.insertBefore(li, insertAfter.nextSibling);
          else navUl.appendChild(li);
        }
      }
    } catch (e) { /* noop */ }

    try {
      // Insert Blog into footer 'Perusahaan' column before Kontak (if present)
      document.querySelectorAll('.nav-column').forEach(function(col) {
        try {
          var h6 = col.querySelector('h6');
          if (!h6 || h6.textContent.trim() !== 'Perusahaan') return;
          var nav = col.querySelector('.footer-nav');
          if (!nav) return;
          if (nav.querySelector('a[href$="blog.html"]')) return;
          var kontakA = nav.querySelector('a[href$="kontak.html"]');
          var a = document.createElement('a');
          a.href = 'blog.html';
          a.textContent = 'Blog';
          if (kontakA) nav.insertBefore(a, kontakA);
          else nav.appendChild(a);
        } catch (err) { /* noop */ }
      });
    } catch (e) { /* noop */ }
  }

  function injectOrderModal() {
    if (document.getElementById('order-modal')) return;

    var modal = document.createElement('div');
    modal.id = 'order-modal';
    modal.className = 'order-modal';
    modal.setAttribute('aria-hidden', 'true');
    modal.innerHTML = [
      '<div class="order-modal-backdrop" data-close-modal></div>',
      '<div class="order-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="order-modal-title">',
      '  <button type="button" class="order-modal-close" aria-label="Tutup" data-close-modal>&times;</button>',
      '  <div class="order-modal-header">',
      '    <div class="order-modal-logo"><img src="images/Logo.webp" alt="SouvenirPro"></div>',
      '    <h3 id="order-modal-title">Mau mulai dari mana?</h3>',
      '    <p>Pilih langkah yang paling sesuai. Kamu bisa langsung mengetik pesan atau pilih opsi cepat di bawah.</p>',
      '  </div>',
      '  <div class="order-modal-animation" aria-hidden="true">',
      '    <div class="dino">🦖</div>',
      '  </div>',
      '  <div class="order-modal-grid">',
      '    <button type="button" class="order-modal-card" data-msg="Halo, saya ingin melihat katalog produk souvenir">',
      '      <span class="order-modal-icon"><i class="bi bi-grid"></i></span>',
      '      <strong>Lihat Katalog</strong>',
      '      <small>Jelajahi produk souvenir &amp; merchandise</small>',
      '    </button>',
      '    <button type="button" class="order-modal-card" data-msg="Halo, saya ingin estimasi paket harga untuk souvenir">',
      '      <span class="order-modal-icon"><i class="bi bi-tags"></i></span>',
      '      <strong>Cek Paket Harga</strong>',
      '      <small>Estimasi budget sebelum pesan</small>',
      '    </button>',
      '    <button type="button" class="order-modal-card" data-msg="Halo, saya ingin info layanan souvenir kantor dan seminar kit">',
      '      <span class="order-modal-icon"><i class="bi bi-briefcase"></i></span>',
      '      <strong>Pelajari Layanan</strong>',
      '      <small>Souvenir kantor, custom &amp; seminar kit</small>',
      '    </button>',
      '    <button type="button" class="order-modal-card" data-msg="Halo, saya ingin mengirim brief untuk kebutuhan detail souvenir">',
      '      <span class="order-modal-icon"><i class="bi bi-envelope-paper"></i></span>',
      '      <strong>Kirim Brief</strong>',
      '      <small>Form kontak untuk kebutuhan detail</small>',
      '    </button>',
      '  </div>',
      '  <div class="order-modal-typing">',
      '    <div class="typing-preview" id="order-typed">' + DEFAULT_WA_MSG + '</div>',
      '    <textarea id="order-modal-input" class="order-modal-input" rows="2" aria-label="Pesan untuk admin">' + DEFAULT_WA_MSG + '</textarea>',
      '  </div>',
      '  <div class="order-modal-footer">',
      '    <p>Butuh jawaban cepat? Chat admin kami di WhatsApp.</p>',
      '    <a href="' + waLink() + '" class="order-modal-wa-btn order-modal-footer-wa" target="_blank" rel="noopener">',
      '      <i class="bi bi-whatsapp"></i> Chat WhatsApp',
      '    </a>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(modal);

    // Setup quick option clicks (cards) and typing behavior
    var orderInput = modal.querySelector('#order-modal-input');
    var typedPreview = modal.querySelector('#order-typed');
    var footerWa = modal.querySelector('.order-modal-footer-wa');

    function updateFooterWa() {
      if (!footerWa) return;
      var m = (orderInput && orderInput.value.trim()) ? orderInput.value.trim() : DEFAULT_WA_MSG;
      footerWa.href = waLink(m);
    }

    modal.querySelectorAll('.order-modal-card').forEach(function(card) {
      card.addEventListener('click', function(e) {
        e.preventDefault();
        var msg = card.getAttribute('data-msg') || DEFAULT_WA_MSG;
        // populate the typing area and preview
        if (orderInput && typedPreview) {
          orderInput.value = msg;
          typedPreview.textContent = msg;
          try { orderInput.focus(); orderInput.selectionStart = orderInput.selectionEnd = orderInput.value.length; } catch (er) {}
        }
        // mark active card
        modal.querySelectorAll('.order-modal-card.active').forEach(function(c) { c.classList.remove('active'); });
        card.classList.add('active');
        // update footer wa href
        updateFooterWa();
        // scroll typing area into view for small screens
        var typingArea = modal.querySelector('.order-modal-typing');
        if (typingArea) typingArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
      });
    });

    if (orderInput && typedPreview) {
      orderInput.addEventListener('input', function() { typedPreview.textContent = orderInput.value; updateFooterWa(); });
      typedPreview.textContent = orderInput.value || DEFAULT_WA_MSG;
      // ensure footer link uses initial value
      updateFooterWa();
    }

    // 'Open app' button removed; use footer Chat WhatsApp to open with the typed message.
  }

  function openOrderModal() {
    var modal = document.getElementById('order-modal');
    if (!modal) return;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    // Lock background scroll and remember position
    try { lockBodyScroll(); } catch (e) {}
    document.body.classList.add('order-modal-open');
    // Start simple typing preview animation when modal opens
    try {
      var typed = modal.querySelector('#order-typed');
      var input = modal.querySelector('#order-modal-input');
      var footer = modal.querySelector('.order-modal-footer-wa');
      if (typed && input) {
        typed.textContent = '';
        var text = input.value || DEFAULT_WA_MSG;
        var i = 0;
        var timer = setInterval(function() {
          typed.textContent += text.charAt(i) || '';
          if (footer) footer.href = waLink(typed.textContent || DEFAULT_WA_MSG);
          i++;
          if (i >= text.length) clearInterval(timer);
        }, 22);
      } else if (footer) {
        footer.href = waLink((input && input.value) ? input.value : DEFAULT_WA_MSG);
      }
    } catch (e) { /* noop */ }
  }

  function closeOrderModal() {
    var modal = document.getElementById('order-modal');
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('order-modal-open');
    try { unlockBodyScroll(); } catch (e) {}
  }

  // Robust lock/unlock for body scroll to prevent background movement
  function lockBodyScroll() {
    try {
      var scrollY = window.scrollY || document.documentElement.scrollTop || 0;
      // store current scroll position
      document.body.dataset._scrollY = String(scrollY);
      // add class to html as well for CSS fallbacks
      try { document.documentElement.classList.add('order-modal-open'); } catch (e) {}
      // fix body to viewport so background doesn't move
      document.body.style.position = 'fixed';
      document.body.style.top = '-' + scrollY + 'px';
      document.body.style.left = '0';
      document.body.style.right = '0';
      // ensure no native smooth scroll jump when unlocking
      try { document.documentElement.style.scrollBehavior = 'auto'; } catch (e) {}
    } catch (e) { /* noop */ }
  }

  function unlockBodyScroll() {
    try {
      var stored = document.body.dataset._scrollY ? parseInt(document.body.dataset._scrollY, 10) : 0;
      // remove fixed positioning
      document.body.style.position = '';
      document.body.style.top = '';
      document.body.style.left = '';
      document.body.style.right = '';
      // remove html class fallback
      try { document.documentElement.classList.remove('order-modal-open'); } catch (e) {}
      // restore scroll
      window.scrollTo(0, stored || 0);
      // tidy up
      try { delete document.body.dataset._scrollY; } catch (e) {}
      // restore scroll-behavior after a tick
      setTimeout(function() { try { document.documentElement.style.scrollBehavior = ''; } catch (e) {} }, 0);
    } catch (e) { /* noop */ }
  }

  function bindOrderModal() {
    injectOrderModal();

    // Attach direct listeners to known triggers to reliably intercept clicks
    try {
      var explicitTriggers = document.querySelectorAll('.btn-getstarted[href*="wa.me"], .souvenir-bottom-cta .btn-primary[href*="wa.me"], .hero-actions .btn-primary[href*="wa.me"], .cta-section .btn-primary[href*="wa.me"]');
      explicitTriggers.forEach(function(t) {
        t.addEventListener('click', function(e) {
          try { e.preventDefault(); e.stopPropagation(); } catch (err) {}
          openOrderModal();
          try { if (t.blur) t.blur(); } catch (err) {}
        });
      });
    } catch (e) { /* noop */ }

    document.addEventListener('click', function(e) {
      var trigger = e.target.closest('.order-modal-trigger, .btn-getstarted[href*="wa.me"], .souvenir-bottom-cta .btn-primary[href*="wa.me"], .hero-actions .btn-primary[href*="wa.me"], .cta-section .btn-primary[href*="wa.me"]');
      if (trigger && (trigger.classList.contains('btn-getstarted') || trigger.classList.contains('order-modal-trigger') || trigger.closest('.souvenir-bottom-cta') || trigger.closest('.hero-actions') || trigger.closest('.cta-section'))) {
          e.preventDefault();
          // prevent click from toggling other UI and remove focus to avoid :focus CSS enlarge
          try { e.stopPropagation(); } catch (er) {}
          openOrderModal();
          try { if (trigger.blur) trigger.blur(); else if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); } catch (er) {}
          return;
        }
      if (e.target.closest('[data-close-modal]')) {
        e.preventDefault();
        closeOrderModal();
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeOrderModal();
    });
  }

  function enhanceWhatsAppFloat() {
    var oldFloat = document.querySelector('a.whatsapp-float');
    if (!oldFloat || document.getElementById('wa-widget')) return;

    var pageIcon = document.querySelector('link[rel="icon"]');
    var logoSrc = pageIcon ? pageIcon.href : '/images/Logo.webp';

    var widget = document.createElement('div');
    widget.id = 'wa-widget';
    widget.className = 'wa-widget';
    widget.innerHTML = [
      '<div class="wa-widget-panel" id="wa-widget-panel" aria-hidden="true">',
      '  <button type="button" class="wa-widget-panel-close" aria-label="Tutup">&times;</button>',
      '  <div class="wa-widget-panel-header">',
      '    <div class="wa-widget-avatar">',
      '      <img src="' + logoSrc + '" alt="SouvenirPro">',
      '      <span class="wa-widget-online"></span>',
      '    </div>',
      '    <div>',
      '      <strong>SouvenirPro</strong>',
      '      <span class="wa-widget-status">Admin online · balas cepat</span>',
      '    </div>',
      '  </div>',
      '  <p class="wa-widget-greet">Halo! Mau konsultasi souvenir apa hari ini? Pilih topik di bawah atau lanjut chat.</p>',
      '  <div class="wa-widget-chips">',
      '    <button type="button" class="wa-chip" data-msg="Halo, saya ingin tanya harga souvenir kantor">Tanya Harga</button>',
      '    <button type="button" class="wa-chip" data-msg="Halo, saya ingin konsultasi paket seminar kit">Seminar Kit</button>',
      '    <button type="button" class="wa-chip" data-msg="Halo, saya ingin pesan souvenir custom logo">Souvenir Custom</button>',
      '  </div>',
      '  <a href="' + waLink() + '" class="wa-widget-cta" target="_blank" rel="noopener">',
      '    <i class="bi bi-whatsapp"></i> Lanjut ke WhatsApp',
      '  </a>',
      '</div>',
      '<button type="button" class="wa-widget-trigger" aria-label="Buka chat SouvenirPro" aria-expanded="false">',
      '  <span class="wa-widget-trigger-logo"><img src="' + logoSrc + '" alt=""></span>',
      '  <span class="wa-widget-trigger-badge"><i class="bi bi-whatsapp"></i></span>',
      '  <span class="wa-widget-trigger-pulse"></span>',
      '</button>'
    ].join('');

    oldFloat.replaceWith(widget);

    var panel = widget.querySelector('.wa-widget-panel');
    var trigger = widget.querySelector('.wa-widget-trigger');
    var closeBtn = widget.querySelector('.wa-widget-panel-close');
    var cta = widget.querySelector('.wa-widget-cta');

    function togglePanel(forceOpen) {
      var open = typeof forceOpen === 'boolean' ? forceOpen : !widget.classList.contains('is-open');
      widget.classList.toggle('is-open', open);
      panel.setAttribute('aria-hidden', open ? 'false' : 'true');
      trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    trigger.addEventListener('click', function() { togglePanel(); });
    closeBtn.addEventListener('click', function() { togglePanel(false); });

    widget.querySelectorAll('.wa-chip').forEach(function(chip) {
      chip.addEventListener('click', function() {
        var msg = chip.getAttribute('data-msg');
        cta.href = waLink(msg);
        window.open(waLink(msg), '_blank', 'noopener');
        togglePanel(false);
      });
    });

    document.addEventListener('click', function(e) {
      if (!widget.classList.contains('is-open')) return;
      if (!widget.contains(e.target)) togglePanel(false);
    });
  }

  /**
   * Intercept contact form submissions that point to forms/contact.php
   * Prevent the POST to server (avoid 405 on static servers) and
   * open WhatsApp with a prefilled message containing the form fields.
   */
  function ensureWAPreviewModal() {
    if (window.__waPreviewModal) return window.__waPreviewModal;
    var modal = document.createElement('div');
    modal.id = 'wa-preview-modal';
    modal.className = 'wa-preview-modal';
    modal.setAttribute('aria-hidden', 'true');
    modal.innerHTML = [
      '<div class="wa-preview-backdrop" data-wa-close></div>',
      '<div class="wa-preview-dialog" role="dialog" aria-modal="true" aria-labelledby="wa-preview-title">',
      '  <button type="button" class="wa-preview-close" data-wa-close aria-label="Tutup">&times;</button>',
      '  <h3 id="wa-preview-title">Pratinjau Pesan WhatsApp</h3>',
      '  <div class="wa-preview-body"><pre id="wa-preview-text" class="wa-preview-text" style="white-space:pre-wrap;"></pre></div>',
      '  <div class="wa-preview-actions">',
      '    <button type="button" class="btn btn-outline wa-preview-edit">Ubah</button>',
      '    <button type="button" class="btn btn-primary wa-preview-open">Buka WhatsApp</button>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(modal);
    modal.querySelectorAll('[data-wa-close]').forEach(function(el) { el.addEventListener('click', function() { closeWAPreview(); }); });
    modal.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeWAPreview(); });
    window.__waPreviewModal = modal;
    return modal;
  }

  function openWAPreview(text, waUrl, form) {
    var modal = ensureWAPreviewModal();
    var textEl = modal.querySelector('#wa-preview-text');
    var openBtn = modal.querySelector('.wa-preview-open');
    var editBtn = modal.querySelector('.wa-preview-edit');
    textEl.textContent = text;
    modal.setAttribute('aria-hidden', 'false');
    modal.classList.add('is-open');

    // (re)bind actions
    openBtn.onclick = function() {
      try { window.open(waUrl, '_blank', 'noopener'); } catch (err) { window.location.href = waUrl; }
      try {
        var sent = form.querySelector('.sent-message');
        var loading = form.querySelector('.loading');
        if (loading) loading.style.display = 'none';
        if (sent) { sent.style.display = 'block'; sent.textContent = 'Mengalihkan ke WhatsApp...'; }
      } catch (er) {}
      closeWAPreview();
    };

    editBtn.onclick = function() {
      closeWAPreview();
      try { var msgEl = form.querySelector('[name="message"]'); if (msgEl) msgEl.focus(); } catch (e) {}
    };
  }

  function closeWAPreview() {
    var modal = window.__waPreviewModal;
    if (!modal) return;
    modal.setAttribute('aria-hidden', 'true');
    modal.classList.remove('is-open');
  }

  function wireContactFormsToWhatsApp() {
    document.querySelectorAll('form[action="forms/contact.php"]').forEach(function(form) {
      if (form.__waBound) return;
      form.__waBound = true;
      form.addEventListener('submit', function(e) {
        // prevent any other handlers (including php-email-form AJAX) from firing
        e.preventDefault();
        try { e.stopImmediatePropagation(); } catch (er) {}

        // let browser show required field UI if invalid
        if (typeof form.checkValidity === 'function' && !form.checkValidity()) {
          try { form.reportValidity(); } catch (er) {}
          return;
        }

        var get = function(name) {
          var el = form.querySelector('[name="' + name + '"]');
          return el ? el.value.trim() : '';
        };

        var name = get('name');
        var email = get('email');
        var phone = get('phone');
        var subject = get('subject');
        var message = get('message');

        var parts = [];
        parts.push('Permintaan Konsultasi — SouvenirPro');
        parts.push('');
        parts.push('Nama: ' + (name || '-'));
        if (email) parts.push('Email: ' + email);
        if (phone) parts.push('WA: ' + phone);
        if (subject) parts.push('Acara: ' + subject);
        parts.push('');
        parts.push('Pesan:');
        parts.push(message || '-');

        var text = parts.join('\n');
        var url = waLink(text);

        openWAPreview(text, url, form);

      }, { capture: true });
    });
  }

  /**
   * Generate Table of Contents for long-form articles
   */
  function generateArticleTOC() {
    document.querySelectorAll('.blog-article').forEach(function(article) {
      var container = article.closest('.container');
      if (!container) return;
      var toc = container.querySelector('.article-toc');
      if (!toc) return;
      var headings = article.querySelectorAll('h2, h3');
      if (!headings.length) { toc.style.display = 'none'; return; }

      var ul = document.createElement('ul');
      headings.forEach(function(h, idx) {
        if (!h.id) {
          var id = h.textContent.trim().toLowerCase().replace(/[^a-z0-9\s-]/gi, '').replace(/\s+/g, '-');
          h.id = id || ('heading-' + idx);
        }
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent.trim();
        if (h.tagName.toLowerCase() === 'h3') a.classList.add('toc-sub');
        li.appendChild(a);
        ul.appendChild(li);
      });

      toc.innerHTML = '<h5>Daftar Isi</h5>';
      toc.appendChild(ul);

      var tocLinks = toc.querySelectorAll('a');
      function highlightTOC() {
        var pos = window.scrollY + 140;
        var current = null;
        headings.forEach(function(h) { if (pos >= h.offsetTop) current = h; });
        tocLinks.forEach(function(link) { link.classList.remove('active'); });
        if (current) {
          var active = toc.querySelector('a[href="#' + current.id + '"]');
          if (active) active.classList.add('active');
        }
      }
      window.addEventListener('scroll', highlightTOC);
      highlightTOC();

      // Smooth scroll on TOC click
      toc.querySelectorAll('a').forEach(function(a) {
        a.addEventListener('click', function(e) {
          e.preventDefault();
          var target = document.querySelector(this.getAttribute('href'));
          if (!target) return;
          var offset = parseInt(getComputedStyle(target).scrollMarginTop) || 90;
          window.scrollTo({ top: target.offsetTop - offset, behavior: 'smooth' });
        });
      });
    });
  }

  function initGalleryLightbox() {
    const items = document.querySelectorAll('.gallery-item');
    if (!items.length) return;

    const modal = document.createElement('div');
    modal.className = 'gallery-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-label', 'Preview produk');
    modal.innerHTML = '<div class="gallery-modal-card"><button type="button" class="gallery-modal-close" aria-label="Tutup preview">×</button><img src="" alt="" /><div class="gallery-modal-caption"></div></div>';
    modal.style.display = 'none';
    document.body.appendChild(modal);

    const image = modal.querySelector('img');
    const caption = modal.querySelector('.gallery-modal-caption');
    const closeBtn = modal.querySelector('.gallery-modal-close');

    function openModal(item) {
      const img = item.querySelector('img');
      image.src = img.src;
      image.alt = img.alt;
      caption.textContent = item.querySelector('.item-label').textContent.trim();
      modal.style.display = 'flex';
      document.body.classList.add('overflow-hidden');
    }

    function closeModal() {
      modal.style.display = 'none';
      document.body.classList.remove('overflow-hidden');
    }

    items.forEach(function(item) {
      item.addEventListener('click', function() { openModal(item); });
    });

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', function(e) {
      if (e.target === modal) closeModal();
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && modal.style.display === 'flex') closeModal();
    });
  }

  function initSouvenirWidgets() {
    if (window.__souvenirWidgetsInit) return;
    window.__souvenirWidgetsInit = true;
    // Replace HEIC images early to avoid broken image placeholders
    try { replaceHEICFallbacks(); } catch (e) {}
    bindOrderModal();
    enhanceWhatsAppFloat();
      // Only add footer descriptive text for Layanan column and mount layanan article.
      try { normalizeLayananLinks(); } catch (e) { /* noop */ }
      try { loadLayananArticle(); } catch (e) { /* noop */ }
      try { wireContactFormsToWhatsApp(); } catch (e) { /* noop */ }
      try { injectBlogLinks(); } catch (e) { /* noop */ }
      try { generateArticleTOC(); } catch (e) { /* noop */ }
      try { initGalleryLightbox(); } catch (e) { /* noop */ }
      try { injectRelatedImageModal(); } catch (e) { /* noop */ }
      try { bindRelatedProductClicks(); } catch (e) { /* noop */ }
      // Ensure any subject inputs show 'Acara' as the placeholder
      try { document.querySelectorAll('input[name="subject"]').forEach(function(i){ i.placeholder = 'Acara'; }); } catch (e) { /* noop */ }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSouvenirWidgets);
  } else {
    initSouvenirWidgets();
  }

  /* Related products image modal: inject once and bind clicks */
  function injectRelatedImageModal() {
    if (document.getElementById('related-image-modal')) return;
    var wrap = document.createElement('div');
    wrap.id = 'related-image-modal';
    wrap.className = 'related-image-modal-backdrop';
    wrap.setAttribute('aria-hidden', 'true');
    wrap.innerHTML = '<div class="related-image-modal-dialog" role="dialog" aria-modal="true">'
      + '<div class="related-image-modal-header"><strong id="rim-title">Preview</strong><button class="related-image-modal-close" aria-label="Tutup">&times;</button></div>'
      + '<div class="related-image-modal-body"><img id="rim-img" src="" alt="Preview produk"><div id="rim-caption" style="margin-top:8px;color:var(--default-color)"></div></div>'
      + '</div>';
    document.body.appendChild(wrap);

    // close handlers
    wrap.addEventListener('click', function(e) {
      if (e.target === wrap || e.target.classList.contains('related-image-modal-close')) {
        wrap.classList.remove('is-open');
        wrap.setAttribute('aria-hidden', 'true');
        try { unlockBodyScroll(); } catch (er) {}
      }
    });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') { var w = document.getElementById('related-image-modal'); if (w && w.classList.contains('is-open')) { w.classList.remove('is-open'); w.setAttribute('aria-hidden','true'); try{ unlockBodyScroll(); }catch(er){} } } });
  }

  function bindRelatedProductClicks() {
    document.querySelectorAll('.related-thumb, .related-product-thumb').forEach(function(el) {
      if (el.__rimBound) return; el.__rimBound = true;
      el.addEventListener('click', function(e) {
        e.preventDefault();
        var src = el.getAttribute('data-image') || el.getAttribute('src') || el.querySelector && (el.querySelector('img') && el.querySelector('img').src);
        var title = el.getAttribute('data-title') || el.getAttribute('alt') || '';
        var caption = el.getAttribute('data-caption') || '';
        var wrap = document.getElementById('related-image-modal');
        if (!wrap) { injectRelatedImageModal(); wrap = document.getElementById('related-image-modal'); }
        var img = wrap.querySelector('#rim-img');
        var t = wrap.querySelector('#rim-title');
        var c = wrap.querySelector('#rim-caption');
        if (img) { img.src = src; img.alt = title || ''; }
        if (t) t.textContent = title || 'Preview';
        if (c) c.textContent = caption || '';
        wrap.classList.add('is-open');
        wrap.setAttribute('aria-hidden', 'false');
        try { lockBodyScroll(); } catch (er) {}
      });
    });
  }

})();