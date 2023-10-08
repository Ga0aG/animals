#!/usr/bin/python
# -*- coding: UTF-8 -*-`

import re

content = []
with open("ompl.md") as file:
    content = file.readlines()[1:]

new_contents = []
current_level = 1
prefix = ""
for line in content:
    level = line.find("-")/2
    match = re.search("\[.*\]",line)
    if not match:
        continue
    name = match.group(0)[1:-1]
    if level == 1:
        prefix=name+"/"
    else:
        if level > current_level+1:
            print("Wrong")
            break
        prefix_level = prefix.split("/")
        prefix = "/".join(prefix_level[:int(level-1)])+"/"
        prefix = prefix+name+"/"
    current_level = level
    new_line = line[:-1]+"("+prefix+name+".md)\n"
    new_contents.append(new_line)


with open("_sidebar.md","w") as file:
    file.write("<!-- docs/_sidebar.md -->\n")
    file.write("\n")
    file.write("- [主页](/)\n")
    file.writelines(new_contents)

