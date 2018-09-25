Python 3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x=3
>>> y=3
>>> print((x+y)*(x/y)%(x-y))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print((x+y)*(x/y)%(x-y))
ZeroDivisionError: float modulo
>>> a=10
>>> b=10
>>> c=((a+b)*(a/b)*(a-b)+(a%b))
>>> print(c)
0.0
>>> 
