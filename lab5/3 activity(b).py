def merge_dicts():
    dict1 = {}
    dict2 = {}

    n1 = int(input("Enter number of elements in first dictionary: "))
    for i in range(n1):
        key = input(f"Enter key {i+1} for dict1: ")
        value = input(f"Enter value for key '{key}': ")
        dict1[key] = value

    n2 = int(input("\nEnter number of elements in second dictionary: "))
    for i in range(n2):
        key = input(f"Enter key {i+1} for dict2: ")
        value = input(f"Enter value for key '{key}': ")
        dict2[key] = value

    merged_dict = {**dict1, **dict2}

    print("\nFirst Dictionary:", dict1)
    print("Second Dictionary:", dict2)
    print("Merged Dictionary:", merged_dict)

# Call the function
merge_dicts()
