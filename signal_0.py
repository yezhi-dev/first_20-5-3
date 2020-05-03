"""
    信号方法处理僵尸
"""

import os
import signal

#处理子进程退出
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
else:
    while True:
        pass


for i in range(5):
    print(i)

print(1)