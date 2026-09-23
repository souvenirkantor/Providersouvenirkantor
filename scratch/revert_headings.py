import os
from bs4 import BeautifulSoup

def revert_headings(soup):
    modified = False
    
    # reverse h2 with class h3 back to h3
    for h in soup.find_all('h2'):
        classes = h.get('class', [])
        if 'h3' in classes:
            h.name = 'h3'
            classes.remove('h3')
            if not classes:
                del h['class']
            else:
                h['class'] = classes
            modified = True
            
    # reverse h3 with class h4 back to h4
    for h in soup.find_all('h3'):
        classes = h.get('class', [])
        if 'h4' in classes:
            h.name = 'h4'
            classes.remove('h4')
            if not classes:
                del h['class']
            else:
                h['class'] = classes
            modified = True
            
    # reverse h3 with class h5 back to h5
    for h in soup.find_all('h3'):
        classes = h.get('class', [])
        if 'h5' in classes:
            h.name = 'h5'
            classes.remove('h5')
            if not classes:
                del h['class']
            else:
                h['class'] = classes
            modified = True
            
    # reverse h3 with class h6 back to h6
    for h in soup.find_all('h3'):
        classes = h.get('class', [])
        if 'h6' in classes:
            h.name = 'h6'
            classes.remove('h6')
            if not classes:
                del h['class']
            else:
                h['class'] = classes
            modified = True

    return modified

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        modified = revert_headings(soup)
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Reverted HTML: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
