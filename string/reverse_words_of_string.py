# Reverse words in a given String in Python

# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks  
# Input : str = "my name is laxmi"
# output : str= laxmi is name my 

def reverse_sentence(sent):
    new_set = []
    for word in sent.split(" ")[::-1]:
        new_set.append(word)
    return " ".join(new_set)

if __name__ == "__main__":
    print(reverse_sentence("geeks quiz practice code"))
    print(reverse_sentence("my name is laxmi"))