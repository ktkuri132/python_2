import multiprocessing
import time


def sing():
    while True:
        print('正在唱歌...')
        time.sleep(0.2)

def dance():
    while True:
        print('正在跳舞...')
        time.sleep(0.2)


if __name__ == '__main__':
    sing_process=multiprocessing.Process(target=sing)
    dance_process=multiprocessing.Process(target=dance)
    sing_process.start()
    dance_process.start()