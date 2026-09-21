# Apresenta as funções públicas do módulo
__all__ = [
    "calcularJurosCompostos",
    "ajustarPorInflacao",
    "calcularRendaPassiva"
]


#encapsulado

def _calcularFatorJuros(taxa: float, tempo: int) -> float:
    return (1 + taxa) ** tempo



def calcularJurosCompostos(
    valorInicial: float,
    aporte: float,
    taxa: float,
    tempo: int,
) -> float:

    if valorInicial < 0 or aporte < 0 or taxa < 0 or tempo <= 0:
        return 0.0

    fator = _calcularFatorJuros(taxa, tempo)

    montante_principal = valorInicial * fator

    if taxa == 0:
        montante_aportes = aporte * tempo
    else:
        montante_aportes = aporte * (fator - 1) / taxa

    return montante_principal + montante_aportes


def ajustarPorInflacao(
    valor: float,
    taxaInflacao: float,
    tempo: int,
) -> float:

    if valor < 0 or taxaInflacao < 0 or tempo <= 0:
        return 0.0

    divisor = _calcularFatorJuros(taxaInflacao, tempo)

    return valor / divisor


def calcularRendaPassiva(
    valorTotal: float,
    taxaRetirada: float,
) -> float:

    if valorTotal <= 0 or taxaRetirada <= 0:
        return 0.0

    return valorTotal * taxaRetirada
