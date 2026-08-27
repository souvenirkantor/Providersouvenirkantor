import os
from bs4 import BeautifulSoup
import re

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
template_path = os.path.join(base_dir, "blog", "speaker-bluetooth-custom-cetak-uv-logo-perusahaan.html")
new_file_path = os.path.join(base_dir, "blog", "pembuatan-speaker-bluetooth-custom-di-malang-raya.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Update title
soup.title.string = "Pembuatan Speaker Bluetooth Custom di Malang Raya - CorporateGifts ID"

# Update meta canonical
canonical = soup.find('link', rel='canonical')
canonical['href'] = "https://providersouvenirkantor.web.id/blog/pembuatan-speaker-bluetooth-custom-di-malang-raya.html"

# Update meta description
meta_desc = soup.find('meta', {'name': 'description'})
meta_desc['content'] = "Pembuatan speaker bluetooth custom di Malang Raya mencakup Kota Malang, Kota Batu, dan Kabupaten Malang dengan kemudahan komunikasi dan pengecekan sampel."

# Update meta keywords
meta_keywords = soup.find('meta', {'name': 'keywords'})
meta_keywords['content'] = "pembuatan speaker bluetooth custom malang, speaker bluetooth custom malang raya, jasa pembuatan speaker bluetooth malang, custom logo speaker malang"

# Update og tags
og_url = soup.find('meta', {'property': 'og:url'})
og_url['content'] = canonical['href']

og_title = soup.find('meta', {'property': 'og:title'})
og_title['content'] = "Pembuatan Speaker Bluetooth Custom di Malang Raya"

og_desc = soup.find('meta', {'property': 'og:description'})
og_desc['content'] = meta_desc['content']

og_image = soup.find('meta', {'property': 'og:image'})
og_image['content'] = "https://providersouvenirkantor.web.id/images/Ilustrasi-proses-cetak-UV-logo-speaker-custom.webp"

twitter_url = soup.find('meta', {'property': 'twitter:url'})
twitter_url['content'] = canonical['href']

twitter_title = soup.find('meta', {'property': 'twitter:title'})
twitter_title['content'] = og_title['content']

twitter_desc = soup.find('meta', {'property': 'twitter:description'})
twitter_desc['content'] = meta_desc['content']

twitter_image = soup.find('meta', {'property': 'twitter:image'})
twitter_image['content'] = og_image['content']

# Update script schema
import json
schema_script = soup.find('script', type='application/ld+json')
if schema_script:
    data = json.loads(schema_script.string)
    data['headline'] = og_title['content']
    data['image'] = [og_image['content']]
    data['datePublished'] = "2026-08-27T08:00:00+07:00"
    data['dateModified'] = "2026-08-27T08:00:00+07:00"
    data['description'] = meta_desc['content']
    schema_script.string = json.dumps(data, indent=4)

# Update h1 and meta info
h1 = soup.find('h1')
h1.string = "Pembuatan Speaker Bluetooth Custom di Malang Raya"

blog_meta = soup.find('div', class_='blog-meta')
spans = blog_meta.find_all('span')
# Update date
if len(spans) > 1:
    spans[1].string = ""
    i_icon = soup.new_tag("i")
    i_icon['class'] = "bi bi-calendar3"
    spans[1].append(i_icon)
    spans[1].append(" 27 Ags 2026")

# Update cover image
cover_img = soup.find('div', class_='article-cover').find('img')
cover_img['src'] = "../images/Ilustrasi-proses-cetak-UV-logo-speaker-custom.webp"
cover_img['alt'] = og_title['content']

# Update content
article_body = soup.find('article', class_='article-body')

new_content_html = """
<p>Pembuatan speaker bluetooth custom di Malang Raya mencakup wilayah Kota Malang, Kota Batu, dan Kabupaten Malang, dengan berbagai penyedia jasa lokal yang menawarkan layanan custom logo dan desain speaker sesuai kebutuhan pemesan.</p>

<ul>
  <li>Malang Raya mencakup Kota Malang, Kota Batu, dan Kabupaten Malang.</li>
  <li>Penyedia jasa lokal umumnya menawarkan konsultasi desain langsung.</li>
  <li>Memesan dari jasa lokal dapat mempermudah komunikasi dan pengecekan sampel.</li>
  <li>Biaya jasa dapat bervariasi tergantung skala usaha dan kapasitas produksi.</li>
  <li>Penting mengecek portofolio dan ulasan sebelum memilih penyedia jasa.</li>
</ul>

<h2 id="cakupan-wilayah">Apa Cakupan Wilayah Malang Raya untuk Layanan Ini?</h2>
<p>Cakupan wilayah Malang Raya untuk layanan pembuatan speaker bluetooth custom umumnya meliputi Kota Malang sebagai pusat kota, Kota Batu yang dikenal sebagai kawasan wisata, dan Kabupaten Malang yang memiliki area lebih luas di sekitarnya.</p>
<p>Ketiga wilayah ini sering disebut sebagai satu kesatuan kawasan karena kedekatan geografis dan mobilitas penduduk yang tinggi antar wilayah.</p>
<p>Banyak penyedia jasa custom merchandise di Kota Malang juga melayani pemesan dari Kota Batu maupun Kabupaten Malang tanpa kendala jarak yang signifikan.</p>
<p>Bagi pemesan yang berada di wilayah Malang Raya, memilih penyedia jasa lokal dapat mempermudah proses konsultasi, terutama jika pemesan ingin melihat langsung sampel produk sebelum melakukan pemesanan dalam jumlah besar.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="speaker-bluetooth-custom-cetak-uv-logo-perusahaan.html">Speaker Bluetooth Custom Cetak UV Logo Perusahaan</a>
</div>

<h2 id="cara-memilih-jasa">Bagaimana Cara Memilih Jasa Pembuatan Speaker Bluetooth Custom di Malang Raya?</h2>
<p>Cara memilih jasa pembuatan speaker bluetooth custom di Malang Raya adalah dengan memeriksa portofolio hasil kerja, menanyakan kapasitas produksi, dan memastikan adanya opsi konsultasi langsung sebelum produksi massal.</p>
<p>Portofolio menjadi acuan utama untuk menilai konsistensi kualitas hasil custom logo maupun desain speaker dari penyedia jasa tersebut.</p>
<p>Kapasitas produksi juga perlu ditanyakan, terutama bagi pemesan dengan kebutuhan dalam jumlah besar dan tenggat waktu tertentu.</p>
<p>Opsi konsultasi langsung, baik secara tatap muka maupun daring, memberikan keuntungan tambahan karena pemesan dapat mendiskusikan detail desain secara lebih rinci dan menyesuaikan kebutuhan sebelum proses produksi dimulai.</p>

<h2 id="keuntungan-memesan">Apa Keuntungan Memesan dari Penyedia Jasa Lokal Malang Raya?</h2>
<p>Keuntungan memesan dari penyedia jasa lokal Malang Raya meliputi kemudahan komunikasi, potensi pengecekan sampel secara langsung, dan dukungan terhadap pelaku usaha di wilayah setempat.</p>
<p>Komunikasi dengan penyedia jasa lokal umumnya lebih mudah dilakukan karena perbedaan zona waktu dan jarak yang minim, sehingga proses revisi desain dapat berlangsung lebih cepat.</p>
<p>Selain itu, pemesan berkesempatan untuk melihat langsung sampel produk sebelum memutuskan pemesanan dalam jumlah besar, yang dapat mengurangi risiko ketidaksesuaian hasil akhir.</p>
<p>Memesan dari penyedia jasa lokal juga turut mendukung pertumbuhan ekonomi kreatif di wilayah Malang Raya, khususnya sektor usaha kecil dan menengah yang bergerak di bidang custom merchandise.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="rekomendasi-speaker-bluetooth-custom-portable.html">Rekomendasi Speaker Bluetooth Custom Portable</a>
</div>

<h2 id="hal-perlu-dikonfirmasi">Apa yang Perlu Dikonfirmasi Sebelum Memesan dari Jasa Lokal?</h2>
<p>Hal yang perlu dikonfirmasi sebelum memesan dari jasa lokal di Malang Raya meliputi estimasi waktu produksi, metode pembayaran, kebijakan revisi desain, dan opsi pengiriman ke luar wilayah jika diperlukan.</p>
<p>Estimasi waktu produksi penting dikonfirmasi di awal agar sesuai dengan tenggat kebutuhan acara atau distribusi merchandise.</p>
<p>Metode pembayaran dan kebijakan revisi desain juga perlu dipahami dengan jelas untuk menghindari kesalahpahaman selama proses kerja sama berlangsung.</p>
<p>Bagi pemesan yang berada di luar wilayah Malang Raya namun tertarik menggunakan jasa lokal ini, sebaiknya turut menanyakan opsi pengiriman produk agar proses distribusi tetap berjalan lancar.</p>

<p>Pembuatan speaker bluetooth custom di Malang Raya menawarkan kemudahan komunikasi dan pengecekan kualitas secara langsung bagi pemesan di wilayah Kota Malang, Kota Batu, dan Kabupaten Malang.</p>
<p>Pastikan memeriksa portofolio, kapasitas produksi, dan kebijakan kerja sama sebelum memutuskan penyedia jasa.</p>
"""

article_body.clear()
new_content_soup = BeautifulSoup(new_content_html, 'html.parser')
for el in new_content_soup:
    article_body.append(el)

# Update TOCs
new_toc_html = """
<a href="#cakupan-wilayah">Apa Cakupan Wilayah Malang Raya untuk Layanan Ini?</a>
<a href="#cara-memilih-jasa">Bagaimana Cara Memilih Jasa Pembuatan Speaker Bluetooth Custom di Malang Raya?</a>
<a href="#keuntungan-memesan">Apa Keuntungan Memesan dari Penyedia Jasa Lokal Malang Raya?</a>
<a href="#hal-perlu-dikonfirmasi">Apa yang Perlu Dikonfirmasi Sebelum Memesan dari Jasa Lokal?</a>
"""
new_toc_soup = BeautifulSoup(new_toc_html, 'html.parser')

mobile_toc = soup.find('div', id='mobile-toc-body').find('nav')
mobile_toc.clear()
for el in BeautifulSoup(new_toc_html, 'html.parser'):
    mobile_toc.append(el)

sidebar_toc = soup.find('div', class_='blog-sidebar').find('nav', class_='toc-list')
sidebar_toc.clear()
for el in BeautifulSoup(new_toc_html, 'html.parser'):
    sidebar_toc.append(el)

with open(new_file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Created new file:", new_file_path)
