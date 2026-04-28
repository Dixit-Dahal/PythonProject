password = input('Enter you secret password:').lower()

SecretPass = password.maketrans('aeios', '@3!0$')

print(f'Your secret agent password is: {password.translate(SecretPass)}')