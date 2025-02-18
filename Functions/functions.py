class Main:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = 0
        
    
    def suma(self, x, y):
       self.sum += self.a + self.b + x + y
       
   
    def imprimir(self):
       return print(f"{self.sum}")