import sys
def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    if height!=0:
        for i in range (0,height+1):
            n=0
            k=height
            while k+1>i:
                sys.stdout.write(' ')
                k=k-1
            else: 

                while n<i:
                    sys.stdout.write('*')
                    n=n+1
            print('')
        pass
    elif height==0:
        pass

if __name__ == '__main__':
    main()
