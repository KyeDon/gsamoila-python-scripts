#!/usr/bin/env python3

import base64
import re

print("Choose what you what to do:")
print("1 Decode from base16")
print("2 Decode from base32")
print("3 Decode from base64")
choice = int(input("Pick a number: "))
times = int(input("How many times do you want to run the encoder: "))
location = input("Please enter the file location: ")


def decode16():
    data = open(location, "r").read()
    decode = base64.b16decode(data.strip(), casefold=True)
    file = open(location, "w")
    file.write(f'{decode}')
    file.close()
    with open(location, "r+") as f:
        text = f.read()
        text = re.sub("^b", "", text)
        text = re.sub("\'", "", text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
    print(decode)


def decode32():
    data = open(location, "r").read()
    decode = base64.b32decode(data.strip(), casefold=True)
    file = open(location, "w")
    file.write(f'{decode}')
    file.close()
    with open(location, "r+") as f:
        text = f.read()
        text = re.sub("^b", "", text)
        text = re.sub("\'", "", text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
    print(decode)


def decode64():
    data = open(location, "r").read()
    decode = base64.b64decode(data.strip())
    file = open(location, "w")
    file.write(f'{decode}')
    file.close()
    with open(location, "r+") as f:
        text = f.read()
        text = re.sub("^b", "", text)
        text = re.sub("\'", "", text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
    print(decode)


if choice == 1:
    for _ in range(times):
        decode16()
elif choice == 2:
    for _ in range(times):
        decode32()
else:
    for _ in range(times):
        decode64()