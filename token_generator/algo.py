from datas import chars, crypt_chars

def crypter (string):
    letters = [*string]
    crypton = [chars[i] for i in letters]
    return '|-.>__|--|-'.join(crypton)

def decrypter(cryto):
    data_brut = cryto.split('|-.>__|--|-')
    chars_uncoded = [crypt_chars[i] for i in data_brut]
    return ''.join(chars_uncoded)

def game():
    print('Hello. Welcome to my game.')
    string = input('Insert a string to crypt and beggin : ')
    token = crypter(string)
    print('Here is your token : ', token )
    dialog = input('Type a command to countinue. Type ( exit ) to quit :')
    while dialog != 'exit' :
        dialog = input('Type a command to countinue. Type ( exit ) to quit :')
        if dialog == "decrypt my token" : print(decrypter(token))
        if dialog.split(" ")[0] == "decrypt:str " : print(decrypter(dialog.split(" ")[0]))


print(game())