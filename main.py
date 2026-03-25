"""
198801 Introduction to Programming: Programming in Python

Final Examination: Ray Transfer Matrix Analysis - main file

:Author: Lukas Niggl
"""

from config import *


def multiply_mat_vec(M, v):
    """
    This function returns the resulting vector of a matrix-vector-product.

    :param M: square matrix of dimension d
    :type M: list of list

    :param v: vector of dimension d
    :type v: list of integer or list of float

    :return: resulting vector of dimension d
    :rtype: list of integer or list of float

    :raises TypeError: if the elements of the matrix/vector are not of type: int or float
    :raises ValueError: if the dimensions of matrix and vector are not matching or matrix is not square matrix
    """

    # Sanity checks
    for row in M:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(MATRIX_ELEMENT_TYPE_ERROR)

    for element in v:
        if not isinstance(element, (int, float)):
            raise TypeError(VECTOR_ELEMENT_TYPE_ERROR)

    # Dimension checks
    for row in M:
        if len(row) != len(M):
            raise ValueError(MATRIX_DIMENSION_ERROR)

    if len(M) != len(v):
        raise ValueError(MATRIX_VECTOR_DIMENSION_ERROR)

    # Calculating the matrix-vector-product
    res, zum = list(), 0
    for i in range(len(M)):
        for j in range(len(v)):
            zum += M[i][j] * v[j]
        res.append(zum)
        zum = 0

    return res


def get_angles(angle, outgoing=True, distance=1 * 10**(-2)):
    """
    Given an angle, the function returns a dictionary of resulting angles from diverse optical devices.

    :param angle: input angle to determine resulting angles
    :type angle: int or float

    :param outgoing: selects mode of getting outgoing angles (True - default) or incoming angles (False)
    :type outgoing: bool

    :param distance: distance of the beam from the optical axis (default 1cm, typical value)
    :type distance: int or float

    :return: dictionary with the resulting angles as values and the optical devices as keys
    :rtype: dict

    :raises TypeError:  if the angle input or the distance is not of type: int or float.
                        if outgoing is not of type: bool
    :raises ValueError: if the angle is not within the range [0°, 90°]
                        if distance is not smaller than the radius of the spherical refraction device (2cm)
    """

    # Sanity check
    if not isinstance(angle, (int, float)):
        raise TypeError(ANGLE_TYPE_ERROR)

    if not isinstance(outgoing, bool):
        raise TypeError(OUTGOING_TYPE_ERROR)

    if not isinstance(distance, (int, float)):
        raise TypeError(DISTANCE_TYPE_ERROR)

    # Range check
    MIN_ANGLE = 0
    MAX_ANGLE = 90
    if not MIN_ANGLE <= angle <= MAX_ANGLE:
        raise ValueError(ANGLE_VALUE_ERROR)

    # Distance check
    MIN_DISTANCE = 0
    if distance >= radius or distance < MIN_DISTANCE:
        raise ValueError(DISTANCE_VALUE_ERROR)

    BEAM_VECTOR = [distance, angle]

    if outgoing:
        out_angles = {'Incoming angle': angle, 'Distance': distance, 'Angle results': dict()}
        for opt_device, matrix in OPTICAL_MATRICES.items():
            out_angles['Angle results'][opt_device] = round(multiply_mat_vec(matrix, BEAM_VECTOR)[1], 2)

    else:
        out_angles = {'Outgoing angle': angle, 'Distance': distance, 'Angle results': dict()}
        for opt_device, matrix in INVERSE_OPTICAL_MATRICES.items():
            out_angles['Angle results'][opt_device] = round(multiply_mat_vec(matrix, BEAM_VECTOR)[1], 2)

    return out_angles


def print_angles(angle_dic):
    """
    Prints the resulting angles in a nice format from a given dictionary.

    :param angle_dic: nested dictionary with input angles, distance and resulting angles
    :type angle_dic: dict

    :return: None
    """

    if 'Incoming angle' in angle_dic.keys():
        print(f"The resulting outgoing angles due to refraction (between air and glass)/ "
              f"reflection for an incoming angle of {angle_dic['Incoming angle']}° at a "
              f"distance of {angle_dic['Distance']}m from the optical axis are:")

    if 'Outgoing angle' in angle_dic.keys():
        print(f"The resulting incoming angles due to refraction (between air and glass)/"
              f"reflection for an outgoing angle of {angle_dic['Outgoing angle']}° at a "
              f"distance of {angle_dic['Distance']}m from the optical axis are:")

    for opt_device, angle in angle_dic['Angle results'].items():
        print(f'{opt_device}: {angle}°')


if __name__ == '__main__':
    print_angles(get_angles(76))
    print()
    print_angles(get_angles(33.07, False, 0.005))
