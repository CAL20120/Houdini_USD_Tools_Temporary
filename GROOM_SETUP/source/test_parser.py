import nodesearch 
from nodesearch import parser
network = hou.node("/obj")

matcher = parser.parse_query("rop_*")
for node in matcher.nodes(network, recursive = True):
    rest_path = node.path()
    rest_node = node.name()