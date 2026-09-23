import os
import re
from PIL import Image

def get_image_dimensions(image_path):
    try:
        with Image.open(image_path) as img:
            return img.size
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return None, None

def generate_alt_from_filename(filename):
    name = os.path.splitext(filename)[0]
    # Replace dashes and underscores with spaces
    name = re.sub(r'[-_]', ' ', name)
    # Capitalize first letter of each word
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def process_html_file(filepath, base_dir):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Regex to find img tags
        img_pattern = re.compile(r'<img\s+([^>]+)>', re.IGNORECASE)
        
        def replace_img(match):
            nonlocal modified
            img_tag_content = match.group(1)
            attrs = {}
            
            # Simple attribute parser
            attr_pattern = re.compile(r'([\w-]+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))')
            for attr_match in attr_pattern.finditer(img_tag_content):
                name = attr_match.group(1).lower()
                val = attr_match.group(2) or attr_match.group(3) or attr_match.group(4) or ""
                attrs[name] = val
                
            src = attrs.get('src', '')
            if not src or src.startswith('http') or src.startswith('//'):
                return match.group(0) # Skip external images
                
            if src.startswith('/'):
                img_path = os.path.join(base_dir, src[1:])
            else:
                img_path = os.path.normpath(os.path.join(os.path.dirname(filepath), src))
                
            width = attrs.get('width')
            height = attrs.get('height')
            alt = attrs.get('alt')
            
            changed = False
            if not width or not height:
                w, h = get_image_dimensions(img_path)
                if w and h:
                    if not width:
                        attrs['width'] = str(w)
                        changed = True
                    if not height:
                        attrs['height'] = str(h)
                        changed = True
                        
            if alt is None or alt.strip() == '':
                filename = os.path.basename(src)
                if filename:
                    attrs['alt'] = generate_alt_from_filename(filename)
                    changed = True
                    
            if changed:
                modified = True
                new_attrs_str = ' '.join(f'{k}="{v}"' for k, v in attrs.items())
                return f'<img {new_attrs_str}>'
            
            return match.group(0)

        new_content = img_pattern.sub(replace_img, content)
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    for root, dirs, files in os.walk(base_dir):
        if 'scratch' in root or '.git' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_html_file(os.path.join(root, file), base_dir)

if __name__ == "__main__":
    main()
