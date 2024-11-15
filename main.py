from functions import *

def call_all_functions():
    """Шаг 19: Вызов всех функций из functions.py."""
    lst = [1, 2, 3, 4, 5]
    reversed_lst = reverse_list(lst)
    print(f"Reversed list: {reversed_lst}")

    modified_lst = modify_list(lst, [10, 20])
    print(f"Modified list: {modified_lst}")

    lists_are_equal = compare_lists([1, 2], [1, 2], [1, 2])
    print(f"Lists are equal: {lists_are_equal}")

    range_lst = select_range(lst, 1, 4)
    print(f"Selected range: {range_lst}")

    new_lst = create_list(6, 7, 8)
    print(f"Created list: {new_lst}")

    inserted_lst = insert_into_list(lst, 2, 99)
    print(f"List after insertion: {inserted_lst}")

    merged_sorted_lst = merge_and_sort([1, 3, 2], [5, 4], reverse=True)
    print(f"Merged and sorted list: {merged_sorted_lst}")

    random_lst = create_random_list()

    threshold_lst = append_with_threshold(lst, [10, 11], [12, 13], threshold=5)
    print(f"Thresholded list: {threshold_lst}")

    sorted_by_length = sort_list_by_length(["abc", "a", "abcd"])
    print(f"Sorted by length: {sorted_by_length}")

    min_val = extract_min(lst)
    print(f"Extracted min value: {min_val}")

    summed_tuples = sum_tuples((1, 2), (3, 4))
    print(f"Summed tuples: {summed_tuples}")

    element_types = tuple_element_types(1, "a", 3.14)
    print(f"Tuple element types: {element_types}")

    is_present = is_element_in_tuple((1, 2, 3), 2)
    print(f"Element present: {is_present}")

    keys = get_dict_keys({"a": 1, "b": 2})
    print(f"Dict keys: {keys}")

if __name__ == "__main__":
    call_all_functions()
