import os

base_dir = r'c:\Provider Kantor\CorporateGifts ID'

replacements = {
    'href=\"../assets/vendor/bootstrap-icons/css/bootstrap-icons.css\"': 'href=\"../assets/vendor/bootstrap-icons/bootstrap-icons.css\"',
    'href=\"ide-corporate-gift-premium-untuk-bisnis.html\"': 'href=\"ide-corporate-gift-premium-bisnis.html\"'
}

for root, dirs, files in os.walk(base_dir):
    if 'scratch' in root or '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old_text, new_text in replacements.items():
                new_content = new_content.replace(old_text, new_text)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {os.path.relpath(filepath, base_dir)}")

print("Done fixing links.")
