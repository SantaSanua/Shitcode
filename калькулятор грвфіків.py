import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def plot_sin():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Графік сінуса')
    plt.show()

def plot_cos():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('Графік косинуса')
    plt.show()

def plot_tan():
    x = np.linspace(-np.pi/2, np.pi/2, 100)
    y = np.tan(x)
    plt.plot(x, y)
    plt.title('Графік тангенса')
    plt.show()

def plot_cotan():
    x = np.linspace(0.01, np.pi-0.01, 100)
    y = 1 / np.tan(x)
    plt.plot(x, y)
    plt.title('Графік котангенса')
    plt.show()


def on_sin_button_click(event):
    plt.clf()  
    plot_sin()

def on_cos_button_click(event):
    plt.clf()
    plot_cos()

def on_tan_button_click(event):
    plt.clf()
    plot_tan()

def on_cotan_button_click(event):
    plt.clf()
    plot_cotan()


sin_button = Button(plt.axes([0.1, 0.01, 0.1, 0.05]), 'Сінус')
sin_button.on_clicked(on_sin_button_click)

cos_button = Button(plt.axes([0.3, 0.01, 0.1, 0.05]), 'Косинус')
cos_button.on_clicked(on_cos_button_click)

tan_button = Button(plt.axes([0.5, 0.01, 0.1, 0.05]), 'Тангенс')
tan_button.on_clicked(on_tan_button_click)

cotan_button = Button(plt.axes([0.7, 0.01, 0.1, 0.05]), 'Котангенс')
cotan_button.on_clicked(on_cotan_button_click)

plt.show()
