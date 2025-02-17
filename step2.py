Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #b00152481
... #17/02/2025
... #Step2.py
... 
... from divisors import divisors
... def perfectNumber(x):
...     result = false
... 
...     if sum(divisors(x)) == x:
...         result = True
... 
...     returm result
... 
... if (perfectNumber(8128)): print("8128 is a perfect number")
... 
