# Jasmine San Juan
# CECS 378 Lab 1
import random
import enchant
#pip install pyenchant

d = enchant.Dict("en_US")

print("Welcome to the Crack tool")
text = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"
mover = 0
key = ''
atp = 0


def shift_cipher_decode(string, n):
    new_string = ''
    for string_char in string:
        temp = 0
        #check for what type of char and how to modify
        if string_char.isalpha():
            temp = ord(string_char)
            temp = temp - n
            temp = temp % 122
            if string_char.isupper():
                if temp < 65:
                    temp += 26
            if string_char.islower():
                # temp += 96
                if temp < 97:
                    temp += 26
            new_string += chr(temp)
            # print(temp)
        else:
            new_string += string_char
    return (new_string)


def SubCiph(string, key):
    spechr = '?,.! -:;@#$%^&*(){}|"<>/_+='
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alphaf = alpha + alpha.upper() + spechr
    keyf = key + key.upper() + spechr
    output = ''
    for x in string:
        output += keyf[alphaf.find(x)]
    # print(output)
    # outputf.writelines(output + '\n')
    return (output)

#generates an Alpha Key
def rndmr(key):
    lmao = list(key)
    random.shuffle(lmao)
    lmao = ''.join(lmao)
    return (lmao)

#mods the Key to have specific chars in specific locations
def keymod(text, key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    letterlst = []
    lettercnt = []
    text = text.lower()
    #indexes char freq
    for i in text:
        if i.isalpha():
            if i in letterlst:
                x = letterlst.index(i)
                lettercnt[x] += 1
                pass
            else:
                letterlst.append(i)
                lettercnt.append(1)
        else:
            pass
    #missing Letters
    for h in alpha:
        if h in letterlst:
            pass
        else:
            letterlst.append(h)
            lettercnt.append(0)

    finalz = list(zip(lettercnt, letterlst))
    finalz.sort(reverse=True)
    #Rearanges specific letters
    lrgval = finalz[0][1]
    lowz = finalz[-1][1]
    lowj = finalz[-2][1]
    lowq = finalz[-3][1]

    keyz = list(key)
    z = keyz.index(lowz)
    x = keyz.index(lrgval)
    j = keyz.index(lowj)
    q = keyz.index(lowq)
    keyz[4], keyz[x] = keyz[x], keyz[4] #finds the bigest and makes it 'e's position
    keyz[9], keyz[j] = keyz[j], keyz[9]
    keyz[15], keyz[q] = keyz[q], keyz[15]
    keyz[25], keyz[z] = keyz[z], keyz[25]
    keyz = ''.join(keyz)
    return(keyz)


print('\nType in the number of your choice\n 1) ShiftCipher\n 2) SubsitutionCipher\n')
choice = input("input number:")
text = input("\nenter encrypted text:")

if choice == '1':
    for i in range(26):
        tmp = 0
        # print(i,shift_cipher_decode(text, i))
        chunk = shift_cipher_decode(text, i).split(' ')
        for word in range(len(chunk)):
            if d.check(chunk[word]) == True:
                tmp += 1
                if tmp == 1:
                    print("Potential word found in shift:", i, chunk[word])
                    print(shift_cipher_decode(text, i), "\n")
                else:
                    pass
elif choice == '2':
    key = 'abcdefghijklmnopqrstuvwxyz'
    # Text = ''
    i = 0
    atp = 0
    mover == 0
    while mover != 1:
        i = 0
        while i <= 0:
            keyr = key = keymod(text,rndmr(key))
            out = SubCiph(text, keyr)
            outs = SubCiph(text, keyr).split(' ')
            # debug
            # keyr = key
            # testa = "fgsd erwt help gsdf trwa low fgds"
            # testb = testa.split(' ')

            for word in range(len(outs)):
                # print(d.check(outs[word]), outs)
                if d.check(outs[word]) == True:
                    print("\n\nword found:\t" + outs[word])
                    print("Key:\t" + keyr)
                    print("Text:\t" + out)
                    i += 1
                    # mover = 'no'
                    mover = input("\n Is this what you were Looking for? To run again type the number 1 else 0: ")
                else:
                    atp += 1
                    #print("attempt:\t" + str(atp))

print('\n Good Bye!!')
