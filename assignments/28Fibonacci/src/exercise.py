def main():
    index = int(input("Enter the index: "))
    #escribe tu código abajo de esta línea
    i=1
    num1=0
    num2=1
    result=0
    if index!=0 and index!=1:

        while i<=index-1:
            result= num1 + num2
            num1= num2
            num2= result
            i=i+1
        print (str(result))
        pass

    elif index==0:
        print('0')
    elif index==1:
        print('1')

    pass

if __name__ == '__main__':
    main()
