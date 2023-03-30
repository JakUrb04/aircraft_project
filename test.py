import aerosandbox as asb
import aerosandbox.numpy as np
from aerosandbox.library import airfoils

wing_airfoil = asb.Airfoil("sd7037")
tail_airfoil = asb.Airfoil("naca0010")

### Tworzenie geometrii 3D do analizy i optymalizacji
# Wszystko jest w metrach lub w stopniach
airplane = asb.Airplane(
    name="First concept",
    xyz_ref=[0, 0, 0],  # Środek cięzkości
    wings=[
        asb.Wing(
            name="Główne skrzydło",
            xyz_le=[0, 0, 0],  # Współrzędne krawędzi natarcia skrzydła
            symmetric=True,  # Czy skrzydło powinno być symetryczne względem oXZ True=tak, False=nie
            xsecs=[  # Przekroje poprzeczne skrzydła ("X")
                asb.WingXSec(  # Podstawa
                    xyz_le=[0, 0, 0],  # Współrzędne krawędzi natarcia XSec względem krawędzi natarcia skrzydła.
                    chord=0.18,
                    twist=2,  # stopnie
                    airfoil=wing_airfoil,  # Płaty są mieszane między danym XSec a następnym.
                    control_surface_is_symmetric=True,
                    # Klapy (powierzchnie kontrolne (stery np) pomiędzy tą XSec i kolejną
                    control_surface_deflection=0,  # stopnie
                ),
                asb.WingXSec(  # Środek
                    xyz_le=[0.01, 0.5, 0],
                    chord=0.16,
                    twist=0,
                    airfoil=wing_airfoil,
                    control_surface_is_symmetric=True,  # Lotka
                    control_surface_deflection=0,
                ),
                asb.WingXSec(  # Góra
                    xyz_le=[0.08, 1, 0.1],
                    chord=0.08,
                    twist=-2,
                    airfoil=wing_airfoil,
                ),
            ]
        ),
        asb.Wing(
            name="Stateczniki poziome",
            symmetric=True,
            xsecs=[
                asb.WingXSec(  # root
                    xyz_le=[0, 0, 0],
                    chord=0.1,
                    twist=-10,
                    airfoil=tail_airfoil,
                    control_surface_is_symmetric=True,  # Ster wysokości
                    control_surface_deflection=0,
                ),
                asb.WingXSec(  # tip
                    xyz_le=[0.02, 0.17, 0],
                    chord=0.08,
                    twist=-10,
                    airfoil=tail_airfoil
                )
            ]
        ).translate([0.6, 0, 0.06]),
        asb.Wing(
            name="Statecznik pionowy",
            symmetric=False,
            xsecs=[
                asb.WingXSec(
                    xyz_le=[0, 0, 0],
                    chord=0.1,
                    twist=0,
                    airfoil=tail_airfoil,
                    control_surface_is_symmetric=True,  # Ster kierunku (?)
                    control_surface_deflection=0,
                ),
                asb.WingXSec(
                    xyz_le=[0.04, 0, 0.15],
                    chord=0.06,
                    twist=0,
                    airfoil=tail_airfoil
                )
            ]
        ).translate([0.6, 0, 0.07])
    ],
    fuselages=[
        asb.Fuselage(
            name="Fuselage",
            xsecs=[
                asb.FuselageXSec(
                    xyz_c=[0.8 * xi - 0.1, 0, 0.1 * xi - 0.03],
                    radius=0.6 * asb.Airfoil("dae51").local_thickness(x_over_c=xi)
                )
                for xi in np.cosspace(0, 1, 30)
            ]
        )
    ]
)


airplane.draw(show_kwargs={"jupyter_backend": "static"})