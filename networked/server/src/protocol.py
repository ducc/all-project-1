import io

OPCODES = [
        # server -> client | the server assigned a player name to the client
        "NAME",

        # server -> client | server tells the client that both players are
        #                    connected so the game can be played
        "READY",

        # client -> server | the client played a move
        "SEND_MOVE",

        # server -> client | the server forwards the other connected client's 
        #                    move to the current client
        "RECV_MOVE",

        # client -> server | client tells the server it is quitting the game
        "SEND_QUIT",

        # server -> client | server tells the client another client has quit 
        #                    the game
        "RECV_QUIT",
]

def get_opcode(name):
    return OPCODES.index(name)

class Message:
    def __init__(self, opcode):
        self.opcode = opcode
        self.buffer = bytearray()
        self.buffer.append(self.opcode)

    def decode(reader):
        opcode = reader.read(1)[0]
        return Message(opcode)

class NameMessage(Message):
    def __init__(self, name):
        super().__init__(get_opcode("NAME"))
        self.name = name
        encoded_name = name.encode("ASCII") 
        name_length = len(encoded_name)
        self.buffer.append(name_length)
        self.buffer.extend(encoded_name)

    def decode(reader):
        name_length = reader.read(1)[0]
        encoded_name = reader.read(name_length)
        name = encoded_name.decode("ASCII")
        return NameMessage(name)

class ReadyMessage(Message):
    def __init__(self):
        super().__init__(get_opcode("READY"))

class SendMoveMessage(Message):
    def __init__(self, tile):
        super().__init__(get_opcode("SEND_MOVE"))
        self.tile = tile
        self.buffer.append(tile)

    def decode(reader):
        tile = reader.read(1)[0]
        return SendMoveMessage(tile)

class RecvMoveMessage(Message):
    def __init__(self, tile):
        super().__init__(get_opcode("RECV_MOVE"))
        self.tile = tile
        self.buffer.append(tile)

    def decode(reader):
        tile = reader.read(1)[0]
        return RecvMoveMessage(tile)

class SendQuitMessage(Message):
    def __init__(self):
        super().__init__(get_opcode("SEND_QUIT"))

class RecvQuitMessage(Message):
    def __init__(self):
        super().__init__(get_opcode("RECV_QUIT"))

