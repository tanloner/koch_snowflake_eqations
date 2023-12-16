import math

def koch_snowflake(order: int = 2, size: float=10):
    """
    Generate coordinates of the Koch Snowflake Fractal.
    
    :param order: The iteration/order of the snowflake.
    :param size: The size of the initial triangle sides.
    
    :return: A list of tuples representing the vertices of the snowflake.
    """

    def koch_curve(p1, p2, order):
        """ Recursive helper function to calculate points for Koch curve. """
        # Base case: return the segment endpoints
        if order == 0:
            return [p1, p2]

        # Divide the segment into 3 parts
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        a = (p1[0] + dx / 3, p1[1] + dy / 3)
        c = (p1[0] + 2 * dx / 3, p1[1] + 2 * dy / 3)

        # Calculate the peak of the triangle
        b_x = (p1[0] + p2[0]) / 2 - math.sqrt(3) * (p1[1] - p2[1]) / 6
        b_y = (p1[1] + p2[1]) / 2 + math.sqrt(3) * (p1[0] - p2[0]) / 6
        b = (b_x, b_y)

        # Recursively calculate the points for each segment
        return koch_curve(p1, a, order - 1) + \
               koch_curve(a, b, order - 1) + \
               koch_curve(b, c, order - 1) + \
               koch_curve(c, p2, order - 1)

    # Initialize the three sides of the triangle
    points = [
        (0, 0),
        (size, 0),
        (size / 2, size * math.sqrt(3) / 2),
        (0, 0)
    ]

    # Generate the snowflake points by applying the Koch curve to each side
    snowflake = []
    for i in range(len(points) - 1):
        snowflake += koch_curve(points[i], points[i + 1], order)
    
    return snowflake
