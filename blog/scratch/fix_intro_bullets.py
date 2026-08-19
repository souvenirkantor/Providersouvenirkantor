import os
import re

blog_dir = r"c:\Provider Kantor\CorporateGifts ID\blog"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the article-body section
    article_body_pattern = re.compile(r'(<article class="article-body">)(.*?)(<h2)', re.DOTALL)
    match = article_body_pattern.search(content)
    
    if not match:
        return False
        
    prefix = match.group(1)
    intro_section = match.group(2)
    suffix = match.group(3)
    
    # We want to find consecutive <p> tags.
    # Split by lines or just regex match <p>...</p>
    p_tags = re.findall(r'<p>(.*?)</p>', intro_section, re.DOTALL)
    
    # If there's 2 or more <p> tags, we keep the first as <p>, the rest as <li> in <ul>
    if len(p_tags) > 1:
        # Check if there's already a <ul> in this intro section, if so, maybe it's already processed
        if '<ul>' in intro_section:
            return False
            
        new_intro = f'\n              <p>{p_tags[0]}</p>\n              <ul>\n'
        for p_content in p_tags[1:]:
            # clean up whitespace if any
            p_content = p_content.strip()
            new_intro += f'                <li>{p_content}</li>\n'
        new_intro += '              </ul>\n\n              '
        
        # We also need to be careful if there are other things like <div class="baca-juga-box"> in intro_section
        # Usually it's just <p> tags, but let's check what was actually replaced.
        # If the original intro_section only contained <p> tags and whitespace, it's safe to replace.
        # Let's count the number of <p>...</p> in intro_section and remove them.
        
        # A safer way to replace:
        lines = intro_section.split('\n')
        new_lines = []
        p_count = 0
        in_p = False
        p_buffer = ""
        
        new_intro_section = ""
        first_p_found = False
        ul_started = False
        
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith('<p>') and line_stripped.endswith('</p>'):
                p_content = line_stripped[3:-4]
                if not first_p_found:
                    new_intro_section += f'              <p>{p_content}</p>\n'
                    first_p_found = True
                else:
                    if not ul_started:
                        new_intro_section += '              <ul>\n'
                        ul_started = True
                    new_intro_section += f'                <li>{p_content}</li>\n'
            elif line_stripped == "":
                pass # skip empty lines and handle later
            else:
                # If there's something else, just append it
                if ul_started:
                    new_intro_section += '              </ul>\n'
                    ul_started = False
                new_intro_section += line + '\n'
                
        if ul_started:
            new_intro_section += '              </ul>\n'
            
        # add a blank line before <h2>
        new_intro_section += '\n              '
        
        new_content = content[:match.start()] + prefix + new_intro_section + suffix + content[match.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

modified_count = 0
for filename in os.listdir(blog_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(blog_dir, filename)
        if process_file(filepath):
            print(f"Modified: {filename}")
            modified_count += 1

print(f"Total modified: {modified_count}")
