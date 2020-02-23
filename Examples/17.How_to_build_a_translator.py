def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter 
    return translation

print(translate(input("enter a phrase:")))
# =======================
# OUTPUT:
# enter a phrase:Hello
# Hgllg
# =======================

def translate_2(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        elif letter in "AEIOU":
            translation = translation + "G"            
        else:
            translation = translation + letter 
    return translation

print(translate_2(input("enter a phrase:")))
# =======================
# OUTPUT:
# enter a phrase:hello
# hgllg
# enter a phrase:HELLO
# HGLLG
# =======================