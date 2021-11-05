inpt = input("Please enter an email:\n")
def is_email(email):
    y = 0
    z = 0
    for x in email:
        if x == "@":
            y += 1
        elif x == ".":
            z += 1
    if z >= 1 and y >= 1:
        return True
    else:
        return False
print(is_email(inpt))