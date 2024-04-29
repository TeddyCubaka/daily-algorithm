def rgb(red, green, blue):
    color = [red, green, blue]
    hexaColor = []
    for i in color:
        if i >= 255:
            hexaColor.append("ff")
        elif i < 0:
            hexaColor.append("00")
        else:
            color = str(hex(i))
            color = "0" + color[2:]
            hexaColor.append(color[-2:])

    return ("".join(hexaColor)).upper()


print(rgb(148, 0, 211))
