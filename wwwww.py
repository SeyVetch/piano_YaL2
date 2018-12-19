import keyboard
import sys
import os
import time
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtCore import Qt


def get_name(line):
    return line.split('"')[1]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.Chose = 'Гачи'
        self.zapis = []
        self.flag = False
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
        self.button_save.resize(100, 23)
        self.button_save.setText("нет записи")
        self.button_save.clicked.connect(self.Saving_music)
        self.button_save = QPushButton(self)
        self.button_save.move(24, 260)        
        self.button_save.resize(75, 23)
        self.button_save.setText("play")
        self.button_save.clicked.connect(self.play_music) #setStyleSheet("background-color: red")
        self.play = ['', None]
        self.f = None
        
    def launch(self):
        i, launchbtn = QInputDialog.getItem(
            self,
            "На чем предподчтете музыцировать?",
            "",
            ("Пианино", "placeholder"),
            0,
            False
        )
        self.Chose = i
        
    def choose_music(self):
        f = open('записи/' + 'lates_one' + '.txt', 'r').read().split('|')[1:]
        name, launchbtn = QInputDialog.getItem(
            self,
            "Выберете название записи",
            "",
            [get_name(j) for j in f],
            0,
            False
        )
        self.play = [[get_name(j) for j in f].index(name), f]
        
    def play_music(self):
        self.choose_music()
        name, f = self.play
        line = f[name]
        notes = line.split('"')[2].split('/')
        for j in notes:
            for i in j:
                if i == 't':
                    QSound.play('piano/C.wav')
                if i == 'y':
                    QSound.play('piano/C#.wav')
                if i == 'u':
                    QSound.play('piano/D.wav')
                if i == 'i':
                    QSound.play('piano/D#.wav')
                if i == 'o':
                    QSound.play('piano/E.wav')
                if i == 'p':
                    QSound.play('piano/F.wav')
                if i == '[':
                    QSound.play('piano/F#.wav')
                if i == ']':
                    QSound.play('piano/G.wav')
                if i == 'q':
                    QSound.play('piano/G#.wav')
                if i == 'w':
                    QSound.play('piano/A.wav')
                if i == 'e':
                    QSound.play('piano/A#.wav')
                if i == 'r':
                    QSound.play('piano/B.wav')

    def launch_piano(self):
        pass
    
    
    def keyPressEvent(self, e):
        self.f = open('записи/' + 'lates_one' + '.txt', 'a')
        note = 'qwertyuiop[]'
        try:
            zapis = []
            if True:
                for i in range(12):
                    if keyboard.is_pressed(note[i]):
                        if self.flag:
                            self.f.write(note[i])
                if e.key() == Qt.Key_T:
                    QSound.play('piano/C.wav')
                if e.key() == Qt.Key_Y:
                    QSound.play('piano/C#.wav')
                if e.key() == Qt.Key_U:
                    QSound.play('piano/D.wav')
                if e.key() == Qt.Key_I:
                    QSound.play('piano/D#.wav')
                if e.key() == Qt.Key_O:
                    QSound.play('piano/E.wav')
                if e.key() == Qt.Key_P:
                    QSound.play('piano/F.wav')
                if e.key() == Qt.Key_BracketLeft:
                    QSound.play('piano/F#.wav')
                if e.key() == Qt.Key_BracketRight:
                    QSound.play('piano/G.wav')
                if e.key() == Qt.Key_Q:
                    QSound.play('piano/G#.wav')
                if e.key() == Qt.Key_W:
                    QSound.play('piano/A.wav')
                if e.key() == Qt.Key_E:
                    QSound.play('piano/A#.wav')
                if e.key() == Qt.Key_R:
                    QSound.play('piano/B.wav')
            self.f.write('/')
        except:
            pass
        self.f.close()

    def Recording_music(self):
        self.f = open('записи/' + 'lates_one' + '.txt', 'a')
        i, okBtnPressed = QInputDialog.getText(
            self, "Жги!!!!", "Введите предпологаемое название композиции")
        if okBtnPressed:
            try:
                self.button_rec.setText(i)
                self.Name_zapisi = i
                self.button_save.setText("Сохранить запись")
                self.flag = True
                self.f.write('|"'+i+'"')
            except Exception as e:
                print(e)
        self.f.close()

    def Saving_music(self):
        if len(self.zapis) == 0:
            self.button_save.setText("нет записи")
            self.button_rec.setText('начать запись')
        elif len(self.zapis) != 0:
            self.flag = False
            self.button_rec.setText("Начать запись")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
