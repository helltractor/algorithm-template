# Decorator

## bootstarp

```python
def bootstrap(f, stack=[]):
    # 定义装饰器函数 bootstrap，用于实现基于生成器的协程功能
    def wrappedfunc(*args, **kwargs):
        # 在每次调用装饰后的函数时执行的逻辑
        if stack:
            # 如果栈不为空，表示已经有协程在执行，直接调用原始函数并返回结果
            return f(*args, **kwargs)
        else:
            # 如果栈为空，需要初始化协程
            to = f(*args, **kwargs)  # 调用原始函数并获取返回值
            while True:
                if type(to) is GeneratorType:
                    # 如果返回值是生成器类型，将生成器推入栈中并获取下一个值
                    stack.append(to)
                    to = next(to)
                else:
                    # 如果返回值不是生成器类型，说明当前协程已结束
                    stack.pop()  # 弹出栈顶生成器
                    if not stack:
                        break  # 如果栈为空，退出循环
                    # 将当前值通过 send() 方法发送给上一个生成器
                    to = stack[-1].send(to)
            return to  # 返回最终结果

    return wrappedfunc  # 返回装饰后的函数
```
