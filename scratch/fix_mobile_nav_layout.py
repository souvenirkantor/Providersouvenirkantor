import os

base_dir = r"C:\Provider Kantor\CorporateGifts ID"
css_path = os.path.join(base_dir, "assets", "css", "main.css")

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_addition = """
/* --- Fix Mobile Nav Layout (Aligned Right & Toggle in Place) --- */
@media (max-width: 1199px) {
  /* Ensure the toggle is pushed to the right */
  .header .navmenu {
    justify-content: flex-end;
    width: 100%;
  }

  /* Keep the toggle icon exactly where it is when menu is active */
  .mobile-nav-active .mobile-nav-toggle {
    position: static !important;
    color: var(--nav-color) !important;
    font-size: 28px !important;
    margin-right: 10px !important;
  }

  /* Prevent navmenu from taking over the screen */
  .mobile-nav-active .navmenu {
    position: static !important;
    background: transparent !important;
  }

  /* Position the dropdown box right below the header container */
  .navmenu ul {
    position: absolute !important;
    inset: auto !important;
    top: 100% !important;
    left: 0 !important;
    right: 0 !important;
    margin-top: 15px !important;
    max-height: calc(100vh - 120px) !important;
    overflow-y: auto !important;
    border-radius: 12px !important;
  }

  /* Add dark overlay to the screen below the header */
  body.mobile-nav-active::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(8, 12, 22, 0.7);
    z-index: 990;
  }
}
"""

if "Fix Mobile Nav Layout" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(css_addition)
    print("Successfully appended mobile nav layout fix to main.css")
else:
    print("Fix already present in main.css")
