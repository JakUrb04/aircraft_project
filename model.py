# first
#import pyjet
#import pyfme 
#import aerosandbox
#import openmdao

import aerosandbox as asb
import aerosandbox.numpy as np
from shutil import which

avl_is_present = which('avl') is not None
sd7037 = asb.Airfoil("sd7037")
tail_airfoil =asb.Airfoil("naca4012")

air = asb.Airplane()

airplane = asb.Airplane(
    name="Blended Wing Body",
    xyz_ref=[3, 0, 0],
    s_ref=200,
    c_ref=3,
    b_ref=30,
    wings=[
        asb.Wing(
            name="Main Wing",
            symmetric=True,
            xsecs=[
                asb.WingXSec(
                    xyz_le=[0, 0, 0],
                    chord=5,
                    twist=2,
                    airfoil=sd7037,
                ),
                asb.WingXSec(
                    xyz_le=[0.2, 5, 1],
                    chord=2,
                    twist=2,
                    airfoil=sd7037,
                )
            ]
        )
    ],
    fuselages=[
        asb.Fuselage(
            name="Fuselage",
            xyz_le=[0, 0, 0],
            xsecs=[
                asb.FuselageXSec(
                    xyz_c=[10 * xi - 0.1, 0, 0.1 * xi - 0.03],
                    radius=5*asb.Airfoil("dae51").local_thickness(x_over_c=xi)
                )
                for xi in np.cosspace(0, 1, 30)
            ]
        )
    ]
)
airplane.draw(show_kwargs={"jupyter_backend": "static"})