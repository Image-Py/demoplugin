# Demo Plugin

**Path:** https://github.com/Image-Py/demoplugin

**Version:** 0.1

**Author:** YXDragon

**Email:** yxdragon@imagepy.org

**Keyword:** demo, tutorial

**Description:** a friendly develop tutorial.

**[English Document](README.md) | [中文文档](READMECN.md)**

*这是一个ImagePy插件项目，里面覆盖了各类插件的编写方法和用法，并配有详细的文档，ImagePy的插件开发者可以以此为参考*



## 安装

ImagePy菜单：`Plugins > Manager > Plugins Manager` 在输入框内输入demo进行查询，选中Demo Plugin，点击`Install`，完成后菜单栏出现Demo菜单，工具栏会加入Demo工具，组件栏也会加入Demo组件。

![06](http://idoc.imagepy.org/demoplugin/06.png)
<div align=center>Install DemoPlugin</div><br>

## [基础预备](doc/chinese/start.md)

**[从这里开始](doc/chinese/start.md)**

1. [什么是插件](doc/chinese/start.md#什么是插件)
2. [Hello World（第一个插件）](doc/chinese/start.md#Hello-World)
3. [Who Are You（带有交互）](doc/chinese/start.md#Who-Are-You)
4. [Questionnaire（参数对话框详解）](doc/chinese/start.md#Questionnaire)
5. [一个文件内实现多个插件](doc/chinese/start.md#一个文件内实现多个插件)



## 插件开发

**[Markdown: 文档提示](doc/chinese/markdown.md)**

1. [Markdown Demo](doc/chinese/markdown.md#MarkDown-Demo)

**[Macros: 用宏串联已有功能](doc/chinese/macros.md#Macros)**

1. [高斯模糊再求反](doc/chinese/macros.md#高斯模糊再求反)
2. [Coins Segment Macros：硬币分割](doc/chinese/macros.md#分割硬币)

**[Workflow: 可交互的宏](doc/chinese/workflow.md)**

1. [Coins Segment Workflow：按照指引进行硬币分割](doc/chinese/workflow.md#硬币分割工作流)

**[Report: 生成报表](doc/chinese/report.md)**

1. [Personal Information：填写个人信息](doc/chinese/report.md#个人信息)
2. [Coins Report：硬币分割成果](doc/chinese/report.md#硬币分割)
3. [Report 插件的设计原则](doc/chinese/report.md#报表模板设计原则)

**[Filter: 二维图像滤波器](doc/chinese/filter.md)**

1. [Invert Demo：无参数的插件](doc/chinese/filter.md#Invert)
2. [Gaussian Demo：带有参数的插件](doc/chinese/filter.md#Gaussian)
3. [Filter 的运行机制](doc/chinese/filter.md#Filter-运行机制)

**[Simple: 图像整体操作](doc/chinese/simple.md)**

1. [Gaussian 3D Demo：三维滤波](doc/chinese/simple.md#Gaussian3D)
2. [Red Lut Demo：设定索引色](doc/chinese/simple.md#SetLUT)
3. [ROI Inflate Demo：操作ROI](doc/chinese/simple.md#Inflate-ROI)
4. [Unit Demo: 设置比例尺及单位](doc/chinese/simple.md#SEt-Scale-And-Unit)
5. [Draw Mark Demo: 设置Overlay Mark](doc/chinese/simple.md#Mark)
6. [Simple 的运行机制](doc/chinese/simple.md#Simple-运行机制)

**[Table: 表格数据](doc/chinese/table.md)**

1. [Generate Table Demo：数据表生成](doc/chinese/table.md#生成成绩单)
2. [Sort By Key Demo：排序](doc/chinese/table.md#根据某科成绩排序)
3. [Table Plot Demo：绘图](doc/chinese/table.md#绘制柱状图)
4. [Table 运行机制](doc/chinese/table.md#Table-运行机制)

**[Free: 没有任何依赖的插件](doc/chinese/free.md)**

1. [New Image Demo: 创建图像](doc/chinese/free.md#创建图像)
2. [About Demo：关于对话框](doc/chinese/free.md#关于对话框)
3. [Close Demo：退出软件](doc/chinese/free.md#退出软件)
4. [Free 的运行机制](doc/chinese/free.md#Free-的运行机制)

**[Tool: 鼠标交互工具](doc/chinese/tool.md)**

1. [Painter Demo：画笔工具](doc/chinese/tool.md#画笔工具)
2. [Tool的运行机制](doc/chinese/tool.md#Tool-的运行机制)

**[Widget: 桌面小部件](doc/chinese/widget.md)**

1. [Widget Demo：桌面小部件演示](doc/chinese/widget.md#桌面组件演示)
2. [Tool的运行机制](doc/chinese/widget.md#widget-的运行机制)



## [插件项目发布](doc/chinese/publish.md)

**[插件的组织方式](doc/chinese/publish.md#功能组织)**

1. [功能划分](doc/chinese/publish.md#功能组织)
2. [顺序设定](doc/chinese/publish.md#功能组织)

**[插件项目创建](doc/chinese/publish.md#插件项目创建)**

1. [创建插件项目仓库](doc/chinese/publish.md#插件项目创建)
2. [编写requirements](doc/chinese/publish.md#插件项目创建)
3. [编写readme](doc/chinese/publish.md#插件项目创建)
4. [插件的安装](doc/chinese/publish.md#插件项目创建)

**[发布到 ImagePy](doc/chinese/publish.md#发布到-ImagePy)**

1. [给ImagePy发Pull Request](doc/chinese/publish.md#发布到-ImagePy)
2. [关于顶级菜单](doc/chinese/publish.md#发布到-ImagePy)



## [文档编写](doc/chinese/document.md)

**[编写操作手册](doc/chinese/document.md#编写操作手册)**

**[查阅操作手册](doc/chinese/document.md#查阅操作手册)**



## [注意事项](doc/chinese/attention.md#注意事项)

**[用户友好性](doc/chinese/attention.md#用户友好性)**

**[开发者友好性](doc/chinese/attention.md#开发者友好性)**

**[及时沟通](doc/chinese/attention.md#及时沟通)**



**本篇文档相对系统的介绍了ImagePy的插件开发，但是依然无法详尽，关于更多ImagePy使用，开发上的问题请在[forum.Image.sc](https://forum.image.sc/)行进行讨论**