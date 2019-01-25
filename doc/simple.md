# Simple

Simple是Filter之外的又一个比较重要的插件，不同的是Simple不着重处理单张图像，而是把图像序列当作整体进行三维处理，此外也用于操作图像之外的相关属性，如ROI, 色彩索引表，比例尺及单位，或图像Mark。



## Gaussian3D

```python
from imagepy.core.engine import Simple
import scipy.ndimage as ndimg

class Gaussian3D(Simple):
	title = 'Gaussian 3D Demo'
	note = ['all', 'stack3d']

	para = {'sigma':2}
	view = [(float, 'sigma', (0,30), 1,  'sigma', 'pix')]

	def run(self, ips, imgs, para = None):
		imgs[:] = ndimg.gaussian_filter(imgs, para['sigma'])
```

note里的stack3d标识是指插件处理一个连续的图像栈，而run函数里，可以通过imgs拿到图像序列，我们对其进行三维高斯滤波，结果重新赋值给imgs。

ImagePy里图像序列分stack2d，stack3d，其中stack2d是基于list的图像序列，便于增加，删除slice。而stack3d是一个连续的numpy数组，便于三维滤波，分析。我们可以通过 **Image > Type > Trans to stack/list** 进行转换。

注意：基于Filter的二维高斯滤波也会处理序列，但处理方式是当成多个二维图像处理，而基于Simple的三维高斯滤波，则是在z方向也进行了卷积。



## SetLUT

```python
from imagepy.core.engine import Simple
import numpy as np

class SetLUT(Simple):
	title = 'Set LUT Demo'
	note = ['all']
	para = {'lut':'red'}
	view = [(list, 'lut', ['red', 'green', 'blue'], str, 'look up', 'table')]

	def run(self, ips, imgs, para = None):
		cmap = [[i==para['lut']] for i in ['red', 'green', 'blue']]
		ips.lut = (cmap*np.arange(256)).astype(np.uint8).T
```

lookup table是一个255*3的色彩映射表，映射表并不改变像素，只改变图像的显示。可以通过ips.lut进行访问或设定。与之相关的还有一个ips.range，是一个二元tuple，设定图像像素的动态范围，对于8位图像，通常是0-255，但对于float类型，range的设定就非常有意义，事实上，在展示时，ImagePy先根据range将图像进行clip，并缩放到0-255，然后再套用索引表。



## Inflate ROI

```python
from imagepy.core.engine import Simple

class Inflate(Simple):
	title = 'Inflate ROI Demo'
	note = ['all', 'req_roi']
	para = {'r':5}
	view = [(int, 'r', (1,100),0, 'radius', 'pix')]

	def run(self, ips, imgs, para = None):
		ips.roi = ips.roi.buffer(para['r'])
```

ROI指明哪些区域是我们关心的，ImagePy中的ROI基于Shapely对象，我们可以对其进行操作，以上是对当前ROI进行扩张的例子。



## Set Scale And Unit

```python
from imagepy.core.engine import Simple

class Unit(Simple):
	title = 'Scale And Unit Demo'
	note = ['all']
	para = {'scale':1, 'unit':'mm'}
	view = [(float, 'scale', (1e-3,1e3), 3, 'scale', ''),
			(str, 'unit', 'scale', '')]

	def run(self, ips, imgs, para = None):
		ips.unit = (para['scale'], para['unit'])
```

默认情况ImagePy中的一切测量，分析结果以像素为单位，但我们可以通过ips.unit对其进行访问和设定。



## Set Random Point Mark

```python
from imagepy.core.engine import Simple
from imagepy.core.mark import GeometryMark
import numpy as np

class Mark(Simple):
	title = 'Random Points Demo'
	note = ['all']

	def run(self, ips, imgs, para = None):
		pts = (np.random.rand(200)*512).reshape((100,2))
		ips.mark = GeometryMark({'type':'points', 'color':(255,0,0), 'lw':1, 'body':pts})
```

mark是图像上的覆盖物，并不改变图像本身。ImagePy定义了一套几何数据结果用于绘制mark，这里简单介绍：



**各种Mark类型及用法**

**point:** {'type':'point', 'color':(r,g,b), 'lw':1, 'body':(x,y)}

**points:** {'type':'points', 'color':(r,g,b), 'lw':1, 'body':[(x1,y1), (x2,y2), ...]}

