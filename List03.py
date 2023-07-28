def main(list1,list2):
    """
    lists list1 and list2 are given. Add them (combine) and return.
    Args:
        list1 (list): parameter
        list2 (list): parameter
    Returns:
        list: return answer
    """
    list1=[1,6,3,9]
    list2=[9,5,'hi',10]
    list=list1+list2
    return list
print(main(list1=[1,6,3,9],list2=[9,5,'hi',10]))