# Лабораторна робота #5
### Basic sync map
Реалізовано звичайний синхронний **map**, який йде по кожному елементу по одному і застосовує функцію. (Для порівняння з асинхронними версіями). 

**main.py**
```python
def sync_map(arr, fn):
    result = []
    for item in arr:
        result.append(fn(item))
        print(result)
    return result

print(sync_map([1, 2, 3], lambda x: x * 2))
```

**output:**
```
[2]
[2, 4]
[2, 4, 6]
[2, 4, 6]
```

З виводу видно, що функція застосовується для кожного елементу по одному.

### Callback версія

Перша асинхронна версія. Замість повернення результату - викликає передану функцію `callback` коли обробка завершена. Всі елементи обробляються одночасно через `asyncio.gather`.

**main.py**
```python
import asyncio
from async_map import async_map_callback


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

def on_done(result):
    print(result)

async_map_callback([1, 2, 3], double, on_done)
```

**output:**
```
[2, 4, 6]

[Done] exited with code=0 in 1.203 seconds
```
`await asyncio.sleep(1)` - імітує затримку введення-виведення.

`on_done` (**callback**) - здійснює фінальний вивід у консоль.

### Error handling
Додали обробку помилок. Тепер **callback** отримує два параметри: *error* і *result*. Якщо щось пішло не так передаємо помилку, якщо все працює - передаємо результат.

### Promise версія

Друга асинхронна версія. Простіша за **callback**. Повертає результат через **await**. Використовує `asyncio.gather` для одночасної обробки всіх елементів.

**main.py**
```python
import asyncio
from async_map import async_map_promise


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    result = await async_map_promise([2, 1, 8], double)
    print("result: ", result)

asyncio.run(main())
```

**output:**
```
result:  [4, 2, 16]
```

### async/await
Реалізовано послідовну версію через цикл.

**main.py**
```python
import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    start = time.time()
    result = await async_map_promise([2, 1, 8], double)
    print("result1: ", result, time.time() - start, "c")

    start = time.time()
    result = await async_map_await([2, 1, 8], double)
    print("result2: ", result, time.time() - start, "c")

asyncio.run(main())
```

**output:**
```
result1:  [4, 2, 16] 1.010911226272583 c
result2:  [4, 2, 16] 3.0216171741485596 c
```

### Скасування
Додаємо скасування до послідовної версії (async_map_await).

**main.py**
```python
import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    cancel = asyncio.Event()
    
    async def cancel_after():
        await asyncio.sleep(2)
        cancel.set()
        print("cancel signal")
    
    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2, 3], double, cancel)
    print("result", result)
    
asyncio.run(main())
```

**output:**
```
cancel signal
canceled
result None

[Done] exited with code=0 in 2.203 seconds
```

Знайдено баг. Якщо сигнал скасування приходить під час обробки останнього елемента то функція повертає результат замість None.
>~~Можливо буде виправлено.~~ **Виправлено**

**main.py**
```python
import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    cancel = asyncio.Event()
    
    async def cancel_after():
        await asyncio.sleep(2)
        cancel.set()
        print("cancel signal")
    
    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2], double, cancel)
    print("result", result)
    
asyncio.run(main())
```

**output:**
```
cancel signal
result [2, 4]

[Done] exited with code=0 in 2.201 seconds
```

Сигнал був, але операцію не відмінено.

### Скасування bug fix

Виправлено. Також додано перевірку на пустий масив. 

**main.py**
```python
import time
import asyncio
from async_map import async_map_promise, async_map_await


async def double(x):
    await asyncio.sleep(1) 
    return x * 2

async def main():
    cancel = asyncio.Event()
    
    async def cancel_after():
        await asyncio.sleep(2)
        cancel.set()
        print("!cancel signal!")
    
    asyncio.create_task(cancel_after())
    result = await async_map_await([1, 2], double, cancel)
    print("result", result)
    
asyncio.run(main())
```

**output:**
```
!cancel signal!
canceled after las element
result None

[Done] exited with code=0 in 2.258 seconds
```





### Підсумок

В результаті роботи реалізовано

Тестування можна провести запустивши `test.py`.

>Дана реалізація є навчальною та демонструє базові принципи. Код можна розширювати та оптимізувати залежно від задачі.