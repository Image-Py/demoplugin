# Start Here

We'll start with the Hello World example, which provides an introduction to the plug-in's loading mechanism and how to configure the parameters dialog for future development.



##  What is plugin

ImagePy is a highly extensible image processing framework. We extend the functions of ImagePy through plug-ins. A plug-in is a piece of code or a file that is placed in a specific location and automatically loaded when ImagePy is launched.  ImagePy native function does not enjoy any privileges in functions of ImagePy - actually. Plug-in is resolved into corresponding UI elements according to these plug-ins directory hierarchy. And we trigger it when click on the corresponding menu or tool. We can use the  `Plugins > Manager > Plugin Tree View`  to view the plug-in and its corresponding source code.

![31](http://idoc.imagepy.org/demoplugin/31.png)
<div align=center>Plugins Tree View</div><br>



## Hello World

Let's start writing our first plug-in to implement a simple Hello World.

```python
from imagepy.core.engine import Free
from imagepy import IPy

class Plugin(Free):
    title = 'Hello World'

    def run(self, para=None):
        IPy.alert('Hello World, I am ImagePy!')
```
This is one of the most simple plug-in, first `import Free, IPy `. Here `Free` is a plug-in type. This type of plug-in does not depend on anything. In `run`, we use `IPy.alert` to pop up a 'Hello world, I am ImagePy!' message box.
![14](http://idoc.imagepy.org/demoplugin/01.png)

<div align=center>Hello World</div><br>

**How is plugin loaded**
We rename the script file as  `hello_plg.py`  above, and copy to ` imagepy > menus > Plugins ` directory in ImagePy. We restart ImagePy, and click  ` Plugins ` menu, then you will see our Hello World plug-in. Some loading principles are as follows:

1. `menus` and its subdirectories will be resolved.
2. files end with `plg.py` will be resolved.
3. ` Plugins ` class in the files will be resolved as a plug-in, ` title ` is menu's caption.



## Who Are You

Next we add some parameters to the plug-in, inviting the user to enter a name and age.

```python
from imagepy.core.engine import Free
from imagepy import IPy

class Plugin(Free):
    title = 'Who Are You'
    para = {'name':'', 'age':0}
    view = [(str, 'name', 'name', 'please'),
            (int, 'age', (0,120), 0, 'age', 'years old')]

    def run(self, para=None):
        IPy.alert('Name:\t%s\r\nAge:\t%d'%(para['name'], para['age']))
```

ImagePy framework implements the parameter dialog generation mechanism, which can generate the corresponding interaction according to `para`, `view`. After completion of interactions, we can get a result of the `para` parameters for interaction in the ` run ` function. In the next example ,we will make more detailed interpretation of the various types of parameters.

![14](http://idoc.imagepy.org/demoplugin/02.png)
<div align=center>Who Are You</div><br>



## Questionnaire

```python
from imagepy.core.engine import Free
from imagepy import IPy

class Plugin(Free):
    title = 'Questionnaire'

    para = {'name':'yxdragon', 'age':10, 'h':1.72, 'w':70, 'sport':True, 'sys':'Mac', 'lan':['C/C++', 'Python'], 'c':(255,0,0)} 

    view = [('lab', 'lab', 'This is a questionnaire'),
            (str, 'name', 'name', 'please'), 
            (int, 'age', (0,150), 0, 'age', 'years old'),
            (float, 'h', (0.3, 2.5), 2, 'height', 'm'),
            ('slide', 'w', (1, 150), 0, 'kg'),
            (bool, 'sport', 'do you like sport'),
            (list, 'sys', ['Windows','Mac','Linux'], str, 'favourite', 'system'),
            ('chos', 'lan', ['C/C++','Java','Python'], 'lanuage you like(multi)'),
            ('color', 'c', 'which', 'you like')]

    def run(self, para=None):
        rst = ['Questionnaire Result', 
            'Name:%s'%para['name'], 
            'Age:%s'%para['age'],
            'Height:%sm'%para['h'], 
            'Weight:%skg'%para['w'], 
            'Like Sport:%s'%para['sport'],
            'Favourite System:%s'%para['sys'],
            'Like lanuage:%s'%para['lan'],
            'Favourite Color:%s'%str(para['c'])]

        IPy.alert('\r\n'.join(rst))
```
Here we implement a questionnaire, which allow the user to input all kinds of information and to show the developer how to use `para`, `view` to configure parameter dialog that they want .


![14](http://idoc.imagepy.org/demoplugin/03.png)
<div align=center>Questionnaire</div><br>

**label:** para type：`no parameters required`, view usage：`('lab', 'lab', 'what you want to show')`

**str:** para type：`str`, view usage：`(str, key, prefix, suffix)`， the ` key ` is correspond with ` key ` of  ` para ` . ` prefix ` and ` suffix ` is used as  tips content before and after the input box.

**int:** para type：`int`，view usage：`(int, key, (lim1, lim2), accu, 'prefix', 'suffix')`，the ` key ` is correspond with ` key ` of  ` para ` .` limit ` used to limit the range of input value，`accu` limits the number of decimal places (0).` prefix ` and ` suffix ` are used as  tips content before and after the input box.

**float:** para type：`float`，view usage：`(int, key, (lim1, lim2), accu, 'prefix', 'suffix')`，the ` key ` is correspond with ` key ` of  ` para ` .` limit ` used to limit the range of input value，`accu` limits the number of decimal places (0).` prefix ` and ` suffix ` are used as  tips content before and after the input box.

**slider:** para type：`int/float`，view usage：`('slide', key, (lim1, lim2), accu, 'prefix')`，the ` key ` is correspond with ` key ` of  ` para ` .` limit ` used to limit the range of input value，`accu` limits the number of decimal places (0). ` prefix ` is used as  tips content before and after the input box.

**bool:** para type：`bool`，view usage：`(bool, 'key', 'label')`，the ` key ` is correspond with ` key ` of  ` para ` .`label` is used as a hint.

**list:** para type：`any type`，view usage：`(list, key, [choices], type, prefix, suffix)`，the ` key ` is correspond with ` key ` of  ` para ` .`choices` is a character option, `type` is the expected output type, such as `str`, `int`. ` prefix ` and ` suffix ` are used as  tips content before and after the input box.

**choices:** para type：`str list`，view usage：`('chos', key, [choices], prefix, suffix)`，Similar to `list`, the difference is that `choices` can support multiple selections, and the options are recorded in the form of `list of string`.

**color:** para type：`(r,g,b) 0-255`， usage：`('color', key, prefix, suffix)`，the ` key ` is correspond with ` key ` of  ` para ` .` prefix ` and ` suffix ` are used as  tips content before and after the input box.



*In addition to the basic data types above, ImagePy also supports some parameters of internal types, such as receiving an image, receiving a table, or making single or multiple selections of the fields of the table, which we will show in later example*



## Implement multi-plugins in one file
We implemented three plug-ins above. And Python has the advantage of being syntax-efficient, so we can implement multiple plug-ins in one file, as follows.

```python
from imagepy.core.engine import Free
from imagepy import IPy

class HelloWorld(Free):
    title = 'Hello World'
    ...
    
class WhoAreYou(Free):
    title = 'Who Are You'
    ...
    
class Questionnaire(Free):
    title = 'Questionnaire'
    ...
    
plgs = [HelloWorld, WhoAreYou, Questionnaire]
```

We will write three classes in a file, then add `plgs = []`, file named `start_plgs.py`. The framework loading principle is as follows:

1.  files in the ` menus ` directory or subdirectory, end with `plgs.py` will be resolved as multi plug-in. 
2.  `plgs` list in the file will be resolved one by one
3. `'-'` in ` plgs`  will be resolved as a menu separator

![14](http://idoc.imagepy.org/demoplugin/04.png)

<div align=center>resolved as menus</div><br>

