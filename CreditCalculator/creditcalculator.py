import math
print("Loan principal: 1000")
print("Month 1: repaid 250")
print("Month 2: repaid 250")
print("Month 3: repaid 500")
print("The loan has been repaid!")

print("Enter the loan principal: ")
q = int(input())
print("What do you want to calculate? ")
print("type 'm' - for number of monthly payments,"
      "type 'p' - for the monthly payment:")
user1 = input()
if user1 == 'm':
    print("Enter the monthly payment: ")
    q_m = int(input())
    payment = math.ceil(q/q_m)
    print("It will take " + str(payment) + " months to repay the loan")
else:
    print("Enter the monthly payment: ")
    q_n = int(input())
    payment1 = math.ceil(q / q_n)
    last_payment = q - (q_n - 1) * payment1
    if last_payment == payment1:
        print("Your monthly payment = " + str(payment1))
    else:
        print("Your monthly payment = " + str(payment1) + "and the last payment = " + str(last_payment))
