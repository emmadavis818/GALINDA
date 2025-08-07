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
def test_import():
    """
    This function tests that we can import data and have assigned attributes of path, fnames, key, and ind.
    """
    gal = GALINDA.Bubble("animation_data/", "m11h_star_coordinates")
    assert hasattr(gal,"path") == True
    assert hasattr(gal,"fnames") == True
    assert hasattr(gal,"key") == True
    assert hasattr(gal,"ind") == True

if __name__ == "__main__":
    test_import()