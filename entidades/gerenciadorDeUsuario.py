#Apresenta a lista de funções a serem disponibilizadas pelo módulo
__all__ = ["CriaUsuario", "ConsultaUsuario", "AtualizaUsuario", 
           "obterTodosUsuarios", "carregarTodosUsuarios", "AdicionarHistorico" ] 

#Encapsulado 
_usuarios = {}

def obterTodosUsuarios() -> dict:
    return _usuarios.copy() #assim não acessa diretamente _usuarios
    
def carregarTodosUsuarios(dadosCarregados: dict) -> None:
    global _usuarios
    _usuarios.clear()
    _usuarios.update(dadosCarregados)
  

def _ValidarDados(u: dict) -> int:

    """
    Retorno 0 -> Dados VÁLIDOS e aprovados
    Retorno 2 -> Parâmetros inválidos, tipos errados ou campos ausentes

    """
    if not isinstance(u, dict): 
        return 2
    
    try: 

        email = u.get("email")
        nome = u.get("nome")
        idade = u.get("idade")
        aporte = u.get("aporte")
        senha = u.get("senha")

        # 2 - Validação se campo for ausente(None) ou vazio ("")

        if email is None or str(email).strip() == "": 
            return 2
        
        if nome is None or str(nome).strip() == "": 
            return 2

        if idade is None: 
            return 2
        
        if aporte is None: 
            return 2
        
        if senha is None or str(senha).strip() == "": 
            return 2

        #3 - Validação de Email ( Possui @?)
        email = str(u.get("email")).strip()
        if '@' not in email : 
            return 2 
    
    
        # 4 -Validação de Nome (nome não está vazio?)
        nome = str(u.get("nome")).strip()
        if nome is None or nome == "" : 
            return 2
    
        #5 - Validação da Idade (idade é número positivo?)

        idade =int(u.get("idade"))
        if (idade < 0) : 
            return 2
    
        #6- aporte é número positivo?
        aporte = float(u.get("aporte"))
        if (aporte <= 0) : 
            return 2

        

        return 0
    
    except(ValueError, TypeError):
        return 2
    


def _VerificaExistenciaEmail(email:str) -> int:
    """
    Retorno 0 -> Usuário encontrado
    Retorno 1 -> Usuário não encontrado

    """
     
    if email in _usuarios: 
        return 0
     
    return 1 

#FUNCÕES DE ACESSO

def CriaUsuario(u: dict, email: str):
    """
    Retorno 0 -> Usuário Inserido com sucesso
    Retorno 1 -> Email já cadastrado
    Retorno 2 -> Dados inválidos

    """

    #1 - Valida os dados antes 
    if _ValidarDados(u) == 2: 
        return 2
    
    #2 - Checa se o email existe 
    if _VerificaExistenciaEmail(email) == 0:
        return 1
    
    #3 - Se o email passou, guarda no dicionário 
    _usuarios[email] = {
        "email": str(u.get("email")).strip(), 
        "nome": str(u.get("nome")).strip(), 
        "idade": int(u.get("idade")), 
        "aporte": float(u.get("aporte")),
        "senha" : str(u.get("senha", "")).strip(), 
        "historico": {"aposentadoria": None, "investimento": None}
    }
    
    return 0 
    

def ConsultaUsuario(email: str):
    """
    Retorna  o  dicionário do usuário se o email for encontrado 
    Retorna 1 se o email não existir 
    """
    email = str(email).strip()
    if email in _usuarios: 
        return _usuarios[email]

    return 1
   
def AtualizaUsuario(email: str, campo: str, valor) -> int:
    """
    Retorna 0 -> Atualizado com sucesso
    Retorna 1 -> Email não encontrado 
    Retorna 2 -> Campo inválido ou Valor Inválido

    """
    if _VerificaExistenciaEmail(email) == 1: 
        return 1 
    
    camposValidos = {"email", "nome", "idade", "aporte"}
    if campo not in camposValidos: 
        return 2
    
    usuario_temp = _usuarios[email].copy() 
    usuario_temp[campo] = valor

    if _ValidarDados(usuario_temp) == 2: 
        return 2
    
    if campo == "email": 
        novo_email = str(valor).strip()

        if novo_email == email: 
            return 0 
        
        if _VerificaExistenciaEmail(novo_email) == 0: 
            return 2
        
        dados_usuarios = _usuarios[email]
        dados_usuarios["email"] = novo_email
        _usuarios[novo_email] = dados_usuarios
        _usuarios.pop(email)
        
    elif campo == "idade": 
       _usuarios[email][campo] = int(valor) 
    
    elif campo == "aporte": 
       _usuarios[email][campo] = float(valor)
    
    else: 
        _usuarios[email][campo] = str(valor).strip()
        
    return 0 


def AdicionarHistorico(email: str, categoria: str, registro: dict) -> int:
    """
    Adiciona uma nova simulação ao histórico do usuário.
    Retorna 0 em sucesso, 1 se o usuário não existir.
    """
    if _VerificaExistenciaEmail(email) == 1:
        return 1
    

    _usuarios[email]["historico"][categoria] = registro
    return 0
    