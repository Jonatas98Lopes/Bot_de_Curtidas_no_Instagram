import PySimpleGUI as sg


class Erro:

    def __init__(self, mensagem, titulo):
        
        sg.theme('LightYellow')

        layout = [
            [sg.Text(mensagem, font=('Helvetica', 14), text_color=('#D63086'))],

            [sg.Text('Por favor, tente novamente.', 
                    font=('Helvetica', 14), text_color=('#D63086'))],
            [sg.Column(
                layout=[
                    [sg.Button('OK?', button_color=('white', '#5C4CC8'), 
                    font=('Helvetica', 14), size=(5, 1))]
                ],
                justification='center',  
                element_justification='center'  
            )]]

        janela = sg.Window(titulo, font='_ 14', size=(550,130))\
        .layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

