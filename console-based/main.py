from Equation import Expression
import numpy as np
import matplotlib.pyplot as plt
from sys import exit, stderr

# Suppress warnings (e. g. Division by Zero) by python -W ignore main.py

def main():
	global expression, result
	expression, result = 2 * (None,)
	alive = True

	# Main loop
	while alive:
		# Input
		expression = read_expression('Enter the expression (in x): ')
		a, b = read_range('Enter the minimum value of x: ', 'Enter the maximum value of x: ')

		# Try to solve for the values in between
		try:
			result = expression((a + b) / 2)
			if result is None:
				raise ValueError
		except:
			print('Bad expression or value(s)!\n', file=stderr)
			continue
		
		# Create arrays for x and y
		x = np.linspace(a, b, 100)
		y = np.vectorize(expression)(x)

		# Plot and display
		axis = plt.axes()
		axis.plot(x, y)
		axis.set_xlim((a, b))
		plt.show()


def read_expression(prompt=''):
	'''
	Read an expression to plot
	'''
	expr_raw = read_input(prompt) # Expression as string
	try:
		expr_eval = Expression(expr_raw, ['x']) # Parse expression, which may be in 'x'
		return expr_eval
	except:
		print('Invalid expression!\n', file=stderr)
		return None

def read_range(*prompts):
	'''
	Read the range for the independent variable (x)
	'''
	range_final = []
	for prompt in prompts:
		# Parse and save input
		range_eval = read_input(' ' + prompt, lambda t: Expression(t)())
		range_final.append(range_eval)
	return range_final

def read_input(prompt='', input_type=str):
	'''
	Read input until valid parseable input of the specified type is received
	'''
	in_val = None
	while in_val is None:
		try:
			# Try to cast input to type
			in_val = input_type(input(prompt))
		except (KeyboardInterrupt, EOFError):
			exit(0)
		except:
			# Invalid input, try again
			print('Invalid value!\n', file=stderr)
			in_val = None
			continue
	return in_val

if __name__ == '__main__':
	main()