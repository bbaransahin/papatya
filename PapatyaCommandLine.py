#TODO: implement a command that shows the architecture of the model without building it
#TODO: implement a command to edit variables of layers and model

import tensorflow as tf

from PapatyaClasses import PapatyaKernel, PapatyaLayer, PapatyaModel

kernel = PapatyaKernel()
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
                            kernel.addInputLayer(name, self.getShape(command[3]), self.pModel)
                        elif(command[2] == "dense"):
                            name = input("layer name: ")
                            kernel.addDenseLayer(name, int(command[3]), self.pModel)
                        elif(command[2] == "output"):
                            name = input("layer name: ")
                            kernel.addOutputLayer(name, int(command[3]), self.pModel)
                        elif(command[2] == "conv1d"):
                            name = input("layer name: ")
                            kernel.addConv1DLayer(name, int(command[3]), int(command[4]), self.pModel)
                        elif(command[2] == "conv2d"):
                            name = input("layer name: ")
                            kernel.addConv2DLayer(name, int(command[3]), self.getShape(command[4]), self.pModel)
                        elif(command[2] == "flatten"):
                            name = input("layer name: ")
                            kernel.addFlattenLayer(name, self.pModel)
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
                    kernel.editLayer(command[2], self.pModel, command[3], int(command[4]))
            elif(command[0] == "summary"):
                self.pModel.printSummary()
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

cli = PapatyaCLI()

while(True):
    userInput = input(">>")
    if(userInput == "exit"):
        break
    cli.executeCommand(userInput)
