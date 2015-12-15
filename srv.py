# -*- coding: utf-8 -*-
# счетчик
N1 = 0
# правильные login:password
accounts = {"user":"true"}

import pickle
import zmq

N1 = 0 # инициализировать счётчик на сервере
print "Initialized"

ctx = zmq.Context()
s = ctx.socket(zmq.REP)
s.bind("tcp://127.0.0.1:41000") # открыть порт
print "Bind at :41000"

while True:
  # такая система "защиты" не спасает от сниффинга,
  # это лишь - банальная блокировка случайных попаданий в порт
  username, password, command = pickle.loads(s.recv())
  # for no KeyError
  if not accounts.has_key(username):
    s.send(pickle.dumps(-1))
    continue
  else:
    if accounts[username] <> password: 
      s.send(pickle.dumps(-1))
      continue
  # основное действие при успешном "логине"
  # keyword passed
  if command == "INC":
    N1 += 1
    print "INC"
    s.send(pickle.dumps(N1))
  elif command == "EXIT":
    print "EXIT"
    s.send(pickle.dumps(-1))
    break
  else:
    print "Error in cmd:", command
    s.send(pickle.dumps(-1))
