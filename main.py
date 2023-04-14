# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (600, 230)
Window.clearcolor = (20 / 600, 50 / 400, 5 / 400, 1)
Window.title = "Помощник"

class MyApp(App):

    # Создание всех виджетов (объектов
    def __init__(self):
        super().__init__()
        self.labela = Label(text='Продукция:')
        self.labelb = Label(text='Каток опорный 4001-21-140 СБ, цена, c НДС: 155 409,60 руб., масса - 188 кг ')
        self.labelc = Label(text='Каток опорный 4001-21-140-01 СБ, цена, c НДС: 155 409,60 руб., масса - 200 кг')
        self.labeld = Label(text='Норма упаковки: 4 единицы на одном паллете')
        self.sumotgruzki = Label(text='Сумма отгрузки, с НДС, руб.:')
        self.mestvsego = Label(text='Количество мест, шт.: ')
        self.massvsego = Label(text='Масса, кг всего: ')
        self.input_data = TextInput(hint_text='Введите количество (шт.)', multiline=False)
        self.input_data.bind(text=self.on_text)  # Добавляем обработчик события

    # Получаем данные и производит их конвертацию
    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.sumotgruzki.text = 'Сумма отгрузки, с НДС, руб. = ' + str(float(data) * (155409.60))
            self.mestvsego.text = 'Количество мест, шт. =  ' + str(float(data) / 4)
            self.massvsego.text = 'Масса всего, кг = ' + str(float(data) * 200)
        else:
            self.input_data.text = ''

    # Основной метод для построения программы

    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.labela)
        box.add_widget(self.labelb)
        box.add_widget(self.labelc)
        box.add_widget(self.labeld)
        box.add_widget(self.input_data)
        box.add_widget(self.sumotgruzki)
        box.add_widget(self.mestvsego)
        box.add_widget(self.massvsego)

        return box

# Запуск проекта
if __name__ == "__main__":
    MyApp().run()