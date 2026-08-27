import os
from bs4 import BeautifulSoup
import json

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
template_path = os.path.join(base_dir, "blog", "speaker-bluetooth-custom-cetak-uv-logo-perusahaan.html")
new_file_path = os.path.join(base_dir, "blog", "10-ide-souvenir-kantor-unik-brand.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

title_text = "10 Ide Souvenir Kantor Unik yang Bikin Klien dan Karyawan Selalu Ingat Brand Anda"
desc_text = "Souvenir kantor unik dan fungsional seperti tumbler custom, seminar kit, diffuser, notebook premium, hingga eco-friendly set yang bikin brand selalu diingat."
keywords_text = "ide souvenir kantor unik, souvenir kantor premium, souvenir perusahaan fungsional, rekomendasi souvenir kantor, merchandise perusahaan unik"
image_path = "https://providersouvenirkantor.web.id/images/Ilustrasi-kumpulan-ide-souvenir-kantor-premium-elegan.webp"
canonical_url = "https://providersouvenirkantor.web.id/blog/10-ide-souvenir-kantor-unik-brand.html"

# Update title
soup.title.string = title_text + " - CorporateGifts ID"

# Update meta canonical
canonical = soup.find('link', rel='canonical')
if canonical:
    canonical['href'] = canonical_url

# Update meta description
meta_desc = soup.find('meta', {'name': 'description'})
if meta_desc:
    meta_desc['content'] = desc_text

# Update meta keywords
meta_keywords = soup.find('meta', {'name': 'keywords'})
if meta_keywords:
    meta_keywords['content'] = keywords_text

# Update og tags
og_url = soup.find('meta', {'property': 'og:url'})
if og_url: og_url['content'] = canonical_url

og_title = soup.find('meta', {'property': 'og:title'})
if og_title: og_title['content'] = title_text

og_desc = soup.find('meta', {'property': 'og:description'})
if og_desc: og_desc['content'] = desc_text

og_image = soup.find('meta', {'property': 'og:image'})
if og_image: og_image['content'] = image_path

twitter_url = soup.find('meta', {'property': 'twitter:url'})
if twitter_url: twitter_url['content'] = canonical_url

twitter_title = soup.find('meta', {'property': 'twitter:title'})
if twitter_title: twitter_title['content'] = title_text

twitter_desc = soup.find('meta', {'property': 'twitter:description'})
if twitter_desc: twitter_desc['content'] = desc_text

twitter_image = soup.find('meta', {'property': 'twitter:image'})
if twitter_image: twitter_image['content'] = image_path

# Update schema
schema_script = soup.find('script', type='application/ld+json')
if schema_script:
    data = json.loads(schema_script.string)
    data['headline'] = title_text
    data['image'] = [image_path]
    data['datePublished'] = "2026-08-27T08:00:00+07:00"
    data['dateModified'] = "2026-08-27T08:00:00+07:00"
    data['description'] = desc_text
    schema_script.string = json.dumps(data, indent=4)

# Update h1 in article-header
article_header_h1 = soup.select_one('.article-header h1')
if article_header_h1:
    article_header_h1.string = title_text

# Update date in blog-meta
blog_meta = soup.select_one('.article-header .blog-meta')
if blog_meta:
    spans = blog_meta.find_all('span')
    if len(spans) > 1:
        spans[1].clear()
        i_icon = soup.new_tag("i")
        i_icon['class'] = "bi bi-calendar3"
        spans[1].append(i_icon)
        spans[1].append(" 27 Ags 2026")

# Update cover image
cover_img_div = soup.find('div', class_='article-cover')
if cover_img_div:
    cover_img = cover_img_div.find('img')
    if cover_img:
        cover_img['src'] = "../images/Ilustrasi-kumpulan-ide-souvenir-kantor-premium-elegan.webp"
        cover_img['alt'] = title_text

new_content_html = """
<p>Souvenir kantor yang itu-itu saja seperti pulpen atau gantungan kunci polos memang praktis, tapi sering kali langsung terlupakan begitu diterima.</p>
<p>Padahal, souvenir yang tepat bisa menjadi media branding jangka panjang yang terus dipakai dan dilihat penerima setiap hari.</p>
<p>Berikut beberapa ide souvenir kantor yang bisa dipertimbangkan agar kesan yang ditinggalkan lebih berbeda dan berkesan.</p>

<h2 id="ide-1">1. Tumbler Custom dengan Desain Minimalis</h2>
<p>Tumbler masih menjadi salah satu pilihan favorit karena fungsinya yang dipakai setiap hari.</p>
<p>Pilih desain yang minimalis dengan warna solid dan logo yang dicetak halus, bukan mencolok berlebihan, agar tetap terlihat elegan saat dibawa ke mana pun.</p>

<h2 id="ide-2">2. Seminar Kit Lengkap</h2>
<p>Untuk acara pelatihan atau workshop, seminar kit berisi tote bag, notebook, pulpen, dan ID card holder dalam satu paket akan terasa lebih rapi dan profesional dibanding barang lepasan.</p>
<p>Peserta juga cenderung lebih menghargai paket lengkap dibanding satu item tunggal.</p>

<h2 id="ide-3">3. Diffuser atau Aromaterapi Mini</h2>
<p>Souvenir jenis ini cocok untuk klien atau tamu penting karena kesannya lebih personal dan mewah.</p>
<p>Diffuser mini dengan kemasan elegan sering dijadikan pajangan meja kerja, sehingga logo perusahaan Anda akan terus terlihat setiap hari.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="ide-corporate-gift-premium-bisnis.html">Ide Corporate Gift Premium untuk Bisnis</a>
</div>

<h2 id="ide-4">4. Notebook dengan Sampul Kulit Sintetis</h2>
<p>Notebook premium dengan sampul kulit sintetis memberi kesan profesional dan lebih awet dibanding notebook kertas biasa.</p>
<p>Cocok diberikan kepada klien korporat atau mitra bisnis dalam pertemuan formal.</p>

<h2 id="ide-5">5. Charger Portable atau Kabel Data Custom</h2>
<p>Di era serba digital, souvenir yang berhubungan dengan kebutuhan gadget sehari-hari seperti power bank atau kabel data custom logo cenderung lebih sering dipakai dibanding souvenir dekoratif semata.</p>

<h2 id="ide-6">6. Kalender Meja Custom Desain</h2>
<p>Meski terlihat sederhana, kalender meja dengan desain custom yang menarik bisa bertahan di meja kerja penerima selama satu tahun penuh, memberikan exposure brand yang jauh lebih lama dibanding souvenir sekali pakai.</p>

<h2 id="ide-7">7. Tas Kanvas atau Tote Bag Custom</h2>
<p>Tote bag custom logo praktis digunakan sehari-hari, baik untuk membawa laptop, dokumen, maupun keperluan pribadi.</p>
<p>Selain fungsional, tote bag juga menjadi media promosi berjalan setiap kali dipakai bepergian.</p>

<h2 id="ide-8">8. Set Alat Tulis Premium</h2>
<p>Kombinasi pulpen, pensil mekanik, dan penghapus dalam satu kemasan eksklusif memberikan kesan lebih istimewa dibanding alat tulis satuan biasa. Cocok untuk souvenir kantor kategori premium bagi klien VIP.</p>

<h2 id="ide-9">9. Payung Custom Logo</h2>
<p>Payung lipat dengan cetakan logo perusahaan menjadi souvenir yang jarang diberikan namun sangat fungsional, terutama di negara dengan curah hujan tinggi seperti Indonesia. Barang ini juga cenderung disimpan dan dipakai berulang kali.</p>

<h2 id="ide-10">10. Eco-Friendly Souvenir Set</h2>
<p>Tren souvenir ramah lingkungan seperti sedotan stainless, sikat gigi bambu, atau tas belanja lipat dari bahan daur ulang semakin diminati karena mencerminkan citra perusahaan yang peduli lingkungan, sekaligus relevan dengan isu keberlanjutan yang sedang tren.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="jenis-souvenir-ramah-lingkungan.html">Jenis Souvenir Ramah Lingkungan</a>
</div>

<p>Memilih souvenir kantor yang tepat sebaiknya tidak hanya berdasarkan harga termurah, tetapi juga mempertimbangkan seberapa sering barang tersebut akan dipakai oleh penerima.</p>
<p>Semakin sering souvenir digunakan dalam aktivitas sehari-hari, semakin besar pula exposure brand perusahaan Anda dalam jangka panjang.</p>
<p>Sebelum menentukan pilihan, ada baiknya berkonsultasi dengan provider souvenir kantor yang berpengalaman agar bisa mendapatkan rekomendasi produk yang sesuai dengan budget dan tujuan acara Anda.</p>
"""

new_toc_html = """
<a href="#ide-1">1. Tumbler Custom dengan Desain Minimalis</a>
<a href="#ide-2">2. Seminar Kit Lengkap</a>
<a href="#ide-3">3. Diffuser atau Aromaterapi Mini</a>
<a href="#ide-4">4. Notebook dengan Sampul Kulit Sintetis</a>
<a href="#ide-5">5. Charger Portable atau Kabel Data Custom</a>
<a href="#ide-6">6. Kalender Meja Custom Desain</a>
<a href="#ide-7">7. Tas Kanvas atau Tote Bag Custom</a>
<a href="#ide-8">8. Set Alat Tulis Premium</a>
<a href="#ide-9">9. Payung Custom Logo</a>
<a href="#ide-10">10. Eco-Friendly Souvenir Set</a>
"""

article_body = soup.find('article', class_='article-body')
if article_body:
    article_body.clear()
    article_body.append(BeautifulSoup(new_content_html, 'html.parser'))

mobile_toc = soup.find('div', id='mobile-toc-body')
if mobile_toc:
    nav = mobile_toc.find('nav')
    if nav:
        nav.clear()
        nav.append(BeautifulSoup(new_toc_html, 'html.parser'))

sidebar_toc_div = soup.find('div', class_='blog-sidebar')
if sidebar_toc_div:
    nav = sidebar_toc_div.find('nav', class_='toc-list')
    if nav:
        nav.clear()
        nav.append(BeautifulSoup(new_toc_html, 'html.parser'))

with open(new_file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify(formatter="html")))

print("Created 10-ide-souvenir-kantor-unik-brand.html")
