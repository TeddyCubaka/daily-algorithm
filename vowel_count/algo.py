# to remove all vowel in a sentence

def remove_vowel(sentence):
    return "".join([i for i in [*sentence] if i not in ["a", "e", "i", "o", "u"]])

def get_count(sentence):
    return len([i for i in sentence if i in "aeiou"])
