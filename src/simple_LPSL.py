from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar

def f5(i,p,e=4):
    """
    Compute an exponential weight of the pixel i
    
    W = i*e^(p)
    
    Parameters
    ----------
    
    i: bidimensional numpy array of integers
    	pixel intensity value that goes from 0 to 63
	
	p: bidimensional numpy array of integers
		it represents the zone priority is an integer equal or greater than 0
		
	Returns
	-------
	A weighted bidimensional numpy matrix 
	
	Examples:
	---------
	
	i = np.array([[40, 51, 37],
       [27, 40, 48],
       [47, 49, 13]])

	p = np.array([[0, 1, 0],
       [3, 0, 0],
       [1, 1, 3]])

	>>f5(i,p)	
	
	array([[  40,  204,   37],
       [1728,   40,   48],
       [ 188,  196,  832]])
	
	
    """
    
    return i*e**(p)

def getN(W,i,j):
    """
    Function to get the highest value of a neighbourhood with the four neighbor rule.
	
    Parameters:
    -----------
	
    W: numpy bidimensional array
	    Map with the weighted values
	
    i: int
	    row index
	
    j: int
	    column index
		
    Returns:
    --------
    opt: boolean
	    False if the center of the neighborhood is not the local maximum, True in contrary sense
		
	Example:
	--------
	
	W = array([[  40,  204,   37],
       [1728,   40,   48],
       [ 188,  196,  832]])
    
	>>getN(W,1,1)
	False
	
	"""
	
    
    ln = ([])
    c = W[i,j]
    ln.append(W[i+1,j])
    ln.append(W[i-1,j])
    ln.append(W[i,j+1])
    ln.append(W[i,j-1])
    opt = False if W[i,j]<max(ln) else True
    return opt

def fuerza_puntual(x,y,im2,h=2,e=2):
    '''
    Filter based on the Newton's Universal gravitational Law.
    It produces a Gravitational Luminance Image representation based on the gravitational force per unit mass that would be exerted on a small mass at that point. It is applied to desaturate, saturated Nighttime images.
    
    It returns a value that represent the total gravitational force exerted on a location with mass m_1 and it is calculated using  the Nighttime image used as gravitational field. This effect works as a low pass filter.
    
    
    
    x: int
    	row
	y: int
		column
		
	im2: numpy bidimensional matrix with positive integers
		image
	
	h: positive integer greater than 0 
		It represents the squared neighborhood of (h+1)^2 units to compute the gravitational force per unit mass
	
	e: positive integer greater than 0 
		Constant that defines the influence of the distance.
	
		
	Returns:
	--------
	s: positive float
		The value of the exerted force. 
		
	Examples:
	---------	
	
	W= np.array([[  40,  204,   37],
       [1728,   40,   48],
       [ 188,  196,  832]])
	
	>>fuerza_puntual(1,1,W)
	108980.0
	

    '''
    s = 0.0 
    g1 = float(im2[x][y])
    xlb = 0 if(x-h)<0 else x-h
    xub = im2.shape[0] if(x+h)> im2.shape[0] else x+h
    
    ylb = 0 if(y-h)<0 else y-h
    yub = im2.shape[1] if(y+h)> (im2.shape[1]) else y+h 
    
    ri = np.arange(xlb,xub)
    rj = np.arange(ylb,yub)
    for i in ri:
        for j in rj:
            d=((i-x)**2+(j-y)**2)**(0.5)
            g2 = float(im2[i][j])
            if d >0: s += (g1*g2)/(d**e)
    return s

def filtro_fuerza_puntual(A,h=3,e=2):
    """
    This function apply the "fuerza_puntual" function to the all image.

    A: bidimensional numpy array with positive floats
	
    h: positive integer greater than 0 
        It represents the squared neighborhood of (h+1)^2 units to compute the gravitational force per unit mass

    e: positive integer greater than 0 
        Constant that defines the influence of the distance.

    Returns:
    --------

    pot1: numpy bidimensional array
        The desaturated image
    """
    
    pot1 = np.zeros(A.shape)
    for i in range(pot1.shape[0]):
        for j in range(pot1.shape[1]):
            pot1[i][j] = fuerza_puntual(i,j,A,h,e)
            
    return pot1


def plot_examples(data,colormaps,filename):
    """
    Helper function to plot data with associated colormap.
    """
    n = len(colormaps)
    #fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
    #                        constrained_layout=False, squeeze=False)
    fig, axs = plt.subplots(1, n, figsize=(6, 5.2),constrained_layout=False, squeeze=False)
   
    scalebar = ScaleBar(1000) # 1 pixel = 0.2 meter
    plt.gca().add_artist(scalebar)
    for [ax, cmap] in zip(axs.flat, colormaps):
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        psm = ax.pcolormesh(np.flip(data,0), cmap=cmap, rasterized=False, vmin=0, vmax=data.max())
        fig.colorbar(psm, ax=ax)
    
    

    plt.savefig(filename, dpi = 150)

#custom_cmap = cm.get_cmap('hot', 256)
#newcolors = custom_cmap(np.linspace(0, 1, 256))
#pink = np.array([200/256, 200/256, 200/256, 1])
#newcolors[:1, :] = pink
#newcmp = ListedColormap(newcolors)
