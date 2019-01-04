while True:
    reply = input('What is your number:')
    if reply == 'stop': break
    print(int(reply)**2)
    print("Bye")

while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!'*8)
    else:
        print(int(reply)**2)
        print('Bye')

while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
        print('Bye')


while True:
    reply = input('Enter text or number: ')
    if  reply == "stop": break
    elif not reply.isdigit():
        print("bad"*8)
    else:
        num = int(reply)
        if num < 20:
            print("low")
        else:
            print(num**2)
    print('bye')


