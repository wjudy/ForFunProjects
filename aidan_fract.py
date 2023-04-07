import numpy as np
import matplotlib.pyplot as plt
import math
from tqdm import tqdm

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def real_part(self):
        return self.real

    def imaginary_part(self):
        return self.imaginary

    def square(self):
        new_a = self.real ** 2 - self.imaginary ** 2
        new_b = self.real * self.imaginary * 2
        return Complex(new_a, new_b)

    def add(self, other):
        new_a = other.real + self.real
        new_b = other.imaginary + self.imaginary
        return Complex(new_a, new_b)

    def ln(self):
        r = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        if self.real == 0:
            theta = 0
        else:
            theta = math.atan(self.imaginary / self.real)
        return Complex(math.log(r), theta)
        
    def __str__(self):
        output = str(self.real) + "+" + str(self.imaginary) + "j"
        return output
    
    def __repr__(self):
        output = str(self.real) + "+" + str(self.imaginary) + "j"
        return output
        

def f(c):
    a = c.real_part()
    b = c.imaginary_part()
    result = Complex.add(Complex.ln(c), Complex(a, b))
    #result = Complex.add(Complex.ln(c), c)
    #print(result)
    return result

def get_complex(complex_value):
    x = complex_value.real_part()
    y = complex_value.imaginary_part()
    return complex(x, y)

c1 = Complex(-1, 2)

def diverge(c, n_iter=200, B=100):
    #c = Complex(c)
    new = f(c)
    for i in range(n_iter):
        new = f(new)

        if abs(get_complex(new)) > B: return 1
    return 0

#Good Code
def fractal(c, max_iter):
    new = f(c)
    n = 0
    while abs(get_complex(new)) <= 100 and n < max_iter:
        new = f(new)
        n += 1
    return n

def mandelbrot(c, max_iter):
    z = 0
    n = 0 
    while abs(z) <= 20000 and n < max_iter:
        z = z ** 2 + c
        n +=1
    return n

#implement class

def fractal_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[fractal(Complex(r, i), max_iter) for r in r1] for i in tqdm(r2)]))

def draw_fractal(xmin, xmax, ymin, ymax, width=600, height=600, max_iter=50, cmap='bone_r'):
    dpi = 80
    img_width = width
    img_height = height
    plt.figure(figsize=(img_width / dpi, img_height / dpi), dpi=dpi)
    r1, r2, fractal_img = fractal_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

    ticks = np.arange(0, img_width, 100)
    x_ticks = xmin + (xmax - xmin) * ticks / img_width
    plt.xticks(ticks, x_ticks, fontsize=8)
    plt.yticks(ticks, x_ticks, fontsize=8)

    plt.imshow(fractal_img.T, cmap=cmap, extent=[xmin, xmax, ymin, ymax])
    plt.savefig('fractal_set.png', dpi=dpi)
    plt.show()

    # get mouse click, create a function for setting a new window around mouse click,
    # recurse on draw_fractal()

if __name__ == '__main__':
    draw_fractal(-1, 1, -1, 1)