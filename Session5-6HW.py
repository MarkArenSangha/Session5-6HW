try:
    gross = float(input("gross: "))
    children = int(input("children: "))
except ValueError:
    print("please enter digits only")
else:
    if gross < 1000:
        tax = 0.10
    elif gross < 2000:
        tax = 0.12
    elif gross < 4000:
        tax = 0.14
    else:
        tax = 0.18

    if gross < 2000:
        tax = tax - (0.01 * children)
    else:
        tax = tax - (0.005 * children)

    if tax < 0:
        tax = 0

    net = gross - (gross * tax)
    print("net:", net)
