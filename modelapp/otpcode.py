import random


def otp_generator():
    number_list = [x for x in range(5)]
    code_list=[]
    for number in range(5):
        number = random.choice(number_list)
        code_list.append(number)
        code = "".join(str(item) for item in code_list)
    
    return code
