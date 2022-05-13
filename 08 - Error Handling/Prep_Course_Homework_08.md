## Manejo de errores

1) Con la clase creada en el módulo 7, tener en cuenta diferentes casos en que el código pudiera arrojar error. Por ejemplo, en la creación del objeto recibimos una lista de números enteros pero ¿qué pasa si se envía otro tipo de dato?

    from Metodos import *
    m = Metodos('hola')

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    c:\Users\tacas\Documents\HENRY\Python-Prep\08 - Error Handling\Prep_Course_Homework_08-Resuelto.ipynb Cell 5' in <cell line: 1>()
    ----> 1 m = Metodos('hola')

    File c:\Users\tacas\Documents\HENRY\Python-Prep\08 - Error Handling\Metodos.py:8, in Metodos.__init__(self, lista)
        6 def __init__(self,lista):
        7     if(type(lista) != list):
    ----> 8         raise ValueError("El valor ingresado no es de tipo 'List' ") 
        9     else:
        10         self.lista = lista

    ValueError: El valor ingresado no es de tipo 'List' 

2) En la función que hace la conversión de grados, validar que los parámetros enviados sean los esperados, de no serlo, informar cuáles son los valores esperados.

    m1 = Metodos([2,3,5,6,2])
    m1.lista_Conversion_grados(1,2)


3) Importar el modulo "unittest" y crear los siguientes casos de pruebas sobre la clase utilizada en el punto 2<br>
Creacion del objeto incorrecta<br>
Creacion correcta del objeto<br>
Metodo valor_modal()<br>

Se puede usar "raise ValueError()" en la creación de la clase para verificar el error. Investigar sobre esta funcionalidad.

    import unittest
    class ProbandoMiClase(unittest.TestCase):
    
    def test_crear_objeto1(self):
        param = 'hola'
        self.assertRaises(ValueError, Metodos, param)
        #self.failUnlessRaises(ValueError, h.Herramientas, param)

    def test_crear_objeto2(self):
        param = [1,2,2,5]
        h1 = Metodos(param)
        self.assertEqual(h1.lista, param)

    def test_valor_modal(self):
        lis = [1,2,1,3]
        h1 = Metodos(lis)
        moda = h1.encontrarMayorRepetido(False)
        resultado = "el numero que mas se repite es el "+str(1)+" con "+str(2)+" repeticiones"
        self.assertEqual(moda, resultado)

4) Probar una creación incorrecta y visualizar la salida del "raise"

    h2 = Metodos('algo')

6) Agregar casos de pruebas para el método verifica_primos() realizando el cambio en la clase, para que devuelva una lista de True o False en función de que el elemento en la posisicón sea o no primo

    class ProbandoMiClase2(unittest.TestCase):

    def test_verifica_primos1(self):
        lis = [2,3,8,10,13]
        h1 = Metodos(lis)
        primos = h1.lista_esPrimo()
        primos_esperado = [True, True, False, False, True]
        self.assertEqual(primos, primos_esperado)
    
    unittest.main(argv=[''], verbosity=2, exit=False)

7) Agregar casos de pruebas para el método conversion_grados()

    class ProbandoMiClase3(unittest.TestCase):
        def test_verifica_conversion1(self):
            lis = [2,3,8,10,13]
            h1 = Metodos(lis)
            grados = h1.lista_Conversion_grados('celsius','farenheit')
            grados_esperado = [35.6, 37.4, 46.4, 50.0, 55.4]
            self.assertEqual(grados, grados_esperado)

8) Agregar casos de pruebas para el método factorial()

    class ProbandoMiClase4(unittest.TestCase):

        def test_verifica_factorial(self):
            lis = [2,3,8,10,13]
            h1 = Metodos(lis)
            factorial = h1.lista_Factorial()
            factorial_esperado = [2, 6, 40320, 3628800, 6227020800]
            self.assertEqual(factorial, factorial_esperado)

9) Completar el código en las funciones del archivo "checkpoint.py" y probarlo a partir de la ejecución del script "tests.py"
    
