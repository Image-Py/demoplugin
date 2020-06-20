from imagepy.core.engine import Simple
import scipy.ndimage as ndimg
import numpy as np

class Gaussian3D(Simple):
	title = 'Gaussian 3D Demo'
	note = ['all', 'stack3d']

	para = {'sigma':2}
	view = [(float, 'sigma', (0,30), 1,  'sigma', 'pix')]

	def run(self, ips, imgs, para = None):
		imgs[:] = ndimg.gaussian_filter(imgs, para['sigma'])

class SetLUT(Simple):
	title = 'Set LUT Demo'
	note = ['all']
	para = {'lut':'red'}
	view = [(list, 'lut', ['red', 'green', 'blue'], str, 'look up', 'table')]

	def run(self, ips, imgs, para = None):
		cmap = [[i==para['lut']] for i in ['red', 'green', 'blue']]
		ips.lut = (cmap*np.arange(256)).astype(np.uint8).T

class Inflate(Simple):
	title = 'Inflate ROI Demo'
	note = ['all', 'req_roi']
	para = {'r':5}
	view = [(int, 'r', (1,100),0, 'radius', 'pix')]

	def run(self, ips, imgs, para = None):
		ips.roi = ips.roi.buffer(para['r'])

class Unit(Simple):
	title = 'Scale And Unit Demo'
	note = ['all']
	para = {'scale':1, 'unit':'mm'}
	view = [(float, 'scale', (1e-3,1e3), 3, 'scale', ''),
			(str, 'unit', 'scale', '')]

	def run(self, ips, imgs, para = None):
		ips.unit = (para['scale'], para['unit'])

class Mark(Simple):
	title = 'Random Points Demo'
	note = ['all']

	def run(self, ips, imgs, para = None):
		pts = (np.random.rand(200)*512).reshape((100,2))
		ips.mark = GeometryMark({'type':'points', 'color':(255,0,0), 'lw':1, 'body':pts})

plgs = [Gaussian3D, SetLUT, Inflate, Unit, Mark]