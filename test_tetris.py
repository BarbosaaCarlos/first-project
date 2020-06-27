#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""Esse arquivo tem os testes para o tetris.

Os testes presentes nesse arquivo usam o unittest (default) para escrever casos de teste.
Para rodar os testes, favor rodar:
    `python3 test_tetris.py`

E observar o relatório gerado, que não tenha erros. Ou seja, um "OK" no final, invés de "FAILED".
"""

import unittest
import sys

try:
    from tetris import WIN_HEIGHT, WIN_WIDTH, mover_peca
except Exception as e:
    print("Falha ao importar 'tetris'. Está nesta pasta?")
    print(e)
    sys.exit(1)


# constantes para simular as teclas
K_LEFT = 276
K_RIGHT = 275
K_DOWN = 274
K_UP = 273

class TestTetris(unittest.TestCase):

    def test_move_peca_esquerda_falha(self):
        ret_x, ret_y = mover_peca(K_LEFT, 0, 0, 10, 10)
        self.assertEqual(ret_x, 0, "bloco em 0x0: impossivel ir para a esquerda")
    def test_move_peca_esquerda_livre(self):
        ret_x, ret_y = mover_peca(K_LEFT, 490, 0, 10, 10)
        self.assertLess(ret_x, 490, "bloco em 490x0: é possivel ir para a esquerda")

    def test_move_peca_abaixo_falha(self):
        ret_x, ret_y = mover_peca(K_DOWN, 0, 490, 10, 10)
        self.assertEqual(ret_y, 0, "não deve mudar o Y, já está a esquerda no fundo")
    def test_move_peca_abaixo_livre(self):
        ret_x, ret_y = mover_peca(K_DOWN, 0, 0, 10, 10)
        self.assertGreater(ret_y, 0, "bloco em 0x0: é possivel descer")

    def test_move_peca_direita_falha(self):
        ret_x, ret_y = mover_peca(K_RIGHT, 490, 0, 10, 10)
        self.assertEqual(ret_x, 490, "bloco de 10x10 em 490x0: impossivel ir para a direita")
    def test_move_peca_direita_livre(self):
        ret_x, ret_y = mover_peca(K_RIGHT, 0, 0, 10, 10)
        self.assertGreater(ret_x, 0, "bloco de 10x10 em 0x0: é possivel ir para a direita")

    def test_move_peca_acima_falha(self):
        ret_x, ret_y = mover_peca(K_UP, 0, 0, 10, 10)
        self.assertEqual(ret_y, 0, "bloco de 10x10 em 0x0: impossivel ir para cima")
    def test_move_peca_acima_livre(self):
        ret_x, ret_y = mover_peca(K_UP, 0, 490, 10, 10)
        self.assertLess(ret_y, 490, "bloco de 10x10 em 490x0: é possivel ir para a cima")

if __name__ == '__main__':
    unittest.main()