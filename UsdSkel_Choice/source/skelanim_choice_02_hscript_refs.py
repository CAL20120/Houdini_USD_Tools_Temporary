# Script pour choisir et binder différentes animations à un usd skel en un seul layer 
# ce script contient de quoi mettre le script python dans un subnet 

#importation des modules utiles
from pxr import Usd, UsdGeom, UsdSkel # type: ignore (permet d'ignorer une erreur)
import hou # type: ignore (module python houdini)
import os # module permettant d'intéragir avec le système d'exploitation

def bind_animation(stage_path, anim_path): 
    stage = Usd.Stage.Open(stage_path)
    if not stage: 
        raise RuntimeError(f"Impossible d'ouvrir la scène : {stage_path}")

    skel_root_prim = None
    for prim in stage.Traverse():
        if prim.GetTypeName() == "SkelRoot": 
            skel_root_prim = prim
            break

    if not skel_root_prim: 
        raise RuntimeError("Aucun skelroot trouvé dans la scène")
    
    skeleton_prim = None
    for prim in stage.Traverse():
        if prim.GetTypeName() == "Skeleton":
            skeleton_prim = prim
            break        
    if not skeleton_prim:
        raise RuntimeError("Aucun skeleton trouvé dans la scène")

## Maintenant on va trouver animation

    anim_prim = stage.GetPrimAtPath(anim_path)
    if not anim_prim or not anim_prim.IsValid(): 
        raise RuntimeError(f"Aucune animation trouvé dans {anim_path}")

## On va enfin pouvoir bind notre animation
    for prim in stage.Traverse():
        binding = UsdSkel.BindingAPI.Apply(skeleton_prim)
        binding.CreateAnimationSourceRel().SetTargets([anim_prim.GetPath()])
        if not binding:
            raise RuntimeError(f"Pas de bind")
    
    anim_choice = None
    print("Animations disponibles :")
    for prim in stage.Traverse():
        if prim.GetTypeName() == "SkelAnimation":
            print(f"Animation trouvée : {prim.GetName()}")
            anim_choice = prim 
            print(f"{anim_choice}")
    
    for prim in stage.Traverse():
        if prim.GetTypeName() == "Skeleton":
            prim.GetChildrenNames()
            print(f"{prim.GetChildrenNames()}")
            
    
    ### End save layer
    stage.GetRootLayer().Save()

# Bind des variables pour la fonction principale

anim_path="/COW_ASSEMBLY/GEOMETRY/GEO/COW_RIG/Cow_LOD_2/joint1/Animation_02"

usd_path = None
def find_node():
    network = hou.node("/obj/RENDER_SQ")
    node = hou.OpNode()
    return usd_path



def find_layer():
    usd_path = hou.pwd().evalParm("File")
bind_animation(
    stage_path = usd_path,
    anim_path=anim_path,
)

print(f"{stage_path}") #type: ignore

# Test à ignorer 
"""
def Get_collect_prims():
    for prim in stage.GetAllPrims():
        if prim.IsA(UsdSkel.Skelanimation):
            print(f"Animation found: {prim.GetPath()}")
        else:
            raise RuntimeError("NONE_FOUND")
"""
""" 
    prim.GetTargets():
        for target in prim.GetTargets(): 
            print(f"Target found: {target}")
"""
