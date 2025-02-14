#!/bin/python3

import base64
import argparse
import os

banner = f"""\033[35m██████╗ ██████╗  █████╗ ███████╗███████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║
██████╔╝██████╔╝███████║███████╗█████╗  ███████╗ ███████║
██╔══██╗██╔══██╗██╔══██║╚════██║██╔══╝  ██╔═══██╗╚════██║
██████╔╝██████╔╝██║  ██║███████║███████╗╚██████╔╝     ██║
╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝      ╚═╝
\033[39m
"""
print(banner)

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--decode", action="store_true")
parser.add_argument("-e", "--encode", action="store_true")
parser.add_argument("-f", "--file")
parser.add_argument("-t", "--text")
parser.add_argument("-o", "--output")
parser.add_argument("-r", "--repeat")
parser.add_argument("-du", "--data_url")

args = parser.parse_args()

text = ""

if args.file:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
    }
    if args.file.startswith("https://") or args.file.startswith("http://"):
        try:
            import requests
        except Exception:
            print("You need the requests module to use this")
            exit()
        print("Grabbing Source Code")
        res = requests.get(args.textorfile, headers=headers, allow_redirects=True)
        print("Grabbed Code")
        text = res.text
        
    elif os.path.exists(args.file):
        with open(args.file, "r") as f:
            text = f.read()
    else:
        print("That is not a file path")
        exit()

if args.text:
    text = args.text

if args.repeat:
    try:
        repeat = int(args.repeat)
    except Exception:
        print("Not a real number...")
else:
    repeat = 0

if args.decode:
    try:
        if repeat != 0:
            decoded_text = text
            for i in range(repeat):
                decoded_text = base64.urlsafe_b64decode(decoded_text.replace("-", "+").replace("_", "/").replace("\\", "/").encode()).decode()
        else:
            decoded_text = base64.urlsafe_b64decode(text.replace("-", "+").replace("_", "/").replace("\\", "/").encode()).decode()
        if args.output:
            with open(args.output, "w+") as f:
                f.write(decoded_text)
        else:
            print(decoded_text)
    except Exception:
        print("Invalid Base64")
if args.encode:
    if repeat != 0:
        encoded_text = text
        for i in range(repeat):
            encoded_text = base64.urlsafe_b64encode(encoded_text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
    else:
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
    if args.output:
        with open(args.output, "w+") as f:
            f.write(encoded_text)
    else:
        print(encoded_text)

if args.data_url:
    if args.data_url == "help":
        print("Data URL Options:")
        print("png: Makes a image/png")
        print("jpg: Makes a image/jpg")
        print("text: Makes a text/plain")
        print("html: Makes a text/html")
    elif args.data_url == "png":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
        url = f"data:image/png;base64,{encoded_text}"
    elif args.data_url == "jpf":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
        url = f"data:image/jpg;base64,{encoded_text}"
    elif args.data_url == "text":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
        url = f"data:text/plain;base64,{encoded_text}"
    elif args.data_url == "html":
        encoded_text = base64.urlsafe_b64encode(text.encode()).decode().replace("-", "+").replace("_", "/").replace("\\", "/")
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
        if args.output:
            with open(args.output, "w+") as f:
                f.write(url)
        else:
            print(url)
