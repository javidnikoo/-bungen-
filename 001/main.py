   
def conv(number):
    numberw = ["Null","ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun","zehn","elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","nuenzehn"]
    zehner = ["","zehn","zwanzig","dreißig","vierzig","fünfzig","sechzig","siebzig","achtzig","neunzig"]
    if number < 0 or number > 9999:
        print("The number is out of the range ")
    else:
        T = int(number / 1000)
        H = int(number / 100)
        H = int( H % 10)
        Z = int(number / 10)
        Z = int( Z % 10)
        E = number % 10

        word=""
        if (T):
            word = numberw[T] + "tausend"
        if (H):
            word = word + numberw[H] + "hundert"
        if (Z == 0):
            word = word + numberw[E]
        elif  Z == 1:
            Z =  number % 100
            word = word + numberw[Z]
        elif (E == 0):
            word = word + zehner[Z]          
        elif(Z):
            word = word + numberw[E] + "und" + numberw[Z] + "zig"
        if  not T and not H and not Z  and E == 1 :
            word="eins" 
    print (word)




input=int(input("please write your number"))
conv(input)