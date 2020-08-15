from PySide2.QtWidgets import \
	QMainWindow, QWidget, QHBoxLayout, \
	QVBoxLayout, QPushButton, QTextEdit
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import backmath


# The main UI of the application
class MyApp(QMainWindow):
	def __init__(self, app, appname, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.hide()
		self.setMinimumSize(640, 480)

		self.setWindowTitle(appname)

		# Make interface layouts
		window = QWidget()
		layout = QVBoxLayout()
		top_section = QHBoxLayout()
		bottom_section = QVBoxLayout()

		# Create widgets and items
		figure = plt.figure()
		canvas = FigureCanvas(figure)
		expr_input = QTextEdit()
		plot_button = QPushButton('Plot')

		# Configure backend
		backmath.configure(canvas=canvas, figure=figure, btn=plot_button, text=expr_input)
		
		# Finalize and display
		...
		top_section.addWidget(canvas)
		bottom_section.addWidget(plot_button)
		layout.addLayout(top_section)
		layout.addLayout(bottom_section)
		window.setLayout(layout)
		self.setCentralWidget(window)
		self.show()