import ordenacaoPOO
import pytest
import Contatempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):

        return Algoritmos_de_Ordenacao.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = Contatempos.ContaTempos()

        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = Contatempos.ContaTempos()

        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):

        for i in range(len(l) - 1):

            if l[i] > l[i + 1]:

                return False

            return True

    def test_bubble_curto_aleat(self, o, l_aleat):
        o.bubble_curto(l_aleat)

        assert self.esta_ordenada(l_aleat)

    def test_selection_sort_aleat(self, o, l_aleat):
        o.selection_sort(l_aleat)

        assert self.esta_ordenada(l_aleat)

    def test_bubble_curto_quas_aleat(self, o, l_quase):
        o.bubble_curto(l_quase)

        assert self.esta_ordenada(l_quase)

    def test_selection_sort_quas_aleat(self, o, l_quase):
        o.selection_sort(l_quase)

        assert self.esta_ordenada(l_quase)
        
