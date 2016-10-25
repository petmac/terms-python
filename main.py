from bs4 import BeautifulSoup
import html2text
import urllib
import urlparse
import os

def download(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html

def compute_path(url):
    u = urlparse.urlparse(url)
    path = u.path.split("/")
    parts = filter(bool, ["output"] + [u.hostname] + path)
    return "/".join(parts) + ".md"

def select(html, selector):
    soup = BeautifulSoup(html, "html.parser")
    selected_tags = soup.select(selector)
    selected_strings = map(str, selected_tags)
    parts = "\n".join(selected_strings)
    return parts

def process(url_and_selector):
    url = url_and_selector[0]
    selector = url_and_selector[1]
    print url
    path = compute_path(url)
    html = download(url)
    selected = select(html, selector)
    markdown = html2text.html2text(selected)
    dir = os.path.dirname(path)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    with open(path, "w") as f:
        f.write(markdown)

config = {
    "http://www.example.com/": "body"
}

if __name__ == '__main__':
    map(process, config.items())
