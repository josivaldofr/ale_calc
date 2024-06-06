from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window

Config.set('graphics', 'width', '320') 
Config.set('graphics', 'height', '510')
Config.set('graphics', 'resizable', 0)  
Builder.load_file('main.kv')

class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculadora, self).__init__(**kwargs)

    def atualizar_display(self, texto):
        self.ids.formula.text += texto

    def limpar_display(self):
        self.ids.formula.text = ''
        self.ids.result.text = ''

    def calcular(self):
        try:
            self.ids.result.text = str(eval(self.ids.formula.text))
        except Exception as e:
            self.ids.result.text = 'Erro'

    def limpar_um_caracter(self):
        self.ids.formula.text = self.ids.formula.text[:-1]

    def inverter_sinal(self):
        texto_atual = self.ids.formula.text
        if texto_atual and texto_atual[0] != '-':
            self.ids.formula.text = '-' + texto_atual
        elif texto_atual:
            self.ids.formula.text = texto_atual[1:]

    def on_textinput(self, text):
        self.atualizar_display(text)

    def on_key_down(self, window, keyboard, keycode, text, modifiers):
        if text is not None:
            if text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'a', 's', 'm', 'd', 'p', 'n']:
                if text == 'a':
                    self.atualizar_display('+')
                elif text == 's':
                    self.atualizar_display('-')
                elif text == 'm':
                    self.atualizar_display('*')
                elif text == 'd':
                    self.atualizar_display('/')
                elif text == 'p':
                    self.atualizar_display('%')
                elif text == 'n':
                    self.inverter_sinal()
                else:
                    self.atualizar_display(text)
            elif text == 'r':
                self.calcular()
            elif text == 'b':
                self.limpar_um_caracter()
            elif text == 'c':
                self.limpar_display()
            elif text == 'escape':
                App.get_running_app().stop()
            return True  # Indica que o evento foi tratado


class Magnus_Calculadora(App):
    def build(self):
        calculadora = Calculadora()
        Window.size = (320, 510)  # Definindo o tamanho da janela
        Window.bind(on_key_down=calculadora.on_key_down)
        return calculadora
if __name__ == '__main__':
    Magnus_Calculadora().run()
