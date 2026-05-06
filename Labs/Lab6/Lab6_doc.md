# Лабораторна робота #6
### Basic data generator
Реалізовано генератор тестових даних. Замість реального великого файлу генеруємо дані на льоту

**main.py**
```python
from stream import generate_data

for line in generate_data(5):
    print(line, end=' ')
```

**output:**
```
value0 value1 value2 value3 value4
```

### Sync generator stream
Реалізовано стрім який приймає джерело даних і віддає елементи по одному

**main.py**
```python
from stream import generate_data, read_stream

for item in read_stream(generate_data(5)):
    print(item)
```

**output:**
```
value0
value1
value2
value3
value4
```

### Chunk processing pipeline
Реалізовано обробку даних стріма. Приймає стрім і функцію **fn** яку застосовує до кожного елементу по одному

**main.py**
```python
from stream import generate_data, read_stream, process_stream


def to_upper(item):
    return item.upper()

pipeline = process_stream(read_stream(generate_data(5)), to_upper)

for item in pipeline:
    print(item)
```

**output:**
```
VALUE0
VALUE1
VALUE2
VALUE3
VALUE4
```

### Async iterator stream
Реалізовано асинхронні версії тих самих функцій. Використовуються в асинхронному коді через `async for`. Дозволяють не блокувати *event loop* поки обробляються дані.

**main.py**
```python
import asyncio
from stream import generate_data, read_stream, process_stream, async_process_stream, async_read_stream


def to_upper(item):
    return item.upper()

async def main():
    source = async_read_stream(generate_data(5))
    async for item in async_process_stream(source, to_upper):
        print(item)
        
asyncio.run(main())
```

**output:**
```
VALUE0
VALUE1
VALUE2
VALUE3
VALUE4
```


### Приклади використання
...

### Підсумок

В результаті роботи реалізовано...

---

Тестування можна провести запустивши `test.py`.

>Дана реалізація є навчальною та демонструє базові принципи [...]. Код можна розширювати та оптимізувати залежно від задачі.