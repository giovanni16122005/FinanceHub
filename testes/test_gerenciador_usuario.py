import unittest 

from entidades.gerenciadorDeUsuario import (
    CriaUsuario, ConsultaUsuario, AtualizaUsuario, 
    carregarTodosUsuarios, AdicionarHistorico
)
class TestGerenciadorUsuario(unittest.TestCase):

    def setUp(self):
        """Garante que a memória encapsulada comece 100% limpa antes de CADA teste."""
        carregarTodosUsuarios({})
   
    def test_01_validar_usuario_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Validação dados válidos")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        retorno = CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 0)

    def test_02_validar_usuario_falta_campos_obrigatórios(self):
        print("Caso de Teste 02 - Validação dados faltando campos obrigatórios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "senha": "123",
        }
        retorno = CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 2)

    def test_03_validar_usuario_tipo_parâmetro_errado(self):
        print("Caso de Teste 03 - Validação passando parâmetro errado")
        usuario = "ana@gmail.com, Ana, 30, 500.0, moderado"
        retorno = CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 2)

    def test_04_validar_usuario_email_formato_errado(self):
        print("Caso de Teste 04 - Validação passando parâmetro errado")
        usuario = {
        "email": "anagmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        retorno = CriaUsuario(usuario, "anagmail.com")
        self.assertEqual(retorno, 2)

    def test_05_validar_email_existe_ok(self):
        print("Caso de Teste 05 - Verificação se email que existe no sistema")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno =  CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 1)
    
    def test_06_validar_nao_email_existe_ok(self):
        print("Caso de Teste 06 - Verificação se email não existe no sistema")
        retorno =  ConsultaUsuario("carlos@gmail.com")
        self.assertEqual(retorno, 1)

    def test_08_criar_usuario_novo_ok(self):
        print("Caso de Teste 08 - Cria novo usuário")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        retorno =  CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 0)
    
    def test_09_criar_usuario_campos_obrigatórios_vazios(self):
        print("Caso de Teste 09 - Tenta criar usuário com campos obrigatórios vazios")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "senha": "123"
        }
        retorno =  CriaUsuario(usuario, "ana@gmail.com" )
        self.assertEqual(retorno, 2)
    
    def test_10_criar_usuario_já_existente(self):
        print("Caso de Teste 10 - Tenta criar usuário já existente no sistema")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno =  CriaUsuario(usuario, "ana@gmail.com")
        self.assertEqual(retorno, 1)
    
    def test_11_busca_usuario_existente(self):
        print("Caso de Teste 11 - Busca Usuário já cadastrado no sistema")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        resultado = ConsultaUsuario("ana@gmail.com")

        self.assertEqual(resultado["email"], "ana@gmail.com")
        self.assertEqual(resultado["historico"], {"aposentadoria": None, "investimento": None})
    
    def test_12_busca_usuario_nao_existente(self):
        print("Caso de Teste 12 - Busca usuário não cadastrado no sistema")
        resultado = ConsultaUsuario("carlos@gmail.com")
        self.assertEqual(resultado, 1)
    
    def test_13_atualiza_usuario_existente(self):
        print("Caso de Teste 13 - Atualiza usuário existente")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno = AtualizaUsuario("ana@gmail.com", "aporte", 800.0)
        self.assertEqual(retorno, 0)
    
    def test_14_atualiza_usuario_nao_existente(self):
        print("Caso de Teste 14 - Atualiza usuário não existente")
        retorno = AtualizaUsuario("carlos@gmail.com", "aporte", 800.0)
        self.assertEqual(retorno, 1)
    
    def test_15_atualiza_usuario_campo_inválido(self):
        print("Caso de Teste 15 - Atualiza campo inválido")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno =  AtualizaUsuario("ana@gmail.com", "cpf", "123.456.789-00")
        self.assertEqual(retorno, 2)
    
    def test_16_atualiza_usuario_valor_inválido(self):
        print("Caso de Teste 16 - Atualiza dado com valor inválido")
        usuario = {
        "email": "ana@gmail.com",
        "nome": "Ana",
        "idade": 30,
        "aporte": 500.0,
        "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno =  AtualizaUsuario("ana@gmail.com", "aporte", "oitocentos")
        self.assertEqual(retorno, 2)
    
    def test_17_atualiza_email_com_sucesso(self):
        print("Caso de Teste 17 - Atualiza e-mail mudando a chave do dicionário")
        usuario = {
            "email": "ana@gmail.com", 
            "nome": "Ana", 
            "idade": 30, 
            "aporte": 500.0,
            "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno = AtualizaUsuario("ana@gmail.com", "email", "anacosta@gmail.com")
        self.assertEqual(retorno, 0)
        self.assertEqual(ConsultaUsuario("ana@gmail.com"), 1)
        
        usuario_atualizado = ConsultaUsuario("anacosta@gmail.com")
        self.assertEqual(usuario_atualizado["email"], "anacosta@gmail.com")

    def test_18_atualiza_email_mesmo_valor_deve_retornar_zero(self):
        print("Caso de Teste 18 - Atualiza e-mail passando o mesmo e-mail atual")
        usuario = {
            "email": "ana@gmail.com", 
            "nome": "Ana", 
            "idade": 30, 
            "aporte": 500.0, 
            "senha": "123"
        }
        CriaUsuario(usuario, "ana@gmail.com")
        retorno = AtualizaUsuario("ana@gmail.com", "email", "ana@gmail.com")
        self.assertEqual(retorno, 0)

    def test_19_atualiza_email_ja_existente_deve_retornar_dois(self):
        print("Caso de Teste 19 - Tenta mudar e-mail para outro que já está cadastrado")
        usuario1 = {
            "email": "ana@gmail.com",
            "nome": "Ana",
            "idade": 30, 
            "aporte": 500.0,
            "senha": "123" # Adicionado senha
        }
        CriaUsuario(usuario1, "ana@gmail.com")

        usuario2 = {
            "email": "carlos@gmail.com", 
            "nome": "Carlos", 
            "idade": 25, 
            "aporte": 300.0,
            "senha": "456" # Adicionado senha
        }
        CriaUsuario(usuario2, "carlos@gmail.com")

        retorno = AtualizaUsuario("ana@gmail.com", "email", "carlos@gmail.com")
        self.assertEqual(retorno, 2)
    
    def test_20_historico_salva_apenas_ultimo_por_categoria(self):
        print("Caso de Teste 20 - Valida gravação do último por categoria no Histórico")
        usuario = {
            "email": "ana@gmail.com", 
            "nome": "Ana", 
            "idade": 30, 
            "aporte": 500.0,
            "senha": "123" # Adicionado senha e corrigido recuo do bloco
        }
        CriaUsuario(usuario, "ana@gmail.com")

        sim1 = {"tipo": "Investimento", "resultado_final": 1000.0}
        sim2 = {"tipo": "Investimento", "resultado_final": 1500.0} 
        sim3 = {"tipo": "Aposentadoria", "resultado_final": 50000.0}

        AdicionarHistorico("ana@gmail.com", "investimento", sim1)
        AdicionarHistorico("ana@gmail.com", "investimento", sim2)
        AdicionarHistorico("ana@gmail.com", "aposentadoria", sim3)

        dados = ConsultaUsuario("ana@gmail.com")
        historico = dados["historico"]
        
        self.assertEqual(historico["investimento"]["resultado_final"], 1500.0)
        self.assertEqual(historico["aposentadoria"]["resultado_final"], 50000.0)

    def test_21_criar_usuario_senha_invalida(self):
        print("Caso de Teste 21 - Tenta criar usuário com senha vazia ou ausente")
        
        # Senha vazia (apenas espaços)
        usuario_senha_vazia = {
            "email": "ana@gmail.com",
            "nome": "Ana",
            "idade": 30,
            "aporte": 500.0,
            "senha": "   "
        }
        retorno1 = CriaUsuario(usuario_senha_vazia, "ana@gmail.com")
        self.assertEqual(retorno1, 2) # Deve barrar com erro 2

        # Sem o campo senha no dicionário
        usuario_sem_senha = {
            "email": "carlos@gmail.com",
            "nome": "Carlos",
            "idade": 25,
            "aporte": 300.0
            # chave "senha" ausente
        }
        retorno2 = CriaUsuario(usuario_sem_senha, "carlos@gmail.com")
        self.assertEqual(retorno2, 2) # Deve barrar com erro 2

if __name__ == '__main__':
    unittest.main()