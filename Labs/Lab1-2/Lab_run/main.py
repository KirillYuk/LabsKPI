import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fib_gen_lib.generator import fib_gen, run

if __name__ == "__main__":
    try:
        sec = int(input("How many seconds work?: "))
        fib_iter = fib_gen()
        run(fib_iter, sec)
    except ValueError:
        print("Please enter a valid number.")
