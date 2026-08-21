import os
import glob
import re

directory = r"c:\Provider Kantor\CorporateGifts ID"

old_text = "CorporateGifts ID - Souvenir Kantor & Merchandise Perusahaan Premium"
new_text = "Provider Souvenir Kantor & Merchandise Perusahaan Premium - CorporateGifts ID"

count = 0

for filepath in glob.glob(os.path.join(directory, '**/*.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Replace the brand title string
    if old_text in content:
        content = content.replace(old_text, new_text)
    
    # 2. Add SEO keywords if not present (except for index.html which already has it, we might want to update it, but let's just add to files that don't have it or replace it)
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1)
        # Clean up title
        title_clean = title.replace('CorporateGifts ID', '').replace('Provider Souvenir Kantor & Merchandise Perusahaan Premium', '').replace('-', ' ')
        words = [w.lower() for w in re.findall(r'\b[a-zA-Z]{4,}\b', title_clean)]
        unique_words = list(dict.fromkeys(words))
        
        # Base keywords
        base_keywords = ["souvenir kantor", "merchandise perusahaan", "corporate gift", "seminar kit", "souvenir premium"]
        
        # Combine
        all_keywords = base_keywords + unique_words
        keywords_str = ", ".join(all_keywords)
        
        keywords_tag = f'\n  <meta name="keywords" content="{keywords_str}">'
        
        if '<meta name="keywords"' not in content:
            # Insert after description
            content = re.sub(r'(<meta name="description" content=".*?">)', r'\1' + keywords_tag, content)
        else:
            # Replace existing keywords
            content = re.sub(r'\n?\s*<meta name="keywords" content=".*?">', keywords_tag, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {count}")
