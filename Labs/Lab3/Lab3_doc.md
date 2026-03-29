# Лаболаторна робота #3
### Створено декоратор `memo`. Він дозволяє кешувати результати функції.

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

### Додано підтримку іменованих параметрів (`kwards`).

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

У результатах тестування ми бачимо цікавий момент: спосіб передачі аргументів прямо впливає на роботу кешу. Хоча виклики **multiply(6, 4)** та **multiply(6, y=4)** математично однакові, у консолі ми бачимо повторне повідомлення про перерахунок. Це наочно доводить, що звичайні аргументи (args) та іменовані (kwards) сприймаються декоратором як різні вхідні дані. Програма створює для них різні ключі в пам'яті: **(6, 4){}** та **(6,){'y': 4}**. Це важливий нюанс, який ми врахуємо при подальшій розробці.

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
В результатах тестування бачимо що результат **3 * 1** було видалено з кешу через обмеження його розміру до 2 ключів. А результат **5 * 5** не зазанав видалення, бо якраз помістився в обмежений кеш.

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
З результатів тестування видно, що з кешу видаляються ті значення до яких найдовше не звертались.

### `LFU`

Реалізовано LFU стратегію. Тепер при переповненні кешу видаляється той елемент, до якого звертались найменшу кількість разів

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
З результатів тестування видно, що з кешу видалили значення для "2" бо до нього не звертались після розрахунку. Натомість значення для "1" залишилось в кеші.

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