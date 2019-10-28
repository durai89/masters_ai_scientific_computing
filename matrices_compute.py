import csv

class Matrix:

    @staticmethod
    def get_size(matrix):
        '''
        Gets the dimension of a given matrix in tuple format.

        params:
            matrix : input matrix.

         returns:
            size of the matrix.
        '''
        return len(matrix), len(matrix[0])

    @staticmethod
    def check_dimensions_add_sub_op(matrix1, matrix2):
        '''
        Checks if the dimensions of two matrices are same
        and if it doesn't matches throws exception.

        params:
           matrix1 : first input matrix.
           matrix2 : second input matrix.
        '''
        if len(matrix1) != len(matrix2) and len(matrix1[0] != len(matrix2[0])):
            raise ValueError("Dimensions of the given matrices don't match..")

    @staticmethod
    def add(matrix1, matrix2):
        '''
        Adds two matrices.

        params:
            matrix1 : first matrix
            matrix2 : second matrix
        returns:
            sum of two matrices
        '''
        Matrix.check_dimensions_add_sub_op(matrix1, matrix2)
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    @staticmethod
    def subtract(matrix1, matrix2):
        '''
        subtracts two matrices.

        params:
            matrix1 : first matrix
            matrix2 : second matrix
        returns:
            result matrix after subtract operation
        '''
        Matrix.check_dimensions_add_sub_op(matrix1, matrix2)
        return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    @staticmethod
    def multiply(matrix1, matrix2):
        '''
        Multiply two matrices.

        params:
          matrix1 : first matrix
          matrix2 : second matrix

        returns:
            result matrix after multiplication
        '''
        if len(matrix1[0]) != len(matrix2):
            raise ArithmeticError("Matrices can't be multiplied. Invalid dimensions")
        product = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
        i = 0
        for row in matrix1:
            for col in range(len(matrix2[0])):
                temp_sum = 0
                k = 0
                for element in row:
                    temp_sum += element * matrix2[k][col]
                    k = k + 1
                product[i][col] = temp_sum
            i = i + 1
        return product

    @staticmethod
    def calc_determinant(matrix):
        '''
        calculate the determinant.

        params:
             matrix:  input matrix

        returns:
            determinant value.
        '''
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Only 2x2 matrices are supported")
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    @staticmethod
    def calc_inverse(matrix):
        '''
        Works out the inverse of a matrix

        params:
            matrix : input matrix

        returns:
            inverse of the given matrix
        '''
        if len(matrix) != 2 or len(matrix[0]) != 2:
            raise ValueError("Only 2x2 matrices are supported")
        determinant = Matrix.calc_determinant(matrix)
        if determinant == 0:
            raise ArithmeticError("Invalid determinant")
        return [[(matrix[1][1] / determinant), (-1 * matrix[0][1] / determinant)],
                [(-1 * matrix[1][0] / determinant), (matrix[0][0] / determinant)]]

    @staticmethod
    def calc_transpose(matrix):
        '''
        Works out the transpose of the given matrix

        params:
            matrix : input matrix

        returns:
            transpose of the given matrix
        '''
        transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transpose[col][row] = matrix[row][col]
        return transpose

    @staticmethod
    def export_matrix_csv(matrix, file_path):
        '''
        Creates a file matrix.csv if not exists and write out the matrix as csv records.

        params:
            input matrix.
        '''
        with open(file_path, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    @staticmethod
    def import_matrix_csv(file_path):
        '''
        Reads matrix.csv and load it into a matrix

        params:
            input matrix.
        '''
        reader = csv.reader(open(file_path, "r"), delimiter=",")
        matrix_input = list(reader)
        result_matrix = [[0 for j in range(len(matrix_input[0]))] for i in range(len(matrix_input))]
        for row in range(len(matrix_input)):
            for col in range(len(matrix_input[0])):
                result_matrix[row][col] = int(matrix_input[row][col])
        return result_matrix