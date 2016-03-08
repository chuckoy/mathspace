import unittest
from graph import Graph


class LoadFileTest(unittest.TestCase):
    """
    Test if app can successfully load file into memory
    """

    def setUp(self):
        f = open('tests/testfile.txt', 'r')
        self._f = f

    def testContentsOfFile(self):
        content = "46B E59 EA C1F 45E 63\n899 FFF 926 7AD C4E FFF"
        self.assertEqual(content, self._f.read())

    def testDownRightGraphConstruction(self):
        content = ("46B E59\n" +
                   "899 FFF")
        graph = Graph(content, mode="dr")
        vertices = {1: int("46B", 16), 2: int("E59", 16),
                    3: int("899", 16), 4: int("FFF", 16)}
        self.assertEqual(vertices, graph.vertices)
        edges = set([('1', '2', 'r'), ('1', '3', 'd'), ('2', '4', 'd'),
                     ('3', '4', 'r')])
        self.assertEqual(edges, graph.edges)

    def testFreeGraphConstruction(self):
        content = ("46B E59 EA\n" +
                   "899 FFF 926\n" +
                   "7AD C4E 63")
        graph = Graph(content, mode="free")
        vertices = {1: int("46B", 16), 2: int("E59", 16),
                    3: int("EA", 16), 4: int("899", 16),
                    5: int("FFF", 16), 6: int("926", 16),
                    7: int("7AD", 16), 8: int("C4E", 16),
                    9: int("63", 16)}
        self.assertEqual(vertices, graph.vertices)
        edges = set([('1', '2', 'r'), ('1', '4', 'd'), ('2', '1', 'l'),
                     ('2', '3', 'r'), ('2', '5', 'd'), ('3', '2', 'l'),
                     ('3', '6', 'd'), ('4', '1', 'u'), ('4', '5', 'r'),
                     ('4', '7', 'd'), ('5', '2', 'u'), ('5', '4', 'l'),
                     ('5', '6', 'r'), ('5', '8', 'd'), ('6', '3', 'u'),
                     ('6', '5', 'l'), ('6', '9', 'd'), ('7', '4', 'u'),
                     ('7', '8', 'r'), ('8', '5', 'u'), ('8', '7', 'l'),
                     ('8', '9', 'r'), ('9', '6', 'u'), ('9', '8', 'l')])
        self.assertEqual(edges, graph.edges)

        content = ("5 4 3\n" +
                   "2 1")
        graph = Graph(content, mode="free")
        vertices = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
        self.assertEqual(vertices, graph.vertices)
        edges = set([('1', '2', 'r'), ('1', '4', 'd'), ('2', '1', 'l'),
                     ('2', '3', 'r'), ('2', '5', 'd'), ('3', '2', 'l'),
                     ('4', '1', 'u'), ('4', '5', 'r'), ('5', '2', 'u'),
                     ('5', '4', 'l')])
        self.assertEqual(edges, graph.edges)

    def testDijkstrasAlgo(self):
        content = ("46B E59\n" +
                   "899 FFF")
        graph = Graph(content, mode="dr")
        solution = 'd,r'
        self.assertEqual(solution, graph.dijkstra())
        content = ("0 0 0 0 0 5\n" +
                   "5 5 5 5 0 5\n" +
                   "0 0 0 5 0 5\n" +
                   "0 5 0 0 0 5\n" +
                   "0 5 5 5 5 5\n" +
                   "0 0 0 0 0 0")
        graph = Graph(content, mode="free")
        solution = 'r,r,r,r,d,d,d,l,l,u,l,l,d,d,d,r,r,r,r,r'
        self.assertEqual(solution, graph.dijkstra())

    def testConstructPath(self):
        content = ("46B E59\n" +
                   "899 FFF")
        graph = Graph(content, mode="dr")
        path = 'd,r'
        self.assertEqual(path, graph.construct_path(['4', '3', '1']))

    def tearDown(self):
        self._f.close()

if __name__ == "__main__":
    unittest.main()
