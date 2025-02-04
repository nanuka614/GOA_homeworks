def remove_elements(main_list, indexes_list):
    for index in indexes_list:
        main_list.pop(index)   
    return main_list

main_list = [1, 2, 3, 4, 5, 6]
indexes_list = [2, 3, 1]

result = remove_elements(main_list, indexes_list)
print(result)


def remove_one_element(main_list, index):
    main_list.pop(index) 
    print(main_list) 


main_list = [1, 2, 3, 4, 5]
remove_one_element(main_list, 2)