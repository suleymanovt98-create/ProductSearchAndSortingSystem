from functions import *


def show_menu():
    print("================================")
    print("     MINI PRODUCT SYSTEM")
    print("================================")
    print()
    print("1. Butun mehsullari goster")
    print("2. Qiymete gore artan sirala")
    print("3. Qiymete gore azalan sirala")
    print("4. Mehsulu adina gore axtar")
    print("5. Mehsulu ID ile axtar")
    print("6. En ucuz mehsulu tap")
    print("7. En bahali mehsulu tap")
    print()
    print("0. Proqramdan cix")
    print()
    print("================================")


while True:
    show_menu()
    choice = input("Secim: ")

    if choice == "1":
        showproducts()

    elif choice == "2":
        sortbypriceasc()

    elif choice == "3":
        sortbypricedesc()

    elif choice == "4":
        searchbyname()

    elif choice == "5":
        searchbyid()

    elif choice == "6":
        getcheapestproduct()

    elif choice == "7":
        getexpensiveproduct()

    elif choice == "0":
        print("Proqram baglandi")

        break
    else:
        print("Yanlis secim")

    print()