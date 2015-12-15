# -*- coding: utf-8 -*-

import zmq
import pickle

context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect("tcp://127.0.0.1:41000") # подключиться к порту

# отправить логин-пароль и команду без аргументов
s.send(pickle.dumps(("user","true","INC")))
res = s.recv() # получить ответ
print pickle.loads(res)

# выполнить 10 тыс. таких же, но - неуспешных попыток
for i in xrange(10000):
  s.send(pickle.dumps(("user","false","INC")))
  res = s.recv()

# снова успешную
s.send(pickle.dumps(("user","true","INC")))
res = s.recv()
# и вывести результат работы с сервером
print pickle.loads(res)
# всего, за один запуск скрипта, счётчик должен увеличиться на +2

# EXIT
s.send(pickle.dumps(("user","true","EXIT")))
