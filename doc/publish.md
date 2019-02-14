# Plug-in Project Release

We discussed each plug-in realizing above.Of course, we can create the python scripts to develop a plugin function  arbitrarily  in ` menus `, ` tools `, ` widgets ` of ImagePy  . But when our plugins are more and more,  function system is more and more complex, of course we will hope to launch into a plug-in project, which can let other users to installa conveniently . Here we discuss how to publish a plug-in project.



## Function organization

**Functional partitioning**

If our plug-in is not a single function, but a set of very systematic functions.Then we should divide and cluster these functions and organize them with folders. For example, all the functionality we wrote earlier can be organized by plug-in type.

![14](http://idoc.imagepy.org/demoplugin/28.png)

<div align=center>functional partitioning</div><br>
**set sequence **

We see that the functional division of plug-in is more clear, but the plugin is sorted in alphabetical order.We want to specify the order, and it is very easy to implement in ImagePy. We  add ` catlog ` fields to the ` init. py ` file, and indicate the order with a list of objects.

`__init__.py`

```python
catlog = ['Start Here', '-', 'Markdown Demo', 'Macros Demo', 'Workflow Demo', '-', 'Filter Demo', 'Simple Demo', 'Table Demo', 'Free Demo', '-', 'WidgetDemo']
```

Once catlog set well, menu will be loaded in specified order, such as :` '-' ` parses to segment line. The ` catlog ` can appear in any plug-in directory, or you can specify plug-in, or you can also specify the order of the folder, or to play a role to the tools (the other way to set the order is  ` plgs ` way  to realize multiple plug-ins ,which is introducted before  ).

![14](http://idoc.imagepy.org/demoplugin/29.png)

<div align=center>sort by catlog</div><br>

The ` catlog ` can appear in any plug-in directory, or  specify a plug-in, or specify the order of the folder, and also play a role to ` tools ` . The ` plgs ` can also specify the order of the plugin for multi plugin file.



## Plugin project creation

**Create a plugin project repository**

If the plug-in is dispersed in ImagePy  , the main folder is not easy to manage.So we create a separate plug-in project warehouse, and create ` menus `, ` tools `, ` widgets ` three folders on the top floor of the warehouse , which contain plug-ins with functional division and correct order .




**write requirements**

Python's biggest advantage is rich in library.As a plug-in project, it is likely to depend on other libraries.By convention, we need to writte the dependence to ` requirements. txt` (When installing a plug-in,ImagePy automatically calls pip to resolve dependency libraries, temporary support only pip, follow-up we will consider supporting conda)



**write readme**

Readme was originally intended for project introduction, but the first few lines of readme are used for plug-in management in ImagePy.So the first few lines of readme need to strictly follow the following specifications, taking this project as an example:

```markdown
# Demo Plugin

Path: https://github.com/Image-Py/demoplugin

Version: 0.1

Author: YXDragon

Email: yxdragon@imagepy.org

Keyword: demo, tutorial

Description: a friendly develop tutorial

*Feel free to write in the following*

```



**Plugin installation**

**`Plugins > Install > Install Plugin`** Enter the github link to the plug-in repository in the dialog box, and ImagePy starts downloading the plug-in, resolving dependencies, and loading it automatically. After loading successfully, we can see that the menu bar, toolbar and component bar are automatically updated. This way, you can send the address of your plug-in project to someone else and for better installing and using it.

![14](http://idoc.imagepy.org/demoplugin/30.png)

<div align=center>Plugin installation</div><br>

## Published to ImagePy

**Send Pull Requestion to ImagePy**

You can also publish your plug-in project to ImagePy, which is a simple process if you have completed your plug-in project. You only need to  ` fork ` a ImagePy, and copy your ` readme ` file to * * ` ImagePy - Plugins - Contribute - Contributors ` * *.Aftr renamed the plug-in project name (not mandatory, but it is the best that can reflect the plug-in function), you try  ImagePy ` Pull Request `. When ImagePy members receive ` Pull Request `, we will ` merge ` your ` Pull Request ` after the test.If any problem ,we will pass ` issue ` to communicate. Once incorporated into the ImagePy main branch, the user can retrieve, or install, or uninstall, and so on through the plug-in manager.

![14](http://idoc.imagepy.org/demoplugin/06.png)

<div align=center>Plugins Manager</div><br>

Plug-in manager will automatically parse ` contributors ` plug-in directory information, thus  ` readme ` of plug-in project must be in accordance with the format to write seriously.It will affect the user's search experience if not. If there is update, please modify the version number, a new ` Pull Request `.And plug-in manager will automatically detect updates.



**About the top-level menu**

We see that after installing the plug-in, the functions in the plug-in project are also loaded into the menu bar, toolbar, and components bar. We can see that the menus, tools, widgets directory in the plug-in project has the same effect as the directory in the main ImagePy project. ** if you don't want the Plugin functionality to be on the top menu, you can control it using the folder structure. **For example, if we want to get my menus to appear under the Plugin, we add a folder named Plugin to the menu of my Plugin project. 

After installing plug-in project , project is decompred into  `plugins ` directory of ImagePy.And ImagePy startup, after parsing main directory, which will parse the plugin directory structure of the project.So that independent management is achieved relatively for the plug-in projects. **As top-level menu space is scarce, please do not use it ,unless it has very rich and systematic functions**