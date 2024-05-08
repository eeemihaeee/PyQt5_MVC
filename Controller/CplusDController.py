from View.CplusDView import CplusDView

#Класс представляет реализацию контроллера. Согласовывает работу представления с моделью.
class CplusDController():
  def __init__(self, inModel):
    #Конструктор принимает ссылку на модель,  созадет и отображает представление.
    self.mModel = inModel
    self.mView = CplusDView(self, self.mModel)
    
    self.mView.show()

  def setC(self):
    #Пре завершиии редактирования поля ввода данных для С контроллер изменаяет свойство модели.
    c = self.mView.ui.le_c.text()
    self.mModel.setC(c)
  def setD(self):
    #Пре завершиии редактирования поля ввода данных для D контроллер изменаяет свойство модели.
    d = self.mView.ui.le_d.text()
    self.mModel.setD(d)
    