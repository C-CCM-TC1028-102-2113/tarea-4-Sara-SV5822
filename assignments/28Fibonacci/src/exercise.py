def main():
    index = int(input("Enter the index: "))
    #escribe tu código abajo de esta línea

    num1=0
    num2=1
    result=0
    if index!=0 and index!=1:

        for i in range (1,index):
            result= num1 + num2
            num1= num2
            num2= result
        print (str(result))

    elif index==0:
        print('0')
    elif index==1:
        print('1')

    pass

if __name__ == '__main__':
    main()
