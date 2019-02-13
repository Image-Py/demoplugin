# <span id = "Write The Operation Manual For The Plugin">Write The Operation Manual For The Plugin</span>

The manual is not a required part, but it is very important that you write your own plug-in to better serve your users. Here we demonstrate how to write a manual for the plug-in.

## Write The Opteration Manual

Under the top-level directory of your plug-in project, create a `doc` folder, where you can write action documents for your plug-in using `markdown`. Note that the file name needs to be the same as the `title` of the plug-in, so that the `ImagePy` document manager can associate the document with the plug-in. Both tool-type and menu-type plug-ins can be documented.

`doc` under all the `markdown` files are parsed and through the file name associated to the corresponding plugin, so there is no mandatory file organization way, but we strongly recommend that maintain a consistent with plug-in directory document directory (create `menus`, `tools`, `widgets` three top-level directory), convenient management and maintenance, so we can add more if necessary directory file, add the corresponding link, so the whole `doc` directory can also be read in the github or other online environment.

## Refer To Operation Manual

When the plugin is finished, we can check the document in the following ways:

1. We can use the Help button in the dialog of parameters
2. Right-click on the toolbar icon
3. Use the various **`Tree`** views under the **`Plugins > Manager`**

![14](http://idoc.imagepy.org/demoplugin/31.png)

<div align=center>view doc from plugin tree view</div><br>   
