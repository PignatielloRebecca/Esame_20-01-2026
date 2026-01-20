import flet as ft
import networkx as nx

from UI.view import View
from model.model import Model
from database.dao import DAO

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def popola_dropdown(self):
        try:
            numero=int(self._view.txtNumAlbumMin.value)
        except:
            self._view.show_alert('inserire un numero')
        artisti=DAO.read_all_artists(numero)
        return artisti






    def handle_create_graph(self, e):
        try:
            numero=int(self._view.txtNumAlbumMin.value)
        except:
            self._view.show_alert('inserire un numero')
        if numero < 0:
            self._view.show_alert('inserire maggiore')
            return

        self._model.build_graph(numero)

        self._view._title.controls.append(ft.Text(f" numero nodi {self._model._graph.number_of_nodes()}, numero di archi {self._model._graph.number_of_edges()}"))

        self._view._page.update()

    def handle_connected_artists(self, id_artista):

        node=nx.node_connected_components(id_artista)





