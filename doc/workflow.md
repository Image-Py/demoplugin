# Workflow Plugin

Macros is a series of command record executed in order, but Workflow is a mix of Macros and Markdown, the same preocess is specified, but Macros does not automatically execute, each step can be adjusted by the user, even some processes can be added or skipped during the process. In addition,  each process developer can set the prompt information, Macro is an automated process, but the Workflow is a guide, which reduces the degree of automation, but is more instructive.


## Coin Split Workflow

```markdown
Coins Segment Workflow Demo
===========================
## Open Image
1. coins
open the coins demo image，we will segment and measure it.
## Segment
1. Up And Down Watershed
check "preview", slide to mark every coins red more or less, mark background green more or less, use "up area".
## Repair the mask
1. Fill Holes
Fill the holes in the conis.
2. Geometry Filter
check "preview", give "area" 100, small fragment less than 100 become dark, then give "back color" 0 to clear them.
## Measure
1. Geometry Analysis
check the indecate we need, here check the "cov", count the cov ellipse.
## Export Result
1. CSV Save
save the measure result as a csv file.
```

![14](http://idoc.imagepy.org/demoplugin/11.png)

<div align=center>Workflow</div><br>

Write a Workflow based on the previous Coin Split Macro, follow the markdown specification, add the necessary notes and chapters, suffix is wf, save to menus or its subfolders, it will be a horizontal block panel when loading, divided into different chapters, click from left to right. Mouse over each section will display the corresponding prompt information, click on the top right to view the entire process

![14](http://idoc.imagepy.org/demoplugin/12.png)

<div align=center>Workflow Demo</div><br>

**Workflow writing and loading**

1. The workflow is a markdown file with the suffix wf
2. The first two lines are the main title, parsed into the main title of the panel
3. The seconda-level heading represents a chapter, which is a function block that resolves to a rectangular panel
4. The number is the command to be executed, starting with a numeric serial number, without parameters, parsing into a button
5. A line of comments can be added below each command. When the user mouse moves over a button, the corresponding description will be displayed
6. Can be copied to menus or its submenus, parsed into menu items at startup
7. You can also drag and drop to the status bar at the bottom of ImagePy to load the workflow
