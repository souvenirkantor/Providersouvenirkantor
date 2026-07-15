from pathlib import Path
import re

root = Path('.')
index_file = root / 'index.html'
text = index_file.read_text(encoding='utf-8')
pattern = re.compile(r'<footer id="footer" class="footer position-relative light-background">[\s\S]*?</footer>')
match = pattern.search(text)
if not match:
    raise SystemExit('Footer block not found in index.html')
footer_block = match.group(0)
files = [*root.glob('*.html'), *root.joinpath('blog').glob('*.html')]
updated_files = []
for f in files:
    if f.name == 'index.html':
        continue
    content = f.read_text(encoding='utf-8')
    if pattern.search(content):
        new_content = pattern.sub(footer_block, content)
        if new_content != content:
            f.write_text(new_content, encoding='utf-8')
            updated_files.append(str(f))
print(f'UPDATED {len(updated_files)} files')
for f in updated_files:
    print(f)
