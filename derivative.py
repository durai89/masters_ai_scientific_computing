'''
Function to calculate symbolic and numerical derivative of an input polynomial of any degree.

:parameter
    :param input_polynomial - input polynomial expressed as list of tuples where first element in tuple represents coefficient
    and the second element is exponent.
    :param dx - smaller dx (tiny nudge to x) to consider for derivative.

:returns
    symbolic derivative polynomial
    numerical derivative value.
'''
def derivative(input_polynomial, dx):
    derivative = None
    numerical_derivative = 0
    for term in input_polynomial:
        if term[1] != 0:
            key = term[1] - 1
            value = round(term[1] * term[0], 2)
            numerical_derivative += value * pow(key, dx)
            if key > 1:
                temp_derivative = str(value) + 'x^' + str(key)
            elif key == 1:
                temp_derivative = str(value) + 'x'
            else:
                temp_derivative = str(value)
            if derivative is not None:
                derivative = derivative + (' +' if value > 0 else '') + ' ' + temp_derivative
            else:
                derivative = temp_derivative
    return derivative, numerical_derivative