import PySimpleGUI as sg
import sqlite3 as lite

sg.theme('DarkGrey2')

# Create widgets
esquerda_col01 = [
    [sg.Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('CPF:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('ENDEREÇO:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('IDADE:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('SEXO:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('', font='arial 13', pad=(0, (0, 15)))],
]

esquerda_col02 = [
    [sg.Input(size=(40, 1), background_color='white',
              font='arial 12', pad=(0, (0, 15)), key='nome')],
    [sg.Input(size=(40, 1), background_color='white',
              font='arial 12', pad=(0, (0, 15)), key='cpf')],
    [sg.Input(size=(40, 1), background_color='white',
              font='arial 12', pad=(0, (0, 15)), key='endereco')],
    [sg.Input(size=(5, 1), background_color='white',
              font='arial 12', pad=(0, (0, 15)), key='idade')],
    [sg.Radio('Masculino', "Rad02", pad=(0, (0, 15)), default=True),
     sg.Radio('Feminino', "Rad02", pad=(0, (0, 15)))],
    [sg.Input(size=(20, 1), readonly=True, background_color='white', font='arial 12', pad=(
        0, (0, 15)), key='idade'), sg.CalendarButton('Nascimento', pad=(0, (0, 15)), location=(200, 200), format="%d %B %Y")]
]

layout_esquerda = [
    [sg.Text('CADASTRO DE ALUNOS', font='arial 20', pad=(0, (0, 25)))],
    [sg.Column(esquerda_col01), sg.Text(' ' * 5), sg.Column(esquerda_col02)],
    [sg.Button('Adicionar', size=(8, 1), font='arial 12'), sg.Button(
        'Atualizar', size=(8, 1), font='arial 12'), sg.Button('Deletar', size=(8, 1), font='arial 12')]
]

layout_direita = [
    [sg.Text('buscarPor:')],
    [sg.Radio('cpf', "Rad01", default=True), sg.Radio('nome', "Rad01")],
    [sg.Text('Informações Alunos:')],
    [sg.Table([[1, 'Jeff Assis', 12108754709, 33, '21 Agosto 1988', 'Masculino', 'Estrada Santana'], [2, 'Jean Assis', 19808754709, 33, '14 Julho 2007', 'Masculino', 'Estrada Santana']], ['Id', 'Nome', 'CPF', 'Idade',
              'Nascimento', 'Sexo', 'Endereço'], num_rows=5)]
]

layout = [
    [sg.Column(layout_esquerda, element_justification='center'),
     sg.VSeparator(), sg.Column(layout_direita)]
]

# Create window
window = sg.Window(
    'Cadastro de Alunos',
    layout=layout
)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
