#import MainWindow_rc
from PyQt5 import QtWidgets
from PyQt5.QtGui import  QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDMeta
from View.MainWindow import Ui_MainWindow

class CplusDView(QtWidgets.QMainWindow, CplusDObserver, metaclass = CplusDMeta):
  #Класс, отвечающий за визуальное представление
  def __init__(self, inController, inModel,parent=None):
    self.mController = inController
    self.mModel = inModel
    #Подключение визуальног преставления
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #Региструем представление, в качестве наблюдателя
    self.mModel.addObserver(self)
    #устанавливаем валидаторы полей ввода данных
    self.ui.le_c.setValidator(QDoubleValidator())
    self.ui.le_d.setValidator(QDoubleValidator())
    #Связываем событие завершения редактирования с метод котроллера
    self.connect(self.ui.le_c, pyqtSignal("editingFinished()"), self.mController.setC)
    self.connect(self.ui.le_d, pyqtSignal("editingFinished()"),self.mController.setD)
    