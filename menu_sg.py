import PySimpleGUI as sg

sg.theme('DarkGrey2')

menu = [
    ['Cadastro', ['Aluno', 'Professor', 'Turma', 'Matricula', 'Notas', 'Fechar']],
    ['Editar', ['Aluno', 'Professor', 'Turma', 'Matricula', 'Notas']],
    ['Consultar', ['Aluno', 'Matricula', 'Notas']]
]

layout = [
    [sg.Menu(menu, background_color='white')],
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
