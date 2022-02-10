#TODO: implement a command that shows the architecture of the model without building it
#TODO: implement a command to edit variables of layers and model

import tensorflow as tf

from PapatyaClasses import PapatyaKernel, PapatyaLayer, PapatyaModel

models = []

class PapatyaCLI:
    def __init__(self):
        print("PapatyaCLI v1")
        self.pModel = None
    def executeCommand(self, command):
        command = command.split(' ')
        try:
            if(command[0] == "help"):
                pass
            elif(command[0] == "add"):
                if(command[1] == "layer" or command[1] == "l"):
                    try:
                        if(command[2] == "input"):
                            name = input("layer name: ")
                            self.addInputLayer(name, self.getShape(command[3]))
                        elif(command[2] == "dense"):
                            name = input("layer name: ")
                            self.addDenseLayer(name, int(command[3]))
                        elif(command[2] == "output"):
                            name = input("layer name: ")
                            self.addOutputLayer(name, int(command[3]))
                        elif(command[2] == "conv1d"):
                            name = input("layer name: ")
                            self.addConv1DLayer(name, int(command[3]), int(command[4]))
                        elif(command[2] == "conv2d"):
                            name = input("layer name: ")
                            self.addConv2DLayer(name, int(command[3]), self.getShape(command[4]))
                        elif(command[2] == "flatten"):
                            name = input("layer name: ")
                            self.addFlattenLayer(name)
                        else:
                            print("couldn't find a layer classified as "+command[2]+", please try something else.")
                    except Exception as e:
                        print("There is a problem while creating or adding the layer, here is the error message:")
                        print(e)
            elif((command[0] == "connect" or command[0] == "c") and command[2] == "to"):
                try:
                    self.pModel.findLayerByName(command[1]).sendOutputTo(command[3])
                    self.pModel.findLayerByName(command[3]).getInputFrom(command[1])
                except Exception as e:
                    print(e)
            elif(command[0] == "build"):
                self.pModel.build()
            elif(command[0] == "list"):
                if(command[1] == "layers"):
                    for layer in self.pModel.layers:
                        print(layer.name, layer.kind)
                else:
                    print("Invalid command please try something else")
            elif(command[0] == "create"):
                if(command[1] == "model"):
                    model = PapatyaModel(input("model name: "))
                    models.append(model)
            elif(command[0] == "set"):
                if(command[1] == "model"):
                    for m in models:
                        if(m.name == command[2]):
                            self.pModel = m
            elif(command[0] == "edit"):
                if(command[1] == "layer" or command[1] == "l"):
                    for l in self.pModel.layers:
                        pass
            else:
                print("Invalid command please try something else")
        except Exception as e:
            print(e)
    def getShape(self, shape):
        shape = shape.split('x')
        returnShape = []
        for i in shape:
            returnShape.append(int(i))
        return tuple(returnShape)
    def addInputLayer(self, name, shape):
        kerasInput = tf.keras.Input(shape=shape)
        pLayer = PapatyaLayer(name, "input", kerasInput)
        self.pModel.addLayer(pLayer)
    def addDenseLayer(self, name, units):
        kerasDense = tf.keras.layers.Dense(units)
        pLayer = PapatyaLayer(name, "hidden", kerasDense)
        self.pModel.addLayer(pLayer)
    def addOutputLayer(self, name, units):
        kerasDense = tf.keras.layers.Dense(units)
        pLayer = PapatyaLayer(name, "output", kerasDense)
        self.pModel.addLayer(pLayer)
    def addConv1DLayer(self, name, filters, kernel_size):
        kerasConv1D = tf.keras.layers.Conv1D(filters, kernel_size)
        pLayer = PapatyaLayer(name, "hidden", kerasConv1D)
        self.pModel.addLayer(pLayer)
    def addConv2DLayer(self, name, filters, kernel_size):
        kerasConv2D = tf.keras.layers.Conv2D(filters, kernel_size)
        pLayer = PapatyaLayer(name, "hidden", kerasConv2D)
        self.pModel.addLayer(pLayer)
    def addFlattenLayer(self, name):
        kerasFlatten = tf.keras.layers.Flatten()
        pLayer = PapatyaLayer(name, "hidden", kerasFlatten)
        self.pModel.addLayer(pLayer)

cli = PapatyaCLI()

while(True):
    userInput = input(">>")
    if(userInput == "exit"):
        break
    cli.executeCommand(userInput)
