def get_rectangle_area(a: float, b: float) -> float:
    """
    Сalculation area of rectangle

    Args:
        a: First side
        b: Second side

    Returns:
        float: Rectangle's area

    Example:
        get_rectangle_area(1, 2)
        # 2
    """
    return a * b

def get_rectangle_perimeter(a: float, b: float) -> float:
    """
    Сalculation perimeter of rectangle

    Args:
        a: First side
        b: Second side

    Returns:
        float: Rectangle's perimeter

    Example:
        get_rectangle_area(1, 2)
        # 6
    """
    return 2 * (a + b)
