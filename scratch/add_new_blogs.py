import os
import datetime
from bs4 import BeautifulSoup

def update_file():
    # Setup
    workspace_dir = r"c:\Provider Kantor\CorporateGifts ID"
    blog_dir = os.path.join(workspace_dir, "blog")
    scratch_dir = os.path.join(workspace_dir, "scratch")
    
    # --- ARTIKEL PERTAMA ---
    title_1 = "Tumbler Reusable sebagai Souvenir Kantor yang Ramah Lingkungan"
    meta_title_1 = "Tumbler Reusable Souvenir Kantor Ramah Lingkungan"
    meta_description_1 = "Tumbler reusable stainless jadi souvenir kantor ramah lingkungan. Kurangi sampah plastik sambil tampilkan logo perusahaan Anda."
    filename_1 = "tumbler-reusable-sebagai-souvenir-kantor-yang-ramah-lingkungan.html"
    image_1 = "ilustrasi-tumbler-reusable-ramah-lingkungan-kantor.webp"
    date_1 = "23 Sep 2026"
    date_iso_1 = "2026-09-23"
    content_1_html = """<p>Tumbler ramah lingkungan kantor berbahan stainless steel reusable memberi solusi souvenir yang mengurangi ketergantungan pada botol plastik sekali pakai di lingkungan kerja.</p>
<p>Tumbler stainless dapat dipakai berulang selama bertahun-tahun tanpa penurunan fungsi signifikan.</p>
<p>Material stainless steel 304 aman untuk kontak makanan dan minuman jangka panjang.</p>
<p>Kemasan minim plastik memperkuat konsistensi konsep souvenir ramah lingkungan.</p>
<p>Laser engraving menjadi metode branding yang tidak menambah lapisan tinta kimia pada bodi.</p>
<p>providersouvenirkantor menyediakan tumbler reusable dengan opsi kemasan berkelanjutan.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="jenis-souvenir-ramah-lingkungan.html">Jenis Souvenir Ramah Lingkungan untuk Perusahaan</a>
</div>

<h2>Tumbler Reusable Mana yang Sesuai untuk Konsep Kantor Ramah Lingkungan?</h2>
<p>Tumbler stainless dengan kemasan kertas daur ulang dan tanpa lapisan plastik tambahan paling sesuai untuk perusahaan yang mengusung konsep souvenir kantor ramah lingkungan secara konsisten.</p>
<p>Tumbler dengan bodi polos tanpa lapisan cat tebal umumnya lebih mudah didaur ulang di akhir masa pakainya dibanding tumbler dengan lapisan coating berlebih.</p>
<p>Pemilihan warna natural stainless atau powder coating tipis menjadi pertimbangan yang relevan untuk konsep ini.</p>
<p>Kemasan pendukung turut menentukan konsistensi konsep.</p>
<p>Box karton polos tanpa laminasi plastik dan tali pengikat berbahan kertas memberi kesan selaras dengan pesan keberlanjutan yang ingin disampaikan perusahaan.</p>

<h2>Manfaat Tumbler Stainless Dibanding Botol Plastik Sekali Pakai</h2>
<p>Tumbler stainless reusable memberi manfaat penggunaan berulang jangka panjang, berbeda dari botol plastik sekali pakai yang umumnya dibuang setelah satu atau beberapa kali pemakaian.</p>
<p>Botol plastik sekali pakai berkontribusi pada volume sampah kantor yang terus bertambah setiap hari, terutama pada acara dengan konsumsi minuman kemasan dalam jumlah besar.</p>
<p>Tumbler reusable mengurangi kebutuhan pembelian botol plastik berulang karena karyawan dapat mengisi ulang dari dispenser air kantor.</p>
<p>Dari sisi material, stainless steel tidak melepaskan mikroplastik ke dalam cairan seperti yang berpotensi terjadi pada sebagian plastik berkualitas rendah saat terpapar panas.</p>
<p>Karakter ini menjadikan tumbler stainless pilihan yang lebih aman untuk pemakaian minuman panas setiap hari.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="tumbler-custom-sebagai-pilihan-souvenir-kantor-paling-diminati.html">Tumbler Custom sebagai Pilihan Souvenir Kantor Paling Diminati</a>
</div>

<h2>Branding Logo yang Selaras dengan Konsep Souvenir Ramah Lingkungan</h2>
<p>Laser engraving menjadi metode branding yang paling selaras dengan konsep ramah lingkungan karena tidak menambahkan lapisan tinta atau pelapis kimia tambahan pada bodi tumbler.</p>
<p>Metode ini mengukir logo langsung ke permukaan material sehingga tidak ada proses pelapisan tambahan yang berpotensi terkelupas dan menjadi limbah mikro dalam jangka panjang.</p>
<p>Hasilnya juga lebih tahan lama dibanding cetak tinta konvensional.</p>
<p>Untuk perusahaan yang tetap menginginkan logo berwarna, cetak UV dengan tinta berbahan dasar aman tetap dapat digunakan pada area terbatas.</p>
<p>Dikombinasikan dengan laser engraving pada bagian lain untuk menjaga keseimbangan antara identitas visual dan konsep keberlanjutan.</p>

<h2>Kemasan Minim Plastik untuk Distribusi Tumbler Ramah Lingkungan</h2>
<p>Kemasan tumbler ramah lingkungan umumnya menggunakan box karton daur ulang, pouch kain, atau kemasan tanpa plastik pembungkus tambahan pada bagian luar.</p>
<p>Box karton daur ulang dengan cetak tinta berbahan dasar air memberi kesan konsisten dengan pesan keberlanjutan yang ingin disampaikan melalui souvenir.</p>
<p>Sekat internal dapat dibuat dari karton bergelombang alih-alih busa plastik konvensional.</p>
<p>Pouch kain berbahan katun atau kanvas dapat digunakan kembali oleh penerima untuk keperluan lain setelah tumbler dikeluarkan, sehingga fungsi kemasan tidak berhenti setelah sekali pakai.</p>
<p>Distribusi dalam jumlah besar tetap dapat mempertahankan konsep ini dengan mengganti selotip plastik dengan pita kertas dan label kertas daur ulang pada setiap unit kemasan.</p>

<h2>Menyampaikan Pesan Keberlanjutan Melalui Souvenir Tumbler Perusahaan</h2>
<p>Souvenir tumbler ramah lingkungan dapat dilengkapi kartu informasi singkat yang menjelaskan manfaat penggunaan berulang.</p>
<p>Tanpa perlu klaim berlebihan mengenai dampak lingkungan yang belum terukur secara spesifik.</p>
<p>Kartu informasi yang menyertakan ajakan sederhana untuk mengisi ulang tumbler di dispenser kantor memberi konteks tambahan bagi penerima mengenai tujuan souvenir tersebut.</p>
<p>Sekaligus memperkuat asosiasi antara perusahaan dan praktik kerja yang lebih berkelanjutan.</p>
<p>Pendekatan ini juga relevan untuk souvenir onboarding karyawan baru, di mana tumbler reusable dapat menjadi bagian dari orientasi mengenai kebijakan pengurangan plastik sekali pakai di lingkungan kantor.</p>

<h2>Wujudkan Souvenir Tumbler Ramah Lingkungan Bersama providersouvenirkantor</h2>
<p>providersouvenirkantor menyediakan tumbler reusable dengan opsi kemasan minim plastik untuk mendukung konsep souvenir kantor yang berkelanjutan.</p>
<p>Sampaikan jumlah penerima, preferensi material, dan konsep kemasan yang diinginkan, lalu tim kami menyusun rekomendasi unit beserta opsi branding yang sesuai.</p>
<p>Hubungi tim konsultasi providersouvenirkantor melalui WhatsApp untuk mendapatkan penawaran resmi dan mock-up desain hari ini.</p>"""

    # --- ARTIKEL KEDUA ---
    title_2 = "Pilihan Botol Minum Custom untuk Souvenir Onboarding Karyawan"
    meta_title_2 = "Botol Minum Custom untuk Souvenir Onboarding Karyawan"
    meta_description_2 = "Botol minum custom logo jadi souvenir onboarding karyawan baru. Kesan pertama yang rapi dan fungsional dari hari pertama kerja."
    filename_2 = "pilihan-botol-minum-custom-untuk-souvenir-onboarding-karyawan.html"
    image_2 = "ilustrasi-botol-minum-emboss-logo-untuk-onboarding.webp"
    date_2 = "23 Sep 2026"
    date_iso_2 = "2026-09-23"
    content_2_html = """<p>Souvenir botol minum karyawan berbahan stainless dengan cetak logo emboss atau laser menjadi pelengkap welcome kit yang memberi kesan rapi pada hari pertama kerja karyawan baru.</p>
<p>Botol minum onboarding umumnya berkapasitas 350 sampai 500 ml agar ringan dan praktis dibawa.</p>
<p>Desain minimalis satu warna memudahkan produksi massal untuk seluruh angkatan karyawan baru.</p>
<p>Logo emboss memberi kesan halus tanpa kontras warna yang mencolok pada bodi botol.</p>
<p>Kemasan box sederhana dengan kartu ucapan menambah kesan personal saat diterima.</p>
<p>providersouvenirkantor menyediakan botol minum custom siap masuk welcome kit karyawan.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="isi-seminar-kit-training-karyawan-baru-terlengkap.html">Isi Seminar Kit Training Karyawan Baru Terlengkap</a>
</div>

<h2>Pilihan Botol Minum untuk Welcome Kit Karyawan Baru</h2>
<p>Botol minum stainless berkapasitas menengah dengan bodi ramping menjadi pilihan paling praktis untuk dimasukkan ke dalam welcome kit karyawan baru bersama material orientasi lainnya.</p>
<p>Bodi ramping memudahkan botol diselipkan bersama dokumen, kartu identitas, dan merchandise lain dalam satu paket welcome kit tanpa menambah volume kemasan secara signifikan.</p>
<p>Warna dasar netral seperti putih, hitam doff, atau abu memberi fleksibilitas visual.</p>
<p>Sehingga botol tetap terlihat rapi berdampingan dengan berbagai desain kemasan welcome kit yang mungkin sudah ditetapkan perusahaan.</p>

<h2>Bagaimana Logo Perusahaan Ditempatkan pada Botol Minum Welcome Kit?</h2>
<p>Logo perusahaan pada botol minum onboarding umumnya ditempatkan pada bagian tengah bodi menggunakan teknik emboss atau laser engraving agar tetap terlihat rapi tanpa kontras warna berlebihan.</p>
<p>Emboss menekan permukaan material membentuk relief logo tanpa menambahkan warna tambahan.</p>
<p>Sehingga cocok untuk bodi botol berwarna gelap yang mengutamakan kesan minimalis dan elegan.</p>
<p>Laser engraving memberi hasil serupa dengan kontras yang sedikit lebih tegas, tergantung warna dasar material.</p>
<p>Kedua metode ini menjaga logo tetap tahan lama meski botol dipakai setiap hari selama masa kerja karyawan.</p>
<p>Untuk perusahaan yang menginginkan logo dengan warna korporat penuh, cetak UV tetap dapat digunakan sebagai alternatif.</p>
<p>Meski umumnya memerlukan perawatan permukaan lebih hati-hati dibanding metode ukir.</p>

<div class="baca-juga-box">
  <strong>Baca Juga:</strong> <a href="tumbler-stainless-logo-perusahaan-untuk-souvenir-karyawan.html">Tumbler Stainless Logo Perusahaan untuk Souvenir Karyawan</a>
</div>

<h2>Kapasitas dan Fitur Botol Minum yang Sesuai untuk Onboarding</h2>
<p>Kapasitas 350 hingga 500 ml dengan fitur tutup screw sederhana menjadi standar yang paling sesuai untuk botol minum onboarding karena ringan, aman dari tumpahan, dan mudah diproduksi massal.</p>
<p>Kapasitas ini cukup untuk kebutuhan minum selama beberapa jam kerja tanpa membuat botol terasa terlalu besar saat dibawa dalam tas kerja karyawan baru.</p>
<p>Fitur tambahan seperti insulasi vakum dapat dipertimbangkan untuk perusahaan yang ingin memberi kesan lebih premium pada welcome kit.</p>
<p>Tutup screw sederhana lebih mudah diproduksi dalam jumlah besar dibanding mekanisme tutup sport yang memiliki lebih banyak komponen bergerak.</p>
<p>Sehingga lebih efisien untuk pesanan onboarding berskala besar dengan tenggat waktu yang ketat.</p>

<h2>Format Kemasan Welcome Kit yang Menyertakan Botol Minum Custom</h2>
<p>Kemasan welcome kit yang menyertakan botol minum custom umumnya berupa box karton dengan sekat sederhana, tote bag kain, atau kombinasi keduanya untuk distribusi ke karyawan baru.</p>
<p>Box karton dengan sekat internal menjaga posisi botol tetap stabil bersama dokumen dan merchandise lain di dalam satu paket.</p>
<p>Format ini memudahkan proses serah terima pada hari orientasi tanpa risiko komponen bergeser atau rusak.</p>
<p>Tote bag kain memberi alternatif yang lebih santai dan dapat digunakan kembali oleh karyawan untuk membawa barang pribadi setelah welcome kit diterima.</p>
<p>Format ini sering dipadukan dengan botol minum, notebook, dan pena dalam satu paket orientasi.</p>
<p>Kartu ucapan singkat berisi nama karyawan dan pesan sambutan dari perusahaan menjadi pelengkap yang memperkuat kesan.</p>
<p>Bahwa welcome kit disiapkan secara khusus untuk hari pertama kerja mereka.</p>

<h2>Menyesuaikan Jumlah Pesanan Botol Minum dengan Jadwal Rekrutmen</h2>
<p>Jumlah pesanan botol minum onboarding disesuaikan dengan proyeksi jumlah karyawan baru dalam periode rekrutmen tertentu.</p>
<p>Mulai dari beberapa unit per bulan hingga puluhan unit untuk perekrutan massal.</p>
<p>Untuk perusahaan dengan jadwal onboarding rutin bulanan, pemesanan dalam batch kecil.</p>
<p>Namun berkala membantu menjaga konsistensi stok tanpa penyimpanan berlebih di gudang internal.</p>
<p>Untuk periode perekrutan massal, seperti pembukaan cabang baru atau program management trainee, pemesanan dalam jumlah besar sekaligus umumnya lebih efisien dari sisi waktu produksi dan konsistensi hasil cetak logo antar batch.</p>

<h2>Siapkan Welcome Kit Karyawan Baru Bersama providersouvenirkantor</h2>
<p>providersouvenirkantor menyediakan botol minum custom logo siap masuk welcome kit untuk menyambut karyawan baru perusahaan Anda.</p>
<p>Sampaikan proyeksi jumlah karyawan baru, jadwal onboarding, dan preferensi desain welcome kit, lalu tim kami menyusun rekomendasi botol minum beserta opsi kemasan yang sesuai.</p>
<p>Kunjungi katalog welcome kit providersouvenirkantor atau hubungi tim konsultasi melalui WhatsApp untuk mendapatkan penawaran resmi hari ini.</p>"""

    template_path = os.path.join(blog_dir, "provider-souvenir-kantor-bandung.html")
    with open(template_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    def generate_article(filename, meta_title, meta_description, title, date, date_iso, image, content_html, url_slug):
        # We replace the relevant parts of the template.
        soup = BeautifulSoup(template_html, "html.parser")
        
        # Meta tags
        soup.title.string = f"{meta_title} - CorporateGifts ID"
        soup.find("meta", {"name": "description"})["content"] = meta_description
        soup.find("link", {"rel": "canonical"})["href"] = f"https://providersouvenirkantor.web.id/blog/{url_slug}"
        soup.find("meta", property="og:url")["content"] = f"https://providersouvenirkantor.web.id/blog/{url_slug}"
        soup.find("meta", property="og:title")["content"] = meta_title
        soup.find("meta", property="og:description")["content"] = meta_description
        soup.find("meta", property="og:image")["content"] = f"https://providersouvenirkantor.web.id/images/{image}"
        soup.find("meta", property="twitter:url")["content"] = f"https://providersouvenirkantor.web.id/blog/{url_slug}"
        soup.find("meta", property="twitter:title")["content"] = meta_title
        soup.find("meta", property="twitter:description")["content"] = meta_description
        soup.find("meta", property="twitter:image")["content"] = f"https://providersouvenirkantor.web.id/images/{image}"
        
        # Schema
        schema = soup.find("script", {"type": "application/ld+json"})
        if schema:
            import json
            import re
            schema_str = schema.string
            # Simple replacement for JSON
            schema_str = re.sub(r'"headline": ".*?"', f'"headline": "{meta_title}"', schema_str)
            schema_str = re.sub(r'"image": \[.*?\]', f'"image": [\n        "https://providersouvenirkantor.web.id/images/{image}"\n      ]', schema_str, flags=re.DOTALL)
            schema_str = re.sub(r'"description": ".*?"', f'"description": "{meta_description}"', schema_str)
            schema_str = re.sub(r'"datePublished": ".*?"', f'"datePublished": "{date_iso}T08:00:00+07:00"', schema_str)
            schema_str = re.sub(r'"dateModified": ".*?"', f'"dateModified": "{date_iso}T08:00:00+07:00"', schema_str)
            schema.string.replace_with(schema_str)

        # Content replacements
        header_title = soup.find("h1")
        if header_title and header_title.parent.name != 'a':
            header_title.string = title
        
        # Meta dates
        for meta_div in soup.find_all("div", class_="blog-meta"):
            # Update date in article header
            spans = meta_div.find_all("span")
            for span in spans:
                if "bi-calendar3" in str(span):
                    span.clear()
                    icon = soup.new_tag("i", attrs={"class": "bi bi-calendar3"})
                    span.append(icon)
                    span.append(f" {date}")
                    break

        # Main image
        cover_div = soup.find("div", class_="article-cover")
        if cover_div:
            img = cover_div.find("img")
            if img:
                img["src"] = f"../images/{image}"
                img["alt"] = title
                
        # Update author image
        author_boxes = soup.find_all("div", class_="author-box")
        for author_box in author_boxes:
            img = author_box.find("img")
            if img:
                img["src"] = "../images/profil-penulis2.webp"

        # Update article body
        article_body = soup.find("article", class_="article-body")
        if article_body:
            article_body.clear()
            content_soup = BeautifulSoup(content_html, "html.parser")
            for child in content_soup.children:
                article_body.append(child)

        # Update TOC dynamically based on h2
        toc_nav = soup.find("nav", class_="toc-list")
        mobile_toc_nav = soup.find("div", id="mobile-toc-body")
        if mobile_toc_nav:
            mobile_toc_nav = mobile_toc_nav.find("nav")
            
        h2s = article_body.find_all("h2")
        
        # Add ids to h2s in article body and generate TOC links
        toc_links = []
        for i, h2 in enumerate(h2s):
            h2_id = f"section-{i+1}"
            h2["id"] = h2_id
            toc_links.append(f'<a href="#{h2_id}">{h2.text}</a>')
            
        if toc_nav:
            toc_nav.clear()
            for link in toc_links:
                toc_nav.append(BeautifulSoup(link, "html.parser"))
                
        if mobile_toc_nav:
            mobile_toc_nav.clear()
            for link in toc_links:
                mobile_toc_nav.append(BeautifulSoup(link, "html.parser"))

        html_str = str(soup)
        html_str = html_str.replace("<html>", '<html lang="id">')
        with open(os.path.join(blog_dir, filename), "w", encoding="utf-8") as out:
            out.write(html_str)

    generate_article(filename_1, meta_title_1, meta_description_1, title_1, date_1, date_iso_1, image_1, content_1_html, filename_1)
    generate_article(filename_2, meta_title_2, meta_description_2, title_2, date_2, date_iso_2, image_2, content_2_html, filename_2)

    # Now update blog.html
    blog_html_path = os.path.join(workspace_dir, "blog.html")
    with open(blog_html_path, "r", encoding="utf-8") as f:
        blog_html = f.read()

    new_blog_cards = f"""<div class="col-md-6" data-aos="fade-up" data-aos-delay="0">
<article class="blog-card">
<a href="blog/{filename_1}"><img alt="{title_1}" decoding="async" loading="eager" src="images/{image_1}"/></a>
<div class="blog-card-body">
<span class="article-tag">Ide Souvenir</span>
<h3><a href="blog/{filename_1}">{title_1}</a></h3>
<div class="blog-meta"><span><i class="bi bi-calendar3"></i> {date_1}</span><span><i class="bi bi-clock"></i> 5 menit</span></div>
<p>{meta_description_1}</p>
<a class="read-more" href="blog/{filename_1}">Baca Artikel <i class="bi bi-arrow-right"></i></a>
</div>
</article>
</div>
<div class="col-md-6" data-aos="fade-up" data-aos-delay="50">
<article class="blog-card">
<a href="blog/{filename_2}"><img alt="{title_2}" decoding="async" loading="eager" src="images/{image_2}"/></a>
<div class="blog-card-body">
<span class="article-tag">Ide Souvenir</span>
<h3><a href="blog/{filename_2}">{title_2}</a></h3>
<div class="blog-meta"><span><i class="bi bi-calendar3"></i> {date_2}</span><span><i class="bi bi-clock"></i> 5 menit</span></div>
<p>{meta_description_2}</p>
<a class="read-more" href="blog/{filename_2}">Baca Artikel <i class="bi bi-arrow-right"></i></a>
</div>
</article>
</div>
"""
    
    # insert after <div class="row g-4" id="blog-grid">
    if '<div class="row g-4" id="blog-grid">' in blog_html:
        blog_html = blog_html.replace('<div class="row g-4" id="blog-grid">', f'<div class="row g-4" id="blog-grid">\n{new_blog_cards}')
    
    with open(blog_html_path, "w", encoding="utf-8") as f:
        f.write(blog_html)
        
    # Update sitemap.xml
    sitemap_path = os.path.join(workspace_dir, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_xml = f.read()
        
    new_sitemap_urls = f"""  <url>
    <loc>https://providersouvenirkantor.web.id/blog/{filename_1}</loc>
    <lastmod>{date_iso_1}T08:00:00+07:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://providersouvenirkantor.web.id/blog/{filename_2}</loc>
    <lastmod>{date_iso_2}T08:00:00+07:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
    if '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' in sitemap_xml:
        sitemap_xml = sitemap_xml.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{new_sitemap_urls}')
        
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
        
    print("Done")

update_file()
