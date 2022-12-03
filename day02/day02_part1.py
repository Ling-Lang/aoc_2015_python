

def main():
    input = open("../inputs/02.in")
    input_string = input.read()
    formated_input = input_string.split('\n')
    length = len(formated_input)
    index = 0
    i = 0
    area = []
    while index < length- 1:
        more = formated_input[index].split(('x'))
        index += 1
        area.append(calc_area(int(more[0]), int(more[1]), int(more[2])))
    for ele in range(0, len(area)):
        i  = i + area[ele]
    print(i)
    input.close()


def calc_area(length, width, heigth):
    side1 = length * width
    side2 = width * heigth
    side3 = heigth * length
    sides = [side1, side2, side3]
    area = (2 * side1) + (2 * side2) + (2 * side3)
    sides.sort()
    area = area + sides[0]
    return area

if  __name__ == "__main__":
    main()
else:
    print("Get fucked again idiot :)")
