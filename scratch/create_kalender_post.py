import os
from bs4 import BeautifulSoup
import json

base_dir = r"c:\Provider Kantor\CorporateGifts ID"
template_path = os.path.join(base_dir, "blog", "pembuatan-speaker-bluetooth-custom-di-malang-raya.html")
new_file_path = os.path.join(base_dir, "blog", "kalender-meja-custom-souvenir-simpel-yang-bertahan-sepanjang-tahun.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

title_text = "Kalender Meja Custom, Souvenir Simpel yang Bertahan Sepanjang Tahun"
desc_text = "Kalender meja custom sebagai souvenir kantor tahan lama, dari jenis, desain, material, hingga waktu produksi yang perlu diperhatikan."
keywords_text = "kalender meja custom, souvenir kantor, kalender meja souvenir, cetak kalender meja, ide souvenir kantor, merchandise perusahaan"
image_path = "https://providersouvenirkantor.web.id/images/Ilustrasi-kalender-meja-custom-elegan-desain-minimalis.webp"
canonical_url = "https://providersouvenirkantor.web.id/blog/kalender-meja-custom-souvenir-simpel-yang-bertahan-sepanjang-tahun.html"
pub_date = "2026-09-04T08:00:00+07:00"
display_date = "04 Sep 2026"

# Update title
if soup.title:
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
    data['datePublished'] = pub_date
    data['dateModified'] = pub_date
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
        spans[1].append(f" {display_date}")

# Update cover image
cover_img_div = soup.find('div', class_='article-cover')
if cover_img_div:
    cover_img = cover_img_div.find('img')
    if cover_img:
        cover_img['src'] = "../images/Ilustrasi-kalender-meja-custom-elegan-desain-minimalis.webp"
        cover_img['alt'] = title_text

# Fix header links (href="/" to href="../index.html")
header_logo = soup.find('a', class_='logo')
if header_logo and header_logo.get('href') == '/':
    header_logo['href'] = '../index.html'

navmenu = soup.find('nav', id='navmenu')
if navmenu:
    beranda_link = navmenu.find('a', href='/')
    if beranda_link:
        beranda_link['href'] = '../index.html'

new_content_html = """
<p>Di antara berbagai pilihan souvenir kantor, kalender meja custom punya keunggulan yang tidak dimiliki banyak produk lain, yaitu masa pakai yang bisa bertahan hingga satu tahun penuh.</p>
<p>Selama periode itu, kalender akan terus berada di meja kerja penerima, memberikan exposure logo perusahaan secara konsisten setiap hari.</p>
<p>Berikut beberapa hal yang perlu diperhatikan agar kalender meja custom benar-benar memberikan dampak maksimal sebagai souvenir kantor.</p>

<h2 id="keunggulan-durasi">Keunggulan Durasi Pemakaian yang Panjang</h2>
<p>Berbeda dengan souvenir yang sifatnya sekali pakai atau hanya dibawa sesekali, kalender meja memiliki fungsi yang membuatnya terus dilihat penerima setiap hari kerja.</p>
<p>Posisinya yang biasa diletakkan di meja kerja membuat logo perusahaan terus terlihat, baik oleh pemiliknya sendiri maupun rekan kerja atau tamu yang berkunjung ke mejanya.</p>
<p>Durasi pemakaian yang panjang ini menjadikan kalender meja sebagai salah satu souvenir dengan rasio biaya terhadap exposure brand yang cukup efisien dibanding produk sekali pakai.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="ide-corporate-gift-premium-bisnis.html">Ide Corporate Gift Premium untuk Bisnis</a>
</div>

<h2 id="jenis-kalender">Jenis Kalender Meja yang Umum Digunakan</h2>
<p>Kalender meja berbentuk berdiri dengan sistem sobek per bulan menjadi pilihan paling umum karena tampilannya yang rapi dan mudah diganti setiap bulan.</p>
<p>Untuk kesan yang lebih modern, beberapa perusahaan memilih format kalender meja lipat berbahan akrilik atau kayu, yang bisa dipakai ulang dengan mengganti isian kertas setiap tahunnya.</p>
<p>Pemilihan jenis kalender sebaiknya disesuaikan dengan gaya visual brand perusahaan, agar tampilannya tetap konsisten dengan identitas yang ingin ditampilkan sepanjang tahun.</p>

<h2 id="desain-visual">Desain Visual yang Perlu Diperhatikan</h2>
<p>Desain kalender meja idealnya tidak hanya menampilkan logo, tetapi juga mempertimbangkan keterbacaan tanggal dan hari secara jelas.</p>
<p>Kombinasi warna yang terlalu ramai justru bisa mengganggu fungsi utama kalender sebagai alat bantu melihat tanggal.</p>
<p>Penambahan elemen visual seperti foto, kutipan, atau ilustrasi musiman membuat kalender tidak hanya fungsional, tetapi juga lebih menarik untuk dilihat sepanjang tahun.</p>
<p>Sentuhan kreatif ini mengubah kalender bulanan menjadi dekorasi yang menyenangkan dan tidak membosankan.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="notebook-custom-sebagai-souvenir-kantor-yang-tetap-relevan-di-era-digital.html">Notebook Custom sebagai Souvenir Kantor yang Tetap Relevan di Era Digital</a>
</div>

<h2 id="material-dasar">Material Dasar yang Memengaruhi Kualitas</h2>
<p>Kertas art paper dengan gramasi tebal umumnya menjadi pilihan standar karena hasil cetakannya tajam dan tidak mudah melengkung.</p>
<p>Untuk bagian dudukan kalender, bahan seperti akrilik atau kayu memberikan kesan lebih premium dan tahan lama dibanding dudukan kertas biasa yang mudah rusak setelah beberapa bulan pemakaian.</p>
<p>Memilih kombinasi material yang tepat antara halaman kalender dan dudukannya akan memengaruhi seberapa awet kalender ini bertahan hingga akhir tahun.</p>

<h2 id="waktu-produksi">Waktu Produksi yang Perlu Diperhitungkan</h2>
<p>Kalender meja biasanya dipesan menjelang akhir tahun, sehingga periode ini menjadi musim tersibuk bagi banyak provider souvenir kantor.</p>
<p>Memesan lebih awal, idealnya beberapa bulan sebelum pergantian tahun, dapat menghindari antrean produksi yang padat sekaligus memberikan waktu lebih leluasa untuk proses desain dan revisi.</p>

<p>Kalender meja custom menawarkan nilai jangka panjang yang jarang dimiliki souvenir kantor lain, karena tetap berada di meja kerja penerima sepanjang tahun.</p>
<p>Memilih jenis, desain, dan material yang tepat akan menentukan seberapa besar dampak branding yang dihasilkan dari souvenir sederhana namun tahan lama ini.</p>
<p>Konsultasikan kebutuhan Anda dengan provider souvenir kantor yang berpengalaman, terutama soal waktu produksi, agar kalender meja siap didistribusikan tepat waktu menjelang tahun baru.</p>
"""

new_toc_html = """
<a href="#keunggulan-durasi">Keunggulan Durasi Pemakaian yang Panjang</a>
<a href="#jenis-kalender">Jenis Kalender Meja yang Umum Digunakan</a>
<a href="#desain-visual">Desain Visual yang Perlu Diperhatikan</a>
<a href="#material-dasar">Material Dasar yang Memengaruhi Kualitas</a>
<a href="#waktu-produksi">Waktu Produksi yang Perlu Diperhitungkan</a>
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

print("Created kalender-meja-custom-souvenir-simpel-yang-bertahan-sepanjang-tahun.html")
