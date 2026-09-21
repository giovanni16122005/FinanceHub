import os
import json
from entidades import gerenciadorDeUsuario
from interface import telas

ARQUIVO_USUARIO = "usuarios.json"

def iniciar_buscando_usuarios_json(): 
    if os.path.exists(ARQUIVO_USUARIO): 
        try: 
            with open(ARQUIVO_USUARIO, "r", encoding= "utf-8") as arquivo: 
                dados = json.load(arquivo)

                gerenciadorDeUsuario.carregarTodosUsuarios(dados)
            
        except Exception:
            print("[AVISO] Arquivo corrompido. Iniciando sistema vazio")

def encerrar_e_salvar_usuarios_json(): 
    print("\nSalvando os dados...")

    dadosFinais = gerenciadorDeUsuario.obterTodosUsuarios()
    with open(ARQUIVO_USUARIO, "w", encoding= "utf-8") as arquivo: 
        json.dump(dadosFinais,arquivo, indent= 4, ensure_ascii= False )
        print("Dados salvos!")




if __name__ == "__main__": 
    iniciar_buscando_usuarios_json() 

    telas.menuPrincipal()

    encerrar_e_salvar_usuarios_json()

