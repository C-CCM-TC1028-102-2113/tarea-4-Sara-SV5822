def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    
    for i in range (height+1):
        if i==0:
            i=i+1
        elif i!=0:
            space=height-i
            a=str(' '*space+'*'*i)
            print(a)


    pass

if __name__ == '__main__':
    main()
