from core import export_tutorials_to_txt, from_url_to_tutorial
from ui import get_urls

tutorials = []
urls = get_urls()

for url in urls:
    tutorials.append(from_url_to_tutorial(url))

if len(tutorials):
    export_tutorials_to_txt(tutorials)
