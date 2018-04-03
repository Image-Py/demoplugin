from imagepy.core.engine import Tool

class Plugin(Tool):
    title = 'Flood Fill'
    para = {'w':10}
    view = [(int, (0,50), 0, 'width/2', 'w','pix')]
        
    def mouse_down(self, ips, x, y, btn, **key):
        print(btn)
        ips.snapshot()
        x, y, r = int(x), int(y), self.para['w']
        obj = ips.img[y-r:y+r,x-r:x+r]
        obj[:] = 255-obj
        ips.update = 'pix'