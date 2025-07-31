import os 
import hou  #type: ignore

hipdir = os.environ["HIP"]

file_Extensions = [".usd", ".usda", ".usdz"]

fileRefs = hou.fileReferences()

for parm, path in fileRefs: 
    if path.lower().endswith(tuple(file_Extensions)):
        print(parm)

