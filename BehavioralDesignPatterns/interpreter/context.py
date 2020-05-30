class Context:

    def __init__(self,input):
        self.input = input
        self.output = 0
    
    def get_input(self):
        return self.input


    def set_input(self,input):
        self.input = input

    
    def get_output(self):
        return self.output

    def set_output(self,output):
        self.output = output

    