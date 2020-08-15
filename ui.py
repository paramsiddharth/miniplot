from PySide2.QtWidgets import \
	QMainWindow, QWidget, QHBoxLayout, \
	QVBoxLayout, QPushButton, QLineEdit, \
	QLabel, QGridLayout, QSizePolicy, \
	QStatusBar, QMessageBox, QSpinBox, \
	QMenuBar
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import backmath

# The main UI of the application
class MyApp(QMainWindow):
	def __init__(self, app, appname, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.hide()
		#self.setMinimumSize(640, 480)
		self.setFixedSize(self.geometry().width(), self.geometry().height())
		self.setWindowIcon(QIcon('icon.ico'))
		self.setWindowTitle(appname)

		# Create menu bar
		menu_bar = QMenuBar()

		help_menu = menu_bar.addAction('&Help')
		about_menu = menu_bar.addAction('A&bout')
		exit_menu = menu_bar.addAction('&Exit')

		self.setMenuBar(menu_bar)

		# Make interface layouts
		window = QWidget()
		layout = QVBoxLayout()
		
		top_section = QVBoxLayout()

		buttons = QGridLayout()
		middle_section = QHBoxLayout()
		
		label_section = QHBoxLayout()
		range_section = QGridLayout()
		clarity_section = QHBoxLayout()
		plot_section = QHBoxLayout()
		bottom_section = QVBoxLayout()

		status_layout = QHBoxLayout()

		# Create widgets and items
		figure = plt.figure()
		canvas = FigureCanvas(figure)
		
		label = QLabel(
			f'''Welcome to {appname}!
Plot any equation of the form y = f(x).
Use the options below to plot your own equation!''')

		help_message = QMessageBox()
		help_message.setTextFormat(Qt.RichText)
		help_message.setText(f'''<h3>Help</h3>
{appname} lets you plot any equation of the form y = f(x).
<br/>
Enter the function f(x), specify the range of x, and click Plot!
<br/><br/>
Operators : <code>+, -, *, /</code><br/>
Variable : <code>x</code><br/>
Functions : <code>sin, cos, tan</code><br/>
<code>pi</code> : π<br/>
<code>e</code> : Exponential e<br/>
<code>c</code> : Speed of Light<br/>''')
		help_message.setStandardButtons(QMessageBox.Ok)
		help_message.setWindowTitle(f'{appname} - Help')
		self.help = help_message

		help_button = QPushButton('Help...')
		help_button.clicked.connect(self.help.exec_)

		about_message = QMessageBox()
		about_message.setWindowTitle(f'{appname} - About')
		about_message.setTextFormat(Qt.RichText)
		about_message.setText(f'''<h3>About</h3>
{appname} is created in PySide2 (Qt), using \
the Matplotlib and Equation PyPI modules for plotting and parsing expressions respectively.
<br/><br/>
Created by <a href="http://paramsid.com">Param Siddharth</a>.''')
		about_message.setStandardButtons(QMessageBox.Ok)
		self.about = about_message

		about_button = QPushButton('About...')
		about_button.clicked.connect(self.about.exec_)
		
		expr_label = QLabel('f(x) =')
		expr_input = QLineEdit()

		range_label1 = QLabel('Minimum (x):')
		range_min = QLineEdit()
		range_label2 = QLabel('Maximum (x):')
		range_max = QLineEdit()

		clarity_label = QLabel('Clarity:')
		clarity_spinbox = QSpinBox()
		clarity_spinbox.setRange(1, 10000)
		clarity_spinbox.setValue(100)

		plot_button = QPushButton('Plot')
		plot_button.setMaximumWidth(200)

		status = QStatusBar()
		status_text = QLabel('')
		status_text.setStyleSheet('color: #999999;')

		attribution = QLabel('Made with <span style="color: red;">❤</span> by <a href="http://paramsid.com">Param</a>')
		attribution.setTextFormat(Qt.RichText)
		attribution.setStyleSheet('color: #555555; font-size: 20px;')
		attribution.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		help_menu.triggered.connect(self.help.exec_)
		about_menu.triggered.connect(self.about.exec_)
		exit_menu.triggered.connect(self.close)

		# Configure backend
		backmath.configure(canvas=canvas, figure=figure, btn=plot_button,
			text=expr_input, limits=(range_min, range_max), status=status_text, 
			range_text=(range_min, range_max), clarity=clarity_spinbox)
		
		# Finalize and display
		top_section.addWidget(canvas)

		buttons.addWidget(help_button, 0, 0, 1, 1)
		buttons.addWidget(about_button, 0, 1, 1, 1)
		
		middle_section.addWidget(label)
		middle_section.addLayout(buttons)

		label_section.addWidget(expr_label)
		label_section.addWidget(expr_input)

		equally_spaced = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		equally_spaced.setHorizontalStretch(1)

		range_label1.setSizePolicy(equally_spaced)
		range_min.setSizePolicy(equally_spaced)
		range_label2.setSizePolicy(equally_spaced)
		range_max.setSizePolicy(equally_spaced)

		range_label1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
		range_label2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		range_section.addWidget(range_label1, 0, 0, 1, 1)
		range_section.addWidget(range_min, 0, 1, 1, 1)
		range_section.addWidget(range_label2, 0, 2, 1, 1)
		range_section.addWidget(range_max, 0, 3, 1, 1)

		clarity_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

		clarity_section.addWidget(clarity_label)
		clarity_section.addWidget(clarity_spinbox)

		plot_section.addWidget(plot_button)

		status.addWidget(status_text)
		status.addPermanentWidget(attribution)

		status_layout.addWidget(status)

		bottom_section.addLayout(label_section)
		bottom_section.addLayout(range_section)
		bottom_section.addLayout(clarity_section)
		bottom_section.addLayout(plot_section)
		
		layout.addLayout(top_section)
		layout.addLayout(middle_section)
		layout.addLayout(bottom_section)
		layout.addLayout(status_layout)
		
		window.setLayout(layout)
		self.setCentralWidget(window)
		self.show()

		status_text.setText('READY ')