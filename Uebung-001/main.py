   
def conv(number):
    zahlw = ["Null","ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun","zehn","elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","nuenzehn"]
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

        wort=""
        if (T):
            wort = zahlw[T] + "tausend"
        if (H):
            wort = wort + zahlw[H] + "hundert"
        if (Z == 0):
            wort = wort + zahlw[E]
        elif  Z == 1:
            Z =  number % 100
            wort = wort + zahlw[Z]
        elif (E == 0):
            wort = wort + zehner[Z]          
        elif(Z):
            wort = wort + zahlw[E] + "und" + zahlw[Z] + "zig"
        if  not T and not H and not Z  and E == 1 :
            wort="eins" 
    print (wort)




zahl=int(input("please write your number"))
conv(zahl)