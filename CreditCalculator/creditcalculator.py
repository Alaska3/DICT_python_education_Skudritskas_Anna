import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--annuity')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--interest')
parser.add_argument('--periods')

arg = parser.parse_args()

arg_arg_type = arg.type
arg_principal = arg.principal
arg_interest = arg.interest
arg_annuity = arg.annuity
arg_payment = arg.payment
arg_periods = arg.periods

print(arg_principal, arg_interest, arg_annuity, arg_periods, arg_payment, arg_arg_type)


# --principal --interest --periods
def a_f():
    principal = int(arg_principal)
    period = int(arg_periods)
    percent = float(arg_interest)
    interest = percent / (12 * 100)

    annuity = principal * ((interest * pow((1 + interest), period)) / (pow((1 + interest), period) - 1))
    over = math.ceil(annuity) * period - principal

    print(f'Your arg_annuity payment: {math.ceil(annuity)}')
    print(f'Overpayment: {over}')


# --principal --payment --interest
def func2():
    principal = int(arg_principal)
    payment = int(arg_payment)
    percent = float(arg_interest)
    interest = percent / (12 * 100)

    if percent:
        x = int(payment) / (int(payment) - (interest / 1200 * int(principal)))
        print(x)
        degree = math.log(int(payment) / (int(payment) - (interest * principal)), (1 + interest))
        year = math.ceil(degree) / 12
        r = str(round(year, 1))
        print(f"It will take {list(r)[0]} years and {list(r)[2]} months to repay this loan")
        print(f"Overpayment: {principal * math.ceil(degree) - int(principal)}", )
    else:
        print("Incorrect parameters")


# --periods --payment --interest
def func3():
    period = float(arg_periods)
    payment = float(arg_payment)
    percent = float(arg_interest)
    if percent != arg_interest:
        percent = float(arg_interest)
        i = percent / (12 * 100)
        num = pow(1 + i, float(period))
        a = i * (1 + i) ** float(period)
        b = (1 + i) ** float(period) - 1
        c = a / b
        d = float(payment) / c
        result = math.floor(float(float(arg_payment) / ((i * num) / (num - 1))))
        print(f"Your loan principal: { round(d)}")
        print(f'Overpayment: {float(payment) * float(period) - result}')
    else:
        print("Incorrect parameters")


# --principal --periods --interest:
def func4():
    principal = int(arg_principal)
    periods = int(arg_periods)
    interest = float(arg_interest)
    total = 0
    i = interest / (100 * 12)
    for m in range(1, periods + 1):
        paidout = principal / periods + i * (principal - principal * (m - 1) / periods)
        total += math.ceil(paidout)
        print(f'Month {m}: paid out {math.ceil(paidout)}')
    overpay = total - periods
    print(f'Overpayment = {overpay}')


if __name__ == "__main__":
    if arg_arg_type == "annuity":
        if arg_principal and arg_interest and arg_periods:
            a_f()
        elif arg_principal and arg_payment and arg_interest:
            func2()
        elif arg_periods and arg_payment and arg_interest:
            func3()
        else:
            print("Incorrect parameters")
    elif arg_arg_type == "diff":
        if arg_principal and arg_periods and arg_interest:
            func4()
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")