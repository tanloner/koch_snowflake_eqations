# Koch Snowflake Project

## Introduction
This project generates and visualizes the Koch Snowflake and it generates all partial line equations that make it up. It was developed as a part of a math project to explore fractal geometry and programming. 
(The Koch Snowflake is constructed by recursively dividing each side of a triangle into smaller segments and creating patterns in a self-similar manner.)

## Features
- Generation of Koch Snowflake vertices for any given order.
- Calculation and formatting of all partial line equations that make up the snowflake.
- Plotting functionality to visualize the fractal pattern.

## Installation
To run this project, you need to have Python installed on your system. Additionally, you will need to install the required packages. You can install them using the following command:

```bash
pip install -r requirements.txt
```
or (since only matplotlib is used):
```
pip install matplotlib
```

## Usage
The project is divided into multiple modules:

1. koch_snowflake.py: Generates the vertices of the Koch Snowflake.
2. snowflake_equations.py: Calculates and formats the equations of the lines forming the snowflake.
3. plot_snowflake.py: Plots the snowflake using matplotlib.

To generate and plot the Koch Snowflake, simply run the plot_snowflake.py script. You can modify the order variable in the script to change the iteration level of the snowflake.

## Example

```python
# In plot_snowflake.py
order = 3  # Change the order to see different iterations of the snowflake
plot_koch_snowflake(order)
```
This will generate and display the Koch Snowflake of the specified order.

## Contributing
Feel free to fork this project and make your own changes, maybe for other fractals, or whatever else you can use this for. Pull requests are welcome for bug fixes, enhancements, or documentation improvements.

## License
This project is open-source and available under the MIT License.