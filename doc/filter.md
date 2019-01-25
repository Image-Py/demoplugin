# Filter

Filter是最重要的一类插件，用于对二维图像进行滤波，也是图像处理中最基础，最普遍的一类应用。



## Invert

```python
from imagepy.core.engine import Filter

class Invert(Filter):
    title = 'Invert Demo'
    note = ['all', 'auto_msk', 'auto_snap']

    def run(self, ips, snap, img, para = None): 
        return 255-snap
```

Invert插件，note指明插件支持任何类型，并且支持roi，支持撤销。我们在run里面返回处理后的结果。关于snap和img，img是当前图像，而如果当note中加入auto_snap标识，在run之前，框架会帮我们把img拷贝给snap，因为多数的滤波器需要一个buffer来卷积，此外撤销和roi支持也必须借助snap。



## Gaussian

```python
from imagepy.core.engine import Filter
from scipy.ndimage import gaussian_filter

class Gaussian(Filter):
    title = 'Gaussian Demo'
    note = ['all', 'auto_msk', 'auto_snap','preview']
    para = {'sigma':2}
    view = [(float, 'sigma', (0,30), 1,  'sigma', 'pix')]
    
    def run(self, ips, snap, img, para = None):
        gaussian_filter(snap, para['sigma'], output=img)
```

Gaussian插件，note指明支持任何类型，并且支持roi，支持撤销，并提供预览功能。para和view指明有一个浮点参数sigma，而run里，我们调用scipy.ndimage.gaussian_filter，对snap进行滤波，输出指向img，如果函数不带输出项，我们将处理结果return即可，框架会帮我们赋值给img。



## Filter运行机制

**note:** 

note选项是行为控制标识，用于控制插件执行的流程，比如让框架进行类型兼容检测，如不满足自动中止。设定通道和序列支持设定，以及是否需要提供预览，roi等支持。

1. all：插件支持任意类型

2. 8-bit：插件支持无符号8位

3. 16-bit：插件支持无符号16位

4. int：插件支持32位，64位整数

5. rgb：插件支持3通道24位彩色

6. float：插件支持32位，64位浮点

   ------

7. not_channel：当处理多通道时，不要框架自动遍历通道（默认情况下会将每个通道依次处理）

8. not_slice：当处理图像序列时，不要询问是否批量处理（默认情况会询问用户）

9. req_roi：是否必须有roi才能够处理

   ---

10. auto_snap：是否需要框架在处理器对当前图像自动缓冲

11. auto_msk：是否自动支持ROI（必须配合auto_snap才生效，原理是用snap恢复ROI以外像素）

12. preview：是否支持预览，调整参数实时查看结果

13. 2int：是否在运算过程中将低于int32的数据转为int32再进行处理（例如避免8位的运算溢出）

14. 2float：是否在运算过程中将低于float32的数据自动转为float32再进行处理（一些运算要求精度）

**para, view:** 参数字典，具体用法参阅start入门。

**run:** 

1. ips：图像封装类，通常在filter中不需要对其进行操作
2. snap：当note里加入auto_snap标识后，在run之前框架会将当前图像拷贝到snap（尽可能实现使用对snap进行处理，将结果赋值给img）
3. img：当前图像，我们将结果赋值给img，或return结果，由框架赋值给img，并完成界面刷新。

**load:** 

def load(self, ips) 最先执行，如果return结果为False，插件将中止执行。默认返回True，如有必要，可以对其进行重载，进行一系列条件检验，如不满足，IPy.alert弹出提示，并返回False。

**preview:**

def preview(self, ips, para) 在预览时执行，默认会调用run处理当前图像，如果有必要可以对其进行重载。