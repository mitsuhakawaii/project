########## differentiation calculater.... ##########

print "input ex)2x...3x... 4x^2"
import string
number = str(raw_input("> "))
if(number.count('^')==1):
    if(number.count('x')==1):
        n2 = number.find('x')
        n = number.find('^')
        two = number[n + 1:len(number)]
        first = number[0:n]
        three = number[0:n2]
        three = int(three)
        two = int(two)
        two2 = two - 1
        if two2==1:
            print  "result : %s" %str(two*three)+"x"
        else:
            result = str(two * three)
            result2 = result + "x" + "^"+str(two2)
            print "result : %s" %result2

    else:
        print "result : 0"


elif(number.count('x')==1):
    print ''.join(number.split('x'))
elif(number=="x"):
    print "result : 1"

else:
    print "result : 0"
