def score(x, y):
    """
    Calculates the score based on the coordinates (x, y) on a dartboard.

    Args:
        x (float): The x-coordinate of the dart's landing point.
        y (float): The y-coordinate of the dart's landing point.

    Returns:
        int: The score based on the distance from the center of the dartboard.
            - If the distance is less than or equal to 1, the score is 10.
            - If the distance is less than or equal to 5, the score is 5.
            - If the distance is less than or equal to 10, the score is 1.
            - Otherwise, the score is 0.
    """
    distance = (x ** 2 + y ** 2) ** 0.5

    if distance <= 1: return 10
    if distance <= 5: return 5
    if distance <= 10: return 1
    return 0
