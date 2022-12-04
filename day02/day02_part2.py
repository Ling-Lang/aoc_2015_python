def main():
    input = open("../inputs/02.in")
    input_string = input.read()
    formated_input = input_string.split('\n')
    length = len(formated_input)
    index = 0
    f_list = []
    v_list = []
    vol = 0
    feet = 0
    while index < length - 1:
        more = formated_input[index].split(('x'))
        v_list.append(calc_volume(int(more[0]), int(more[1]), int(more[2])))
        more.sort(key=int)
        f_list.append(calc_feet(int(more[0]), int(more[1])))
        index += 1

    for ele in range(0, len(v_list)):
        vol = vol + v_list[ele]
    for elem in range(0, len(f_list)):
        feet = feet + f_list[elem]
    print(feet+vol)
    input.close()

def calc_volume(length, width, heigth):
    vol = length * heigth * width
    return vol
def calc_feet(small_1, small_2):
    feet = small_1 + small_1 + small_2 + small_2
    return feet

if  __name__ == "__main__":
    main()
else:
    print("Get fucked again idiot :)")
