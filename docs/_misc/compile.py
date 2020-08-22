# coding: utf-8
import os 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

import sys
sys.path.append("../../../easychart") #add the easychart path

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
            contents.append(f"chart.save(\"../static/charts/{filename.replace('py','json')}\", indent=4)")
        contents.append("\n")        
                
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "compiled.py"), "w") as f: 
    f.write("\n".join(contents))

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "compiled.py"), "r") as f: 
    exec(f.read())

for filename in os.listdir(directory):
    if filename.endswith(".rst"):
        contents = []
        with open(os.path.join(directory, filename), "r") as file:
            for line in file.read().split("\n"):
                if re.match(r"^\s+$", line):
                    continue
                if line.startswith(".. easychart:chart"): 
                    chart = line.split(":")[-1]

                    contents.append(".. raw:: html \n")
                    contents.append(f'    <div class="chart-container" style="min-height:400px" data-filename="../../_static/charts/{chart}.json?v=1"></div>')
                    contents.append("\n")
                    contents.append(f".. literalinclude:: /_misc/examples/{chart}.py")
                else:
                    contents.append(line)
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../contents/examples", filename), "w") as file:
            file.write("\n".join(contents))

#run the make html
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
os.system("make clean")
os.system("make html")
