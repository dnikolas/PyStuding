import zmq

port = 5555
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(f'tcp://*:{port}')
poller = zmq.Poller()
poller.register(server, zmq.POLLIN)
socks = dict(poller.poll(5 * 1000))
while True:
    req = server.recv()
    print(req)
    server.send(bytes('Ok!', 'utf-8'))
