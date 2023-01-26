# Check if string is rotated by two places

def isRotated(a, b):
    rotated_strings =  [ a[2:]+a[:2], a[len(a)-2:]+a[:len(a)-2]]
    if b in rotated_strings:
        print("{} can be obtained by rotating {} 2 places".format(b,a))
    else:
        print("{} can not be obtained by rotating {} 2 places".format(b,a))

if __name__ == "__main__":
    a = "amazon"
    b = "azonam"
    isRotated(a, b)
    a = "geeksforgeeks"
    b = "geeksgeeksfor"
    isRotated(a, b)