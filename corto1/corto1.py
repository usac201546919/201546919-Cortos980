sec = int(input("Entroduzca un numero"))



while sec != 1:
     if sec%2==0:
         sec=sec/2
         print(sec)
         
     else:
         sec=(sec*3)+1
         print(sec)
         