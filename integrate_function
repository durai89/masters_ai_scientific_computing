'''
Function to calculate symbolic and definite integral of a polynomial of any degree.

:parameter
    :param poly - input polynomial expressed as list of tuples where first element in tuple represents coefficient
    and the second element is exponent.
    :param start - integral lower range
    :param stop - integral upper range

:returns
    symbolic integral polynomial
    definite_integral_value
'''
def integrate(poly, start, stop):
    integral_map = {}
    integral_a = 0
    integral_b = 0
    integral = None
    for term in poly:
        key = term[1] + 1
        value = round(term[0] / (term[1] + 1), 2)
        integral_map[key] = value
        integral_a += value * pow(start, key)
        integral_b += value * pow(stop, key)
        temp_integral = None
        if key > 1:
            temp_integral = str(value) + 'x^' + str(key)
        elif key == 1:
            temp_integral = str(value) + 'x'
        if integral is not None:
            integral = integral + \
                       (' +' if value > 0 else '') + ' ' + temp_integral
        else:
            integral = temp_integral
    def_integral = integral_b - integral_a
    return integral + " + C", def_integral