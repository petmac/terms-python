from bs4 import BeautifulSoup
import html2text
import urllib
import urlparse
import os

def download(url):
    response = urllib.urlopen(url)
    html = response.read()
    return html.decode('utf-8')

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
    return parts.decode("utf-8")

def convert(html, url):
    h = html2text.HTML2Text(baseurl=url)
    h.body_width = 0
    return h.handle(html).encode("utf-8")

def process(url_and_selector):
    url = url_and_selector[0]
    selector = url_and_selector[1]
    print url
    path = compute_path(url)
    html = download(url)
    selected = select(html, selector)
    markdown = convert(selected, url)
    dir = os.path.dirname(path)
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    with open(path, "w") as f:
        f.write(markdown)

config = {
    "http://www.example.com/": "body",
    "https://www.apple.com/legal/internet-services/itunes/uk/terms.html": "#main *",
    "https://twitter.com/tos": "#main-content",
    "https://twitter.com/privacy": "#main-content",
    "https://twitter.com/rules": "article",
    "https://play.google.com/about/play-terms.html": "#play-play-terms.html > div.play-contained",
    "https://play.google.com/about/developer-content-policy-print/": ".print__content",
    "https://play.google.com/intl/ALL_us/about/developer-distribution-agreement.html": "div.play-contained",
}

if __name__ == '__main__':
    map(process, config.items())
