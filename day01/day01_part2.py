def main():
    floor = 0
    index = 0
    f = open("../inputs/01.in")
    str = f.read()
    for element in str:
        if element == "(":
            floor += 1
            index += 1
        if element == ")":
            floor -= 1
            index += 1
        if floor == -1:
            break ;
    print(index)

if __name__ == "__main__":
    main()
else:
    print("Get fucked idiot :)")
