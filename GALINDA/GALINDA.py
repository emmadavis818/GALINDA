import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import glob
import h5py
from matplotlib import rc
rc("animation", html = "html5")

class Bubble(object):
    """
    Bubble contains all the functions for animating n-body and hydrodynamical simulations.
    
    Args: path (string): File path to a folder of data to animate (files should be hdf5)
          key (string): Data source to be plotted (header of hdf5 file) 
          ind (array): 2D array/list/tuple containing which indices the GALINDA will plot over 

    Attrs: fnames (array): A numpy array of filenames to animate
           key (string): Data source to be plotted (header of hdf5 file) 
           ind (array): 2D array/list/tuple containing which indices the GALINDA will plot over
    """

    def __init__(self,path,key,ind = [0,1]):
        self.path = path
        if "*" not in self.path:
            self.path += "*"
            
        self.fnames = glob.glob(path + "*")
        self.key = key
        self.ind = ind 

        
    def histogram(self):
        """
        Creates attributes for 2D histograms
        
        Attrs: to_plot (array): Array of values to plot
               binX (array): Histogram's x-values for bins
               binY (array): Histogram's y-values for bins
            
        """
        self.to_plot,self.binX,self.binY = np.histogram2d(self.x,self.y, bins = self.bins)
        
        
    def plot(self,i):
        """
        Function that plots a 2D histogram of data values
        
        Args: i (int): The index for which timestep to plot
        
        Attrs: f (h5py directory): An h5py directory of all the data in the i-th timestep
               data (array): Data to be plotted
               x (array): The x values of the simulation
               y (array): The y values of the simulation
               bins (array): The number of bins to put the data into (for a size N array, we have round(sqrt(N))/2)
               
        """
        self.f = h5py.File(self.fnames[i])
        self.data = np.array(self.f[self.key])
        self.x,self.y = self.data[:,self.ind[0]], self.data[:,self.ind[1]]
        self.bins = int(np.sqrt(len(self.x))/2)
        self.histogram()
        
        if not hasattr(self, "fig"):
            self.fig, self.ax = plt.subplots()
        
        if not hasattr(self, "im"):
            self.im = plt.imshow(self.to_plot)
        else:
            self.im.set_data(self.to_plot)
    
    def animate(self,figsize = (8,8)):
        """
        Animation!
        
        Args: figsize (tuple): How big to make the images
        
        Attrs: fig (Figure): The figure to animate on
               ax (Axes): The axes to animate on
               ani (Animation): The animation itself
        """
        self.fig, self.ax = plt.subplots(figsize = figsize)
        self.ani = animation.FuncAnimation(self.fig, self.plot, np.arange(len(self.fnames)))
        
    def save_ani(self,save_file, fps = 5):
        """
        Save an animation
        
        Args: save_file (string): The name that the user would like to save the animation
              fps (int): Number of frames per second for the animation
        
        """
        if not hasattr(self, "ani"):
            self.animate()
            
        if save_file[-4:] != ".mp4":
            save_file += ".mp4"
            
        FFwriter = animation.FFMpegWriter(fps=fps)
        self.ani.save(save_file, writer = FFwriter)