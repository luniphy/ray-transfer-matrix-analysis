"""
198801 Introduction to Programming: Programming in Python

Final Examination: Ray Transfer Matrix Analysis - data file

:Author: Lukas Niggl
"""

# Error messages
MATRIX_ELEMENT_TYPE_ERROR = 'The matrix elements must be of type integer or float.'
VECTOR_ELEMENT_TYPE_ERROR = 'The vector elements must be of type integer or float.'
MATRIX_DIMENSION_ERROR = 'The matrix must be a square matrix.'
MATRIX_VECTOR_DIMENSION_ERROR = 'The number of columns of the matrix must match number of elements of vector.'

ANGLE_TYPE_ERROR = 'The angle must be of type integer or float.'
ANGLE_VALUE_ERROR = 'The angle must be within [0°, 90°].'
OUTGOING_TYPE_ERROR = 'The chosen mode must be of type boolean.'
DISTANCE_TYPE_ERROR = 'The distance must be of type integer or float.'
DISTANCE_VALUE_ERROR = 'The distance must be smaller than the radius of the spherical refraction device and greater ' \
                       'or equal 0.'


# Refractive indices
# -> Wikipedia: https://de.wikipedia.org/wiki/Brechungsindex#Brechungsindex_der_Luft_und_anderer_Stoffe
n_air = 1.000292
n_glass = 1.52

# Additional values for optical matrices
radius = 2 * 10**(-2)  # Typical value: 2cm
curvature = 1 / radius
focal_point_focussing = 0.01  # Typical value 1cm
focal_point_defocussing = - focal_point_focussing

# Matrices for optical devices (Wikipedia: https://de.wikipedia.org/wiki/Matrizenoptik)
OPTICAL_MATRICES = {'Refraction at plane': [[1, 0],
                                            [0, n_air / n_glass]],
                    'Refraction at sphere': [[1, 0],
                                             [(n_air / n_glass - 1) * curvature, n_air / n_glass]],
                    'Refraction at focussing thin lens': [[1, 0],
                                                          [-1 / focal_point_focussing, 1]],
                    'Refraction at defocussing thin lens': [[1, 0],
                                                            [-1 / focal_point_defocussing, 1]],
                    'Reflection at plane mirror': [[1, 0],
                                                   [0, 1]]}

# (Used Mathematica to determine the inverse matrices)
INVERSE_OPTICAL_MATRICES = {'Refraction at plane': [[1, 0],
                                                    [0, n_glass / n_air]],
                            'Refraction at sphere': [[1, 0],
                                                     [(n_glass / n_air - 1) * curvature, n_glass / n_air]],
                            'Refraction at focussing thin lens': [[1, 0],
                                                                  [1 / focal_point_focussing, 1]],
                            'Refraction at defocussing thin lens': [[1, 0],
                                                                    [1 / focal_point_defocussing, 1]],
                            'Reflection at plane mirror': [[1, 0],
                                                           [0, 1]]}
