import os
import re
from bs4 import BeautifulSoup

def process_css(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        new_lines = []
        for line in lines:
            if '{' in line or ',' in line or line.strip().endswith('h4') or line.strip().endswith('h5') or line.strip().endswith('h6') or line.strip().endswith('h3'):
                # We only want to modify the selector part
                parts = line.split('{')
                if len(parts) > 0:
                    selectors = parts[0].split(',')
                    new_selectors = []
                    for sel in selectors:
                        sel = sel.strip()
                        if not sel:
                            continue
                        new_selectors.append(sel)
                        # If selector targets a heading tag, duplicate it with a class
                        for tag in ['h3', 'h4', 'h5', 'h6']:
                            # match tag at the end of selector or followed by pseudo class
                            # e.g. ".card h4" or ".card h4:hover" or just "h4"
                            if re.search(rf'\b{tag}\b', sel):
                                new_sel = re.sub(rf'\b{tag}\b', f'.{tag}', sel)
                                if new_sel not in new_selectors:
                                    new_selectors.append(new_sel)
                    
                    parts[0] = ',\n'.join(new_selectors) + (' {' if '{' in line else '')
                    # preserve indentation
                    indent = len(line) - len(line.lstrip())
                    new_lines.append((' ' * indent) + parts[0] + ('{' + parts[1] if len(parts) > 1 else '\n'))
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
                
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated CSS: {filepath}")
    except Exception as e:
        print(f"Error processing CSS {filepath}: {e}")

def fix_headings(soup):
    modified = False
    
    # 1. Blog titles (skip h2): h3 -> h2
    for card in soup.select('.blog-card h3, .article-card h3'):
        card.name = 'h2'
        classes = card.get('class', [])
        if 'h3' not in classes:
            classes.append('h3')
        card['class'] = classes
        modified = True

    # 2. achievement-list h4 (skip h3): h4 -> h3
    for h in soup.select('.achievement-content h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 3. features h4: h4 -> h3
    for h in soup.select('.feature-content h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True

    # 4. testimonials h4: h4 -> h3
    for h in soup.select('.user-info h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 5. contact info h4: h4 -> h3
    for h in soup.select('.card-content h4, .info-item h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 6. footer h6: h6 -> h3
    for h in soup.select('.footer h6, .footer-top h6'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h6' not in classes:
            classes.append('h6')
        h['class'] = classes
        modified = True
        
    # 7. footer h5: h5 -> h3
    for h in soup.select('.footer h5, .footer-newsletter h5'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h5' not in classes:
            classes.append('h5')
        h['class'] = classes
        modified = True
        
    # 8. page-features h4: h4 -> h3
    for h in soup.select('.mini-feature h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 9. product card h4: h4 -> h3
    for h in soup.select('.product-body h4, .product-card h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 10. overview card h4: h4 -> h3
    for h in soup.select('.overview-header h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True

    # 11. benefit card h4: h4 -> h3
    for h in soup.select('.benefit-card h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 12. timeline h4: h4 -> h3
    for h in soup.select('.timeline-content h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 13. consultation form h4: h4 -> h3
    for h in soup.select('.form-header h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True
        
    # 14. layanan article faq h4: h4 -> h3
    for h in soup.select('.article-faq .faq-item h4'):
        h.name = 'h3'
        classes = h.get('class', [])
        if 'h4' not in classes:
            classes.append('h4')
        h['class'] = classes
        modified = True

    return modified

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        modified = fix_headings(soup)
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated HTML: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    
    # Process CSS first
    css_path = os.path.join(base_dir, 'assets', 'css', 'main.css')
    if os.path.exists(css_path):
        process_css(css_path)
    
    # Process HTML
    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
