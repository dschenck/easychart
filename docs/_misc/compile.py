# coding: utf-8
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

import sys

sys.path.append("../../../easychart")  # add the easychart path

import re
import json
import easychart

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")

for filename in os.listdir(directory):
    if not filename.endswith(".py"):
        continue

    with open(os.path.join(directory, filename), "r") as file:
        contents = file.read().strip()
        contents += "\n"
        contents += f"chart.save(\"../static/charts/{filename.replace('py','json')}\", indent=4)"
    try:
        exec(contents)
    except Exception as e:
        print(f"Error compiling {filename} ({e})")

# run the make html
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
os.system("make clean")
os.system("make html")
