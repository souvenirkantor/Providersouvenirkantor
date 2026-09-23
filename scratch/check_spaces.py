import os
import re

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or 'scratch' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    for match in re.finditer(r'<img[^>]*src=[\"\']([^\"\']+)[\"\']', content, re.IGNORECASE):
                        src = match.group(1)
                        if ' ' in src:
                            print(f"Space in src: {src} in {filepath}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    main()
