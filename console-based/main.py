from Equation import Expression
import numpy as np
import matplotlib.pyplot as plt
from sys import exit

# Suppress warning for division by zero

def main():
	global expression, fx, result
	expression, fx, result = 3 * (None,)
	alive = True

	while alive:
		expression = read_expression('Enter the expression (in x): ')
		a, *b = read_range('Enter the minimum value of x: ', 'Enter the maximum value of x: ')

		try:
			result = expression((a + b) / 2)
			if result is None:
				raise ValueError
		except:
			print('Bad expression or value(s)!\n')
			continue
		
		x = np.linspace(a, b, 100)
		y = np.vectorize(expression)(x)

		axis = plt.axes()
		axis.plot(x, y)
		axis.set_xlim((a, b))
		plt.show()


def read_expression(prompt=''):
	expr_raw = read_input(prompt)
	try:
		expr_eval = Expression(expr_raw, ['x'])
		return expr_eval
	except:
		print('Invalid expression!\n')
		return None

def read_range(*prompts):
	range_final = []
	for prompt in prompts:
		range_eval = read_input(prompt, lambda t: Expression(t)())
		range_final.append(range_eval)
	return range_final

def read_input(prompt='', input_type=str):
	in_val = None
	while in_val is None:
		try:
			in_val = input_type(input(prompt))
		except (KeyboardInterrupt, EOFError):
			exit(0)
		except:
			in_val = None
			continue
	return in_val

if __name__ == '__main__':
	main()