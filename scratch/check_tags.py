import os
import re

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    broken_tags = []

    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or 'scratch' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    for match in re.finditer(r'<img[^>]*>', content, re.IGNORECASE):
                        tag = match.group(0)
                        if 'src=' not in tag:
                            broken_tags.append(f"No src: {tag} in {filepath}")
                        elif '\"' not in tag and '\'' not in tag:
                            broken_tags.append(f"Weird quotes: {tag} in {filepath}")
                except Exception as e:
                    pass

    if broken_tags:
        for b in broken_tags[:20]: print(b)
    else:
        print("No malformed img tags found.")

if __name__ == "__main__":
    main()
