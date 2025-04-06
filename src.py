def convert(number):
     result = ""
     #Se incorpora un diccionario para convertir los números romanos
     #Notar que es clave que se comience desde el número más grande al más pequeño, para formar el número como corresponde 
     romansNumbers = [
          (1000,"M"),
          (900,"CM"),
          (500,"D"),
          (400,"CD"),
          (100,"C"),
          (90,"XC"),
          (50,"L"),
          (40,"XL"),
          (10,"X"),
          (9,"IX"),
          (5,"V"),
          (4,"IV"),
          (1,"I")
     ]
     #Consultar si es que estan los numeros que se proporcionan
     for value, numeral in romansNumbers:
         #Se hace un ciclo para recorrer el diccionario entonces a medida que encuentre un valor menor al número entero
         #se le resta el valor al número entero y se le suma el número romano al resultado, de esta forma se va formando el número romano
         #por cada nueva iteración.
         while number >= value:
             number -= value
             result += numeral
     return result