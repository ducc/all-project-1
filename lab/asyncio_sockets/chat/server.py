import asyncio


# represents a connection
class ConnectionProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        # get the remote address to which the socket is connected
        remote_addr = transport.get_extra_info("peername")
        print("Connection from {}".format(remote_addr))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print("Data received: {!r}".format(message))

        if (message == "exit"):
            print("closing connection!")
            self.transport.close()


# creating a new asyncio event loop
loop = asyncio.get_event_loop()

# create the server coroutine - each connection creates a new ConnectionProtocol instance
coro = loop.create_server(ConnectionProtocol, "127.0.0.1", 12345)

# creates a task on the event loop to run coro until it has completed
server = loop.run_until_complete(coro)

# serve requests until keyboard interrupt
print("serving on {}".format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# close server & shutdown the event loop
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

