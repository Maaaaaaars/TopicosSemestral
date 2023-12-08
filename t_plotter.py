import numpy as np
import matplotlib.pyplot as plt

def plot_rows(data, rows):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(rows):
        x = [point[0] for point in data[i]]
        y = [point[1] for point in data[i]]
        z = [point[2] for point in data[i]]
        ax.scatter(x, y, z, label=f'Row {i+1}')  # Add label for each row

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.legend()  # Add legend

    plt.show()