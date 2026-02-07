# main.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_random_data(size: int) -> pd.DataFrame:
    """
    Generates a DataFrame with random data.

    Args:
    size (int): The number of rows in the DataFrame.

    Returns:
    pd.DataFrame: A DataFrame with two columns 'x' and 'y'.
    """
    np.random.seed(0)
    data = {
        'x': np.random.rand(size),
        'y': np.random.rand(size)
    }
    return pd.DataFrame(data)

def create_line_plot(data: pd.DataFrame) -> None:
    """
    Creates a line plot from the given DataFrame.

    Args:
    data (pd.DataFrame): A DataFrame with two columns 'x' and 'y'.

    Returns:
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(data['x'], data['y'], marker='o')
        plt.title('Line Plot')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error creating line plot: {str(e)}")

def create_scatter_plot(data: pd.DataFrame) -> None:
    """
    Creates a scatter plot from the given DataFrame.

    Args:
    data (pd.DataFrame): A DataFrame with two columns 'x' and 'y'.

    Returns:
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(data['x'], data['y'])
        plt.title('Scatter Plot')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error creating scatter plot: {str(e)}")

def main() -> None:
    """
    The main function that runs the program.

    Returns:
    None
    """
    try:
        data = generate_random_data(100)
        create_line_plot(data)
        create_scatter_plot(data)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()