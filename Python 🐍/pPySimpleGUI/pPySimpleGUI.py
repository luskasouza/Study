from PySimpleGUI import PySimpleGUI as sg

# Layout

sg.theme('DarkAmber')

layout = [
    [sg.Image("./icons/icons.png")],
    [sg.Text('Usuรกrio'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salva o login ๐')],
    [sg.Button('Entrar')]
]
# Janela

janela = sg.Window('Tela de Login', layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos ==   'Entrar':
        if valores['usuario'] == 'teste' and valores['senha'] == 'teste':
            print('๐พ Bem-vindo ๐พ \n' +"๐ " +valores['usuario'] + " ๐")