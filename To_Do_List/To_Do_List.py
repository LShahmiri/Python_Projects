tasks=[] # Create an empty list to store tasks

while True:
    print('1. Add task ')
    print('2. Remove task')
    print('3. Show list')
    print('4. quit')


    choice=input('Enter choice: ')
    if choice=='1':
        task=input('Enter task: ')
        tasks.append(task) # Add task to the top of the list
    elif choice=='2':
        task=input('Enter task: ') # Remove a task from the list
        if task in tasks:
            tasks.remove(task)
        else:
            print('Task not found.')
    elif choice=='3':
        print( 'To Do list is ')
        for task in tasks:
            print('- '+ task) # Displey the list
    elif choice=='4':
        break # Exit the loop
    else:
        print('Invalid choice, try again')
    

