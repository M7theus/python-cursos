import PySimpleGUI as sg

Layout = [
    [sg.Text("Pegar cotação da moeda")],
    [sg.InputText()],
    [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
    [sg.Text("A cotação foi de tanto")],
]

janela = sg.Window("Título da janela", Layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
janela.close()