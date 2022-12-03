def main():
    floor = 0
    f = open("../inputs/01.in")
    str = f.read()
    for element in str:
        if element == "(":
            floor += 1
        if element == ")":
            floor -= 1
    print(floor)
    f.close()

if __name__ == "__main__":
    main()
else:
    print("Get fucked idiot :)")
