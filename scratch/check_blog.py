import re
with open(r'c:\Provider Kantor\CorporateGifts ID\blog.html', 'r', encoding='utf-8') as f:
    html = f.read()
for match in re.finditer(r'<img[^>]*src=[\"\']([^\"\']+)[\"\']', html, re.IGNORECASE):
    print(match.group(1))
