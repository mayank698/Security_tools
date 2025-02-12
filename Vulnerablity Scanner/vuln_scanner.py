#!usr/bin/env python

import scanner_class
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Specify the target.")
    parser.add_argument("-i", "--ignore", dest="ignore",
                        help="Specify links to ignore if any.")
    parser.add_argument("-c", "--crawl", dest="crawl", help="Use crawler.")
    options = parser.parse_args()
    if not options.target:
        parser.error("[+] Please specify the target. Type `-h` for help.")
    return options


options = get_arguments()
if options.target:
    target_url = options.target
    links_to_ignore = options.ignore
    data_dict = {"username": "admin", "password": "password", "Login": "submit"}
    scanner = scanner_class.Scanner(target_url, links_to_ignore)
    scanner.session.post("http://192.168.164.130/dvwa/login.php", data=data_dict)
    scanner.run_scanner()
    if options.crawl:
        scanner.crawl()
