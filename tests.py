"""
198801 Introduction to Programming: Programming in Python

Final Examination: Ray Transfer Matrix Analysis - testing file

:Author: Lukas Niggl



multiply_mat_vec(M, v) -------------------------------------------------------------------------------------------------

Correct arguments:

>>> multiply_mat_vec([[3]], [2])
[6]
>>> multiply_mat_vec([[1, 0], [0, 1]], [2, 3])
[2, 3]
>>> multiply_mat_vec([[7.2, -0.1], [3.5, 2]], [-1, 3.4])
[-7.54, 3.3]
>>> multiply_mat_vec([[1, 1, 0], [0, -1, 2], [2, 0, 3]], [1, 0, 2])
[1, 4, 8]
>>> multiply_mat_vec([[4, 0, 6, -3], [0, 0, 3, 4], [-2, 1, 0, 4], [1, 1, 0, 5]], [4, 1, 2, -1])
[31, 2, -11, 0]


Invalid types:

>>> multiply_mat_vec([[1, '2'], [3, 4]], [1, 0])
Traceback (most recent call last):
...
TypeError: The matrix elements must be of type integer or float.
>>> multiply_mat_vec([[-1, 9], [None, 4]], [0, 5])
Traceback (most recent call last):
...
TypeError: The matrix elements must be of type integer or float.
>>> multiply_mat_vec([[-1, 8], [4.4, 5]], [0, '13'])
Traceback (most recent call last):
...
TypeError: The vector elements must be of type integer or float.


Invalid arguments:

>>> multiply_mat_vec([[-1, 9], [1, -4], [4, -4]], [0, 5])
Traceback (most recent call last):
...
ValueError: The matrix must be a square matrix.
>>> multiply_mat_vec([[4, 7, -4], [1, 5, 10]], [0, 5.4, 1])
Traceback (most recent call last):
...
ValueError: The matrix must be a square matrix.
>>> multiply_mat_vec([[-1, 9, 4], [1, -4, 0], [1, 1, 3]], [4, 0])
Traceback (most recent call last):
...
ValueError: The number of columns of the matrix must match number of elements of vector.
>>> multiply_mat_vec([[-4, 6], [-1, -3]], [0, 1.2, 1])
Traceback (most recent call last):
...
ValueError: The number of columns of the matrix must match number of elements of vector.



get_angles(angle, outgoing, distance) ----------------------------------------------------------------------------------

Correct arguments:

>>> get_angles(0.001)
{'Incoming angle': 0.001, 'Distance': 0.01, 'Angle results': {'Refraction at plane': 0.0, 'Refraction at sphere': -0.17, 'Refraction at focussing thin lens': -1.0, 'Refraction at defocussing thin lens': 1.0, 'Reflection at plane mirror': 0.0}}
>>> get_angles(45)
{'Incoming angle': 45, 'Distance': 0.01, 'Angle results': {'Refraction at plane': 29.61, 'Refraction at sphere': 29.44, 'Refraction at focussing thin lens': 44.0, 'Refraction at defocussing thin lens': 46.0, 'Reflection at plane mirror': 45.0}}
>>> get_angles(23.34, False)
{'Outgoing angle': 23.34, 'Distance': 0.01, 'Angle results': {'Refraction at plane': 35.47, 'Refraction at sphere': 35.73, 'Refraction at focussing thin lens': 24.34, 'Refraction at defocussing thin lens': 22.34, 'Reflection at plane mirror': 23.34}}
>>> get_angles(39, False, 0.001)
{'Outgoing angle': 39, 'Distance': 0.001, 'Angle results': {'Refraction at plane': 59.26, 'Refraction at sphere': 59.29, 'Refraction at focussing thin lens': 39.1, 'Refraction at defocussing thin lens': 38.9, 'Reflection at plane mirror': 39.0}}
>>> get_angles(89.99, True, 0.019)
{'Incoming angle': 89.99, 'Distance': 0.019, 'Angle results': {'Refraction at plane': 59.22, 'Refraction at sphere': 58.9, 'Refraction at focussing thin lens': 88.09, 'Refraction at defocussing thin lens': 91.89, 'Reflection at plane mirror': 89.99}}


Invalid types:

>>> get_angles('23')
Traceback (most recent call last):
...
TypeError: The angle must be of type integer or float.
>>> get_angles(62, 'False')
Traceback (most recent call last):
...
TypeError: The chosen mode must be of type boolean.
>>> get_angles(62, False, '0.005')
Traceback (most recent call last):
...
TypeError: The distance must be of type integer or float.


Invalid arguments:

>>> get_angles(90.01)
Traceback (most recent call last):
...
ValueError: The angle must be within [0°, 90°].
>>> get_angles(-0.01)
Traceback (most recent call last):
...
ValueError: The angle must be within [0°, 90°].
>>> get_angles(45, True, -0.01)
Traceback (most recent call last):
...
ValueError: The distance must be smaller than the radius of the spherical refraction device and greater or equal 0.
>>> get_angles(21, False, 0.021)
Traceback (most recent call last):
...
ValueError: The distance must be smaller than the radius of the spherical refraction device and greater or equal 0.



print_angles(angle_dic) ------------------------------------------------------------------------------------------------

Correct arguments:

>>> print_angles(get_angles(47))
The resulting outgoing angles due to refraction (between air and glass)/ reflection for an incoming angle of 47° at a distance of 0.01m from the optical axis are:
Refraction at plane: 30.93°
Refraction at sphere: 30.76°
Refraction at focussing thin lens: 46.0°
Refraction at defocussing thin lens: 48.0°
Reflection at plane mirror: 47.0°
>>> print_angles(get_angles(23.55, False, 0.004))
The resulting incoming angles due to refraction (between air and glass)/reflection for an outgoing angle of 23.55° at a distance of 0.004m from the optical axis are:
Refraction at plane: 35.79°
Refraction at sphere: 35.89°
Refraction at focussing thin lens: 23.95°
Refraction at defocussing thin lens: 23.15°
Reflection at plane mirror: 23.55°
"""

from main import *
import doctest
