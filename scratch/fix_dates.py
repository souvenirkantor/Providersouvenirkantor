import os
import re
import glob

# Path to the directory
directory = r"c:\Provider Kantor\CorporateGifts ID"

# Regex pattern to match datePublished and dateModified with YYYY-MM-DD format
pattern = re.compile(r'"(datePublished|dateModified)": "([0-9]{4}-[0-9]{2}-[0-9]{2})"')

count = 0

for filepath in glob.glob(os.path.join(directory, '**/*.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, num_replacements = pattern.subn(r'"\1": "\2T08:00:00+07:00"', content)
    
    if num_replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {filepath}")

print(f"Total files updated: {count}")
