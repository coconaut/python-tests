__author__ = 'coconaut'
import sys

# Dijksta's algorithm for shortest distance between vertices in a graph

class Vertex:
    def __init__(self, key):
        self.key = key
        self.distance = sys.maxint
        self.prev = None
        self.visited = False


# alias for laziness
def _fz(x):
    return frozenset(x)


class Graph:
    # graph will have vertices and edges
    # edge will be a dictionary:
    #   key = frozenset({from_node, to_node})
    #   val = distance

    def __init__(self, vertices, edges):
        # expect vertices: [Vertex]
        self.vertices = {}
        for v in vertices:
            self.add_vertex(v)

        # expect edges: [(from, to, distance)]
        self.edges = {}
        for f, t, d in edges:
            self.add_edge(f, t, d)

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def add_edge(self, from_v, to_v, distance):
        s = _fz([from_v, to_v])
        self.edges[s] = distance

    def get_remaining(self):
        return filter(lambda v: v.visited is False, self.vertices.values())

    def get_min(self):
        vals = self.vertices.values()
        if vals:
            current = None
            current_d = sys.maxint
            for v in vals:
                if v.distance < current_d and v.visited is False:
                    current = v
                    current_d = v.distance
            return current
        else:
            return None

    def get_active_neighbors(self, key):
        # find neighbors
        rel_edges = filter(lambda e: key in e, self.edges)
        verts = []
        for f, t in rel_edges:
            if f != key:
                verts.append(self.vertices[f])
            elif t != key:
                verts.append(self.vertices[t])
        # only return where visited is False
        rem_verts = filter(lambda v: v.visited is False, verts)
        return rem_verts


def dijkstra(graph, source_key):
    # set source distance
    graph.vertices[source_key].distance = 0
    while graph.get_remaining():
        # find min vertex distance-wise
        min = graph.get_min()

        # mark visited
        min.visited = True

        # find neighbors
        neighbors = graph.get_active_neighbors(min.key)

        # loop, see if this path is shorter
        for n in neighbors:
            new_d = min.distance + graph.edges[_fz([min.key, n.key])]
            if new_d < n.distance:
                n.distance = new_d
                n.prev = min

    return graph.vertices


# helper to walk through final distances
def rec_node_walker(node, acc):
    acc.insert(0, node.key)
    if node.prev is not None:
        return rec_node_walker(node.prev, acc)
    else:
        return acc


if __name__ == '__main__':
    # create sample graph problem
    keys = [1, 2, 3, 4, 5, 6]
    vs = [Vertex(i) for i in keys]
    egs = [
        (1, 2, 7),
        (1, 3, 9),
        (1, 6, 14),
        (2, 3, 10),
        (2, 4, 15),
        (3, 4, 11),
        (3, 6, 2),
        (4, 5, 6),
        (5, 6, 9)
    ]

    # create graph
    graph = Graph(vs, egs)

    # find shortest distances from node 1
    res = dijkstra(graph, 1)
    for i in res.values():
        print "%i has min distance %i from %i" % (i.key, i.distance, 1)

    # find shortest path from 1 to 5
    dest = res[5]
    path = rec_node_walker(dest, [])
    print "Shortest path from 1 to 5: %s" % path


# TODO: Bellman-Ford?
