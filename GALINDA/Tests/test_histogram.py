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
def test_histogram(i):
    gal = GALINDA.Bubble("animation_data/", "m11h_star_coordinates")
    plot = gal.histogram(i)
    assert hasattr(gal,"to_plot") == True
    assert hasattr(gal,"binX") == True
    assert hasattr(gal,"binY") == True


    return plot #change the input her eto test edge cases

if __name__ == "__main__":
    test_histogram(0)