import unittest
from  test import hola

class checar(unittest.TestCase):
    def test_hola(self):
        b = hola("lola", 18)
        self.assertEqual(b,"hola mi nombre es lola y tengo 18")  #compara de que el codigo esta bien 

if __name__ == "__main__":
    unittest.main() 