# @author: Luiz Henrique Dias Lima

# @func: binary_search
# param: 1st: The list/array containg integer number; 2nd: Initial position; 3rd: End of the list; 4th: The element to be searched
# returns: If the element exists, then the functions returns the position that contains the elemnt 
# if not found, the returns -1
# @cost: O(log N)
# @requirements: The list must be sorted.
def binary_search(p_list, p_left, p_right, p_elem):

    v_middle = (p_left + p_right) // 2
    if p_list[v_middle] == p_elem:
        return v_middle
    # If the element is greater than p_list[v_middle], then it must be on the right 
    elif p_list[v_middle] < p_elem:
        return binary_search(p_list, v_middle + 1, p_right, p_elem)
    # If the element is smaller than p_list[v_middle], then  it must be on the left of the list 
    else:
        return binary_search(p_list, p_left, p_right - 1, p_elem) 

    return -1
if __name__ == "__main__":
    v_size = int(input("Enter the size of the list: "))
    v_list_elem = []

    try:
        for i in range(0, v_size):
            elem = int(input("Enter the value: "))
            v_list_elem.append(elem)

    except ValueError as e:
        print(f"The typed value is not a number {e}")

    v_list_elem.sort()
    try:
        elem_query = int(input("Enter the value to be searched: "))
    except ValueError as e:
        print(f"The typed value is not a number {e}")

    position = binary_search(v_list_elem, 0, len(v_list_elem) - 1, elem_query) 

    if(position > -1):
        print("Element found at position: %d" %position)
    else:
        print("Element not found")    