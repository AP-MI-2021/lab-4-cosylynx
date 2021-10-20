def show_menu():
    print(' ')
    print("1. Introdu listele")
    print("2. Verifică dacă listele au același număr de element pare")
    print("3. Afișează intersecția listelor.")
    print('4. ')
    print("5. Verifică dacă elementele din cele doua liste sunt divizibile cu toate elementele din a treia lista.")
    print("x. ")
    print(' ')


def read_list():
    list_size = int(input("Dați dimensiunea listei: "))
    result_list = []
    while list_size:
        element = int(input("Introduceți un element: "))
        result_list.append(element)
        list_size -= 1
    print(result_list)
    return result_list


def count_even(lst):
    even_elements = 0
    for element in lst:
        if element % 2 == 0:
            even_elements += 1
    return even_elements


def same_ammount_even(list1, list2):
    if count_even(list1) == count_even(list2):
        print("Cele două liste au același număr de elemente pare.")
    else:
        print("Cele două liste au un număr diferit de elemente pare.")

def list_intersection(list1, list2):
    intersection = []
    for element_l1 in list1:
        for element_l2 in list2:
            if element_l1 == element_l2:
                intersection.append(element_l1)
    return intersection

def show_intersection(list1, list2):
    if list_intersection(list1, list2) != []:
        print(f"Intersecția listelor este {list_intersection(list1, list2)}")
    else:
        print("Cele două liste nu au elemente comune.")

def mirror_element(number):
    mirror_number = 0
    while number != 0:
        mirror_number = mirror_number * 10 + number % 10
        number = number // 10
    return mirror_number

def div_by_third_list(list1, list2):
    print("Introdu o a treia listă: ")
    list3 = read_list()
    for element1 in list1:
        divisible = True
        for element3 in list3:
            if element1 % element3 != 0:
                divisible = False
        if divisible:
            element1 = mirror_element(element1)
    for element2 in list2:
        divisible = True
        for element3 in list3:
            if element2 % element3 != 0:
                divisible = False
        if divisible:
            element2 = mirror_element(element2)
    return list1, list2


def main():
    list_1 = []
    list_2 = []
    while True:
        show_menu()
        option = input("Alegeți o opțiune din listă: ")
        print(' ')
        if option == '1':
            print("Introduceți prima listă: ")
            list_1 = read_list()
            print("Introduceți a doua listă: ")
            list_2 = read_list()

        elif option == '2':
            if list_1 != [] and list_2 != []:
                same_ammount_even(list_1, list_2)
            else:
                print("Apăsați 1 și ENTER pentru a introduce valori în ambele liste.")

        elif option == '3':
            if list_1 != [] and list_2 != []:
                show_intersection(list_1, list_2)
            else:
                print("Apăsați 1 și ENTER pentru a introduce valori în ambele liste.")
            
        elif option == '5':
            if list_1 != [] and list_2 != []:
                print(f"Cele două liste prelucrate sunt {div_by_third_list(list_1, list_2)}")
            else:
                print("Apăsați 1 și ENTER pentru a introduce valori în ambele liste.")

        elif option == 'x':
            break

main()