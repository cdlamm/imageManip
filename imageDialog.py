import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class imageDialog(QWidget):
   def __init__(self, parent = None):
      super(imageDialog, self).__init__(parent)

   def getGamma(self):
      num,ok = QInputDialog.getDouble(self,"Gamma Input","Enter Gamma Correction Value")

      if ok:
         return num

   def getAMix(self):
      num,ok = QInputDialog.getDouble(self,"Foreground Image Input","Enter Foreground Mix Value")

      if ok:
         return num

   def getBMix(self):
      num,ok = QInputDialog.getDouble(self,"Background Image Input","Enter Background Mix Value")

      if ok:
         return num

   def getLum(self):
      num,ok = QInputDialog.getDouble(self,"LumaKey Hue Value","Enter Value You Wish to Extract")

      if ok:
         return num

   def getHueLow(self):
      num,ok = QInputDialog.getInt(self,"Low Hue Range Input","Enter lowest value of hue you wish to clear (0-360)")

      if ok:
         return num

   def getHueHigh(self):
      num,ok = QInputDialog.getInt(self,"High Hue Range Input","Enter highest values of hue you wish to clear (0-360)")

      if ok:
         return num

   def getSatLow(self):
      num,ok = QInputDialog.getDouble(self,"Low Saturation Range Input","Enter lowest values of saturation you wish to clear (0-1)")

      if ok:
         return num
