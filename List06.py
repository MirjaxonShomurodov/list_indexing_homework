def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    n=True
    list1=[0,1,0,1,0]
    list1[0]=n
    list1[4]=n
    return list1
print(main("list1"))