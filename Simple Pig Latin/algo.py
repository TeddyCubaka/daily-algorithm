def pig_it(text):
    output = []
    for i in text.split(" ") :
        if i.lower() not in list(map(chr, range(97, 123))) and len(i) == 1 : output.append(i[1:] + i[0])
        else : output.append(i[1:] + i[0]  + "ay")
    return " ".join(output)
