def main():
  #escribe tu código abajo de esta línea

    n=0
    num=float(input(''))
    prom= 0
    
    while num>0:
      prom=prom+num
      n=n+1
      num=float(input(''))

    print(prom/n)

if __name__ == '__main__':
    main()
