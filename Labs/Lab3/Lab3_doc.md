# Лабораторна робота #3
### Реалізовано декоратор `memo`, який забезпечує кешування результатів викликів функцій.

**test.py**
```python
@memo()
def multiply(x):
    print("calc for", x)
    return x*x

print(multiply(3))
print(multiply(3))
print(multiply(5))
print(multiply(5))
print(multiply(5))
```

**output:**
```
calc for 3
9
9
calc for 5
25
25
25
```

Отримані дані підтверджують роботу кешу: повторні виклики з однаковими значеннями не запускають процес обчислення. Замість цього система звертається до кешу і повертає раніше збережене значення, що значно скорочує час виконання програми.

На даному етапі кеш є необмеженим. Це може призвести до надмірного використання оперативної пам'яті при великій кількості різних вхідних даних.

### Додано підтримку іменованих параметрів (`kwargs`).

**test.py**
```python
@memo()
def multiply(x, y=1):
    print("calc", x, "*", y)
    return x * y

print(multiply(3))
print(multiply(3))
print(multiply(5))
print(multiply(5))
print(multiply(5, 3))
print(multiply(5, 3))
print(multiply(6, 4))
print(multiply(6, y=4))
print(multiply(x=6, y=4))
```

**output:**
```
calc 3 * 1
3
3
calc 5 * 1
5
5
calc 5 * 3
15
15
calc 6 * 4
24
calc 6 * 4
24
calc 6 * 4
24
```

У результатах тестування ми бачимо цікавий момент: спосіб передачі аргументів прямо впливає на роботу кешу. Хоча виклики **multiply(6, 4)** та **multiply(6, y=4)** математично однакові, у консолі ми бачимо повторне повідомлення про перерахунок. Це наочно доводить, що звичайні аргументи (args) та іменовані (kwargs) сприймаються декоратором як різні вхідні дані. Програма створює для них різні ключі в пам'яті: **(6, 4){}** та **(6,){'y': 4}**. Це важливий нюанс, який ми врахуємо при подальшій розробці.

### Додано настраюваний ліміт кешу

Реалізовано найпростіший механізм обмеження: коли місце закінчується, програма видаляє той запис, який потрапив у кеш найпершим. Керується розмір кешу через **max_size**.

**test.py**
```python 
@memo(max_size=2)
def multiply(x, y=1):
    print("calc", x, "*", y)
    return x * y

print(multiply(3))
print(multiply(4))
print(multiply(5))
print(multiply(3))
print(multiply(5, 5))
print(multiply(5, 3))
print(multiply(5, 5))
```

**output:**
```
calc 3 * 1
3
calc 4 * 1
4
calc 5 * 1
5
calc 3 * 1
3
calc 5 * 5
25
calc 5 * 3
15
25
```
В результатах тестування видно, що значення **3 * 1** було видалено з кешу через обмеження його розміру до 2 елементів. А результат **5 * 5** не зазнав видалення, бо якраз помістився в обмежений кеш.

### `LRU`

Реалізовано LRU стратегію. Тепер при переповненні кешу видаляється той елемент, до якого найдовше не звертались.

**test.py**
```python 
@memo(max_size=2, strategy="lru")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(1))
print(multiply(2))
print(multiply(1))
print(multiply(3))
print(multiply(2))
print(multiply(3))
print(multiply(1))
```

**output:**
```
calc 1 * 2
2
calc 2 * 2
4
2
calc 3 * 2
6
calc 2 * 2
4
6
calc 1 * 2
2
```
З результатів тестування видно, що з кешу видаляється елемент, до якого найдовше не звертались.

### `LFU`

Реалізовано LFU стратегію. При переповненні кешу видаляється той елемент, до якого звертались найменшу кількість разів

**test.py**
```python 
@memo(max_size=2, strategy="lfu")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(1))
print(multiply(1))
print(multiply(2))
print(multiply(3))
print(multiply(2))
print(multiply(1))
```

**output:**
```
calc 1 * 2
2
2
calc 2 * 2
4
calc 3 * 2
6
calc 2 * 2
4
2
```
З результатів тестування видно, що з кешу видалили значення для "2" оскільки він мав найменшу кількість звернень серед усіх елементів кешу. Натомість значення для "1" залишилось в кеші.

### kwargs `bug fix`

Виправлено баг, при якому відбувався перерахунок значень для однакових іменованих аргументів, які були написані в різному порядку:

**test.py**
```python 
@memo(max_size=2, strategy="lru")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(x = 2, y = 3))
print(multiply(y = 3, x = 2))
```

**output:**
```
key: (){'x': 2, 'y': 3}
calc 2 * 3
6
key: (){'y': 3, 'x': 2}
calc 2 * 3
6
```
Виправлено баг за допомогою сортування іменованих аргументів:

```python
key = (str(args) + str(sorted(kwargs.items())))
```

**test.py**
```python 
@memo(max_size=2, strategy="lru")
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(x = 2, y = 3))
print(multiply(y = 3, x = 2))
```

**output:**
```
key: ()[('x', 2), ('y', 3)]
calc 2 * 3
6
key: ()[('x', 2), ('y', 3)]
6
```

### `TTL` support

Реалізовано механізм TTL (Time To Live), який обмежує час зберігання значень у кеші. Якщо час життя елемента перевищено, він вважається застарілим і обчислюється повторно.

**test.py**
```python 
@memo(ttl=2)
def multiply(x, y=2):
    print("calc", x, "*", y)
    return x * y

print(multiply(2))
print(multiply(2))
time.sleep(2)
print(multiply(2))
print(multiply(2))
time.sleep(1.99)
print(multiply(2))
```

**output:**
```
key: (2,)[]
calc 2 * 2
4
key: (2,)[]
4
key: (2,)[]
calc 2 * 2
4
key: (2,)[]
4
key: (2,)[]
4

[Done] exited with code=0 in 4.079 seconds
```
З результатів тестування видно, що з кешу видалилось значення при затримці >=2 секунд, натомість значення зберігається в кеші, якщо час очікування не перевищує TTL.


### Custom eviction 

Додано можливість передати власну функцію видалення замість вбудованих стратегій. Функція отримує три словники і повертає ключ який треба видалити.

**test.py**
```python 
def my_custom(cache, access_time, use_count):
    return max(cache, key=cache.get)

@memo(max_size=2, custom=my_custom)
def custom_test(x):
    print("calc", x, "*", x)
    return x * x

print("CUSTOM test")
print(custom_test(5))
print(custom_test(2))
print(custom_test(8))
print(custom_test(3))
print(custom_test(2))
print(custom_test(8))
```

**output:**
```
CUSTOM test
calc 5 * 5
25
calc 2 * 2
4
calc 8 * 8
64
calc 3 * 3
9
4
calc 8 * 8
64
```

З результатів тестування видно що при переповненні кешу видалився запис 
для значення 8 оскільки він мав найбільший результат (64). 
Після видалення повторний виклик з тим самим аргументом призвів до перерахунку.

## Підсумок
В результаті розробки реалізовано повноцінний декоратор мемоізації з наступними можливостями:

- базове кешування результатів функції
- підтримка іменованих аргументів (kwargs)
- обмеження розміру кешу (max_size)
- стратегія LRU - видалення найдавніше використаного
- стратегія LFU - видалення найрідше використаного
- TTL - автоматичне видалення застарілих записів
- custom eviction - власна функція видалення

Тестування можна провести запустивши `test.py`.

>Реалізація демонструє основні підходи до побудови систем кешування. Код може бути розширений та оптимізований під конкретні задачі.