import random
class Produto:
  def __init__(self, nome, valor, serial):
    self._nome = nome
    self._valor = valor
    generate_serial(serial)

  def generate_serial(base):
    key = random.randint(100000, 199999)
    self._serial = key * base


class Quadrinho(Produto):
 def __init__(self, nome, valor, editora, autor):
  super().init(nome, valor, 7)
  self._editora = editora
  self._autor = autor

class Caneca(Produto):
  def __init__(self, nome, valor, capacidade, material):
    super().init(nome, valor, 5)
    self._capacidade = capacidade
    self._material = material

class Camisa(Produto):
  def __init__(self, nome, valor, tamanho, material):
    super().init(nome, valor, 3)
    self._tamanho = tamanho
    self._material = material
