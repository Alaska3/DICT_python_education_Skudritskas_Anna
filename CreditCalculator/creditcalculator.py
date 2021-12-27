import math

print("Loan principal: 1000")
print("Month 1: repaid 250")
print("Month 2: repaid 250")
print("Month 3: repaid 500")
print("The loan has been repaid!")

print("Enter the loan principal: ")
q = int(input())
print("What do you want to calculate? ")
print("type 'n' - for number of monthly payments,"
      "type 'a' - for annuity monthly payment amount,"
      "type 'p' - for loan principal:")
user1 = input()
if user1 == 'n':
    print("Enter the loan principal: ")
    p = int(input())
    print("Enter the monthly payment: ")
    q_n = int(input())
    print("Enter the loan interest: ")
    l = int(input()) / 1200
    payment = math.ceil(math.log(q_n / (q_n - (l * p), (1 + l))))
    if payment % 12 == 0:
        s = payment // 12
        print("It will take " + str(s) + "months to repay this loan!")
    elif payment % 12 != 0:
        s = payment // 12
        k = payment % 12
        print("It will take " + str(s) + "years and " + str(k) + "months to repay this loan!")
    elif payment // 12 == 0:
        print("It will take " + str(payment) + "years to repay this loan!")
elif user1 == 'a':
    print("Enter the loan principal: ")
    p = float(input())
    print("Enter the number of periods: ")
    n = float(input())
    print("Enter the loan interest: ")
    l = float(input()) / 1200
    i_n = (1 + l) ** n
    a = math.ceil(p * (l * i_n / (i_n - 1)))
    print("Your monthly payment = " + str(a) + "!")
elif user1 == 'p':
    print("Enter the annuity payment: ")
    a = float(input())
    print("Enter the number of periods: ")
    k = float(input())
    print("Enter the loan interest: ")
    l = float(input()) / 1200
    l_k = (1 + l) ** k
    p = round(a / (l * l_k / (l_k - 1)))
    print("Your loan principal = " + str(p) + "!")
