def convert(number):
   romans = {
        4: "IV",
        5: "V",
        10: "X",
   }
   if number in romans:
    return romans[number]
   else:
    return "I" * number
 

 
    