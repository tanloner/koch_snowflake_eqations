import matplotlib.pyplot as plt
from koch_snowflake import koch_snowflake
from snowflake_equations import koch_snowflake_equations, format_equations

def plot_koch_snowflake(vertices: list, equations: list):
    """
    Plot the Koch snowflake using matplotlib.

    :param vertices: The vertices of the snowflake.
    :param equations: The equations of the lines in the snowflake.
    """
    plt.figure(figsize=(8, 8))
    
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        if "x =" in equations[i]:  # Vertical line
            plt.plot([x1, x1], [y1, y2], 'b')
        else:  # Non-vertical line
            plt.plot([x1, x2], [y1, y2], 'b')
    
    plt.xlim(-1, 11)
    plt.ylim(-3, 9)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Koch Snowflake (Iteration 2)')

    plt.show()


if __name__ == "__main__":
    order = 2
    vertices = koch_snowflake(order)
    equations = koch_snowflake_equations(vertices)
    formatted_equations = format_equations(vertices, equations)
    print(*formatted_equations, sep="\n")
    plot_koch_snowflake(vertices, equations)
