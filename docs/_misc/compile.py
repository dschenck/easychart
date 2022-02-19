# coding: utf-8
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

import sys

sys.path.append("../../../easychart")  # add the easychart path

import re
import json
import easychart

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "examples")

contents = []
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        contents.append(f"# {filename}")
        with open(os.path.join(directory, filename), "r") as file:
            contents.extend(file.read().strip().split("\n"))
            contents.append(
                f"chart.save(\"../static/charts/{filename.replace('py','json')}\", indent=4)"
            )
        contents.append("\n")

exec("\n".join(contents))

# run the make html
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
os.system("make clean")
os.system("make html")
