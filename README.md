# Demo Plugin

**Path:** https://github.com/Image-Py/demoplugin

**Version:** 0.1

**Author:** YXDragon

**Email:** yxdragon@imagepy.org

**Keyword:** demo, tutorial

**Description:** a friendly develop tutorial.

*这是一个ImagePy插件项目，里面覆盖了各类插件的编写方法和用法，并配有详细的文档，ImagePy的插件开发者可以以此为参考*



## 安装

ImagePy菜单：`Plugins > Manager > Plugins Manager` 在输入框内输入demo进行查询，选中Demo Plugin，点击`Install`，完成后菜单栏出现Demo菜单，工具栏会加入Demo工具，组件栏也会加入Demo组件。

![06](http://idoc.imagepy.org/demoplugin/06.png)
<div align=center>Install DemoPlugin</div><br>

## [从这里开始](doc/start.md#基础预备)

1. [什么是插件](doc/start.md#什么是插件)
2. [Hello World（第一个插件）](doc/start.md#Hello)
3. [Who Are You（带有交互）](doc/start.md#Who)
4. [Questionnaire（参数对话框详解）](doc/start.md#Questionnaire)
5. [一个文件内实现多个插件](doc/start.md#一个文件内实现多个插件)



## 插件开发

**[Markdown: 文档提示](doc/markdown.md#Markdown)**

1. [Markdown Demo](doc/markdown.md#Demo)

**[Macros: 用宏串联已有功能](doc/macros.md#Macros)**
1. [关于插件的加载方式](doc/macros.md#关于插件的加载方式)
2. [高斯模糊再求反](doc/macros.md#高斯模糊再求反)
3. [Coins Segment Macros：硬币分割](doc/macros.md#分割硬币)

**[Workflow: 可交互的宏](doc/workflow.md#Workflow)**
1. [Coins Segment Workflow: 按照指引进行硬币分割](doc/workflow.md#分割硬币)
2. [工作流编写及加载方式](doc/workflow.md#工作流编写及加载方式)

**[Filter: 二维图像滤波器](doc/filter.md#Filter)**
1. [Invert Demo：无参数的插件](doc/filter.md#Invert)
2. [Gaussian Demo：带有参数的插件](doc/filter.md#Gaussian)
3. [Filter运行机制](doc/filter.md#Filter运行机制)

**[Simple: 图像整体操作](doc/simple.md#Simple)**
1. [Gaussian 3D Demo：三维滤波](doc/simple.md#Gaussian3D)
2. [Red Lut Demo：操作索引表](doc/simple.md#SetLUT)
3. [ROI Inflate Demo：操作ROI](doc/simple.md#ROI)
4. [Unit Demo: 设置比例尺及单位](doc/simple.md#Unit)
5. [Draw Mark Demo: 设置Overlay Mark](doc/simple.md#Mark)
6. [Simple运行机制](doc/simple.md#Simple运行机制)

**[Table: 表格数据](doc/table.md#Table)**
1. [Generate Table Demo：数据表生成](doc/table.md#生成成绩单)
2. [Sort By Key Demo：排序](doc/table.md#根据某科成绩排序)
3. [Table Plot Demo：绘图](doc/table.md#绘制柱状图)
4. [Table运行机制](doc/table.md#Table运行机制)

**[Free: 没有任何依赖的插件](doc/free.md#Free)**
1. [New Image Demo: 新建图像](doc/free.md#创建图像)
2. [About Demo：关于对话框](doc/free.md#关于对话框)
3. [Close Demo：退出程序](doc/free.md#退出软件)
4. [Free的运行机制](doc/free.md#Free的运行机制)

**[Tool: 鼠标交互工具](doc/tool.md#Tool)**
1. [Painter Demo：画笔工具](doc/tool.md#画笔工具)
2. [Tool的运行机制](doc/tool.md#Tool的运行机制)

**[Widget: 桌面小部件](doc/widget.md#Widget)**
1. [Widget Demo：桌面小部件演示](doc/widget.md#画笔工具)
2. [Tool的运行机制](doc/widget.md#Tool的运行机制)



## [插件项目发布](doc/publish.md#插件项目发布)

**[插件的组织方式](doc/publish.md#功能组织)**
1. [功能划分](doc/publish.md#功能划分)
2. [顺序设定](doc/publish.md#顺序设定)

**[插件项目的发布](doc/publish.md#创建插件项目仓库)**
1. [编写requirements](doc/publish.md#requirements)
2. [为Readme加入的插件头信息](doc/publish.md#编写readme)
3. [发布到ImagePy](doc/publish.md#发布到ImagePy)

**插件的安装与管理**
1. 通过连接安装插件](doc/publish.md#Widget
2. 插件管理器](doc/publish.md#Widget



## [文档编写](doc/document.md#文档编写)

为插件编写操作手册



## [注意事项](doc/attention.md#注意事项)

1. [用户友好性](doc/attention.md#用户友好性)
2. [开发者友好性](doc/attention.md#开发者友好性)
3. [及时沟通](doc/attention.md#及时沟通)
