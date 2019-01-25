from imagepy.core.engine import Free
from imagepy import IPy
import numpy as np

class NewImage(Free):
    title = 'New Image Demo'
    para = {'name':'new image','w':300, 'h':300}
    view = [(str, 'name', 'name',''),
            (int, 'w', (1,2048), 0,  'width', 'pix'),
            (int, 'h', (1,2048), 0,  'height', 'pix')]

    def run(self, para = None):
        imgs = [np.zeros((para['h'], para['w']), dtype=np.uint8)]
        IPy.show_img(imgs, para['name'])

class About(Free):
    title = 'About Demo'

    def run(self, para=None):
        IPy.alert('ImagePy v0.2')

class Close(Free):
    title = 'Exit Program Demo'
    asyn = False

    def run(self, para = None):
        IPy.curapp.Close()

plgs = [NewImage, About, Close]