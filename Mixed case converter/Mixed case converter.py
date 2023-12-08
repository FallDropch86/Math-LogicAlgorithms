import time

def mixed_case(userinpt):
    result = ""
    for index, char in enumerate(userinpt):
        if index % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

print("Mixed case example : Hello World! -> hElLo wOrLd!")

user_input = input("Enter the sentence you would like to change into mixed case: ")

print(mixed_case(user_input))

time.sleep(1000)
