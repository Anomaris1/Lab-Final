from sales import Sales


sales_list = []


def menu():
    print()
    print('MENU')
    print('A - Add        M - Display')
    print('D - Delete     S - Search')
    print()

    choice = input('Enter Choice: ')
    choice = choice.lower()
    print()

    if choice == 'a':
        add()
    elif choice == 'm':
        display()
    elif choice == 'd':
        delete()
    elif choice == 's':
        search()
    else:
        print()
        print('Not a choice.')
        menu()


def add():
    while True:
        SN = input('Vehicle Serial Number: ')
        color = input('Vehicle Color: ')
        brand = input('Vehicle Brand: ')
        plate_no = input('Vehicle Plate Number: ')
        price = input('Vehicle Price: ')

        door = input('Number of Doors: ')
        passenger = input('Number of Passenger: ')
        owner = input('Vehicle Owner Name: ')

        qty = input('Vehicle Quantity: ')
        discount = input('Discount(%): ')
        amount = 0

        sales = Sales(qty, discount, amount)
        sales.door = door
        sales.passenger = passenger
        sales.owner = owner
        sales.SN = SN
        sales.color = color
        sales.brand = brand
        sales.plate_no = plate_no
        sales.price = price

        sales_list.append(sales)

        print()
        ans = input('Enter another? [y/n]: ')

        if ans != 'y':
            break

    menu()


def display():
    print()
    print('Sales')
    print('-------------------------------------------------------------------------------')
    print('#    | Owner    | Brand - Color    | Plate#    | QTY    | Price    | Discount    | Total Amount')
    i = 0
    for s in sales_list:
        print(f'{i} \t | {s.owner} \t | {s.getBrandColor()} \t | {s.getPlateNo()} \t | {s.qty} \t | {s.getPrice()} \t | {s.discount}% ({s.computeTotalDiscount()}) \t | {s.computeTotalAmount()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    menu()


def delete():
    print()
    i = int(input('Enter index: '))
    sales_list.pop(i)
    print()
    print('Deleted.')
    menu()


def search():
    i = int(input('Enter index: '))
    print(f'{i} \t | {sales_list[i].owner} \t | {sales_list[i].getBrandColor()} \t | {sales_list[i].getPlateNo()} \t | {sales_list[i].qty} \t | {sales_list[i].getPrice()} \t | {sales_list[i].discount}% \t | {sales_list[i].computeTotalDiscount()}')
    menu()


menu()
