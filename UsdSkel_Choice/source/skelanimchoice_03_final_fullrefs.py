# Script pour choisir et binder différentes animations à un usd skel en un seul layer 
# ce script contient de quoi mettre le script python dans un subnet 

from pxr import Usd, UsdGeom, UsdSkel # type: ignore
import hou # type: ignore
import os
import nodesearch #type: ignore
from nodesearch import parser #type: ignore

### Définir le node à rechercher et trouver le path du parm filepath
## définir les variables importantes 
hipdir = os.environ["HIP"]
network_obj = hou.node("/obj/")    

### cette fonction n'est pas utilisée 
def print_parent():
    node = hou.pwd()
    fileRefs = hou.fileReferences()
    for parm in fileRefs:
        break

def find_network():
    type_matcher_net = nodesearch.NodeType("lopnet")
    for node in network_obj.children():
        if type_matcher_net.matches(node):
            lop_path = hou.node(node.path())
        else:
            print("rien")
    return lop_path


def find_node():
    matcher = parser.parse_query("ANIM_INDEX_ROOT_PTH")
    for node in matcher.nodes(find_network(), recursive = True):
        node_anims = hou.node(node.path())
        parm_anim_index = node_anims.evalParm("filepath1")
    return parm_anim_index


### Maintenant on peut venir chercher nos anims et les bind
def bind_animation(stage_path, anim_path): 
    stage = Usd.Stage.Open(stage_path)
    if not stage: 
        print(f"Impossible d'ouvrir la scène : {stage_path}")

    skel_root_prim = None
    for prim in stage.Traverse():
        if prim.GetTypeName() == "SkelRoot": 
            skel_root_prim = prim
            break

    if not skel_root_prim: 
        print("Aucun skelroot trouvé dans la scène")
    
    skeleton_prim = None
    for prim in stage.Traverse():
        if prim.GetTypeName() == "Skeleton":
            skeleton_prim = prim
            skel_prims = True
            break        
    if not skeleton_prim:
        print("Aucun skeleton trouvé dans la scène")

## Maintenant on va trouver animation
    anim_prim = stage.GetPrimAtPath(anim_path)
    if not anim_prim or not anim_prim.IsValid(): 
        skel_prims = False
        print(f"Aucune animation trouvé dans {anim_path}")
        
        

## On va enfin pouvoir bind notre animation
    found = False
    for prim in stage.Traverse():
        if skel_prims == True:
            binding = UsdSkel.BindingAPI.Apply(skeleton_prim)
            binding.CreateAnimationSourceRel().SetTargets([anim_prim.GetPath()])
        else:
            print("pas de bind")
    
    anim_choice = None
    for prim in stage.Traverse():
        if prim.GetTypeName() == "SkelAnimation":
            anim_choice = prim 
    
    for prim in stage.Traverse():
        if prim.GetTypeName() == "Skeleton":
            prim.GetChildrenNames()
            
    ### End save layer
    stage.GetRootLayer().Save()

node_hda_kw = hou.pwd().parent()
anim_path = node_hda_kw.evalParm("anim_path_prim")

bind_animation(
    stage_path=find_node(),
    anim_path=anim_path,
)
