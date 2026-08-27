import os

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
js_path = os.path.join(base_dir, "assets", "js", "main.js")
css_path = os.path.join(base_dir, "assets", "css", "main.css")

# 1. Update main.js
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

target_str = """      <li class="dropdown"><a href="${relPrefix}layanan.html"${isServicePage ? ' class="active"' : ''}><span>Layanan</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="${relPrefix}souvenir-kantor.html">Souvenir Kantor</a></li>
          <li><a href="${relPrefix}souvenir-custom.html">Souvenir Custom</a></li>
          <li><a href="${relPrefix}merchandise-perusahaan.html">Merchandise Perusahaan</a></li>
          <li><a href="${relPrefix}seminar-kit.html">Seminar Kit</a></li>
        </ul>
      </li>"""

replacement_str = """      <li class="dropdown"><a href="${relPrefix}layanan.html"${isServicePage ? ' class="active"' : ''}><span>Layanan</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
        <ul>
          <li><a href="${relPrefix}souvenir-kantor.html">Souvenir Kantor</a></li>
          <li><a href="${relPrefix}souvenir-custom.html">Souvenir Custom</a></li>
          <li><a href="${relPrefix}merchandise-perusahaan.html">Merchandise Perusahaan</a></li>
          <li><a href="${relPrefix}seminar-kit.html">Seminar Kit</a></li>
        </ul>
      </li>
      <li class="d-xl-none text-center" style="margin-top: 15px; padding: 0 15px;"><a class="btn-getstarted" href="https://wa.me/6288989643555?text=Halo,%20saya%20ingin%20pesan%20souvenir" style="display: block; width: 100%;">Pesan Sekarang</a></li>"""

if target_str in js_content:
    js_content = js_content.replace(target_str, replacement_str)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Successfully updated main.js")
else:
    print("Target string not found in main.js!")

# 2. Update main.css
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_addition = """

/* --- Fix Mobile Header Button --- */
@media (max-width: 1199px) {
  .header-container > .btn-getstarted {
    display: none !important;
  }
}
"""

if "Fix Mobile Header Button" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Successfully updated main.css")
else:
    print("CSS fix already exists.")
