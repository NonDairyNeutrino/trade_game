import planet

def is_planar(network : list[list[int]], planet_list : list[planet.Planet]) -> bool:
    """
    Algorithm to determin if the given network has no crossing connections.
    Inspired from the Networkx network analysis python package at https://github.com/networkx/networkx
    """
    order = len(planet_list) # number of planets in
    size  = len(network)     # number of connections
    return order > 2 and size > 3 * order - 6

class Test:

    K5 = [[0,1,1,1,1], [1,0,1,1,1], [1,1,0,1,1], [1,1,1,0,1], [1,1,1,1,0]]

    def test_non_planar(self):
        # K_5
        graph_non_planar = self.K5
        print(*graph_non_planar, sep="\n")
        print(f"K-5 is planar: {is_planar(graph_non_planar, [1 for i in range(5)])}")

    def test_planar(self):
        # K_4
        graph_non_planar = self.K5
        graph_planar     = [[graph_non_planar[i][j] for j in range(len(graph_non_planar) - 1)] for i in range(len(graph_non_planar) - 1)]
        print(*graph_planar, sep="\n")
        print(f"K-4 is planar: {is_planar(graph_planar, [1 for i in range(4)])}")

if __name__ == "__main__":
    test = Test()
    test.test_non_planar()
    test.test_planar()