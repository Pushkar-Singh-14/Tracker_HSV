Tracker for HSV model
===================


Manually putting values for HSV model can be quite frustrating. Easiest way to deal with it is make a openCV based trackbars which allow us to adjust the values manually using a trackbar. So with the help of this, we can able to adjust different combination of values in one go.


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


> - **lower_hue, lower_sat, lower_val: :**  As the name suggest, its a lower value of Hue, Saturation, Value(Brightness)

> - **upper_hue, upper_sat, upper_val: :**  Similary, its a upper value of Hue, Saturation, Value(Brightness).


