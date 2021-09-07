def main():
  #escribe tu código abajo de esta línea
    n=int(input('ingresa un numero'))
    num=0

    while num<n:
        num=num+1

        if num%2!=0:
            sig='#'
        elif num%2==0:
            sig='%'

        print(str(num)+'-'+str(sig))




if __name__ == '__main__':
    main()
