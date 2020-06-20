from imagepy.core.engine import Free
import numpy as np

class NewImage(Free):
    title = 'New Image Demo'
    para = {'name':'new image','w':300, 'h':300}
    view = [(str, 'name', 'name',''),
            (int, 'w', (1,2048), 0,  'width', 'pix'),
            (int, 'h', (1,2048), 0,  'height', 'pix')]

    def run(self, para = None):
        imgs = [np.zeros((para['h'], para['w']), dtype=np.uint8)]
        self.app.show_img(imgs, para['name'])

class About(Free):
    title = 'About Demo'

    def run(self, para=None):
        self.app.alert('ImagePy v0.2')

class Close(Free):
    title = 'Exit Program Demo'
    asyn = False

    def run(self, para = None):
        self.app.Close()

plgs = [NewImage, About, Close]