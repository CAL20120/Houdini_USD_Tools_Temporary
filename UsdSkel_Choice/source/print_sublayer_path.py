# https://www.sidefx.com/docs/houdini/hom/hou/NodeConnection.html
# https://www.sidefx.com/docs/houdini/hom/hou/nodeType_.html
import os 
import hou #type: ignore 

hipdir = os.environ["HIP"]
node = hou.pwd()
file_parm = "filepath1"

def print_parent():
    node = hou.pwd()
    parent_node = node.parent()
    parm = parent_node.parm('filepath1')
    if parm is not None: 
        print(parm.path())
    else : 
        print("Aucun paramètre trouvé")
    
print_parent()

def print_path_attribute(): 
    parent_node = node.parent()
    parm_layer = parent_node.parm(file_parm)
    if parm_layer is not None: 
        print(hou.OpNodeConnection(node))
    else: 
        print("pas de layer connexion")

print_path_attribute()

def path_attribute(): 
    fileRefs = hou.fileReferences()
    for parm, path in fileRefs:
        print(parm)
        
def find_parent_attribute():
    while node in hou.OpNodeConnections(): 
        if hou.nodeType() == "sublayer": 
            hou.getName()
            print(f"{hou.getName()}") 
        else : 
            print("pas de parent trouvé")