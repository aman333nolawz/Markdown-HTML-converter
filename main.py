#!/usr/bin/env python3
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("in_file", help="Markdown file you want to convert to html")
parser.add_argument("out_file", help="Name of the output file")
args = parser.parse_args()

in_file = args.in_file
out_file = args.out_file

with open(in_file, "r") as markdown_file:
    markdown_code = markdown_file.read()

extensions = [
    "tables",
    "pymdownx.superfences",
    "pymdownx.highlight",
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.keys",
]

with open("template.html", "r") as f:
  html = f.read()

body = markdown.markdown(
    markdown_code, extensions=extensions
)
html = html.replace("{{ content }}", body)

with open(out_file, "w") as html_file:
    html_file.write(html)

print("Done!")
