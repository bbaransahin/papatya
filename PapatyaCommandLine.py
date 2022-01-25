import tensorflow as tf

class PapatyaLayer:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    def sendOutputTo(self, nextLayer):
        self.nextLayer = nextLayer
    def getInputFrom(self, previousLayer):
        self.previousLayer = previousLayer

class PapatyaModel:
    def __init__(self, name):
        print("A PapatyaModel named "+name+" is initialized.")
        self.name = name
        self.layers = []
    def addLayer(self, pLayer):
        self.layers.append(pLayer)
    def build(self):
        pass

class PapatyaCLI:
    def __init__(self):
        print("PapatyaCLI v1")
        self.layers = []
    def executeCommand(self, command):
        command = command.split(' ')
        if(command[0] == "help"):
            pass
        elif(command[0] == "add"):
            if(command[1] == "layer"):
                if(command[2] == "input"):
                    inputs = tf.keras.Input(shape=self.getShape(command[3]))
        elif(command[0] == "init"):
            pass
        elif(command[0] == "exit"):
            isRun = False
    def getShape(self, shape):
        shape = shape.split('x')
        returnShape = ()
        for i in shape:
            returnShape = shape + (i,)
        return shape

isRun = True
cli = PapatyaCLI()

while(isRun):
    userInput = input(">>")
    cli.executeCommand(userInput)
