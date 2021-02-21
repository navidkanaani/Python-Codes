import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config

Config.set('graphics', 'resizable', 1)

class CalcLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()