**line:** {'type':'line', 'color':(r,g,b), 'lw':1, 'style':'-', 'body':[(x1,y1), (x2,y2), ...]}

**lines:** {'type':'lines', 'color':(r,g,b), 'lw':1, 'style':'-', 'body':[[(x1,y1), (x2,y2), ...], [...]]}

**polygon:** {'type':'polygon', 'color':(r,g,b), 'fcolor':(r,g,b), 'lw':1, 'style':'o', 'body':[(x1,y1), (x2,y2), ...]}

**polygons:** {'type':'polygons', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'lw':1, 'style':'o', 'body':[[(x1,y1), (x2,y2), ...], [...]]}
**circle:** {'type':'circle', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':(x,y,r)}

**circles:** {'type':'circles', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':[(x1,y1,r1), (x2,y2,r2)]}

**ellipse:** {'type':'ellipse', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':(x,y,l1,l2,ori)}

**ellipses:** {'type':'ellipses', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':[(x1,y1,a1,b1,ori1), (x2,y2,a2,b2,ori2), ...]}
**rectangle:** {'type':'rectangle', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':True, 'body':(x,y,w,h)}

**rectangles:** {'type':'rectangles', 'color':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':[(x1,y1,w1,h1),(x2,y2,w2,h2),...]}

**text:** {'type':'text', 'color':(r,g,b), 'fcolor':(r,g,b), 'size':8, 'pt':True, 'body':(x,y,txt)}

**texts:** {'type':'texts', 'color':(r,g,b), 'fcolor':(r,g,b), 'size':8, 'pt':True, 'body':[(x1,y1,txt1),(x2,y2,txt2)]}

---

**layer:** {'type':'layer', 'num':-1, 'clolor':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':[sequence of basic element]}
		
**layers:** {'type':'layers', 'num':-1, 'clolor':(r,g,b), 'fcolor':(r,g,b), 'fill':False, 'body':{1:layer1, 2:layer2, ...}}



**以上各个基础元素，形式类似，这里统一讲解各个参数的意义：**

**type:** 元素类型

**color:** 颜色

**fcolor:** 填充色 (只有面状要素有)

**fill:** 是否填充 (只有面状要素有)

**lw:** 线条宽度

**style:** 线条风格，有'-o'代表线条和节点都绘制，当然也可以选择只绘制线条或节点，或都不

**size:** 文字高度 (只有文字有)

**body:** 几何数据，根据各个类型而定



**要素集合**

**layer:** layer可以指定color, fcolor, fill, 不同的是，layer的body存放的是其他基础要素，其实以上各种要素，除了type，body其他的属性都是非必须的，如果当前要素没有指定，则会取自其所属的layer，如果没有所属layer，或layer也未指定，则会使用默认。



**layers:** layers是更高级的要素集合，与layer不同的是，layers的body是一个字典，而且在图像序列中，只绘制层号所对应的layer，这样可以实现对图像序列的每一张设定一个对应的mark。



## Simple运行机制

**note:** 

note选项是行为控制标识，用于控制插件执行的流程，比如让框架进行类型兼容检测，如不满足自动中止。设定通道和序列支持设定，以及是否需要提供预览，roi等支持。

1. all：插件支持任意类型

2. 8-bit：插件支持无符号8位

3. 16-bit：插件支持无符号16位

4. int：插件支持32位，64位整数

5. rgb：插件支持3通道24位彩色

6. float：插件支持32位，64位浮点

   ------

7. req_roi：是否必须有roi才能够处理

8. stack：要求必须是图像序列

9. stack2d：要求必须是离散图像序列(list)

10. stack3d：要求必须是连续图像序列(ndarray)

11. preview：是否显示预览选项

**para, view:** 

参数字典，具体用法参阅start入门。

**run:** 

1. ips：图像封装类，我们可以通过ips对roi, mark, lut, range, unit等进行操作
2. imgs：图像序列，对其进行操作，如三维滤波，或分析，可以以表格形式展示结果。

**load:** 

def load(self, ips) 最先执行，如果return结果为False，插件将中止执行。默认返回True，如有必要，可以对其进行重载，进行一系列条件检验，如不满足，IPy.alert弹出提示，并返回False。

**preview:**

def preview(self, ips, para) Simple虽然定义了preview，但默认是什么也不做的，因为对于三维滤波等操作，往往需要很长的运算时间，因而并不适合预览，如有需要可以重载。