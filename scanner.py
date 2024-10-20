import requests


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


url = "192.168.164.130/mutillidae"
with open("../../../usr/share/wordlists/dirb/common.txt", "r") as wordlists_file:
    for lines in wordlists_file:
        words = lines.strip()
        test_url = url + "/" + words
        response = request(test_url)
        if response:
            print(f"[+] Discovered URL --> {test_url}")
        
