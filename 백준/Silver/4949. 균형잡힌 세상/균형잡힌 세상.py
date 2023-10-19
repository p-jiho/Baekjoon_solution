
def bracket(str):
    if str == "(" or str == ")" or str == "[" or str == "]" or str == ".":
        return str


while(True):
    str = input()
    if str == ".":
        break

    result = list(filter(bracket, list(str)))

    x = []
    for brac in result:
        if  brac == "(" or brac == "[":
            x.append(brac)
        elif brac == ")":
            if len(x) == 0 or x[-1] != "(":
                print("no")
                break
            else:
                del x[-1]
        elif brac == "]":
            if len(x) == 0 or x[-1] != "[":
                print("no")
                break
            else:
                del x[-1]
        elif brac == ".":
            if len(x) == 0:
                print("yes")
                break
            else:
                print("no")
                break