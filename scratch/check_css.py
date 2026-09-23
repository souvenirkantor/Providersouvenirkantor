import os
import re

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    css_files = []

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or 'scratch' in root:
            continue
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))

    broken = []
    for css in css_files:
        try:
            with open(css, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for match in re.finditer(r'url\([\'\"]?(?!data:)(?!http)([^\'\"\)]+)[\'\"]?\)', content, re.IGNORECASE):
                url = match.group(1).strip()
                
                # Resolve URL
                if url.startswith('/'):
                    path = os.path.join(base_dir, url.lstrip('/'))
                else:
                    path = os.path.normpath(os.path.join(os.path.dirname(css), url))
                
                # Remove query params or hash if any (like fonts.woff?v=1)
                path = path.split('?')[0].split('#')[0]
                
                if not os.path.exists(path):
                    broken.append(f"Broken CSS url: {url} in {css}")
        except Exception as e:
            pass

    if broken:
        for b in broken: print(b)
    else:
        print("All CSS urls exist.")

if __name__ == "__main__":
    main()
