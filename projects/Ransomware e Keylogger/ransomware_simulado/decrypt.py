import os
from cryptography.fernet import Fernet

PASTA_ALVO = "arquivos_teste"

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivos():
    chave = carregar_chave()
    fernet = Fernet(chave)

    for nome_arquivo in os.listdir(PASTA_ALVO):
        caminho = os.path.join(PASTA_ALVO, nome_arquivo)

        with open(caminho, "rb") as f:
            conteudo = f.read()

        conteudo_decriptado = fernet.decrypt(conteudo)

        with open(caminho, "wb") as f:
            f.write(conteudo_decriptado)

    print("Descriptografia concluída com sucesso (simulação).")

if __name__ == "__main__":
    descriptografar_arquivos()
