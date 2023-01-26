# Python | Program to check if a string contains any special character

def is_there_special_char(st):
    is_special = False
    for i in st:
        if not i.isalnum():
            is_special = True
            break
    return is_special

if __name__ == "__main__":
    sts = ["shubham@", "Pandey"]
    for st in sts: 
        if is_there_special_char(st):
            print("{0} contains special char".format(st))
        else:
            print("{0} doesn't contain special char".format(st))