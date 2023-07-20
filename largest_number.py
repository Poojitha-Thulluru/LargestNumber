def get_largest_number(nums_array: list) -> str:
    digit_array: list = []
    for index in range(len(nums_array)):
        if len(str(nums_array[index])) > 1:
            while nums_array[index] > 0:
                digit_array.append(str(nums_array[index] % 10))
                nums_array[index] //= 10
        else:
            digit_array.append(str(nums_array[index]))

    digit_array.sort(reverse=True)

    return "".join(digit_array)


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The largest number is : ", get_largest_number(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
