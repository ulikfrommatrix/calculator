from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class Buttons(GridLayout):
    background_color = [0, 0, 1, 1]

class Text(Label):
    pass

class Container(BoxLayout):
    pass

class MyApp(App):

    def build(self):
        self.formula = ''
        gl = Buttons()
        bl = Container()

        self.bl_text = Text()

        bl.add_widget(self.bl_text)

        gl.add_widget(Widget())
        gl.add_widget(Button(text='x2', on_press=self.operations, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='/', on_press=self.operations, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='backspace', on_press=self.input_number, background_color = [1, 0, 0, 9]))


        gl.add_widget(Button(text='7', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='8', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='9', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='X', on_press=self.operations, background_color = [1, 0, 0, 9]))


        gl.add_widget(Button(text='4', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='5', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='6', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='+', on_press=self.operations, background_color = [1, 0, 0, 9]))


        gl.add_widget(Button(text='1', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='2', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='3', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='-', on_press=self.operations, background_color =[1, 0, 0, 9]))

        gl.add_widget(Button(text='clear', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='0', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='.', on_press=self.input_number, background_color = [1, 0, 0, 9]))
        gl.add_widget(Button(text='=', on_press=self.result, background_color =[1, 0, 0, 9]))


        bl.add_widget(gl)
        return bl



    def update(self):
        self.bl_text.text = self.formula


    def operations(self, instance):
        if str(instance.text).lower() == 'x':
            self.formula += '*'


        if str(instance.text) == 'x2':
            self.formula += '**2'

        if str(instance.text) == '/':
            self.formula += '/'

        self.update()


    def result(self, instance):
        self.bl_text.text = str(eval(self.bl_text.text))
        if isinstance(eval(self.bl_text.text), float):
            round(float(self.bl_text.text))
        self.bl_text.text = str(eval(self.bl_text.text))
        self.formula = '0'


    def input_number(self, instance):

        if self.formula == '0':
            self.formula = ''

        if instance.text == 'backspace':
            self.formula = self.formula[:-1]
            self.update()

        if instance.text == 'clear':
            self.formula = ""
            self.update()

        if instance.text != 'backspace' and instance.text != 'clear':
            self.formula += str(instance.text)
            self.update()



if __name__ == "__main__":
        MyApp().run()
