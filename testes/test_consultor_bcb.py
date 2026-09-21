import unittest
from unittest.mock import patch
import requests

from servicos.consultor_bcb import obterValorIndicador

class TestConsultorBCB(unittest.TestCase):

    def test_01_obter_indicador_valido_sucesso(self):
        print("Caso de Teste 01 (BCB) - Busca Selic com sucesso na API real")
       
        valor = obterValorIndicador("selic")
        
        self.assertIsInstance(valor, float)
        self.assertGreater(valor, 0.0)

    def test_02_obter_indicador_invalido_retorna_zero(self):
        print("Caso de Teste 02 (BCB) - Busca indicador inexistente no dicionário")
        
        valor = obterValorIndicador("teste")
        
        self.assertEqual(valor, 0.0)

  
    def test_03_obter_indicador_com_erro_de_conexao(self):
        print("Caso de Teste 03 (BCB) - Simula queda de internet ou erro na API (Deve ativar o Fallback)")
        
        # Usamos o 'patch' para simular que o requests.get disparou uma exceção (queda de rede)
        with patch('requests.get', side_effect=requests.exceptions.ConnectionError):
            valor = obterValorIndicador("cdi")
            
            self.assertEqual(valor, 0.75) #vai para o valor padrão caso a api quebre
            self.assertIsInstance(valor, float)


if __name__ == '__main__':
    unittest.main()