import pyperclip

output = ""

risgravien = ["亜", "贝", "匚", "刀", "巳", "千", "气", "卄", "工", "丁", "开", "乙", "山", "冂", "〇", "卩", "口", "尺", "巛", "十", "凵", "人", "巫", "乂", "丫", "之", "𐌀", "𐌁", "𐌂", "𐌃", "𐌄", "𐌅", "𐌆", "𐌇", "𐌉", "𐌊", "𐌋", "𐌌", "𐌍", "𐌎", "𐌏", "𐌐", "𐌒", "𐌓", "𐌔", "𐌕", "𐌖", "𐌗", "𐌘", "𐌙", "𐌚", "𐌛"]

english = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

mapping = dict(zip(english, risgravien))

while True:
    text = input("Enter a string (:::3#17 to exit): ")

    if text == ":::3#17":
        break

    for character in text:
        if character.isalpha():
            output += mapping.get(character, character)
        else:
            output += character

    print("Converted string (precopied):", output)
    pyperclip.copy(output)
    output = ""