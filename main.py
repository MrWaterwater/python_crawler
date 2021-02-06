import maoyan
import time

if __name__ == '__main__':
    for i in range(10):
        maoyan.maoyan(offset=i * 10)
        time.sleep(1)