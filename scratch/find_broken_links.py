import os
import re
from urllib.parse import urlparse

base_dir = r'c:\Provider Kantor\CorporateGifts ID'

def check_links():
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    broken_links = []
    link_pattern = re.compile(r'href=[\"\']([^\"\']+)[\"\']')
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                content = f.read()
            except Exception as e:
                print(f'Error reading {file_path}: {e}')
                continue
                
            links = link_pattern.findall(content)
            for link in links:
                if link.startswith('http') or link.startswith('mailto:') or link.startswith('tel:') or link.startswith('#') or link.startswith('javascript:'):
                    continue
                # Local link
                link_clean = link.split('#')[0].split('?')[0]
                if not link_clean:
                    continue
                
                # Resolve relative path
                if link_clean.startswith('/'):
                    target_path = os.path.join(base_dir, link_clean.lstrip('/'))
                else:
                    target_path = os.path.normpath(os.path.join(os.path.dirname(file_path), link_clean))
                    
                if not os.path.exists(target_path) and not os.path.isdir(target_path):
                    broken_links.append({'file': file_path, 'link': link, 'target': target_path})
                    
    for b in broken_links:
        print(f"Broken link in {os.path.relpath(b['file'], base_dir)}: href=\"{b['link']}\" (resolves to {b['target']})")
        
    print(f"Total broken links found: {len(broken_links)}")

if __name__ == '__main__':
    check_links()
