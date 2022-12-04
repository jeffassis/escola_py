import PySimpleGUI as sg

sg.theme('DarkGrey2')

layout = [
    [[sg.Menubar(
        [['Cadastro', ['Aluno', 'Exit']], ['Sobre', ['helpme', ]]])]]
]


window = sg.Window(
    'Tela de Login',
    size=(800, 600),
    layout=layout
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Aluno':
        import cad_aluno
window.close()
