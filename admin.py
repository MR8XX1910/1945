#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def Space(j):
    print(" " * j, end="")

def findAdmin(file_path, site_link):
    try:
        with open(file_path, "r") as f:
            print("\n\nAvailable links : \n")
            for sub_link in f:
                sub_link = sub_link.strip()
                if not sub_link:
                    continue
                req_link = "http://" + site_link + "/" + sub_link
                req = Request(req_link)
                try:
                    response = urlopen(req)
                except HTTPError:
                    print(f"\033[91mNOT OK => {req_link}\033[0m")  # Red color for failed attempts
                    continue
                except URLError:
                    print(f"\033[91mNOT OK => {req_link}\033[0m")  # Red color for failed attempts
                    continue
                else:
                    print(f"\033[92mOK => {req_link}\033[0m")  # Green color for successful attempts
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def Credit():
    Space(9)
    print(" ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂( ☠ )▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")
    Space(9)
    print("           ┃   +++    Admin Login Web    +++    ┃")
    Space(9)
    print("           ┃         Script by Mr.8xx           ┃")
    Space(9)
    print("           ┃           t.me/MR.8XX              ┃")
    Space(9)
    print(" ▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂( ☠ )▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂")

if __name__ == "__main__":
    Credit()
    file_path = input("Enter the path to the link.txt file: ")
    site_link = input("Enter Site Name \n(ex : example.com or www.example.com ): ")
    findAdmin(file_path, site_link)
