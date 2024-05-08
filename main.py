import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Model.CplusDModel import CplusDModel
from Controller.CplusDController import CplusDController

def main():
  app = QApplication(sys.argv)
  #Создаем модель
  model = CplusDModel()
  #создаем контроллер и передаеи ему ссылку
  controller = CplusDController(model)
  #Запускаем приложение
  app.exec()
if __name__ == "__main__":
  main()