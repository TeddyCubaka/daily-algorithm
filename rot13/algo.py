def rot13(str):
    upper = range(65, 91)
    lower = range(97, 123)
    string = ""
    for l in str:
        if ord(l) in upper or lower:
            interval = upper if ord(l) in upper else lower
            string = string + chr(ord(l)+13 if ord(l)
                                  in interval else ord(l)-26)
        else:
            string = string + l
    return string


print(rot13("teddy"))
