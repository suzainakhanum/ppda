def merge_dicts_add_values():
    dict1 = {}
    dict2 = {}

    n1 = int(input("Enter number of elements in first dictionary: "))
    for i in range(n1):
        key = input(f"Enter key {i+1} for dict1: ")
        value = int(input(f"Enter integer value for key '{key}': "))
        dict1[key] = value

    n2 = int(input("\nEnter number of elements in second dictionary: "))
    for i in range(n2):
        key = input(f"Enter key {i+1} for dict2: ")
        value = int(input(f"Enter integer value for key '{key}': "))
        dict2[key] = value

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Add values for overlapping keys
        else:
            merged_dict[key] = value

    print("\nFirst Dictionary:", dict1)
    print("Second Dictionary:", dict2)
    print("Merged Dictionary (with summed overlapping values):", merged_dict)

# Call the function
merge_dicts_add_values()
