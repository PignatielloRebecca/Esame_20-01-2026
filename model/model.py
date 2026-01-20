import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()

        self._map_nodi={}
        self._lista_nodi=[]

        self._map_archi=[]


    def load_all_artists(self):
        #self._artists_list = DAO.get_all_artists()
        #print(f"Artisti: {self._artists_list}")
        pass


    def load_artists_with_min_albums(self, min_albums):
        for a in DAO.read_all_artists(min_albums):
            self._map_nodi[a.id]=a
        return self._map_nodi

    def load_generi(self, minimo):

        for g in DAO.read_all_genere(minimo):
            self._map_archi.append(g)
        return self._map_archi


    def build_graph(self, min_albums):

        self._lista_nodi=[id for id in self.load_artists_with_min_albums(min_albums).keys()]
        self._graph.add_nodes_from(self._lista_nodi)

        self._map_archi=self.load_generi(min_albums)

        for i in range(len(self._map_archi)):
            for j in range(i+1,len(self._map_archi)):
                o1=DAO.read_all_genere(min_albums)[i]

                o2=DAO.read_all_genere(min_albums)[j]

                if o1.genere==o2.genere:
                    self._graph.add_edge(o1.id,o2.id)

        return self._graph


