from PySimpleGUI import Window, Button, Text, Image, Input

layout = [
    [Image(filename='simpleGui/livro.png')],
    [Text('E-mail:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Button('Login!'), Button('Esqueci a senha')]
]


window = Window(
    'Titulo da janela',
    layout=layout,
    element_justification='c'
)

window.read()

window.close()
