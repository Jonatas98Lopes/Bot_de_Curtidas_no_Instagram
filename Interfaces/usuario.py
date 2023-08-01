import PySimpleGUI as sg


class DadosUsuario:

    def __init__(self):
        
        sg.theme('LightYellow')

        layout = [
            [sg.Text('Digite seu nome de usuário no Instagram:', 
                    font=('Helvetica', 14), text_color=('#D63086'))],

            [sg.Input(size=(70,5), background_color='white', 
                    key='user_name', font=('Helvetica', 12), text_color=('#5C4CC8'))],

            [sg.Text('Digite sua senha:', font=('Helvetica', 14), text_color=('#D63086'))],
            [sg.Input(password_char='*',size=(70,5), background_color='white',
                    key='password', font=('Helvetica', 12), text_color=('#5C4CC8'))],

            [sg.Text('Qual o nome da página que deseja monitorar?', font=('Helvetica', 14), text_color=('#D63086'))],
            [sg.Input(size=(70,5), background_color='white',
                    key='page', font=('Helvetica', 12), text_color=('#5C4CC8'))],

            [sg.Text('Digite o comentário padrão a inserir nas publicações:', font=('Helvetica', 14), 
                    text_color=('#D63086'))],
            [sg.Multiline(size=(70, 5), background_color='white', key='comment', 
                    font=('Helvetica', 12), text_color=('#5C4CC8'), sbar_background_color='pink')],

            [sg.Button('Enviar', button_color=('white', '#5C4CC8'), font=('Helvetica', 14)), 
             sg.Button('Cancelar', button_color=('white', 'red'), font=('Helvetica', 14))]
            
        ]

        janela = sg.Window('Dados do Usuário:', font='_ 14', size=(500,380)).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

