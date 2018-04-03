from imagepy.core.engine import Filter                  # 引入Filter基类
from scipy.ndimage import gaussian_filter

class Invert(Filter):                                   # 继承Filter，名称必须是Plugin
    title = 'Invert Demo'                               # 标题
    note = ['all', 'auto_msk', 'auto_snap']             # 行为标签

    def run(self, ips, snap, img, para = None):         # 处理函数
        return 255-snap

class Gaussian(Filter):
    title = 'Gaussian Demo'
    note = ['all', 'auto_msk', 'auto_snap','preview']
    para = {'sigma':2}
    view = [(float, (0,30), 1,  'sigma', 'sigma', 'pix')]
    
    def run(self, ips, snap, img, para = None):
        gaussian_filter(snap, para['sigma'], output=img)

plgs = [Invert, Gaussian]