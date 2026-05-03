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



### Приклади використання
...

### Підсумок

В результаті роботи реалізовано...

---

Тестування можна провести запустивши `test.py`.

>Дана реалізація є навчальною та демонструє базові принципи [...]. Код можна розширювати та оптимізувати залежно від задачі.