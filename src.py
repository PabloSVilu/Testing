def convert(number):
   #Se incorpora un diccionario para convertir los números romanos
     result = ""
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
         #Se hace un ciclo para recorrer el diccionario y se va restando el valor
         while number >= value:
             number -= value
             result += numeral
     return result