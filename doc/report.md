#  Report 插件

很多问题，最终我们都需要将分析结果整理成报表，生成PDF文档，或者打印。虽然现在LaTex，Markdown等基于标签语言的文档工具非常强大，但是Excel依然是受众最广，上手最简单，精细布局能力最强的表格软件，此外Excel具有强大的数据处理，图表生成功能，因而ImagePy选择Excel作为报表功能载体，用户可自己设计Excel模板，并且在特定单元格中加入标记并保存，将后缀改为rpt，这样就成为了ImagePy的报表插件。



**报表插件的加载方式**

1. menus及其子文件夹下的rpt后缀文件会被解析成报表模板。
2. 也可以将模板文件拖拽到ImagePy最下方的状态栏来执行。



## 个人信息

这里用一张个人信息卡来展示如何制作模板并标记单元格。为了方便打印，我们需要根据自己的情况，先设定纸张大小，这里设置为A5。其次为了精确布局，我们将Excel的视图切换为页面布局，这样单元格尺寸设定都会以cm为单位。

---

![06](http://idoc.imagepy.org/demoplugin/33.png)

<div align=center>personal information template</div><br>

---

![06](http://idoc.imagepy.org/demoplugin/34.png)

<div align=center>personal information result</div><br>

## 硬币分割

我们继续用硬币分割与测量的例子，将分析结果制作成报表。这里我们精心设计一个实验报告，里面包基础信息，处理过程图片，以及结果表格，并在Excel中对结果做了统计，针对面积列，绘制了柱状图。

![06](http://idoc.imagepy.org/demoplugin/37.png)

<div align=center>do coins segment in ImagePy</div><br>

![06](http://idoc.imagepy.org/demoplugin/38.png)

<div align=center>generate coins report</div><br>

## 报表模板设计原则

ImagePy在执行报表插件时，会首先对Excel模板进行解析，分析各个Work Sheet，并检测每个单元格，将所有变量标记提取，以对话框形式与用户交互，确认后，将全部信息回填，并另存。使用非常方便，但我们必须遵循一定的原则来设计模板，这里详细介绍。



*为了方便打印，我们需要根据自己的情况，先设定纸张大小，这里设置为A5。其次为了精确布局，我们将 Excel 的视图切换为页面布局，这样单元格尺寸设定都会以cm为单位。*



**通用语法**

`{type Var_Name = Default Value # note}`，任何类型的变量标记都遵循这个格式，其中大括号为变量标识，而其他项有些项是必须，有些可选，对于不同类型稍有差异，具体如下。

**基础参数**

`int,float,str,txt,bool`：这几个基础参数，语法格式一致以str为例，`{str Name = YX Dragon # please input your name here}`，其中类型与变量名是必须的，默认值与注释为可选。`str`与`txt`的差别在于，在ImagePy的交互对话框中，`txt`可以接收多行文字。

**选择参数**

`list`：用法举例`{list Favourite_System = [Windows, Linux, Mac] # please select your favourite system}`，对于list选项，默认值必须提供，用中括号框住，选项用逗号分开，空格会被忽略，注释为可选。

**图像参数**

`img`：用法举例`{img My_Photo = [4.8,4.8,0.9,0] # you photo here`，对于img类型，默认值必须提供，是一个中括号，里面四个数字，分别代表：长度(cm)，高度(cm)，留白比例（0.9代表四周留10%），是否拉伸（0表示保持比例，1可以拉伸），注释为可选。

**表格参数**

`tab`：用法举例`{tab Record = [1,3,0,0] # the result table}`，对于tab类型，默认值必须提供，是一个中括号，里面四个数字，分别代表：行距（不合并单元格为1），列距（不合并单元格为1），标题行相对位置（-1代表数据区域的上一行，0代表不填充标题），索引列行对位置（-1代表数据区域的左边一列，0代表不填充索引），注释为可选。