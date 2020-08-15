from Equation import Expression
import numpy as np

def configure(canvas, figure, btn, text):
	# Define plotting function	
	def plot_result():
		# Clear canvas
		figure.clear()
		axes = figure.add_subplot(1, 1, 1)

		# Calculate
		x = np.linspace(1, 10, 100)
		y = x ** 2
		a, b = 1, 10

		# Draw
		axes.set_xlim((a, b))
		axes.plot(x, y)
		canvas.draw()
	
	# Plot on click
	btn.clicked.connect(plot_result)