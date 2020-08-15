from Equation import Expression
import numpy as np
from sys import stderr

def configure(canvas, figure, btn, text, limits, status, range_text, clarity):	
	def show_error(prompt=''):
		# print(f'Error: {prompt}', file=stderr)
		status.setText(f'ERROR: {prompt} ')
		status.setStyleSheet('color: red;')

	def plot_result(sample=False):
		# For the sample
		if sample:
			text.setText('sin(x)')
			range_text[0].setText('0')
			range_text[1].setText('2 * pi')
			plot_result()

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
		x = np.linspace(a, b, clarity.value())
		try:
			y = np.vectorize(fx)(x)
		except:
			show_error('Invalid expression!')
			return

		# Draw
		axes.set_xlim((a, b))
		axes.axis('on')
		axes.plot(x, y)
		axes.set_title(f'$y = {str(fx)}$') #.replace(' \\times ', ' '))
		axes.set_xlabel('x')
		axes.set_ylabel('y')
		canvas.draw()
		status.setText('SUCCESS ')
		status.setStyleSheet('color: green;')

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
	plot_result(sample=True)