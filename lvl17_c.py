import zmq
from datetime import datetime
import time

host = '127.0.0.1'
port = 5555
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(f'tcp://{host}:{port}')
for i in range(1, 100):
    #t = str(datetime.now())
    t = 'Hi1'
    client.send(bytes(t, 'utf-8'))
    time.sleep(5)
    print(client.recv())
