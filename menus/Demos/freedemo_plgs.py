from imagepy.core.engine import Free
from imagepy import IPy
import numpy as np

class NewImage(Free):
    title = 'New Image Demo'
    para = {'name':'Undefined','width':300, 'height':300, 'type':'8-bit','slice':1}
    view = [(str, 'name', 'name',''),
            (int, (1,2048), 0,  'width', 'width', 'pix'),
            (int, (1,2048), 0,  'height', 'height', 'pix'),
            (list, ['8-bit','RGB'], str, 'Type', 'type',''),
            (int, (1,2048), 0,  'slice', 'slice', '')]

    #process
    def run(self, para = None):
        w, h = para['width'], para['height']
        channels = (1,3)[para['type']=='RGB']
        slices = para['slice']
        shape = (h,w,channels) if channels!=1 else (h,w)
        imgs = [np.zeros(shape, dtype=np.uint8) for i in range(slices)]
        IPy.show_img(imgs, para['name'])

class About(Free):
    title = 'About Demo'
    asyn = False
    def run(self, para=None):
        IPy.alert('ImagePy v0.2')
        
class Topic(Free):
    title = 'Topic Demo'
    asyn = False
    def run(self, para=None):
        webbrowser.open('http://www.imagepy.org/document')

plgs = [NewImage, About, Topic]