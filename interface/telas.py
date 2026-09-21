from entidades import CriaUsuario, ConsultaUsuario, AtualizaUsuario

from servicos.simuladores import (
    simulador_aposentadoria,
    simulador_investimento
)

__all__ = ["menuPrincipal"]


def menuPrincipal() -> None:

    while True:
        print("\n")
        print("------ Bem-vindo ao Finance Hub! ------")
        print("1 - Cadastro")
        print("2 - Login")
        print("3 - Sair")

        print("\n")


        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:
            cadastroUsuario()

        elif opcao == 2:
            login()

        elif opcao == 3:
            print("Obrigada por usar o Finance Hub! Até logo.")
            break

        else:
            print("Opção inválida ! Tente novamente")


def menuSistemaLogado(nomeUsuario: str, email: str) -> None:

    while True:

        print("\n")
        print(f"------ Olá, {nomeUsuario} ------")
        print("1 - Atualizar dados")
        print("2 - Simulador de Aposentadoria")
        print("3 - Simulador de Investimentos")
        print("4 - Histórico")
        print("5 - Sair")
        print("\n")
        
        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:

            email = AtualizarDadosUsuario(email)

            dados_atualizados = ConsultaUsuario(email)

            if dados_atualizados != 1:
                nomeUsuario = dados_atualizados["nome"]

        elif opcao == 2:

            usuario = ConsultaUsuario(email)

            simulador_aposentadoria(
                usuario["aporte"], email
            )

        elif opcao == 3:

            simulador_investimento(email)

        elif opcao == 4: 

            usuario = ConsultaUsuario(email)
            
            if usuario == 1:
                print("Erro ao carregar os dados do usuário.")
                continue
                
            historico = usuario.get("historico", {"aposentadoria": None, "investimento": None})
            
            print(f"\n ------ Últimas Simulações de {nomeUsuario} ------\n")
            
            if not historico["aposentadoria"] and not historico["investimento"]:
                print("Você ainda não realizou nenhuma simulação.")
            else:
                # Mostrar a última de Aposentadoria
                if historico["aposentadoria"]:
                    apo = historico["aposentadoria"]
                    print(f"[Última Simulação] Tipo: {apo['tipo']}")
                    print(f"    Taxa Utilizada: {apo['taxa_utilizada']}%")
                    print(f"    Aporte Mensal: R$ {apo['aporte_mensal']:.2f}")
                    print(f"    Tempo: {apo['tempo_anos']} anos")
                    print(f"    -> RESULTADO FINAL: R$ {apo['resultado_final']:.2f}")
                    print("-" * 40)
                
                # Mostrar a última de Investimento
                if historico["investimento"]:
                    inv = historico["investimento"]
                    print(f"[Última Simulação] Tipo: {inv['tipo']}")
                    print(f"    Taxa Utilizada: {inv['taxa_utilizada']}%")
                    print(f"    Valor Inicial: R$ {inv['valor_inicial']:.2f}")
                    print(f"    Tempo: {inv['tempo_meses']} meses")
                    print(f"    -> RESULTADO FINAL: R$ {inv['resultado_final']:.2f}")
                    print("-" * 40)

        elif opcao == 5:

            print("Obrigada por usar o Finance Hub! Até logo.")
            break

        else:
            print("Opção inválida ! Tente novamente")


def AtualizarDadosUsuario(email: str) -> str:

    while True:

        print("------ATUALIZA USUÁRIO------")
        print("1 - Atualizar email")
        print("2 - Atualizar nome")
        print("3 - Atualizar idade")
        print("4 - Atualizar aporte")
        print("5 - Voltar ao Menu Principal")

        try:
            opcao = int(input("Insira sua opção: "))

        except ValueError:
            print("Por favor, insira apenas as opções dadas")
            continue

        if opcao == 1:

            campo = "email"
            dado = input("Digite novo email: ").strip()

        elif opcao == 2:

            campo = "nome"
            dado = input("Digite novo nome: ").strip()

        elif opcao == 3:

            campo = "idade"

            try:
                dado = int(input("Digite sua nova idade: "))

            except ValueError:
                print("Idade deve ser um número inteiro!")
                continue

        elif opcao == 4:

            campo = "aporte"

            try:
                dado = float(input("Digite seu novo aporte mensal (R$): "))

            except ValueError:
                print("Aporte deve ser um número decimal!")
                continue

        elif opcao == 5:

            return email

        else:

            print("Opção Inválida!")
            continue

        resultado = AtualizaUsuario(
            email=email,
            campo=campo,
            valor=dado
        )

        if resultado == 0:

            print("Perfil atualizado com sucesso!")

            if campo == "email":
                email = dado

        elif resultado == 1:

            print("Este email não foi encontrado no sistema")

        elif resultado == 2:

            print(
                "Dados inválidos! Verifique se há campos vazios ou valores negativos"
            )


def cadastroUsuario() -> None:

    print("------CADASTRO USUÁRIO------")

    email = input("Digite seu email: ").strip()
    nome = input("Digite seu nome: ").strip()

    try:
        idade = int(input("Digite sua idade: "))

    except ValueError:
        print("Idade deve ser um número inteiro!")
        return

    try:
        aporte = float(input("Digite seu aporte mensal (R$): "))

    except ValueError:
        print("Aporte deve ser um número decimal!")
        return
    
    senha = input("Digite sua senha: ").strip()


    novoUsuario = {
        "email": email,
        "nome": nome,
        "idade": idade,
        "aporte": aporte,
        "senha": senha, 
    }

    resultado = CriaUsuario(
        u=novoUsuario,
        email=email
    )

    if resultado == 0:

        print("Cadastro realizado com sucesso!")

    elif resultado == 1:

        print("Este email já está cadastrado no sistema")

    elif resultado == 2:

        print(
            "Dados inválidos! Verifique se há campos vazios ou valores negativos"
        )


def login() -> None:

    print("------ LOGIN ------")

    email = input("Digite seu email: ").strip()

    usuario = ConsultaUsuario(email)

    if usuario == 1:

        print("Email não cadastrado! Cadastre-se primeiro")
        return
    
    senha = input("Digite sua senha: ").strip()

    if senha != usuario.get("senha"):
        print("Senha incorreta! Acesso negado.")
        return

    nome_usuario = usuario["nome"]

    menuSistemaLogado(
        nomeUsuario=nome_usuario,
        email=email
    )
