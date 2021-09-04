def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea

    for i in range (height+1):
        space=height-i
        a=' '*space+'*'*i
        print(a)



    pass

if __name__ == '__main__':
    main()
