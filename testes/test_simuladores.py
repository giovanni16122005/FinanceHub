import unittest

from entidades.CalculoFinanceiro import (
    calcularJurosCompostos,
    calcularRendaPassiva
)


class TestSimuladores(unittest.TestCase):

    def test_01_calcular_juros_compostos(self):
        print("Caso de Teste 01 - Cálculo de juros compostos")

        resultado = calcularJurosCompostos(
            valorInicial=1000,
            aporte=0,
            taxa=0.01,
            tempo=12
        )

        self.assertGreater(resultado, 1000)

    def test_02_calcular_renda_passiva(self):
        print("Caso de Teste 02 - Cálculo de renda passiva")

        resultado = calcularRendaPassiva(
            valorTotal=100000,
            taxaRetirada=0.04
        )

        self.assertEqual(resultado, 4000)

    def test_03_juros_compostos_parametros_invalidos(self):
        print("Caso de Teste 03 - Juros compostos com parâmetros inválidos")

        resultado = calcularJurosCompostos(
            valorInicial=-1000,
            aporte=0,
            taxa=0.01,
            tempo=12
        )

        self.assertEqual(resultado, 0.0)

    def test_04_renda_passiva_parametros_invalidos(self):
        print("Caso de Teste 04 - Renda passiva com parâmetros inválidos")

        resultado = calcularRendaPassiva(
            valorTotal=-1000,
            taxaRetirada=0.04
        )

        self.assertEqual(resultado, 0.0)


if __name__ == "__main__":
    unittest.main()
