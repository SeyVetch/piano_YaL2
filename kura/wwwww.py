import keyboard
import sys
import os
from PyQt5.Multimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QInputDialog
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.zapis = []

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Piano')

        self.launchbtn = QPushButton('Выберите инструмент',self)
        self.launchbtn.move(50, 60)
        self.launchbtn.clicked.connect(self.launch)

        self.button_rec = QPushButton(self)
        self.button_rec.move(200, 260)
        self.button_rec.setText("Начать запись")
        self.button_rec.clicked.connect(self.Recording_music)
        self.button_save = QPushButton(self)
        self.button_save.move(100, 260)
        self.button_save.setText("Сохранить запись")
        self.button_save.clicked.connect(self.Saving_music)

    def launch(self):
        i, launchbtn = QInputDialog.getItem(
            self,
            "На чем предподчтете музыцировать?",
            "",
            ("Пианино", "Гачи"),
            1,
            False
        )
        self.Chose = i

    def launch_piano(self):
        if self.Chose == 'Гачи':
            if keyboard.is_pressed('q'):
                'Another victim.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('q')
            if keyboard.is_pressed('w'):
                'Boy next door.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('w')
            if keyboard.is_pressed('e'):
                'Deep dark fantasies.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('e')
            if keyboard.is_pressed('r'):
                'Do you like what you see.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('r')
            if keyboard.is_pressed('t'):
                'Dungeon master.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('t')
            if keyboard.is_pressed('y'):
                'fuck you....mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('y')
            if keyboard.is_pressed('u'):
                'FUCK YOU.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('u')
            if keyboard.is_pressed('i'):
                'ganging up.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('i')
            if keyboard.is_pressed('o'):
                'I dont do Anal.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('o')
            if keyboard.is_pressed('p'):
                'Iam cumming.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('p')
            if keyboard.is_pressed('a'):
                'Id be right happy to.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('a')
            if keyboard.is_pressed('s'):
                'It gets bigger when i pull on it.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('s')
            if keyboard.is_pressed('d'):
                'Its a loan.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('d')
            if keyboard.is_pressed('f'):
                'Its Mcarb.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('f')
            if keyboard.is_pressed('g'):
                'Its so fucking deep.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('g')
            if keyboard.is_pressed('h'):
                'Lash of the spanking.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('h')
            if keyboard.is_pressed('j'):
                'Lets suck some dick.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('j')
            if keyboard.is_pressed('k'):
                'Lube it up.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('k')
            if keyboard.is_pressed('l'):
                'Mmmmh.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('i')
            if keyboard.is_pressed('z'):
                'Oh shit iam sorry.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('z')
            if keyboard.is_pressed('x'):
                'Oh yes sir.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('x')
            if keyboard.is_pressed('c'):
                'Orgasm 1.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('c')
            if keyboard.is_pressed('v'):
                'Orgasm 2.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('v')
            if keyboard.is_pressed('b'):
                'RIP EARS ORGASM.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('b')
            if keyboard.is_pressed('n'):
                'WOO.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('n')
            if keyboard.is_pressed('m'):
                'Spit YEEEEEAAAAHHH.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('m')
        if self.Chose == 'Пианино':
            if keyboard.is_pressed('q'):
                'Another victim.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('q')
            if keyboard.is_pressed('w'):
                'Boy next door.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('w')
            if keyboard.is_pressed('e'):
                'Deep dark fantasies.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('e')
            if keyboard.is_pressed('r'):
                'Do you like what you see.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('r')
            if keyboard.is_pressed('t'):
                'Dungeon master.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('t')
            if keyboard.is_pressed('y'):
                'fuck you....mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('y')
            if keyboard.is_pressed('u'):
                'FUCK YOU.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('u')
            if keyboard.is_pressed('i'):
                'ganging up.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('i')
            if keyboard.is_pressed('o'):
                'I dont do Anal.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('o')
            if keyboard.is_pressed('p'):
                'Iam cumming.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('p')
            if keyboard.is_pressed('a'):
                'Id be right happy to.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('a')
            if keyboard.is_pressed('s'):
                'It gets bigger when i pull on it.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('s')
            if keyboard.is_pressed('d'):
                'Its a loan.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('d')
            if keyboard.is_pressed('f'):
                'Its Mcarb.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('f')
            if keyboard.is_pressed('g'):
                'Its so fucking deep.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('g')
            if keyboard.is_pressed('h'):
                'Lash of the spanking.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('h')
            if keyboard.is_pressed('j'):
                'Lets suck some dick.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('j')
            if keyboard.is_pressed('k'):
                'Lube it up.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('k')
            if keyboard.is_pressed('l'):
                'Mmmmh.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('i')
            if keyboard.is_pressed('z'):
                'Oh shit iam sorry.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('z')
            if keyboard.is_pressed('x'):
                'Oh yes sir.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('x')
            if keyboard.is_pressed('c'):
                'Orgasm 1.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('c')
            if keyboard.is_pressed('v'):
                'Orgasm 2.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('v')
            if keyboard.is_pressed('b'):
                'RIP EARS ORGASM.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('b')
            if keyboard.is_pressed('n'):
                'WOO.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('n')
            if keyboard.is_pressed('m'):
                'Spit YEEEEEAAAAHHH.mp3'.play()
                if self.button_1.is_pressed:
                    self.zapis.append('m')


    def Recording_music(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Жги!!!!", "Введите предпологаемое название композиции")
        if okBtnPressed:
            self.button_1.setText(i)
            self.Name_zapisi = i

    def Saving_music(self):
        if len(self.zapis) == 0:
            self.button_save.setText("нет записи")
        elif len(self.zapis) != 0:
            self.button_save.setText("Сохранить запись")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
