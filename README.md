Tracker for HSV model
===================


Manually putting values for HSV model can be quite frustrating. The easiest way to deal with it is to make an OpenCV based trackbars which allow us to adjust the values manually using a trackbar. So with the help of this, we can able to adjust the different combination of values in one go


----------


Documents
-------------

Let's take a look at it, 


```python
def tracker (filename)

```

> - **file_name :**  This is everything this function need, you can pass a full path of file or a variable in which image is stored, it can work in both ways,


This program returns
```python 
return lower_hue, lower_sat, lower_val, upper hue, upper_sat, upper_val
```


> - **lower_hue, lower_sat, lower_val: :**  As the name suggests, its a lower value of Hue, Saturation, Value(Brightness)

> - **upper_hue, upper_sat, upper_val: :**  Similarly, its an upper value of Hue, Saturation, Value(Brightness).

if you need any kind of help you can just type

```python
import Tracker_HSV as tr
tr.help()
```

```python
#For full code Explanation, please visit 
#https://py2py.com/Tracker-for-HSV-model-Overview-and-Explanation
#Github: https://github.com/Pushkar-Singh-14/Tracker_HSV
#PyPI: https://pypi.org/project/Tracker-HSV/
```

