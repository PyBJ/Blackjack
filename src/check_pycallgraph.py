from pycallgraph2 import PyCallGraph
from pycallgraph2 import Config as graph_config
from pycallgraph2.output import GraphvizOutput

output_config = graph_config(max_depth=7)
graphviz = GraphvizOutput(output_file="UML_Diagram22.png")


with PyCallGraph(output=graphviz, config=output_config):
    def my_fun():
        print("HELLO")
    my_fun()
