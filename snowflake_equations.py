def koch_snowflake_equations(vertices: list):
    """
    Generate the equations of the lines forming the Koch snowflake.

    :param vertices: A list of tuples representing the vertices of the snowflake.

    :return: A list of string representations of the line equations.
    """
    equations = []
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        if x1 == x2:
            equation = f"x = {x1}"
        else:
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            equation = f"y = {m:.2f}x + {b:.2f}"

        equations.append(equation)
    return equations

def format_equations(vertices: list, equations: list):
    """
    Format the equations of the Koch snowflake for better readability.

    :param vertices: The vertices of the snowflake.
    :param equations: The equations of the lines in the snowflake.

    :return: List of Formatted string representations of the line equations.
    """
    formatted_equations = []
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        if "x =" in equations[i]:  # Vertical line
            continue
            #equation = f"x = {x1:.2f} ({x1:.2f}|{x2:.2f})"
        else:  # Non-vertical line
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            equation = f"y = {m:.2f}x + {b:.2f} ({x1:.2f}|{x2:.2f})"

        formatted_equations.append(equation)
    return formatted_equations
