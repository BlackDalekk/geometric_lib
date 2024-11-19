import math


def area(r):
    """
    Сalculation area of circle

    Args:
        r: Radius

    Returns:
        float: Circle's area

    Example:
        area(1)
        # 3.14
    """
    return math.pi * r * r


def perimeter(r):
    """
    Сalculation area of circle

    Args:
        r: Radius

    Returns:
        float: Circle's perimeter

    Example:
        perimeter(1)
        # 6.28
    """
    return 2 * math.pi * r
