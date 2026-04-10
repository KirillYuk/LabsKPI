# Лабораторна робота #4
### Class BiQueue
Створено клас `BiQueue` який буде містити наші методи. Створено список `self.queue`, де будемо зберігати всі елементи.

**main.py**
```python 
from queue import  BiQueue

q = BiQueue()
print(q.queue)
```

**output:**
```
[]
```

### Додавання елементу
Створено метод додавання елементу. Метод приймає два параметри: сам елемент (**item**) та його пріорітет (**priority**).

**main.py**
```python 
from queue import  BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)
print(q.queue)
```

**output:**
```
[(0, 5, 'A'), (1, 1, 'B'), (2, 3, 'C')]
```
У виводі ми також бачимо значення перед пріорітетом, це порядковий номер (**self.counter**).
А значить структура така `[..,(порядк.номер, пріорітет, 'значення'),..]`

### Видалення елементу з черги за пріорітетом
Створено метод видалення елементу. Метод приймає параметр `mode`: найвищий пріорітет (**highest**) або найнижчий (**lowest**). Також для оптимізації замість `def` було використано `lambda` функцію, яка допомагає порівняти саме значення пріорітетів.

**main.py**
```python 
from queue import  BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)
print(q.dequeue('highest'))
print(q.dequeue('lowest'))
print(q.queue)
```

**output:**
```
A
B
[(2, 3, 'C')]
```
В результаті виведено та видалено 2 елементи: **A** з найвищим пріорітетом та **B** з найнижчим пріорітетом.

### Видалення елементу з черги за часом додавання
Доповнено метод видалення елементу. Метод так само приймає параметр `mode`, але тепер ще два додаткові: найстаріший (**oldest**) або найновіший (**newest**). Ці режими працюють за принципами `FIFO` (First In, First Out) та `LIFO` (Last In, First Out). Також використано `lambda` функцію для порівняння порядкового номеру елементів.

**main.py**
```python 
from queue import  BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)
print(q.dequeue('oldest'))
print(q.dequeue('newest'))
print(q.queue)
```

**output:**
```
A
C
[(1, 1, 'B')]
```
В результаті виведено та видалено 2 елементи: **A** який додано першим (він найстаріший) та **C** який додано останім (він найновіший).

### Перегляд елемента за обраним режимом
Додано функцію `peep` для перегляду елемента за обраним режимом без видалення з черги.

**main.py**
```python 
from queue import BiQueue

q = BiQueue()
q.enqueue("A", 5)
q.enqueue("B", 1)
q.enqueue("C", 3)

print(q.peek('highest'))
print(q.peek('lowest'))
print(q.peek('oldest'))
print(q.peek('newest'))
print(q.queue)
```

**output:**
```
A
B
A
C
[(0, 5, 'A'), (1, 1, 'B'), (2, 3, 'C')]
```
Просто вивід елементів за обраним режимом.