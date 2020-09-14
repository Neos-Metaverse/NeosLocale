#!/bin/env python3

## All data is derived from distrowatch.com and wikipedia.

from googletrans import Translator, LANGUAGES
import json
import copy

LANGFOLDER = "LANG/"
t = Translator()
#for key in LANGUAGES:
#    print(key, "->", LANGUAGES[key])
for item in LANGUAGES.items():
    with open(LANGFOLDER+'base.json') as JSONfile:
        DATA = json.load(JSONfile)
    print(f"Translating NEOS Language File to {item[0]}.")
    DATA["localeCode"] = item[0]
    for key in DATA["messages"].items():
        if key[1] != "":
            DATA["messages"][key[0]] = t.translate(key[1], src='en', dest=item[0]).text
            print(f"[{item[0]}]{key[0]}: {key[1]} -> {DATA['messages'][key[0]]}")
    with open(LANGFOLDER+item[0]+".json",'w') as jsonfile:
        json.dump(DATA,jsonfile)