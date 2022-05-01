## 捕获异常：
````python
try:
    pass

except *** :
    pass

````

## 捕获未知异常：
```python

try:
    pass


except Exception as result:
    print()

```


## 异常捕获的完整语法：
```python
try:
    pass
except1:
    pass
except2:
    pass
except Exception as result:
    print("result")
else:
    #没有异常才会执行的代码
    pass
finally：
    #无论是否有异常都会执行的代码
    print("无论是否有异常都会执行的代码")

```