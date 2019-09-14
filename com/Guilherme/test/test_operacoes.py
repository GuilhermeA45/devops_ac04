from unittest import TestCase
from com.Guilherme.operacoes import Operacoes

class TestOperacoes(TestCase):
	def setUp(self):
		self.operacoes = Operacoes()
	
	def test_multiplicacao(self):
		self.assertEqual(self.operacoes.multiplicacao(5, 2), 10) 