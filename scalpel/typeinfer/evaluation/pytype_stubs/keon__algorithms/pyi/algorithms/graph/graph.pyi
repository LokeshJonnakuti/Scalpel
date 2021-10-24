# (generated with --quick)

from typing import Any, Dict, List

class DirectedEdge:
    nf: Any
    nt: Any
    def __eq__(self, obj) -> Any: ...
    def __init__(self, node_from, node_to) -> None: ...
    def __repr__(self) -> str: ...

class DirectedGraph:
    adjmt: Dict[Node, List[Node]]
    edges: List[DirectedEdge]
    nodes: List[Node]
    def __init__(self, load_dict = ...) -> None: ...
    def add_edge(self, node_name_from, node_name_to) -> None: ...
    def add_node(self, node_name) -> Node: ...

class Graph:
    V: Any
    graph: Dict[Any, list]
    tc: list
    def __init__(self, vertices) -> None: ...
    def add_edge(self, u, v) -> None: ...

class Node:
    name: Any
    def __bool__(self) -> Any: ...
    def __eq__(self, obj) -> Any: ...
    def __ge__(self, obj) -> Any: ...
    def __gt__(self, obj) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, name) -> None: ...
    def __le__(self, obj) -> Any: ...
    def __lt__(self, obj) -> Any: ...
    def __ne__(self, obj) -> Any: ...
    def __repr__(self) -> Any: ...
    @staticmethod
    def get_name(obj) -> Any: ...