#/usr/bin/env python
#see
import numpy as np
import matplotlib.pyplot as plt
if __name__ == '__main__':
 	x=np.arange(-np.pi,np.pi,0.01)
 	y=np.sin(x)
 	plt.plot(x,y,'g')
 	plt.show()