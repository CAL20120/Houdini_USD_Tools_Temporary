import os 
import hou #type: ignore
from nodesearch import parser #type: ignore
import nodesearch #type: ignore

hipdir = os.environ["HIP"]

### cette fonction n'est pas utilisée 
def print_parent():
    node = hou.pwd()
    fileRefs = hou.fileReferences()
    for parm in fileRefs:
        print(parm)
        break
    
network = hou.node("/obj/1_RENDER_SQ")

def find_network():
    if network != None: 
        print(f"network trouvé : {network.path()}")
        return network
    else: 
        print("pas de network")
### network est une vaiable globale

resultats = None
array_resultats = []
def find_node():
    type_matcher = nodesearch.NodeType("sublayer")
    found = False
    for node in network.allSubChildren():
        if type_matcher.matches(node):
            found = True
            array_resultats.append(hou.NetworkMovableItem.name(node))
    resultats = tuple(array_resultats)
    if not found:
        print("aucun node sublayer")
    print(f"{resultats}")

find_node()

### si on voulait sortir la data avec un tuple on peut le faire comme ça
"""""
def find_node():
    type_matcher = nodesearch.NodeType("sublayer")
    found = False
    resultats = tuple(
        node for node in network.allSubChildren()
        if type_matcher.matches(node)
    )   
    if not found:  
        print("pas de node sublayer")
    print(resultats)
    return resultats
"""""
