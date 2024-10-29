#!usr/bin/env python
import requests
import re
import urllib.parse as urlparse


target_url = "http://192.168.164.130/mutillidae/"
target_list = []


def extract_links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
    href_links = extract_links(url)
    for links in href_links:
        links = urlparse.urljoin(url, links)

        if "#" in links:
            links = links.split("#")[0]

        if target_url in links and links not in target_list:
            target_list.append(links)
            print(links)
            crawl(links)
crawl(target_url)