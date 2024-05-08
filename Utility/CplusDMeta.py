try:
		from PyQt5.QtCore import pyqtWrapperType
except ImportError:
		from PyQt5.QtCore import QObject
		pyqtWrapperType = type(QObject)
from abc import ABCMeta

#Модуль реализации метакласса, необхомого для работы предаставления.
#pyqtWrapperType - метакласс, общий для оконных компонентов бибилотеки QT
#ABCMeta - метакласс для реализации астрактных суперклассов

#CplusDMeta - метакласс для представления.

class CplusDMeta(pyqtWrapperType, ABCMeta):
  pass
