from graphviz import Digraph

# This code is from Andrej's lecture
# It plots an expression as a graph. 

def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in v._prev:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges


def graph_datapoint(root):
    dot = Digraph(format="svg", graph_attr={'rankdir': 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))

        dot.node(name=uid, label="{ %s | data %.4f }" % (n._label, n.data,), shape="record")
        if n._op:
            dot.node(name=uid+n._op, label=n._op)
            dot.edge(uid+n._op, uid)

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2))+n2._op)
    
    return dot