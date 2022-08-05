# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018

    Creates a 2-dimensional curve and plots tangent vectors
"""

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange
from geomdl import operations

import numpy as np
import matplotlib.pyplot as plt


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))


"""
Curve Evaluation
"""

curve = BSpline.Curve()
curve.degree = 3
curve.ctrlpts = exchange.import_txt("../curve2d/ex_curve03.cpt")
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))
curve.delta = 0.01
curve.evaluate()

"""
Tangent Vector Evaluation
"""

eval_pts = [0.0, .2, .5, .6, .8, 1.0]
curvetan = [operations.tangent(curve, u, normalize=True) for u in eval_pts]

"""
Control Points, Curve and Tangent Vector Plotting
"""

ctrlpts = np.array(curve.ctrlpts)
curve_pts = np.array(curve.evalpts)
ctarr = np.array(curvetan)

plt.figure(figsize=(10.67, 8), dpi=96)

yaxis = plt.plot((-1, 25), (0, 0), "k-")

control_polygon, = plt.plot(
    ctrlpts[:, 0],
    ctrlpts[:, 1],
    color='black',
    linestyle='-.',
    marker='o',
    markersize='3'
)

curve_plot, = plt.plot(
    curve_pts[:, 0],
    curve_pts[:, 1],
    color='green',
    linestyle='-'
)

tangents_plot = plt.quiver(
    ctarr[:, 0, 0],
    ctarr[:, 0, 1],
    ctarr[:, 1, 0],
    ctarr[:, 1, 1],
    color='blue',
    angles='xy',
    scale_units='xy',
    scale=1,
    width=0.003
)

tanlinekey = plt.quiverkey(
    tangents_plot,
    23.75,
    -14.5,
    35,
    "Tangent Vectors",
    coordinates='data',
    labelpos='W'
)

plt.legend([control_polygon, curve_plot], ["Control Points", "Evaluated Curve"])
plt.axis([-1, 25, -15, 15])
plt.show()
