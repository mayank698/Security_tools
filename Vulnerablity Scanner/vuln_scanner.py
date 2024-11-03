#!usr/bin/env python

import scanner_class

target_url = "http://192.168.164.130/dvwa/"
links_to_ignore = ["http://192.168.164.130/dvwa/logout.php"]
data_dict = {"username":"admin","password":"password","Login":"submit"}
scanner = scanner_class.Scanner(target_url,links_to_ignore)
scanner.session.post("http://192.168.164.130/dvwa/login.php",data = data_dict)
scanner.crawl()
scanner.run_scanner()