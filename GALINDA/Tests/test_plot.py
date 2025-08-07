# %%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import glob
import h5py
from matplotlib import rc
rc("animation", html = "html5")
from GALINDA import GALINDA

# %%
def test_plot():
    """
    Test that plot function produces a plot of the screenshot file for animation.
    This function will also assert that the given attributes fig and im were assigned.

    We'll test on the 0th file.
    """
    gal = GALINDA.Bubble("animation_data/", "m11h_star_coordinates")
    plot = gal.plot(0)
    
    assert hasattr(gal,"fig") == True
    assert hasattr(gal,"im") == True

    return plot

if __name__ == "__main__":
    test_plot()