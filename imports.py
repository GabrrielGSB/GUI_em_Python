import sys
import csv
import serial
import os
import time as t
from PyQt5.QtCore import Qt, QTimer, QProcess
from PyQt5.QtGui import QColor, QPalette, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QTabWidget,
  QWidget,
  QHBoxLayout,
  QStackedLayout,
  QVBoxLayout,
  QComboBox,
  QLineEdit,
  QApplication
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
# from CriarCSV import *