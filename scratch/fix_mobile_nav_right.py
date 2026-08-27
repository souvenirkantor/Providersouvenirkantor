import os

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
css_path = os.path.join(base_dir, "assets", "css", "main.css")

css_addition = """
/* --- Push Mobile Nav Toggle to Right --- */
@media (max-width: 1199px) {
  .header .navmenu {
    justify-content: flex-end !important;
    width: 100%;
  }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if "Push Mobile Nav Toggle to Right" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Successfully appended flex-end fix to main.css")
else:
    print("Fix already exists.")
