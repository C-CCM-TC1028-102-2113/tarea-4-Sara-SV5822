def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea

    for i in range (0,height+1):
        n=0
        k=height
        while k>i:
            print(' ',end='')
            k=k-1
        else: 

            while n<i:
             print('*',end='')
             n=n+1
        print('')
    pass

if __name__ == '__main__':
    main()
