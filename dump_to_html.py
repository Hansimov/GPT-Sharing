from bs4 import BeautifulSoup
import cssutils
import subprocess
from pathlib import Path


class MD2HTML:
    def __init__(self):
        self.md_filename = "prompts-cheat-sheet.md"
        self.html_filename = Path(self.md_filename).stem + ".html"
        self.css_filename = "./prompt-cheat-sheet-dark.css"

    def convert_md_to_html(self):
        cmd_md_to_html = (
            f"npx markmap-cli {self.md_filename} -o {self.html_filename} "
            f"--no-toolbar --no-open "
        )
        subprocess.run(cmd_md_to_html, shell=True)

    def parse_html(self):
        with open(self.html_filename, "r") as rf:
            html_str = rf.read()
        self.soup = BeautifulSoup(html_str, "html.parser")

    def add_css_to_html(self):
        css_link_tag = self.soup.new_tag("link", rel="stylesheet", href=css_filename)
        self.soup.head.append(css_link_tag)
        # css_str = cssutils.parseFile(css_filename)
        # style_str = f"<style>\n{css_str.cssText.decode()}\n</style>"
        # soup.head.append(BeautifulSoup(style_str, "html.parser"))

        self.soup.title.string = "Prompt Engineering Cheat Sheet"

    def add_favicon_to_html(self):
        favicon_link_tag = self.soup.new_tag(
            "link",
            rel="shortcut icon",
            href="https://img.uxwing.com/wp-content/themes/uxwing/download/brands-social-media/chatgpt-icon.svg",
        )
        self.soup.head.append(favicon_link_tag)

    def dump_to_html(self):
        new_html_str = str(self.soup)
        with open(self.html_filename, "w") as wf:
            wf.write(new_html_str)

    def run(self):
        self.convert_md_to_html()
        self.parse_html()
        self.add_css_to_html()
        self.add_favicon_to_html()
        self.dump_to_html()
