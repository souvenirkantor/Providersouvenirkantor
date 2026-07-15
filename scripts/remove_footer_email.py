import os
from pathlib import Path
pattern = '<a href="#" aria-label="Email" class="social-link"><i class="bi bi-envelope"></i><span>Email</span></a>'
root = Path(__file__).resolve().parent.parent
for p in root.rglob('*.html'):
    if p.suffix == '.html' and not str(p).endswith('.bak'):
        text = p.read_text(encoding='utf-8')
        if pattern in text:
            bak = p.with_suffix(p.suffix + '.bak')
            if not bak.exists():
                bak.write_text(text, encoding='utf-8')
            new = text.replace(pattern, '')
            p.write_text(new, encoding='utf-8')
            print('Updated', p)
print('Done')
