from imagepy.core.engine import Simple
import scipy.ndimage as ndimg
import numpy as np

class RedLUT(Simple):
	title = 'Red LUT Demo'
	note = ['all']

	def run(self, ips, imgs, para = None):
		lut = np.zeros((256,3), dtype=np.uint8)
		lut[:,0] = np.arange(0, 256)
		ips.lut = lut

class Gaussian3D(Simple):
	title = 'Gaussian 3D Demo'
	note = ['all', 'stack3d']

	#parameter
	para = {'sigma':2}
	view = [(float, (0,30), 1,  'sigma', 'sigma', 'pix')]

	#process
	def run(self, ips, imgs, para = None):
		imgs[:] = ndimg.gaussian_filter(imgs, para['sigma'])

class Inflate(Simple):
    """Inflate: derived from imagepy.core.engine.Simple """
    title = 'Inflate ROI Demo'
    note = ['all', 'req_roi']
    para = {'r':5}
    view = [(int, (1,100),0, 'radius', 'r','pix')]

    def run(self, ips, imgs, para = None):
        ips.roi = ips.roi.buffer(para['r'])
        
plgs = [Gaussian3D, RedLUT, Inflate]