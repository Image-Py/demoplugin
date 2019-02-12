# Table Plug-in

Table is another very important data type besides image. In a sense, the results of scientific image analysis will eventually be returned to table. ImagePy  have very good support to table type data ,whose core data structure is ` pandas.DataFrame `.



## Generate transcripts

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

We generated table through a ` Free ` plug-in. Table is a ` pandas. The DataFrame ` object, which is displayed by ` IPy. show_table(df, title)` .

![14](http://idoc.imagepy.org/demoplugin/19.png)

<div align=center>generate score list</div><br>


## Sort by subject grade

```python
from imagepy.core.engine import Table

class Sort(Table):
    title = 'Table Sort Demo'

    para = {'by':'Math'}
    view = [('field', 'by', 'item', '')]

    def run(self, tps, data, snap, para=None):
        tps.data.sort_values(by=para['by'], inplace=True)
```

Here is the help of a new argument types, ` field `, and the parameter type is a radio type, which don't need us to provide options and get automatically from the current form of ` columns `. ` run `  directly change ` DataFrame ` itself by ` inplace ` parameters.Some operations can not modify itself, whose result can be return.

![14](http://idoc.imagepy.org/demoplugin/20.png)

<div align=center>sort by math</div><br>


## Draw bar graph

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

Here is the help of a new argument types, ` fields `, and the parameter type is actually a multiple-choice type, which don't need us to provide options and get automatically from the current form of ` columns `.When the table is selected some columns in the interface, the corresponding items are also checked by default in the parameters dialog box. Pandas bring our own drawing functions, but it is worth mentioning that the plug-in joined ` asyn = False `, which tells ImagePy not to  enable asynchronous execution ` run `.Because this plug-in involved in ` UI `, and it must be conducted in the main thread.


![14](http://idoc.imagepy.org/demoplugin/21.png)

<div align=center>bar chart</div><br>

## Table operation mechanism

**note:** 

` note ` option is behavior control indicators, which is used to control the plug-in implementation process.Such as allowing framework to be compatible with the types of tests,if not meet ,the automatic suspension will happen.And it is different from the Filter and simple ` note ` .

1. `req_sel`：It needs selection district
2. `req_row`：It needs to select the row
3. `req_col`：It needs to select the column
4. `auto_snap`：The framework automatically buffers the data before processing
5. `row_msk`：In snap , it only bufferS the selected rows
6. `col_msk`：In snap , it only buffeSr the selected columns
7. `num_only`：In snap , it only buffers only numeric value columns
8. `preview`：Whether to display preview option

**para, view:** 

Parameter dictionary, see start for details.

**run:** 

1. ` tps ` : table wrapper class.We can visit or operate ` rowmsk ` and  ` colmsk `  by ` tps ` 
2. ` snap ` : the buffer of table.If there is a ` auto_snap ` logo, it can take effect.
3. ` data ` : current table can be  operation.

**load:** 

` def load (self, tps) ` are executed first.If ` return ` results for ` False `, plug-in will suspend execution. The default return ` True `.If necessary, which can be overloaded to add a series of condition inspection. If not meet, ` IPy. alert ` pops up prompts, and returns the ` False `.

**preview:**

def preview (self, tps, para) ` will automatically perform ` run ` and update by default , which can be overloaded in need .