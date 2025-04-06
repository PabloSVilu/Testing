def convert(number):
   #Se incorpora un diccionario para convertir los números romanos
     result = ""
     romansNumbers = [
          (1, "I"),
          (4, "IV"),
          (5, "V"),
          (9, "IX"),
          (10, "X"),
          (40, "XL"),
          (50, "L"),
          (90, "XC"),
          (100, "C"),
          (400, "CD"),
          (500, "D"),
          (900, "CM"),
          (1000, "M")
     ]
     #Consultar si es que estan los numeros que se proporcionan, O(n^2)
     for value, numeral in reversed(romansNumbers):
         #Se hace un ciclo para recorrer el diccionario y se va restando el valor
         while number >= value:
             number -= value
             result += numeral
     return result