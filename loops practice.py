ip_adresses = []
while True:
    ip = input('what is the ip: ')

    if ip == 'done':
        break
    elif ip == 'print':
        print(ip_adresses)
    else:
        ip_adresses.append(ip)