#pip install xmltodict
#pip install pandas
import xmltodict
import os
import pandas as pd


#######
def pegar_infos(dic_arquivo, valores):
    nf_infos = dic_arquivo.get("Nfe", {}).get("infNFe") or dic_arquivo.get("nfeProc", {}).get("NFe", {}).get("infNFe")
    numero_nota = nf_infos['@Id']
    emitente = nf_infos['emit']['xNome']
    destinatario = nf_infos['dest']['xNome']
    endereco = nf_infos['dest']['enderDest']
    peso = nf_infos['transp'].get('vol', {}).get("peso8", "Nçao informado")

    valores.append([numero_nota, emitente, destinatario, endereco, peso])
####### Funcao pega os arquivos do xml e transforma em dicionario


lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "emitente", "destinatario", "endereco", "peso"]
valores = []


##########
for arquivo in lista_arquivos:
    with open(f"nfs/{arquivo}", "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        pegar_infos(dic_arquivo, valores)

tabela = pd.DataFra(data=valores, columns=colunas)
tabela.to_excel("NotasFiscais.xlsx", index=False)
####### Pega o dicionario e atribui a uma planilha