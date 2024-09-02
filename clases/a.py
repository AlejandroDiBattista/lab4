import numpy as np
import matplotlib.pyplot as pt 
import streamlit as sl
def cuadratica(x):
    return -4  *x * x - 3 * x + 50

x = np.linspace(-3.14,3.14,50)
print(x.size)
y = cuadratica(x)
r = np.random.normal(0,2,x.size)
pt.scatter(x,y+r)
