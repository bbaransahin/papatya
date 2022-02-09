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
        print("Couldn't find the layer named as "+name)
        return None
    def findLayerByKind(self, kind):
        for l in self.layers:
            if(l.kind == kind):
                return l
        print("Couldn't find the layer in kind of "+kind)
        return None
    def build(self):
        try:
            self.inputs = self.findLayerByKind("input").kerasLayer
            for l in self.layers:
                if(not l.nextLayer == None):
                    self.connectTwoLayer(l,self.findLayerByName(l.nextLayer))
            self.outputs = self.findLayerByKind("output").kerasLayer
            self.kerasModel = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
            print(self.kerasModel.summary())
        except Exception as e:
            print("There is a problem while building the Papatya Model, here is the error message:")
            print(e)