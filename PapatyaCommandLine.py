import tensorflow as tf

class PapatyaCLI:
    def __init__(self):
        print("PapatyaCLI v1")
        self.layers = []
    def executeCommand(command):
        command = command.split(' ')
        if(command[0] == "help"):
            pass
        elif(command[0] == "add"):
            if(command[1] == "layer"):
                if(command[2] == "input"):
                    pass
        elif(command[0] == "init"):
            pass
    def getShape(shape):
        shape = shape.split('x')
        returnShape = ()
        for i in shape:
            returnShape = shape + (i,)
        returnShape
