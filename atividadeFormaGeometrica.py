class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base = base
        self.altura = altura
    def calculaArea(self):
       self.area = self.base * self.altura

    def calculaPerimetro(self):
        self.perimetro=2*(self.base + self.altura)

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = (self.base * self.altura) / 2

    def calculaPerimetro(self):
        self.perimetro = 3 * self.base
