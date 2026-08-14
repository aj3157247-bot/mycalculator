from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class CalculatorApp(App):

    def build(self):
        main = BoxLayout(
            orientation="vertical",
            padding=50,
            spacing=50,
        )

        self.display = TextInput(
            text="",
            font_size=100,
            halign="right",
            multiline=False,
            readonly=True,
            size_hint_y=1
        )

        main.add_widget(self.display)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        for row in buttons:
            row_layout = BoxLayout(
                orientation="horizontal",
                spacing=50
            )

            for value in row:
                button = Button(
                    text=value,
                    font_size=50
                )

                button.bind(
                    on_press=lambda instance, x=value: self.press(x)
                )

                row_layout.add_widget(button)

            main.add_widget(row_layout)

        clear_button = Button(
            text="Clear",
            font_size=100,
            size_hint_y=1
        )

        clear_button.bind(on_press=self.clear)
        main.add_widget(clear_button)

        return main

    def press(self, value):
        if value == "=":
            self.calculate()
        else:
            self.display.text += value

    def clear(self, instance):
        self.display.text = ""

    def calculate(self):
        try:
            result = eval(self.display.text)
            self.display.text = str(result)
        except:
            self.display.text = "Error"


CalculatorApp().run()
