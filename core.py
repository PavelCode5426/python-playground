import datetime
from pathlib import Path
import re
import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'vproxy.aerovaradero.avianet.cu:8080',
    # 'https':''
}


class Tutorial:
    name: str
    files: list

    def __init__(self, name, files=[]) -> None:
        self.name = name
        self.files = files
        super().__init__()


def generate_folder_for_files():
    today = datetime.datetime.now()
    folder_name = today.strftime("%Y%m%d%H")  # Date to the desired string format
    folder = Path(folder_name)
    folder.mkdir(exist_ok=True, parents=True)

    return folder


def from_url_to_tutorial(url) -> Tutorial:
    r = requests.get(url,verify=False)
    soup = BeautifulSoup(r.text, 'lxml')

    title = soup.title.string
    links = soup.find_all('a', href=True)

    tutorial = Tutorial(title)
    for link in links:
        href = link.get('href')
        if ".rar" in href:
            tutorial.files.append(f"{href}\n")
    return tutorial


def export_tutorials_to_txt(tutorials: list[Tutorial]):
    folder = generate_folder_for_files()

    with open(f"{folder}/all.txt", 'w') as f1:
        for tutorial in tutorials:
            with open(f'{folder}/{tutorial.name}.txt', 'w') as f2:
                f2.writelines(tutorial.files)
            f2.close()
            f1.writelines(tutorial.files)
    f1.close()
