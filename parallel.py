from concurrent.futures import ProcessPoolExecutor
import time


def function_1():
    for i in range(100):
        time.sleep(1)
        print(f'function_1: {i+1}回目')


def function_2(male, female):
    for i in range(100):
        time.sleep(1)
        print(f'function_2: {i+1}回目, {male}, {female}')


def function_3(foo, baz):
    for i in range(100):
        time.sleep(1)
        print(f'function_3: {i+1}回目, {foo}, {baz}')


def function_4(foo, baz):
    for i in range(100):
        time.sleep(1)
        print(f'function_4: {i+1}回目, {foo}, {baz}')


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.submit(function_1)
        executor.submit(function_2, 'たかし', 'かな')
        executor.submit(function_3, 'aaa', 'bbb')
        executor.submit(function_4, 'xyz', 'qqq')
