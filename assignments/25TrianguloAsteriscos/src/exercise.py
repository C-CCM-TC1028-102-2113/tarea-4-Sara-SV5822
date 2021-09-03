import sys
def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    if height!=0:
        for i in range (0,height):
            n=0
            k=height
            while k>i+1:
                sys.stdout.write(' ')
                k=k-1
            else: 

                while n<i+1:
                    sys.stdout.write('*')
                    n=n+1
            print('')
        pass
    elif height==0:
        pass

if __name__ == '__main__':
    main()
