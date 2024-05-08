class CplusDModel:
  def __init__(self):
    self._mC = 0
    self._mD  = 0
    self._mSum = 0
    self._mObservers = []
  @property
  def c(self):
    return self._mC
  @property
  def d(self):
      return self._mD
  @property
  def sum(self):
      return self._mSum
  @c.setter
  def c(self, value):
    self._mC = value
    self._mSum = self._mC + self._mD
    self.notifyObservers()
  @d.setter
  def d(self, value):
      self._mD = value
      self._mSum = self._mC + self._mD
      self.notifyObservers()
  def addserver(self, inObserver):
      self._mObservers.append(inObserver)

  def removeObserver(self, inObserver):
    self._mObservers.remove(inObserver)

  def notifyObservers(self):
    for x in self._mObservers:
      x.modelIsChanged()
#Класс CplusDModel представляет собой реалицию модели данных. В модели хранятся переменные: c,d,sum. Модель представляет собой интерфейс, через который можно работать с хранимыми значениями.
#Модель содержит методы регистрации, удаления и оповещиния наблюдателей. 
#Паттерн наблюдатель - означает, что класс должен поддерживать функции добавления, удаления, оповещения наблюдателей. При этом модель полностью не зависит от контроллеров и представлений. Все созданные наблюдатели должны быть потомками абстракного класса, при вызове метода оповещения(modelIsChanged()).
  
    
    