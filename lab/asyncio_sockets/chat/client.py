import asyncio


class ConnectionProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport):
        print("Connected!")
        
        while True:
            message = input("your message: ")

            transport.write(message.encode())
            print("Data sent: {!r}".format(message))

            if (message == "exit"):
                break

        print("Shutting down!")
        self.loop.stop()

    def data_received(self, data):
        print("Data received: {!r}".format(data.decode()))

    def connection_lost(self, exc):
        print("The server closed the connection")
        print("Stop the event loop")
        self.loop.stop()


loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: ConnectionProtocol(loop), "127.0.0.1", 12345)

loop.run_until_complete(coro)
loop.run_forever()
loop.close()

