#  Macros Plugin

Macros are a series of command records that can be used to repeat operations, instead of writing our own commands, we use a macro recorder to do the recording. Macro recorder in **`Plugins > Macros> Macros Recorder`**. We save the recorded commands to one of the menus or its subfolders, the MC suffix, and reboot to get them corresponding position.

![14](http://idoc.imagepy.org/demoplugin/08.png)

<div align=center>Macros Recorder</div><br>

**About The Loading Way Of Plugin**

1. The mc suffix file under the menus and its subfolders is resolved to a macro.
2. You can also drag and drop macro files into the status bar at the bottom of the ImagePy for execution.

## Gaussian Blur Then Invert

```python
Gaussian>{'sigma': 2}
Invert>None
```

These are two commands, Click and then perform the Gaussian and Invert.

![14](http://idoc.imagepy.org/demoplugin/09.png)

<div align=center>Gaussian And Invert</div><br>

1. Macros are structured in this way of `name of Plugin>Parameters of the dictionary`
2. If no arguments using `None` placeholder.
3. If a parameter-needed command is given to `None`, ImagePy will pop up the parameter dialog box for interaction.

## Coins Segmentation

```python
coins>None
Up And Down Watershed>{'thr1': 36, 'thr2': 169, 'type': 'up area'}
Fill Holes>None
Geometry Filter>{'con': '4-connect', 'inv': False, 'area': 100.0, 'l': 0.0, 'holes': 0, 'solid': 0.0, 'e': 0.0, 'front': 255, 'back': 0}
Geometry Analysis>{'con': '8-connect', 'center': True, 'area': True, 'l': True, 'extent': False, 'cov': True, 'slice': False, 'ed': False, 'holes': False, 'ca': False, 'fa': False, 'solid': False}
```

The above is a process of coin segmentation recorded macro, click will automatically perform coins segmentation, preprocessing, area filtering, area analysis, generate table. (we don't normally record 'open images' to macros, of course)

![14](http://idoc.imagepy.org/demoplugin/10.png)

<div align=center>Coins Segment Macros</div><br>
