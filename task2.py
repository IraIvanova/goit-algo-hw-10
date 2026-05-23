import numpy as np
import scipy.integrate as spi
from view import draw


def f(x):
    return x ** 3 + 1.2 * x

def monte_carlo_area(a, b, num_points=100000, num_experiments = 10):
    y_max = f(b)
    average_area = 0

    for _ in range(num_experiments):
        x_random = np.random.uniform(a, b, num_points)
        y_random = np.random.uniform(0, y_max, num_points)

        points = list(zip(x_random, y_random))
        under_curve_points = [(x, y) for x, y in points if y <= f(x)]

        M = len(under_curve_points)
        N = len(points)

        area = (M / N) * ((b - a) * y_max)
        average_area += area

    average_area /= num_experiments

    return average_area


if __name__ == '__main__':
    a = 0
    b = 2
    n = 100000

    draw(a, b, f)

    quad_result, error = spi.quad(f, a, b)
    mc_result = monte_carlo_area(a, b, n)

    print("Monte Carlo result:", mc_result)
    print("Quad result:", quad_result)
