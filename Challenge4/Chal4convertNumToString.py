def convertNumToString(n):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    zerotoTwenty = ["", "one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","Fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    bignumber = ["","hundred", "thousand", "Million"]
    #print(len(str(n)))
    #print(bignumber[2])
    if n == 0:
        numberinword = numberzero(n)
        return numberinword
    elif n<=19:
        numberinword = numberlessthantwenty(n)
        return numberinword
    elif n<=99:
        numberinword = numberlessthanhundred(n)
        return numberinword
    elif n<=999:
        numberinword = numberlessthanthousand(n)
        return numberinword
    elif n<=999999:
        numberinword = numberlessthanmillion(n)
        return numberinword
    elif n == 1000000:
        return("One" + " " + bignumber[3])
    else:
        return("Invalid Number: Number must be less than or equal to one Million")
####
def numberzero(n):
    answer = "zero"
    return answer
####
def numberlessthantwenty(n):
    zerotoTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "Fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return (zerotoTwenty[n])
#####
def numberlessthanhundred(n):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    zerotoTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "Fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    number = str(n)
    if number[1] == 0:
        return(tens[int(number[0])])
    else:
        return(tens[int(number[0])] + " " + zerotoTwenty[int(number[1])])
#######
def numberlessthanthousand(n):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    zerotoTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "Fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    bignumber = ["", "hundred", "thousand", "Million"]
    number = str(n)
    if number[-2:] == "00":
        return(zerotoTwenty[int(number[0])] + " " + bignumber[1])
    elif int(number[-2:]) < 20:
        return(zerotoTwenty[int(number[0])] + " " + bignumber[1] + " " + zerotoTwenty[int(number[-2:])])
    else:
        return(zerotoTwenty[int(number[0])] + " " + bignumber[1] + " " + tens[int(number[1])] + " " + zerotoTwenty[int(number[2])])
#####
def numberlessthanmillion(n):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    zerotoTwenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "Fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    bignumber = ["", "hundred", "thousand", "Million"]
    number = str(n)
    n1 = number[:-3]
    n2 = number[-3:]
    if n2 == "000":
        x = ""
    elif int(n2) < 20:
        x = numberlessthantwenty(int(n2))
    elif int(n2) <= 99:
        x = numberlessthanhundred(int(n2))
    elif int(n2) <= 999:
        x = numberlessthanthousand(int(n2))

    if int(n1) < 20:
        y = numberlessthantwenty(int(n1))
    elif int(n1) <= 99:
        y = numberlessthanhundred(int(n1))
    elif int(n1) <= 999:
        y = numberlessthanthousand(int(n1))

    return(y + " " + bignumber[2] + " " + x)