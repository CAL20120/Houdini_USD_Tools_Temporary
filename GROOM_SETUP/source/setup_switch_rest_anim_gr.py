import nodesearch #type: ignore
from nodesearch import parser #type: ignore
import hou #type: ignore

network = hou.node("/obj")
def find_network():
    matcher_net = nodesearch.NodeType("lopnet")
    for node in network.children():
        if matcher_net.matches(node):
            lop_path = hou.node(
                node.path()
            )
        else: 
            raise RuntimeError("pas de lopnet")
    return lop_path


#### EXECUTE ROP REST FUNCTION
matcher_name_rop = parser.parse_query("rop_rest")
found = None
def execute_rop_rest():
    found = False
    for node in matcher_name_rop.nodes(find_network(), recursive = True):
        found = True
        rest_node = hou.node(node.path())
    if not found: 
        print("pas de node : \n Rop Rest")
    parm_execute = rest_node.parm("execute")
    parm_execute.pressButton()



matcher_name_rop_anim = parser.parse_query("rop_anim")
def execute_rop_anim():
    found = False
    for node in matcher_name_rop_anim.nodes(find_network("lopnet"), recursive = True):
        found = True
        anim_node = hou.node(node.path())
    if not found: 
        print("pas de node : \n Rop Anim")
    parm_execute = anim_node.parm("execute")
    parm_execute.pressButton()