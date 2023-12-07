import base64
import cv2
import numpy as np

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def encodar_imagem(caminho_imagem):
    with open(caminho_imagem, "rb") as arquivo_imagem:
        return base64.b64encode(arquivo_imagem.read()).decode('utf-8')