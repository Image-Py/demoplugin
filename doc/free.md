# Free 插件

Free是不需要任何依赖就可以独立运行的插件，我们可以在里面做任何事，如创建图像，下载在线资源等。



## 创建图像

```python
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
```

这里通过一个例子，创建一副新图像，同样我们可以通过para，view进行参数交互。

![14](http://idoc.imagepy.org/demoplugin/22.png)

<div align=center>New Image</div><br>


## 关于对话框

```python
from imagepy.core.engine import Free
from imagepy import IPy

class About(Free):
    title = 'About Demo'

    def run(self, para=None):
        IPy.alert('ImagePy v0.2')
```

早在Hello World时就接触过，这里用作关于对话框。

![14](http://idoc.imagepy.org/demoplugin/23.png)

<div align=center>ImagePy Alert</div><br>


## 退出软件

```python
from imagepy.core.engine import Free
from imagepy import IPy

class Close(Free):
    title = 'Exit Program Demo'
    asyn = False

    def run(self, para = None):
        IPy.curapp.Close()
```

退出软件是Free类型插件一个非常典型的应用，但值得一提的是，插件中加入了`asyn = False`，这个标识告诉ImagePy不要启用异步执行`run`，因为窗口关闭属于`UI`操作，必须在主线程进行。



## Free 的运行机制

Free相比其他插件是运行机制最简单的，因为Free不需要做任何的流程准备，`run`也只有通过交互得到的`para`一个参数，完全放权给开发者。

**para, view:** 

参数字典，具体用法参阅start入门。

**run:** 

获取交互结果，做任何想做的事

**load:** 

`def load(self, ips)` 最先执行，如果`return`结果为`False`，插件将中止执行。默认返回`True`，如有必要，可以对其进行重载，进行一系列条件检验，如不满足，`IPy.alert`弹出提示，并返回`False`。

