import os
import re

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    broken_images = []

    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # regex to find src in img tags
                    for img_match in re.finditer(r'<img\s+[^>]*src=[\"\']([^\"\']+)[\"\']', content, re.IGNORECASE):
                        src = img_match.group(1)
                        
                        # Skip external links
                        if src.startswith('http') or src.startswith('//') or src.startswith('data:'):
                            continue
                        
                        if src.startswith('/'):
                            img_path = os.path.join(base_dir, src.lstrip('/'))
                        else:
                            img_path = os.path.normpath(os.path.join(root, src))
                        
                        if not os.path.exists(img_path):
                            broken_images.append(f"Broken: {src} in {filepath}")
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    if broken_images:
        for b in broken_images:
            print(b)
    else:
        print("All internal images exist.")

if __name__ == "__main__":
    main()
