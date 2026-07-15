/**
 * SouvenirPro — modal pesan & widget WhatsApp bermerek
 */
(function() {
  'use strict';

  var WA_NUMBER = '6288989643555';
  var DEFAULT_MSG = 'Halo, saya ingin konsultasi souvenir dari website SouvenirPro';

  function waLink(message) {
    return 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(message || DEFAULT_MSG);
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
      '    <p>Pilih langkah yang paling sesuai. Tidak semua tombol harus langsung ke WhatsApp.</p>',
      '  </div>',
      '  <div class="order-modal-grid">',
      '    <a href="katalog.html" class="order-modal-card">',
      '      <span class="order-modal-icon"><i class="bi bi-grid"></i></span>',
      '      <strong>Lihat Katalog</strong>',
      '      <small>Jelajahi produk souvenir &amp; merchandise</small>',
      '    </a>',
      '    <a href="harga.html" class="order-modal-card">',
      '      <span class="order-modal-icon"><i class="bi bi-tags"></i></span>',
      '      <strong>Cek Paket Harga</strong>',
      '      <small>Estimasi budget sebelum pesan</small>',
      '    </a>',
      '    <a href="layanan.html" class="order-modal-card">',
      '      <span class="order-modal-icon"><i class="bi bi-briefcase"></i></span>',
      '      <strong>Pelajari Layanan</strong>',
      '      <small>Souvenir kantor, custom &amp; seminar kit</small>',
      '    </a>',
      '    <a href="kontak.html" class="order-modal-card">',
      '      <span class="order-modal-icon"><i class="bi bi-envelope-paper"></i></span>',
      '      <strong>Kirim Brief</strong>',
      '      <small>Form kontak untuk kebutuhan detail</small>',
      '    </a>',
      '  </div>',
      '  <div class="order-modal-footer">',
      '    <p>Butuh jawaban cepat? Chat admin kami di WhatsApp.</p>',
      '    <a href="' + waLink() + '" class="order-modal-wa-btn" target="_blank" rel="noopener">',
      '      <i class="bi bi-whatsapp"></i> Chat WhatsApp',
      '    </a>',
      '  </div>',
      '</div>'
    ].join('');

    document.body.appendChild(modal);
  }

  function openOrderModal() {
    var modal = document.getElementById('order-modal');
    if (!modal) return;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('order-modal-open');
  }

  function closeOrderModal() {
    var modal = document.getElementById('order-modal');
    if (!modal) return;
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('order-modal-open');
  }

  function bindOrderModal() {
    injectOrderModal();

    document.addEventListener('click', function(e) {
      var trigger = e.target.closest('.order-modal-trigger, .btn-getstarted[href*="wa.me"], .souvenir-bottom-cta .btn-primary[href*="wa.me"]');
      if (trigger && (trigger.classList.contains('btn-getstarted') || trigger.classList.contains('order-modal-trigger') || trigger.closest('.souvenir-bottom-cta'))) {
        e.preventDefault();
        openOrderModal();
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

  window.addEventListener('load', function() {
    bindOrderModal();
    enhanceWhatsAppFloat();
  });
})();
