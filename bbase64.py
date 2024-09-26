#!/bin/python3

import base64
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--decode", action="store_true")
parser.add_argument("-e", "--encode", action="store_true")
parser.add_argument("-f", "--file", action="store_true")
parser.add_argument("-du", "--data_url")
parser.add_argument("textorfile")

args = parser.parse_args()

text = ""

if args.file:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
    }
    if args.textorfile.startswith("https://") or args.textorfile.startswith("http://"):
        try:
            import requests
        except Exception:
            print("You need the requests modual to use this")
            exit()
        print("Grabbing Source Code")
        res = requests.get(args.textorfile, headers=headers, allow_redirects=True)
        print("Grabbed Code")
        text = res.text
        
    elif os.path.exists(args.textorfile):
        with open(args.textorfile, "r") as f:
            text = f.read()
    else:
        text = args.textorfile
else:
    text = args.textorfile

if args.decode:
    decoded_text = base64.urlsafe_b64decode(text.encode()).decode()
    print(decoded_text)
if args.encode:
    encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/")
    print(encoded_text)

if args.data_url:
    if args.data_url == "help":
        print("Data URL Options:")
        print("png: Makes a image/png")
        print("jpg: Makes a image/jpg")
        print("text: Makes a text/plain")
        print("html: Makes a text/html")
    elif args.data_url == "png":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/")
        url = f"data:image/png;base64,{encoded_text}"
    elif args.data_url == "jpf":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/")
        url = f"data:image/jpg;base64,{encoded_text}"
    elif args.data_url == "text":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/")
        url = f"data:text/plain;base64,{encoded_text}"
    elif args.data_url == "html":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/")
        url = f"data:text/html;base64,{encoded_text}"
    else:
        url = "Invalid Option"
    
    if url == "Invalid Option":
        print("That is an invalid option")
        print("Data URL Options:")
        print("png: Makes a image/png")
        print("jpg: Makes a image/jpg")
        print("text: Makes a text/plain")
        print("html: Makes a text/html")
    else:
        print(url)