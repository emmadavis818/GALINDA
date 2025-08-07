import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import glob
import h5py
from matplotlib import rc
rc("animation", html = "html5")
from GALINDA import GALINDA

# %%
def test_animate():
    """
    Testing the animation function on files saved in animation_data. 
    This should show the animation in a pop-up window.
    """
    gal = GALINDA.Bubble("animation_data/", "m11h_star_coordinates")
    gal.animate()
    
    assert hasattr(gal,"fig") == True
    assert hasattr(gal,"ax") == True
    assert hasattr(gal,"ani") == True

    return gal.ani
    
#%%
if __name__ == "__main__":
    anim = test_animate()
    plt.show()