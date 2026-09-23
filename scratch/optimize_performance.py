import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Defer non-critical CSS
    # Looks for: <link href=".../aos.css" rel="stylesheet"/>
    # And replaces with: <link href="..." rel="stylesheet" media="print" onload="this.media='all'"/>
    def css_replacer(match):
        href = match.group(1)
        return f'<link href="{href}" rel="stylesheet" media="print" onload="this.media=\'all\'"/>'

    content = re.sub(
        r'<link\s+href="([^"]*(?:aos\.css|swiper-bundle\.min\.css|bootstrap-icons\.css))"\s+rel="stylesheet"\s*/?>',
        css_replacer,
        content,
        flags=re.IGNORECASE
    )

    # 2. Remove AOS from Hero Elements
    def aos_replacer(match):
        tag = match.group(0)
        tag = re.sub(r'\s*data-aos="[^"]*"', '', tag, flags=re.IGNORECASE)
        tag = re.sub(r'\s*data-aos-delay="[^"]*"', '', tag, flags=re.IGNORECASE)
        return tag

    hero_pattern = re.compile(
        r'<[a-zA-Z1-6]+(?:[^>]*\bclass="[^"]*(?:hero-badge|hero-title|hero-description|hero-actions|hero-metrics|page-title)[^"]*"[^>]*)>',
        re.IGNORECASE
    )
    content = hero_pattern.sub(aos_replacer, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Optimized {filepath}")

def main():
    base_dir = r"c:\Provider Kantor\CorporateGifts ID"
    for root, dirs, files in os.walk(base_dir):
        if 'node_modules' in root or '.git' in root or 'scratch' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
