# Лабораторна робота #4
### Class BiQueue
Реалізовано клас `BiQueue`, який містить основну логіку роботи черги. Створено список `self.queue`, де будемо зберігати всі елементи.

**main.py**
```python 
from queue import BiQueue

q = BiQueue()
print(q.queue)
```

**output:**
```
[]
```

### Додавання елементу
Створено метод додавання елементу. Метод приймає два параметри: сам елемент (**item**) та його пріоритет (**priority**).

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
У виводі ми також бачимо значення перед пріоритетом, це порядковий номер (`self.counter`).
А значить структура така *[..,(порядк.номер, пріоритет, 'значення'),..]*

### Видалення елементу з черги за пріоритетом
Створено метод видалення елементу. Метод приймає параметр `mode`: найвищий пріоритет (`highest`) або найнижчий (`lowest`). Для визначення потрібного елемента використано `lambda` функцію як ключ порівняння.

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
В результаті виведено та видалено 2 елементи: **A** з найвищим пріоритетом та **B** з найнижчим пріоритетом.

### Видалення елементу з черги за часом додавання
Доповнено метод видалення елементу. Метод так само приймає параметр `mode`, але тепер ще два додаткові: найстаріший (`oldest`) або найновіший (`newest`). Ці режими працюють за принципами **FIFO** (First In, First Out) та **LIFO** (Last In, First Out). Також використано `lambda` функцію для порівняння порядкового номеру елементів.

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
Додано функцію `peek` для перегляду елемента за обраним режимом без видалення з черги.

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
Метод `peek` дозволяє переглянути елемент відповідно до обраного режиму без його видалення з черги.


### Bug fix
Виявлено помилку: при виклику методів `dequeue` та `peek` для порожньої черги виникала помилка ValueError:

**main.py**
```python
from queue import BiQueue

q = BiQueue()

print(q.peek('highest'))
print(q.peek('lowest'))
print(q.peek('oldest'))
print(q.peek('newest'))
print(q.queue)
```

**output:**
```
ValueError: max() iterable argument is empty
```
Баг виправлено через додавання перевірки довжини черги:

```python
def dequeue(self, mode):
    if len(self.queue) == 0:
        return None
```

**output:**
```
None
None
None
None
[]
```
### Підсумок

В результаті роботи реалізовано двосторонню пріоритетну чергу, яка підтримує доступ до елементів як за пріоритетом, так і за порядком їх додавання. Реалізація дозволяє виконувати операції `enqueue`, `dequeue` та `peek` у різних режимах.

Тестування можна провести запустивши `test.py`.

>Дана реалізація є навчальною та демонструє базові принципи роботи двосторонньої пріоритетної черги. Код можна розширювати та оптимізувати залежно від задачі.