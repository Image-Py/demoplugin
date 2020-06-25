# Matters Needing Attention
Although the details are not exhaustive, we have introduced the development, release and documentation of plug-ins. Here are some considerations for the development process.



## User Friendliness

If it is for your own use, you don't need to spend too much energy. But you want other users to be able to use your plug-ins, then user friendliness is very important, including:

1. **Reasonable functional organization**

   Divide the functions reasonably and present them with appropriate titles.

2. **Reasonable interaction way**

   For example, the parameter design of the plug-in can have a certain degree of versatility but not messy, and the use of the tool is in line with the use habits.

3. **A concise document**

   If you have the energy, it is best to write a manual for the plug-in. It is necessary to be illustrated.

4. **Optimize the performance experience as much as possible**

   Of course, this point is endless, and mainly depends on the algorithm. The faster the better, waiting is always bad.



## Developer Friendliness

**ImagePy puts developer friendliness in the same position as user friendliness**, because developers and users are a group that can learn from each other, and the line between the two is blurred And they can be transformed into each other. Here are a few development concepts of ImagePy.

1. **ImagePy is not an algorithm library, just a connector**

   ImagePy does not reserch algorithms, but only provides necessary presentation and interaction. It is committed to enabling algorithm developers to configure algorithms with minimal code. You can integrate them into ImagePy, and turn algorithms into tools for others, even non-programmers.

2. **Isolate the UI as much as possible**

   UI for scientific research or the programmer is always unpleasant, ImagePy try your best to isolate UI. Most configuration functions can all be ` para `, ` view ` configuration dialog box to complete the parameters generated, and ` tool ` is abstracted as ` mouse_down `, ` mouse_up `, ` mouse_move `, ` mouse_wheel ` four interface implementation. And some deeply customed  function have to use ` widget `, only this it requires developers to write your own UI code.


3. **Takes the algorithm itself as the core**

   Image data of ImagePy is based on ` Numpy `, tabular data based on ` Pandas `, vector data based on ` Shapely `, and these are universal data structures that are the equivalent of Python standard of scientific computing. As connectors, ImagePy is only support, and not interfere in writing of the algorithm. **so developers must not realize the core algorithm in ` run ` function implementation, because other developers will not be able to use them, which the meaning of open source will be discounted**. Algorithm, UI, and hybrid events  result in ImageJ1 algorithm code difficultly invoked by other developers, who have to use ` IJ.run(...) `. Perhaps ImageJ2 is trying to change this situation. So this is not allowed in the ImagePy usage. 

   **The way we recommend:**

   1）if your plug-in only implements simple data manipulation with a few lines of code, OK, it can be implemented in ` run `.

   2) If your algorithm is relatively complex, so it is best to write it in a separate file, and this module do not refer to any ImagePy related modules, which only based on ` Numpy `, ` Pandas ` standards such as scientific computing library. So that others can copy out, and ` import ` use.

   3) if your algorithm is of great significance, versatility is very strong. Be sure to create a separate algorithm project, upload ` pypi `, and import it from your plug-in project (remember to add it in requirements.txt).

4. **About macros and headless**

   Compared with ImageJ, ImagePy's macro function is very limited. Only serialise existing function, but can not implement other logic. It is closely related to the design concept of ImagePy that **ImagePy is just connector!**. Python is already so easy and powerful, why bother learning another obscure and non-generic macro? ImagePy have not support ` headless ` as well, because all the functions to the algorithm itself are the core, and ImagePy only provides **interaction**. So in the case of headless, interaction does not exist. Then what is the value of ImagePy ? What's the point of using ImagePy? **If all functions can be provided in the form of libraries not depend on ImagePy, why does developers want to write `macros` or ` headless ` code rather than a pure python code?**



## Communicate Timely

Compared with ImageJ, ImagePy is still a child, and its framework and functions are not perfect yet. However, the advantage is that we can control and adjust it in real time without considering the powerful and huge plug-in system on our backs. As a plugin developer, if you encounter any difficulties in the process of plug-in development, and please feel free to contact us.Especially when you feel a plug-in development very complex, it is possible that we lack of some aspect support of framework. We can discuss at any time on the plug-in development ,and at the same time,we improve the main frame together. Let ImagePy better realize the value of connector and serve users and developers.

ImagePy is a partner of www.forum.image.sc, and any development, usage issues can be discussed there.

