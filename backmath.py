from Equation import Expression
import numpy as np
from sys import stderr

def configure(canvas, figure, btn, text, limits):	
	def show_error(prompt=''):
		print(f'Error: {prompt}', file=stderr)

	def plot_result():
		# Clear canvas
		figure.clear()
		axes = figure.add_subplot(1, 1, 1)

		# Read input
		fx = read_expression()
		a, b = read_range()
		if fx is None:
			show_error('Invalid expression!')
			return
		
		if a is None or b is None:
			show_error('Invalid range!')
			return

		# Calculate
		clarity = 100
		x = np.linspace(a, b, clarity)
		try:
			y = np.vectorize(fx)(x)
		except:
			show_error('Invalid expression!')
			return

		# Draw
		axes.set_xlim((a, b))
		axes.axis('on')
		axes.plot(x, y)
		canvas.draw()

	def read_expression():
		expr_raw = text.text()
		try:
			expr_eval = Expression(expr_raw, ['x'])
			return expr_eval
		except:
			return None

	def read_range():
		a_raw, b_raw = limits[0].text(), limits[1].text()
		try:
			a_eval = Expression(a_raw)()
			b_eval = Expression(b_raw)()
			return a_eval, b_eval
		except:
			return 2 * (None,)
	
	# Plot on click
	btn.clicked.connect(plot_result)