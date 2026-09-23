import os
from bs4 import BeautifulSoup
import json

base_dir = r"c:\Provider Kantor\CorporateGifts ID"
template_path = os.path.join(base_dir, "blog", "pembuatan-speaker-bluetooth-custom-di-malang-raya.html")
new_file_path = os.path.join(base_dir, "blog", "payung-custom-souvenir-kantor-yang-jarang-dilirik-tapi-selalu-terpakai.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

title_text = "Payung Custom, Souvenir Kantor yang Jarang Dilirik tapi Selalu Terpakai"
desc_text = "Payung custom sebagai souvenir kantor, dari jenis, material tahan lama, hingga teknik cetak logo yang tepat pada permukaan kain payung."
keywords_text = "payung custom, souvenir kantor, payung souvenir, cetak logo payung, ide souvenir"
image_path = "https://providersouvenirkantor.web.id/images/Ilustrasi-payung-custom-elegan-logo-perusahaan-minimalis.webp"
canonical_url = "https://providersouvenirkantor.web.id/blog/payung-custom-souvenir-kantor-yang-jarang-dilirik-tapi-selalu-terpakai.html"
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
        cover_img['src'] = "../images/Ilustrasi-payung-custom-elegan-logo-perusahaan-minimalis.webp"
        cover_img['alt'] = title_text

new_content_html = """
<p>Saat membahas ide souvenir kantor, payung custom sering luput dari daftar pilihan utama.</p>
<p>Padahal, di negara dengan curah hujan tinggi seperti Indonesia, payung termasuk barang yang benar-benar dibutuhkan dan disimpan untuk dipakai berulang kali, bukan sekadar pelengkap souvenir semata.</p>
<p>Berikut beberapa hal yang perlu dipertimbangkan sebelum menjadikan payung custom sebagai pilihan souvenir kantor perusahaan Anda.</p>

<h2 id="nilai-fungsional">Nilai Fungsional yang Jarang Tertandingi Souvenir Lain</h2>
<p>Berbeda dengan sebagian besar souvenir yang sifatnya pelengkap, payung memiliki fungsi yang sangat konkret dan dibutuhkan hampir sepanjang tahun.</p>
<p>Penerima cenderung menyimpan payung di dalam tas atau mobil untuk berjaga-jaga, sehingga peluang barang ini benar-benar dipakai jauh lebih tinggi dibanding souvenir dekoratif.</p>
<p>Karena sifatnya yang jarang diberikan sebagai souvenir, payung custom juga cenderung terasa lebih istimewa dan diingat penerimanya dibanding produk umum seperti pulpen atau notebook.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="notebook-custom-sebagai-souvenir-kantor-yang-tetap-relevan-di-era-digital.html">Notebook Custom sebagai Souvenir Kantor yang Tetap Relevan di Era Digital</a>
</div>

<h2 id="jenis-payung">Jenis Payung yang Umum Dipilih untuk Souvenir Korporat</h2>
<p>Payung lipat menjadi pilihan paling populer karena ukurannya yang ringkas dan mudah dibawa dalam tas kerja sehari-hari.</p>
<p>Untuk kesan yang lebih premium, beberapa perusahaan memilih payung lipat otomatis yang bisa terbuka dan tertutup hanya dengan satu tombol, memberikan kenyamanan tambahan bagi penerima.</p>
<p>Sementara itu, payung golf berukuran besar lebih jarang dipilih sebagai souvenir massal karena ukurannya yang kurang praktis, namun tetap relevan untuk kategori souvenir eksklusif bagi klien atau tamu VIP dalam acara tertentu.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="tumbler-custom-sebagai-pilihan-souvenir-kantor-paling-diminati.html">Tumbler Custom sebagai Pilihan Souvenir Kantor Paling Diminati</a>
</div>

<h2 id="material-daya-tahan">Material yang Memengaruhi Daya Tahan Payung</h2>
<p>Kain payung berbahan pongee dengan lapisan anti air menjadi standar umum karena daya tahannya yang baik terhadap cuaca sekaligus ringan saat dibawa.</p>
<p>Rangka payung berbahan fiberglass juga lebih disarankan dibanding rangka besi biasa, karena lebih tahan terhadap tekanan angin tanpa mudah patah.</p>
<p>Memilih material yang tepat akan memengaruhi seberapa lama payung custom ini bisa terus dipakai, yang pada akhirnya berdampak pada seberapa lama exposure logo perusahaan bertahan di tangan penerimanya.</p>

<h2 id="area-teknik-cetak">Area dan Teknik Cetak Logo pada Kain Payung</h2>
<p>Logo pada payung biasanya dicetak menggunakan teknik sablon pada salah satu sisi kain, atau pada bagian sarung pembungkus payung untuk desain yang lebih terlihat saat payung dalam keadaan tertutup.</p>
<p>Pemilihan warna kain yang kontras dengan warna logo perlu diperhatikan agar hasil cetakan tetap terlihat jelas.</p>
<p>Untuk logo dengan detail rumit, sebaiknya disederhanakan terlebih dahulu, mengingat permukaan kain payung yang melengkung membuat detail kecil cenderung kurang presisi saat dicetak dibanding permukaan datar seperti notebook atau tote bag.</p>

<p>Payung custom menawarkan nilai fungsional yang jarang ditemukan pada souvenir kantor lain, sekaligus memberikan kesan berbeda karena jarang dipilih sebagai souvenir umum.</p>
<p>Memilih jenis, material, dan teknik cetak yang tepat akan menentukan seberapa lama payung ini bertahan dan terus dipakai oleh penerimanya.</p>
<p>Diskusikan kebutuhan ini dengan provider souvenir kantor yang berpengalaman, agar payung custom yang diproduksi benar-benar sesuai dengan target penerima dan anggaran yang tersedia.</p>
"""

new_toc_html = """
<a href="#nilai-fungsional">Nilai Fungsional yang Jarang Tertandingi Souvenir Lain</a>
<a href="#jenis-payung">Jenis Payung yang Umum Dipilih untuk Souvenir Korporat</a>
<a href="#material-daya-tahan">Material yang Memengaruhi Daya Tahan Payung</a>
<a href="#area-teknik-cetak">Area dan Teknik Cetak Logo pada Kain Payung</a>
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

print("Created payung-custom-souvenir-kantor-yang-jarang-dilirik-tapi-selalu-terpakai.html")
