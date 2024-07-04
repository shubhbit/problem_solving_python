# Input: ["flower","flow","flight"]
# Output: "fl"

def longest_common_prefix(input_list):
    common_prefix = ""
    for indx, i in enumerate(input_list[0]):
        if False in [False for word in input_list if word[indx]!=i]:
            break
        else:
            common_prefix += i
    return common_prefix

if __name__ == "__main__":
    inp = ["flower","flow","flight"]
    print(longest_common_prefix(inp))
    inp = ["flower","flow","floight"]
    print(longest_common_prefix(inp))