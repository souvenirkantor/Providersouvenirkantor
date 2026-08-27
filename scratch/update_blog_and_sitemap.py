import os
from bs4 import BeautifulSoup

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
blog_path = os.path.join(base_dir, "blog.html")
sitemap_path = os.path.join(base_dir, "sitemap.xml")

# Update blog.html
with open(blog_path, 'r', encoding='utf-8') as f:
    blog_html = f.read()

soup_blog = BeautifulSoup(blog_html, 'html.parser')
blog_grid = soup_blog.find('div', id='blog-grid')

new_card_html = """
<div class="col-md-6" data-aos="fade-up" data-aos-delay="50">
  <article class="blog-card">
    <a href="blog/pembuatan-speaker-bluetooth-custom-di-malang-raya.html"><img src="images/Ilustrasi-proses-cetak-UV-logo-speaker-custom.webp" alt="Pembuatan Speaker Bluetooth Custom di Malang Raya" loading="lazy" decoding="async"></a>
    <div class="blog-card-body">
      <span class="article-tag">Layanan Custom</span>
      <h3><a href="blog/pembuatan-speaker-bluetooth-custom-di-malang-raya.html">Pembuatan Speaker Bluetooth Custom di Malang Raya</a></h3>
      <div class="blog-meta"><span><i class="bi bi-calendar3"></i> 27 Ags 2026</span><span><i class="bi bi-clock"></i> 5 menit</span></div>
      <p>Pembuatan speaker bluetooth custom di Malang Raya mencakup Kota Malang, Kota Batu, dan Kabupaten Malang dengan kemudahan komunikasi dan pengecekan sampel.</p>
      <a href="blog/pembuatan-speaker-bluetooth-custom-di-malang-raya.html" class="read-more">Baca Artikel <i class="bi bi-arrow-right"></i></a>
    </div>
  </article>
</div>
"""
new_card_soup = BeautifulSoup(new_card_html, 'html.parser')

if blog_grid:
    blog_grid.insert(0, new_card_soup.div)
    with open(blog_path, 'w', encoding='utf-8') as f:
        # Note: writing soup might alter format slightly, better to use replace or just string find/replace if bs4 messes it up. Let's see.
        f.write(str(soup_blog))
    print("Updated blog.html")
else:
    print("blog-grid not found!")

# Update sitemap.xml
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_xml = f.read()

# using simple string insertion for sitemap to avoid bs4 xml formatting issues
insert_pos = sitemap_xml.find("</urlset>")
if insert_pos != -1:
    new_url_entry = """  <url>
    <loc>https://providersouvenirkantor.web.id/blog/pembuatan-speaker-bluetooth-custom-di-malang-raya.html</loc>
    <lastmod>2026-08-27T08:00:00+07:00</lastmod>
    <priority>0.7</priority>
  </url>\n"""
    sitemap_xml = sitemap_xml[:insert_pos] + new_url_entry + sitemap_xml[insert_pos:]
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)
    print("Updated sitemap.xml")
else:
    print("</urlset> not found in sitemap!")
