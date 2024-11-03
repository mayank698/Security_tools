#!usr/bin/env python
import requests
import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_list = []
        self.links_to_ignore = ignore_links

    def extract_links(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links(url)
        for links in href_links:
            links = urlparse.urljoin(url, links)

            if "#" in links:
                links = links.split("#")[0]

            if (
                self.target_url in links
                and links not in self.target_list
                and links not in self.links_to_ignore
            ):
                self.target_list.append(links)
                print(links)
                self.crawl(links)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="lxml")
        return parsed_html.findAll("form")

    def submit_form(self, url, value, form):
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")

        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
            post_data[input_name] = input_value
        if method == "post":
            return requests.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for links in self.target_list:
            forms = self.extract_forms(links)
            for form in forms:
                print(f"[+] Testing form in {links}")
                is_vulnerable_to_xss = self.xss_test_form(form, links)
                if is_vulnerable_to_xss:
                    print(f"\n\n[ >> ] {links} is vulnerable to xss")
                    print(form)
            if "=" in links:
                print(f"[+] Testing {links}")
                is_vulnerable_to_xss = self.xss_test_link(links)
                if is_vulnerable_to_xss:
                    print(f"\n\n[ >> ] {links} is vulnerable to xss")
                    print(links)

    def xss_test_form(self, form, url):
        xss_payload = "<sCript>alert(1)</scrIpt>"
        response = self.submit_form(url, xss_payload.encode(), form)
        return xss_payload.encode() in response.content

    def xss_test_link(self, url):
        xss_test_script = "<sCript>alert(1)</scrIpt>"
        url = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        return xss_test_script.encode() in response.content
