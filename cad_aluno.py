import PySimpleGUI as sg
from model.model_aluno import *

# TEMA DO PYSIMPLEGUI
sg.theme('DarkGrey2')

# CREATE WIDGETS
esquerda_col01 = [
    [sg.Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('CPF:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('ENDEREÇO:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('IDADE:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('SEXO:', font='arial 13', pad=(0, (0, 15)))],
    [sg.Text('', font='arial 13', pad=(0, (0, 15)))],
]

esquerda_col02 = [
    [sg.Input(size=(40, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='nome')],
    [sg.Input(size=(40, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cpf')],
    [sg.Input(size=(40, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='endereco')],
    [sg.Input(size=(5, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='idade')],
    [sg.Radio('Masculino', "Rad02", pad=(0, (0, 15)), default=True, key='-MALE-'), sg.Radio('Feminino', "Rad02", pad=(0, (0, 15)), key='-FEMALE-')],
    [sg.Input(size=(20, 1), readonly=True, background_color='white', font='arial 12', pad=(0, (0, 15)), key='data'), sg.CalendarButton('Nascimento', pad=(10, (0, 15)), location=(200, 200), format="%d %B %Y")]
]

layout_esquerda = [
    [sg.Text('CADASTRO DE ALUNOS', font='arial 20', pad=(0, (0, 25)))],
    [sg.Column(esquerda_col01), sg.Text(' ' * 5), sg.Column(esquerda_col02)],
    [sg.Button('Adicionar', size=(8, 1), font='arial 12'), sg.Button('Atualizar', size=(8, 1), font='arial 12'), sg.Button('Deletar', size=(8, 1), font='arial 12')]
]

# POPULA -TABLE-
tb = mostrar_info()
Headings = ['ID', 'NOME', 'CPF', 'IDADE', 'SEXO', 'DATA', 'ENDEREÇO']


layout_direita = [
    [sg.Text('Buscar Por:', font='arial 20', pad=(0, (0, 25)))],
    [sg.Radio('CPF', "Rad01", pad=(0, (0, 15)), default=True), sg.Radio('NOME', "Rad01", pad=(0, (0, 15)))],
    [sg.Text('INFORMARÇÕES DOS ALUNOS', font='arial 13', pad=(0, (0, 15)))],
    [sg.Table(tb, Headings, pad=(0, (0, 15)), num_rows=15, key='-TABLE-')]
]

layout = [
    [sg.Column(layout_esquerda, element_justification='center'), sg.VSeparator(), sg.Column(layout_direita)]
]

# ADICIONA UM ALUNO
def add_aluno(values):
    nome = values['nome']
    cpf = values['cpf']
    idade = values['idade']
    if values['-MALE-']:
        sexo = 'Masculino'
    else:
        sexo = 'Feminino'

    data = values['data']
    endereco = values['endereco']

    lista = [nome, cpf, idade, sexo, data, endereco]

    if nome == '':
        sg.popup('Erro', 'O nome nao pode ser vazio')
    else:
        add_aluno_info(lista)
        sg.popup('Sucesso', 'Os dados foram inseridos com sucesso')

# DELETA UM ALUNO
def del_aluno(values):
    lista = [values['-TABLE-'][0]]
    deletar_aluno_info(lista)

# ATUALIZA A Table
def update_table(window):
    tb = mostrar_info()
    table = window.AllKeysDict['-TABLE-']
    table.Update(tb)
    window.refresh()

# CREATE WINDOW
window = sg.Window('Cadastro de Alunos', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Adicionar':
        add_aluno(values)
        update_table(window)

    elif event == 'Deletar':
        if values['-TABLE-']==[]:
            sg.popup('Selecione uma linha')
        else:
            if sg.popup_ok_cancel('Can not undo Delete: Continue?') == 'OK':
                del_aluno(values)
                update_table(window)


window.close()
