from pathlib import Path
import re

root = Path(r'c:\Landio-pro\Landio-pro')
pattern = re.compile(
    r'<section class="ad-banner-section" aria-label="Iklan jasa pembuatan website UMKM">.*?</section>',
    re.S
)
replacement = (
    '<section class="ad-banner-section" aria-label="Iklan SouvenirPro">\n'
    '      <a class="cg-banner-wrapper" href="https://wa.me/6288989643555?text=Halo,%20saya%20ingin%20konsultasi%20souvenir" '
    'target="_blank" rel="noopener" style="display: block; width: 100%; max-width: 820px; margin: 20px auto; padding: 0; text-align: center;">\n'
    '        <img title="Iklan SouvenirPro" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJc8HBBG1EiYlEWYJj2D1R67SEOZZ44jMHW5dIXfw06znzTyZ30Kn2ev2YO7WvTyIPS_JaN0CLcFPXy78gg_e-5KdoQR8mZL-MKVWwu-n1pxEdcI4Ch6IBTVge95KRx5zZ_zrCugXuSq9bJ3_rA4B-mAYjT4ZfcA4-kDvHwsmNVcXcL056Wh5r5CGQPrvG/s1080/Jasa%20Pembuatan%20Website%20Souvenir%20Kantor.gif" '
    'alt="Iklan SouvenirPro" border="0" style="width: 100%; height: auto; display: block; border-radius: 12px; box-shadow: 0 14px 32px rgba(15, 23, 42, 0.12);" loading="lazy" decoding="async" />\n'
    '      </a>\n'
    '    </section>'
)
changed = []
for path in sorted(root.rglob('*.html')):
    if 'assets' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    new = pattern.sub(replacement, text)
    if new != text:
        path.write_text(new, encoding='utf-8')
        changed.append(path.relative_to(root))

print(f'changed {len(changed)} files')
for p in changed:
    print(p)
