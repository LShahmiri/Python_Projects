#Defining a list of items
grocery_list=[]

while True:
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Show List')
    print('4. Quit')

    choice= input('Enter choice: ')

    if choice=='1':
        item=input('Enter item: ')
        grocery_list.append(item)
    elif choice=='2':
        item=input('Enter item: ')
        if item in grocery_list:
            grocery_list.remove(item)
        else:
            print('Item does not exict')
    elif choice=='3':
        print('Grocery list: ')
        for item in grocery_list:
            print('- '+item)
    elif choice=='4':
        break
    else:
        print('Invalid choice please select another number.')
        
