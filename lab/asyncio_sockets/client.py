import asyncio

class ConnectionHandler(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print("Data sent: {!r}".format(self.message))

    def data_received(self, data):
        print("Data received: {!r}".format(data.decode()))

    def connection_lost(self, exc):
        print("The server closed the connection")
        print("Stop the event loop")
        self.loop.stop()

loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: ConnectionHandler("Hello World!", loop), "127.0.0.1", 12345)

loop.run_until_complete(coro)
loop.run_forever()
loop.close()

