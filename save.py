def full(surname, name, phone, note, orient):
    if orient == '1':
        file = open('vertikal.csv', 'a')
        file.write(f'{surname}\n{name}\n{phone}\n{note}\n\n')
        file.close()
    if orient == '2':
        with open('horizont.csv', 'a') as file:
            file.write(f'{surname};{name};{phone};{note}\n\n')
            file.close()