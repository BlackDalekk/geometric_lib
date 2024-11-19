def area(a: float, h: float) -> float:
    """
    Сalculation area of tiangle

    Args:
        a: First side
        h: Height

    Returns:
        float: Tiangle's area

    Example:
        area(1, 2)
        # 1
    """
    return a * h / 2 

def perimeter(a: float, b: float, c: float) -> float:
    """
    Сalculation perimeter of tiangle

    Args:
        a: First side
        b: Second side
        c: Third side

    Returns:
        float: Tiangle's perimeter

    Example:
        perimeter(1, 2, 3)
        # 6
    """
    return a + b + c 
