print('In getpass')
i = input('Enter any key:')
try:
    import getpass
    p = getpass.getpass(prompt = 'Enter:')
    print(f'Got password:{p}')
    i = input('Enter any key:')
except Exception as e:
    print("Can't Open")
    print(e)
    i = input('Enter any key:')
    
