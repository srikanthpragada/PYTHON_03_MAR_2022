import threading


class PrintThread(threading.Thread):
    def run(self):
        for n in range(1, 11):
            print('Child ' + str(n))


print(threading.main_thread())
pt = PrintThread()
pt.start()
for n in range(1, 11):
    print('Main ' + str(n))
