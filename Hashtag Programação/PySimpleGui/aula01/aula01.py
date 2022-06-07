import PySimpleGUI as sg
from cotacao import pegar_cotacoes

Layout = [
    [sg.Text("Pegar cotação da moeda")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
    [sg.Text("",key="texto_cotacao")],
]

janela = sg.Window("Sistema de cotação", Layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar cotação":
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela["texto_cotacao"].update(f"Pegando cotação {codigo_cotacao} é de R${cotacao}")
janela.close()