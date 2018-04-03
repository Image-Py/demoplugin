from imagepy.core.util import fileio
from scipy.misc import imread, imsave
from imagepy.core.manager import ReaderManager, WriterManager

ReaderManager.add('png', imread)
WriterManager.add('png', imsave)

class OpenPNG(fileio.Reader):
	title = 'PNG Open Demo'
	filt = ['PNG']

class SavePNG(fileio.Writer):
	title = 'PNG Save Demo'
	filt = ['PNG']

import pydicom

def readdmc(path):
	return pydicom.read_file(path, force=True).pixel_array

ReaderManager.add('dcm', imread)

class OpenDCM(fileio.Reader):
	title = 'DCM Open Demo'
	filt = ['DCM']
plgs = [OpenPNG, SavePNG, OpenDCM]