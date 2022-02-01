#BUG: There is a bug in exit command
import tensorflow as tf

class PapatyaLayer:
    def __init__(self, name, kind, kerasLayer):
        # name is simply id of the layer
        # choose one for kind {"input","hidden","output"}
        self.name = name
        self.kind = kind
        self.kerasLayer = kerasLayer
        self.nextLayer = None
        self.previousLayer = None
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
    def connectTwoLayer(self, pLayer0, pLayer1):
        pLayer1.kerasLayer = pLayer1.kerasLayer(pLayer0.kerasLayer)
    def findLayerByName(self, name):
        for l in self.layers:
            if(l.name == name):
                return l
    def findLayerByKind(self, kind):
        for l in self.layers:
            if(l.kind == kind):
                return l
    def build(self):
        self.inputs = self.findLayerByKind("input").kerasLayer
        for l in self.layers:
            if(not l.nextLayer == None):
                self.connectTwoLayer(l,self.findLayerByName(l.nextLayer))
        self.outputs = self.findLayerByKind("output").kerasLayer
        self.kerasModel = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
        print(self.kerasModel.summary())

class PapatyaCLI:
    def __init__(self):
        print("PapatyaCLI v1")
        self.pModel = PapatyaModel(input("Papatya Model Name: "))
    def executeCommand(self, command):
        command = command.split(' ')
        if(command[0] == "help"):
            pass
        elif(command[0] == "add"):
            if(command[1] == "layer"):
                if(command[2] == "input"):
                    inputs = tf.keras.Input(shape=self.getShape(command[3]))
                    pLayer = PapatyaLayer(input("layer name: "), "input", inputs)
                    self.pModel.addLayer(pLayer)
                elif(command[2] == "dense"):
                    dense = tf.keras.layers.Dense(int(command[3]), activation="relu")
                    pLayer = PapatyaLayer(input("layer name: "), "hidden", dense)
                    self.pModel.addLayer(pLayer)
                elif(command[2] == "output"):
                    output = tf.keras.layers.Dense(int(command[3]), activation="softmax")
                    pLayer = PapatyaLayer(input("layer name: "), "output", output)
                    self.pModel.addLayer(pLayer)
        elif(command[0] == "connect" and command[2] == "to"):
            self.pModel.findLayerByName(command[1]).sendOutputTo(command[3])
            self.pModel.findLayerByName(command[3]).getInputFrom(command[1])
        elif(command[0] == "build"):
            self.pModel.build()
        elif(command[0] == "init"):
            pass
        elif(command[0] == "exit"):
            isRun = False
    def getShape(self, shape):
        shape = shape.split('x')
        returnShape = []
        for i in shape:
            returnShape.append(int(i))
        return returnShape

isRun = True
cli = PapatyaCLI()

while(isRun):
    userInput = input(">>")
    cli.executeCommand(userInput)
