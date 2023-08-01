import PySimpleGUI as sg


class Fim:

    def __init__(self):
        
        sg.theme('LightYellow')

        layout = [
            [sg.Text('Feito! O programa ficará parado por, no mínimo, 24 horas.', 
            font=('Helvetica', 14), text_color=('#D63086'))],

            [sg.Column(
                layout=[
                    [sg.Button('OK', button_color=('white', '#5C4CC8'), 
                    font=('Helvetica', 14), size=(5, 1))]],
                justification='center',  
                element_justification='center')]]

        janela = sg.Window('Fim de programa:', font='_ 14', size=(530,90), 
        auto_close=True, auto_close_duration=5).layout(layout)

	
        self.button, self.values = janela.Read() 
        janela.close()

