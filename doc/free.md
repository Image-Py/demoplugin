# Free

Free是不需要任何依赖就可以独立运行的插件



## 生成成绩单

```python
from imagepy.core.engine import Free
from imagepy import IPy
import numpy as np
import pandas as pd

class Score(Free):
	title = 'Student Score'

	def run(self, para=None):
		index = ['Stutent%s'%i for i in range(1,6)]
		columns = ['Math', 'Physics', 'Biology', 'History']
		score = (np.random.rand(20)*40+60).reshape((5,4)).astype(np.uint8)
		IPy.show_table(pd.DataFrame(score, index, columns), 'Scores')
```

我们通过一个Free插件生成表格，表格是一个pandas.DataFrame对象，通过IPy.show_table(df, title)来展示。



## 根据某科成绩排序

```python
from imagepy.core.engine import Table

class Sort(Table):
	title = 'Table Sort Demo'

	para = {'by':'Math'}
	view = [('field', 'by', 'item', '')]

	def run(self, tps, data, snap, para=None):
		tps.data.sort_values(by=para['by'], inplace=True)
```

这里用到了一种新的参数类型，field，这种参数类型其实是一个单选类型，但是不需要我们提供选项，会自动从当前表格的columns中获取。run中通过inplace参数直接改变DataFrame本身，一些操作无法修改本身，可以将结果return。



## 绘制柱状图

```python
class Bar(Table):
	title = 'Score Chart Demo'
    asyn = False
    
	para = {'item':[]}
	view = [('fields', 'item', 'select items')]

	def run(self, tps, data, snap, para = None):
		data[para['item']].plot.bar(stacked=True, grid=True, title='Score Chart')
		plt.show()
```

这里又遇到了一种参数类型，fields，这种参数类型其实是一个多选类型，但是不需要我们提供选项，会自动从当前表格的columns中获取。当表格从界面上被选中若干列，参数对话框里对应的项也会被默认勾上。我们用pandas自带的绘图函数，但值得一提的是，插件中加入了asyn = False，这个标识告诉ImagePy不要启用异步执行run，因为这个插件涉及了UI，必须在主线程进行。
