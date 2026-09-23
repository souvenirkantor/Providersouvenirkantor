import os

blog_html_path = r"c:\Provider Kantor\CorporateGifts ID\blog.html"
with open(blog_html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_card = """<div class="col-md-6" data-aos="fade-up" data-aos-delay="50">
<article class="blog-card">
<a href="blog/provider-souvenir-kantor-semarang.html"><img alt="Provider Souvenir Kantor untuk Kawasan Industri dan Perdagangan di Semarang" decoding="async" loading="lazy" src="images/Ilustrasi-koleksi-souvenir-korporat-premium-desain-elegan.webp"/></a>
<div class="blog-card-body">
<span class="article-tag">Provider Souvenir</span>
<h3><a href="blog/provider-souvenir-kantor-semarang.html">Provider Souvenir Kantor untuk Kawasan Industri dan Perdagangan di Semarang</a></h3>
<div class="blog-meta"><span><i class="bi bi-calendar3"></i> 08 Sep 2026</span><span><i class="bi bi-clock"></i> 5 menit</span></div>
<p>Provider souvenir kantor untuk kawasan industri dan perdagangan di Semarang, cocok untuk perusahaan manufaktur, kampus, dan pesanan skala besar.</p>
<a class="read-more" href="blog/provider-souvenir-kantor-semarang.html">Baca Artikel <i class="bi bi-arrow-right"></i></a>
</div>
</article>
</div>
"""

insert_index = content.find('<div class="row g-4" id="blog-grid">')
if insert_index != -1:
    insert_point = content.find('>', insert_index) + 1
    content = content[:insert_point] + "\n" + new_card + content[insert_point:]
    
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("blog.html updated")
else:
    print("Failed to find insert point in blog.html")

# Update sitemap.xml
sitemap_path = r"c:\Provider Kantor\CorporateGifts ID\sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

new_sitemap_entry = """  <url>
    <loc>https://providersouvenirkantor.web.id/blog/provider-souvenir-kantor-semarang.html</loc>
    <lastmod>2026-09-08</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sitemap_insert_index = sitemap_content.find('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
if sitemap_insert_index != -1:
    insert_point = sitemap_content.find('>', sitemap_insert_index) + 1
    sitemap_content = sitemap_content[:insert_point] + "\n" + new_sitemap_entry + sitemap_content[insert_point:]
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print("sitemap.xml updated")
else:
    print("Failed to find insert point in sitemap.xml")
