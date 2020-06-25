#  Tool Plug-in

The Tool plug-in is used to complete mouse interaction and is loaded as icons on the toolbar at startup. Typical tool plug-ins are ROI editing, brushes, measuring tools, etc.



## Brush Tool

```python
from imagepy.core.engine import Tool
from skimage.draw import line, circle

def drawline(img, oldp, newp, w, value):
    if img.ndim == 2: value = sum(value)/3
    oy, ox = line(*[int(round(i)) for i in oldp+newp])
    cy, cx = circle(0, 0, w/2+1e-6)
    ys = (oy.reshape((-1,1))+cy).clip(0, img.shape[0]-1)
    xs = (ox.reshape((-1,1))+cx).clip(0, img.shape[1]-1)
    img[ys.ravel(), xs.ravel()] = value

class Plugin(Tool):
    title = 'Pencil'
    
    para = {'width':1, 'value':(255, 255, 255)}
    view = [(int, 'width', (0,30), 0,  'width', 'pix'),
            ('color', 'value', 'color', '')]
    
    def __init__(self):
        self.status = False
        self.oldp = (0,0)
        
    def mouse_down(self, ips, x, y, btn, **key):
        self.status = True
        self.oldp = (y, x)
        ips.snapshot()
    
    def mouse_up(self, ips, x, y, btn, **key):
        self.status = False
    
    def mouse_move(self, ips, x, y, btn, **key):
        if not self.status:return
        w, value = self.para['width'], self.para['value']
        drawline(ips.img, self.oldp, (y, x), w, value)
        self.oldp = (y, x)
        ips.update()
        
    def mouse_wheel(self, ips, x, y, d, **key):pass
```

By overloading ` mouse_down `,  ` mouse_up `,  ` mouse_move ` method, we can realize the mouse interaction. Here, we implement one of the most common brush tool. When the mouse is pressed, tag ` status` will be ` True `, with drawing in the process of the mouse movement, and updating the display.

![14](http://idoc.imagepy.org/demoplugin/24.png)

<div align=center>Brush Tool</div><br>


**Tool loading method**

1. The file must end up with ` _tol.py ` ,and the class name must be ` Plugin ` (one file can only contain one tool)
2. The file must be in ` tools ` submenu directory level 
3. It is required for the toolbar icon to have a GIF file , 16*16, with the same name as `tool` 
4. Click to select and apply to the canvas. If there are `para` and `view` parameters, you can click doublely to configure them.


![14](http://idoc.imagepy.org/demoplugin/25.png)

<div align=center>Tool loading</div><br>

## Tool operating mechanism

**title:** title

**mouse_down:** ` mouse_down (self, ips, x, y, btn ** key): `Mouse pressed cause to the trigger.`  ips` is  ` ImagePlus ` wrapper class. We can get the current image by the` ips.img `. And we can sequencely get the unit, image indexing table, ROI and additional information on scale and unit corresponding by the ` ips.lut ` , the  ` ips.roi `, and the ` ips.unit `. The x, y is the current mouse position under the data coordinate system.The ` btn ` triggers the mouse button, such as : `0:no`, `1:left`, `2:mid key`, and `3:right`. We can obtain if corresponding function key is pressed or not by the ` key ['alt'] `, the ` key ['ctrl'] `, and the `key ['shift'] `. And ` key['canvas'] ` can get  ` canvas ` object of triggering event.

**mouse_up:** ` mouse_up (self, ips, x, y, btn, ** key) : ` When release pressed mouse, it cause to the trigger.Specific parameters are the same as  ` mouse_down `. 

**mouse_move:** ` mouse_up (self, ips, x, y, btn, ** key) : ` When mouse moves, it cause to the trigger. Specific parameters are the same as  ` mouse_down `. 

**mouse_wheel:** ` mouse_up (self, ips, x, y, btn, ** key) : ` When  the mouse wheel rolls, it cause to the trigger.Specific parameters are the same as  ` mouse_down `. 

