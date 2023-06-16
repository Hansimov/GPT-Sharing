from bs4 import BeautifulSoup
import cssutils
import subprocess
from pathlib import Path

md_filename = "prompts-cheat-sheet.md"
html_filename = Path(md_filename).stem + ".html"
cmd_md_to_html = (
    f"npx markmap-cli {md_filename} --no-toolbar --no-open -o {html_filename}"
)

css_filename = "./prompt-cheat-sheet-dark.css"
subprocess.run(cmd_md_to_html, shell=True)

with open(html_filename, "r") as rf:
    html_str = rf.read()
soup = BeautifulSoup(html_str, "html.parser")

link_tag = soup.new_tag("link", rel="stylesheet", href=css_filename)
soup.head.append(link_tag)

# css_str = cssutils.parseFile(css_filename)
# style_str = f"<style>\n{css_str.cssText.decode()}\n</style>"
# soup.head.append(BeautifulSoup(style_str, "html.parser"))

new_html_str = str(soup)
with open(html_filename, "w") as wf:
    wf.write(new_html_str)
