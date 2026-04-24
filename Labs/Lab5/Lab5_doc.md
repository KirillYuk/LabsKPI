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




### Підсумок

В результаті роботи реалізовано

Тестування можна провести запустивши `test.py`.

>Дана реалізація є навчальною та демонструє базові принципи. Код можна розширювати та оптимізувати залежно від задачі.