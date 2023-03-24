"Displaying a Barchart"
L = [5,10,4,16,19,3]

print(f'Index{"Value":>8}   Bar')
for index, value in enumerate ( L ):
    print(f'{index:>5}{value:>8}   {"*" * value}')