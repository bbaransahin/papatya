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
        self.setParameters()
        self.isConnected = False
    def sendOutputTo(self, nextLayer):
        self.nextLayer = nextLayer
    def getInputFrom(self, previousLayer):
        self.previousLayer = previousLayer
    def setParameters(self):
        pass

class PapatyaModel:
    def __init__(self, name):
        print("A PapatyaModel named "+name+" is initialized.")
        self.name = name
        self.layers = []
        self.kerasModel = None
    def addLayer(self, pLayer):
        self.layers.append(pLayer)
    def connectTwoLayer(self, pLayer0, pLayer1):
        pLayer1.kerasLayer = pLayer1.kerasLayer(pLayer0.kerasLayer)
        pLayer1.isConnected = True
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
            if(self.inputs == None):
                return None
            for l in self.layers:
                if(not l.nextLayer == None):
                    self.connectTwoLayer(l,self.findLayerByName(l.nextLayer))
            self.outputs = self.findLayerByKind("output").kerasLayer
            if(not self.outputs == None):
                self.kerasModel = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
            else:
                self.kerasModel = tf.keras.Model(inputs=self.inputs, outputs=l)
            print(self.kerasModel.summary())
        except Exception as e:
            print("There is a problem while building the Papatya Model, here is the error message:")
            print(e)

class PapatyaKernel:
    def __init__(self):
        print("papatya kernel initialized")
    def addInputLayer(self, name, shape, model):
        kerasInput = tf.keras.Input(shape=shape, name=name)
        pLayer = PapatyaLayer(name, "input", kerasInput)
        model.addLayer(pLayer)
    def addDenseLayer(self, name, units, model):
        kerasDense = tf.keras.layers.Dense(units, name=name)
        pLayer = PapatyaLayer(name, "hidden", kerasDense)
        model.addLayer(pLayer)
    def addOutputLayer(self, name, units, model):
        kerasDense = tf.keras.layers.Dense(units, name=name)
        pLayer = PapatyaLayer(name, "output", kerasDense)
        model.addLayer(pLayer)
    def addConv1DLayer(self, name, filters, kernel_size, model):
        kerasConv1D = tf.keras.layers.Conv1D(filters, kernel_size, name=name)
        pLayer = PapatyaLayer(name, "hidden", kerasConv1D)
        model.addLayer(pLayer)
    def addConv2DLayer(self, name, filters, kernel_size, model):
        kerasConv2D = tf.keras.layers.Conv2D(filters, kernel_size, name=name)
        pLayer = PapatyaLayer(name, "hidden", kerasConv2D)
        model.addLayer(pLayer)
    def addFlattenLayer(self, name, model):
        kerasFlatten = tf.keras.layers.Flatten(name=name)
        pLayer = PapatyaLayer(name, "hidden", kerasFlatten)
        model.addLayer(pLayer)
    def editLayer(self, name, model, variable_name, new_value):
        if(model.kerasModel == None and (not model.findLayerByName(name).isConnected)):
            code  = "model.findLayerByName(\""+name+"\").kerasLayer."+variable_name+"="+str(new_value)
            exec(code)
        elif(model.kerasModel == None and model.findLayerByName(name).isConnected):
            for l in model.kerasModel.layers:
                if(l.name == name):
                    pass
        elif(not model.kerasModel == None):
            pass