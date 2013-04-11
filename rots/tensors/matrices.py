import numbers

def gauss_jordan(m, eps = 1.0/(10**10)):
    """ Puts given matrix (2D array) into the Reduced Row Echelon Form.
        Returns True if successful, False if 'm' is singular.
        NOTE: make sure all the matrix items support fractions! Int matrix will NOT work!
        Written by Jarno Elonen in April 2005, released into Public Domain"""

    assert isinstance(m, list), \
           'Input must be a matrix represented as a list of lists'
    assert isinstance(eps, numbers.Number), 'Input must be a number'
    if __debug__:
        for row in m:
            assert isinstance(row, list), \
                   'Input must be a matrix represented as a list of lists'
            for item in row:
                assert isinstance(item, numbers.Number), \
                       'All elements in the matrix must be numbers'
    
    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
        maxrow = y
        for y2 in range(y+1, h):    # Find max pivot
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for y2 in range(y+1, h):    # Eliminate column y
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # Backsubstitute
        c  = m[y][y]
        for y2 in range(0,y):
            for x in range(w-1, y-1, -1):
                m[y2][x] -=  m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w):       # Normalize row y
            m[y][x] /= c
    return True

def solve(M, b):
    """
    solves M*x = b
    return vector x so that M*x = b
    :param M: a matrix in the form of a list of list
    :param b: a vector in the form of a simple list of scalars
    """
    assert isinstance(b, list), \
           'Input must be a vector repressented as a list'
    assert isinstance(M, list), \
           'Input must be a matrix represented as a list of lists'
    if __debug__:
        for row in M:
            assert isinstance(row, list), \
                   'Input must be a matrix represented as a list of lists'
            for item in row:
                assert isinstance(item, numbers.Number), \
                       'All elements in the matrix must be numbers'
    
    m2 = [row[:]+[right] for row,right in zip(M,b) ]
    return [row[-1] for row in m2] if gauss_jordan(m2) else None

def inv(M):
    """
    return the inv of the matrix M
    """

    assert isinstance(M, list), \
           'Input must be a matrix represented as a list of lists'
    if __debug__:
        for row in M:
            assert isinstance(row, list), \
                   'Input must be a matrix represented as a list of lists'
            for item in row:
                assert isinstance(item, numbers.Number), \
                       'All elements in the matrix must be numbers'
    
    #clone the matrix and append the identity matrix
    # [int(i==j) for j in range_M] is nothing but the i(th row of the identity matrix
    m2 = [row[:]+[int(i==j) for j in range(len(M) )] for i,row in enumerate(M) ]
    # extract the appended matrix (kind of m2[m:,...]
    return [row[len(M[0]):] for row in m2] if gauss_jordan(m2) else None

def zeros( s , zero=0):
    """
    return a matrix of size `size`
    :param size: a tuple containing dimensions of the matrix
    :param zero: the value to use to fill the matrix (by default it's zero )
    """
    return [zeros(s[1:] ) for i in range(s[0] ) ] if not len(s) else zero

def OpenGL_to_matrix(matrix):
    ''' Takes a matrix in OpenGL standard (a single list of all elements
        in column major order, 4x4) and turns it into a matrix represented as
        a list of lists in row major order. The matrices must be 4x4. '''
    assert isinstance(matrix, list), 'Input must be a matrix in OpenGl standard'
    assert len(matrix) == 16, 'Input must be a matrix in OpenGl standard'
    if __debug__:
        for item in matrix:
            assert isinstance(item, numbers.Number), \
                   'Input must be a matrix in OpenGl standard'

    copy = matrix[:]
    out  = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for i in range(len(copy)):
        out[i%4][i//4] = copy[i]
    return out

def matrix_to_OpenGL(matrix):
    ''' Takes a matrix represented as a list of lists and turns it into a
        matrix in OpenGL standard. The matrices must be 4x4.'''
    assert isinstance(matrix, list), \
           'Input must be a matrix represented as a list of lists'
    assert len(matrix) == 4, 'The matrix must be 4x4'
    if __debug__:
        for row in matrix:
            assert isinstance(row, list), \
                   'Input must be a matrix represented as a list of lists'
            assert len(row) == 4, 'The matrix must be 4x4'
            for elem in row:
                assert isinstance(elem, numbers.Number), 'All elements must be numbers'

    copy = matrix[:][:]
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(4):
        for j in range(4):
            out[4*j + i] = copy[i][j]

    return out