from sys import argv
from PySide2.QtWidgets import QApplication
import ui

# Made with ❤ by Param

def main():
	# Initialize application
	global app, appname
	app = QApplication(argv)
	appname = 'Plotly'

	# Create main window
	programmme = ui.MyApp(app, appname)
	programmme.show()

	app.exec_()

if __name__ == '__main__':
	main()