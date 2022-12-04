import PySimpleGUI as sg
import sqlite3 as lite

sg.theme('DarkGrey2')

# Create widgets
layout_esquerda = [
    [sg.Image(filename='simpleGui/livro.png')],
    [sg.Text('JeffAssis©', font='arial 10 underline', pad=(0, (20, 0)))]
]

layout_direita = [
    [sg.Text('SEJA BEM VINDO', font='arial 20 bold', pad=(0, (0, 25)))],
    [sg.Text('Usuário:', pad=(0, (0, 15)), size=(6, 1)),
     sg.Input(key='usuario', pad=(0, (0, 15)), size=(30, 1))],
    [sg.Text('Senha:', pad=(0, (0, 15)), size=(6, 1)), sg.Input(
        key='senha', pad=(0, (0, 15)), size=(30, 1), password_char='*')],
    [sg.Push(), sg.Button('Login', font='arial 12',
                          size=(8, 1), pad=(10, (0, 0))), sg.Push()],
    [sg.Text('', key='mensagem', font='arial 11', pad=(0, (30, 15)))]
]

layout = [
    [sg.Column(layout_esquerda, element_justification='c'),
     sg.VSeparator(), sg.Column(layout_direita, element_justification='c')]
]

# Create window
window = sg.Window(
    'Tela de Login',
    layout=layout,
)

# Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Login':
        usuario = values['usuario']
        senha = values['senha']
        if usuario == "" and senha == "":
            window['mensagem'].update('Usuário ou senha não pode ser vazios!')
        else:
            try:
                with lite.connect('dados.db') as db:
                    c = db.cursor()
                find_user = ('select * from user where nome = ? and senha = ?')
                c.execute(
                    find_user, [usuario, senha])
                result = c.fetchall()
                if result:
                    window.hide()
                    import menu_sg
                else:
                    window['mensagem'].update('Usuário ou senha inválidos!')
            except Exception as es:
                window['mensagem'].update(f'Error Due to: {str(es)}')
window.close()
