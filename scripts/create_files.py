#!/usr/bin/python3
# -*- coding: UTF-8 -*-`

import re
import os
import sys
from enum import Enum
from pathlib import Path
from tracemalloc import start

def is_species(name):
    return not any([char in name for char in ["界", "门", "纲", "科", "目", "现象"]])

format_check = False
try:
    format_check = sys.argv[1]
except:
    pass

AnimalAttributeList = [
    "| 别称|",
    "| 属|",
    "| 分布|",
    "| 寿命|",
    "| 外形特征|",
    "| 食性|",
    "| 习性|",
    "| 繁殖|",
]
def get_animal_attribute():
    return ["\n\n|属性|说明|\n","| ---- | ---- |\n"]+ [mem+"|\n" for mem in AnimalAttributeList]+["\n"]

PlantAttributeList =[
    "| 别称|",
    "| 属|",
    "| 分布|",
    "| 寿命|",
    "| 外形特征|",
    "| 繁殖|",
]
def get_plant_attribute():
    return ["\n\n|属性|说明|\n","| ---- | ---- |\n"]+ [mem+"|\n" for mem in PlantAttributeList]+["\n"]

FungiAttributeList = [
    "| 别称|",
    "| 属|",
    "| 生长环境|",
    "| 外形特征|",
    "| 繁殖|",
]
def get_fungi_attribute():
    return ["\n\n|属性|说明|\n","| ---- | ---- |\n"]+ [mem+"|\n" for mem in FungiAttributeList]+["\n"]

with open("_sidebar.md") as file:
    lines = file.readlines()
    for line in lines:
        matchs = re.search("\(..+\)", line)
        if not matchs:
            continue
        file_name = matchs.group(0)[1:-1]
        md_file = Path(file_name)
        if not os.path.isfile(file_name):
            print("Create file: " + file_name)
            folder_name = "/".join(file_name.split("/")[:-1])
            os.makedirs(folder_name, exist_ok=True)
            # Add documents to each category
            md_file.touch(exist_ok=True)
            with open(md_file, "a") as doc_file:
                doc_file.writelines(["# " + file_name.split("/")[-1][:-3]])
                doc_file.writelines(["\n\n"])
                if "现象" in file_name:
                    pass
                elif is_species(file_name.split("/")[-1][:-3]) and "动物界" in file_name:
                    doc_file.writelines(get_animal_attribute())
                elif is_species(file_name.split("/")[-1][:-3]) and "植物界" in file_name:
                    doc_file.writelines(get_plant_attribute())
                elif is_species(file_name.split("/")[-1][:-3]) and "真菌界" in file_name:
                    doc_file.writelines(get_fungi_attribute())
                doc_file.writelines(["参考:\n"])
        # Format document
        elif format_check:
            if "现象" not in file_name and is_species(file_name.split("/")[-1][:-3]) and "动物界" in file_name:
                with open(md_file, 'r') as doc_file:
                    content = doc_file.readlines()
                rewrite = False
                if not any(["|属性|" in line for line in content]):
                    new_content = content + get_animal_attribute()
                    rewrite = True
                else:
                    target_ind = 0
                    target = AnimalAttributeList[target_ind]
                    new_content = content
                    count = 0
                    check_line = 0
                    for ind in range(len(content)):
                        if '|属性|' in content[ind]:
                            check_line = ind+2
                    for ind in range(len(AnimalAttributeList)):
                        if AnimalAttributeList[ind] not in new_content[check_line]:
                            rewrite = True
                            new_content.insert(check_line, AnimalAttributeList[ind]+"|\n")
                        check_line+=1
                if rewrite:
                    print(file_name)
                    with open(md_file, 'w') as doc_file:
                        doc_file.writelines(new_content)
