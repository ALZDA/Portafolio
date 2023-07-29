#def es_primo(numero):
    #contador = 0

   # for i in range (1, numero + 1):
        #if i == 1 or i == numero:
            #continue
        #if numero % i == 0:
            #contador+= 1
    #if contador == 0:
        #return True
    #else:
       # return False


#Pasos para definir si un número es primo o no 

def es_primo(numero):
     for i in range(2,int(numero**0.5)+1):
        if numero % i == 0: 
            return False
        else:
            return True
        

def run ():
    numero = int(input("Escribe un número: "))
    if es_primo(numero):
        print ("Es primo")
    else:
       print("No es primo")
    #numero = int(input("Escribe un número: "))
    #if es_primo(numero):
        #print ("Es primo")
    #else:
       # print("No es primo")

if __name__ == "__main__":
    run()