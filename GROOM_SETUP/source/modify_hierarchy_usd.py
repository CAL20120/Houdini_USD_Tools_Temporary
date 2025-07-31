from pxr import Usd, UsdGeom  #type: ignore
import nodesearch
from nodesearch import parser
import hou

network = hou.node("/obj")
def focus_net(type_net):
    matcher_lop = nodesearch.NodeType(type_net)
    for node in network.allSubChildren():
        lop_net = matcher_lop.matches(node)
        print(node.path())
        break
    else: 
        print("pas de network")
focus_net("lopnet")



stage = Usd.Stage.Open()

for prim in stage.Traverse():
    prim_curves =  prim.GetTypeName() == "BasicsCurves"
    print(prim_curves)
    prim_curves_path = prim_curves.GetPath()


prim_curve = stage_ref.RedefinePrim(prim_curves_path, 'BasicsCurves')