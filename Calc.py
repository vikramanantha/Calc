print('Welcome! This code will help you with your math! Remember to not use decimals or negitives and the operations are:')
print("+ = Addition \n- = Subtraction \n* = Multiplication \n/ = Division \n** = Exponents (to the Power of)")
num1 = input("Type the first number here! ")
num1 = int(num1)
oper = input('Type the operation here!')
num2 = input("Type the second number here! ")
num2 = int(num2)
if oper != '+' and oper != '-' and oper != '*' and oper != '/' and oper != '**': 
    input("You did not type in an operation. Exiting.")
    quit()
elif oper == '/' and num2 == 0:
    input("Sorry, you can't divide numbers by 0 because if you have 10 cookies and no friends, you can't have your non-exictent friends have cookies.")
    quit()


if oper == '+':
    print("You have", num1, "cookie(s) and your friend Bob gave you", num2, "cookie(s). How many cookies do you have now?")
    result = num1 + num2
    result = str(result)
    askresult = input("Type how many cookies you would have now here ")
    if askresult == result:
       input("Yes, that is the correct answer.")
       quit()
    elif askresult != result:
       print("Sorry, the correct answer was", result)
       input("\b")
       quit()

elif oper == '-':
    print("You have", num1, "apple(s) and you ate", num2, "apple(s). How many cookies do you have now?")
    result = num1 - num2
    result = str(result)
    askresult = input("Type how many apple(s) you would have now here ")
    if askresult == result:
       input("Yes, that is the correct answer.")
       quit()
    elif askresult != result:
       print("Sorry, the correct answer was", result)
       input("\b")
       quit()

elif oper == '*':
    print("You have", num1, "child(ren) and you buy him/her/them (each)", num2, "pair(s) of clothes. How many pair(s) of clothes do(es) (s)he/they have now?")
    result = num1 * num2
    result = str(result)
    askresult = input("Type how many pair(s) of clothes your child(ren) have now here ")
    if askresult == result:
       input("Yes, that is the correct answer.")
       quit()
    elif askresult != result:
       print("Sorry, the correct answer was", result)
       input("\b")
       quit()

elif oper == '/':
    print("You have", num1, "child(ren) trying to be crammed into some amount of buses and each bus can hold", num2, "seats. How many buses do you need?")
    result = num1 / num2
    result = str(result)
    askresult = input("Type how many buses you need here ")
    if askresult == result:
       input("Yes, that is the correct answer.")
       quit()
    elif askresult != result:
       print("Sorry, the correct answer was", result)
       input("\b")
       quit()


