# def main(list_num):
#     """
#     A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
#     Args:
#         list_num (list): parameter
#     Returns:
#         int: return answer
#     """
#     return
def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1=["a","s","d","f","g","h","j","k","l","q"]
    return list1[:n-1:-1]
print(main("list1",3))