#encoding:utf-8
from queue import Queue
list_a = ['a','v','s','2','o','9','s']
q = Queue()
for str in list_a:
   q.put(str)


for s in range(q.qsize()):
   b = q.get()
   print(b)
   if b == '2':
      print('-----2-----')
   else:
      q.put(b)

print(q.qsize())
