
from servicos.consultor_bcb import obterValorIndicador

from entidades.CalculoFinanceiro import (
    calcularJurosCompostos,
    calcularRendaPassiva
)

from entidades.gerenciadorDeUsuario import AdicionarHistorico

__all__ = [
    "simulador_aposentadoria",
    "simulador_investimento",
    "calculaJuros",
    "simulaAcumulacao",
    "calculaTempoParaAposentar",
    "calcularValorASerRecebido"
]

# =========================
# FUNÇÕES DE CÁLCULO
# =========================

def calculaJuros(valor: float, taxa: float, tempo: int) -> float:
    """
    Calcula o montante final utilizando juros compostos.
    """

    return calcularJurosCompostos(
        valorInicial=valor,
        aporte=0,
        taxa=taxa,
        tempo=tempo
    )


def simulaAcumulacao(
    aporte_mensal: float,
    taxa: float,
    meses: int
) -> float:
    """
    Simula a acumulação de patrimônio ao longo do tempo.
    """

    return calcularJurosCompostos(
        valorInicial=0,
        aporte=aporte_mensal,
        taxa=taxa,
        tempo=meses
    )


def calculaTempoParaAposentar(
    aporte_mensal: float,
    objetivo: float,
    taxa: float
) -> int:
    """
    Calcula quantos meses são necessários para atingir
    um patrimônio objetivo.
    """

    acumulado = 0
    meses = 1

    while acumulado < objetivo:

        acumulado = calcularJurosCompostos(
            valorInicial=0,
            aporte=aporte_mensal,
            taxa=taxa,
            tempo=meses
        )

        meses += 1

    return meses


def calcularValorASerRecebido(
    patrimonio: float,
    anos: int
) -> float:
    """
    Calcula uma estimativa de renda passiva mensal.
    """

    return calcularRendaPassiva(
        valorTotal=patrimonio,
        taxaRetirada=1 / (anos * 12)
    )


# =========================
# FUNÇÕES INTEGRADAS AO MENU
# =========================

def simulador_aposentadoria(aporte: float, email_usuario: str) -> None:
    """
    Executa uma simulação de aposentadoria utilizando
    a Selic obtida na API do Banco Central.
    """

    taxa_selic = obterValorIndicador("selic")

    if taxa_selic == 0:
        print("Erro ao consultar a Selic.")
        return

    taxa_mensal = (taxa_selic / 100) / 12

    anos = int(input("Quantos anos deseja investir? "))

    resultado = simulaAcumulacao(
        aporte_mensal=aporte,
        taxa=taxa_mensal,
        meses=anos * 12
    )

    print("\n===== RESULTADO APOSENTADORIA =====")
    print(f"Valor acumulado: R$ {resultado:.2f}")

    dados_simulacao = {
        "tipo": "Aposentadoria",
        "aporte_mensal": aporte,
        "tempo_anos": anos,
        "taxa_utilizada": taxa_selic,
        "resultado_final": round(resultado, 2)
    }
    

    AdicionarHistorico(email_usuario, "aposentadoria", dados_simulacao)



def simulador_investimento(email_usuario: str) -> None:
    """
    Executa uma simulação de investimento utilizando
    o CDI obtido na API do Banco Central.
    """

    valor = float(input("Valor inicial do investimento: "))
    meses = int(input("Quantidade de meses: "))

    taxa_cdi = obterValorIndicador("cdi")

    if taxa_cdi == 0:
        print("Erro ao consultar o CDI.")
        return

    taxa_mensal = (taxa_cdi / 100) 

    resultado = calcularJurosCompostos(
        valorInicial=valor,
        aporte=0,
        taxa=taxa_mensal,
        tempo=meses
    )

    print("\n===== RESULTADO INVESTIMENTO =====")
    print(f"Valor final: R$ {resultado:.2f}")

    dados_simulacao = {
        "tipo": "Investimento",
        "valor_inicial": valor,
        "tempo_meses": meses,
        "taxa_utilizada": taxa_cdi,
        "resultado_final": round(resultado, 2)
    }
    
    AdicionarHistorico(email_usuario,"investimento", dados_simulacao)
