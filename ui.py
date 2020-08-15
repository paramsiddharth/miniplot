from PySide2.QtWidgets import \
	QMainWindow, QWidget, QHBoxLayout, \
	QVBoxLayout, QPushButton, QLineEdit, \
	QLabel, QGridLayout, QSizePolicy
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
		
		top_section = QVBoxLayout()
		
		label_section = QHBoxLayout()
		range_section = QGridLayout()
		bottom_section = QVBoxLayout()

		# Create widgets and items
		figure = plt.figure()
		canvas = FigureCanvas(figure)
		
		label = QLabel(
			f'''Welcome to {appname}!
Plot any equation of the form y = f(x).

Enter the function f(x), specify the range of x, and click Plot!''')
		
		expr_label = QLabel('f(x) =')
		expr_input = QLineEdit()

		range_label1 = QLabel('Minimum (x):')
		range_min = QLineEdit()
		range_label2 = QLabel('Maximum (x):')
		range_max = QLineEdit()

		plot_button = QPushButton('Plot')

		# Configure backend
		backmath.configure(canvas=canvas, figure=figure, btn=plot_button, text=expr_input, limits=(range_min, range_max))
		
		# Finalize and display
		...
		top_section.addWidget(canvas)

		label_section.addWidget(expr_label)
		label_section.addWidget(expr_input)

		equally_spaced = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		equally_spaced.setHorizontalStretch(1)

		range_label1.setSizePolicy(equally_spaced)
		range_min.setSizePolicy(equally_spaced)
		range_label2.setSizePolicy(equally_spaced)
		range_max.setSizePolicy(equally_spaced)

		range_label1.setAlignment(Qt.AlignRight)
		range_label2.setAlignment(Qt.AlignRight)

		range_section.addWidget(range_label1, 0, 0, 1, 1)
		range_section.addWidget(range_min, 0, 1, 1, 1)
		range_section.addWidget(range_label2, 0, 2, 1, 1)
		range_section.addWidget(range_max, 0, 3, 1, 1)
		
		bottom_section.addWidget(label)
		bottom_section.addLayout(label_section)
		bottom_section.addLayout(range_section)
		bottom_section.addWidget(plot_button)
		
		layout.addLayout(top_section)
		layout.addLayout(bottom_section)
		
		window.setLayout(layout)
		self.setCentralWidget(window)
		self.show()