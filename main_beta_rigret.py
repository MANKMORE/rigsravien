import tkinter as tk
import pyperclip


risgravien = ["亜", "贝", "匚", "刀", "巳", "千", "气", "卄", "工", "丁", "开", "乙", "山", "冂", "ϴ", "卩", "口", "尺", "巛", "十", "凵", "人", "巫", "乂", "丫", "之", "𐌀", "𐌁", "𐌂", "𐌃", "𐌄", "𐌅", "𐌆", "𐌇", "𐌉", "Պ", "𐌊", "𐌋", "𐌌", "𐌍", "ბ", "𐌐", "𐌒", "𐌓", "𐌔", "𐌕", "𐌖", "Վ", "𐌗", "𐌘", "𐌙", "𐌚"]

english = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

mapping = dict(zip(english, risgravien))
mapping2 = dict(zip(risgravien, english))

def to_rigsravien():
    text = entry_top.get()
    output = ""

    for character in text:
        if character.isalpha():
            output += mapping.get(character, character)
        else:
            output += character

    entry_bottom.delete(0, tk.END)
    entry_bottom.insert(0, output)
    pyperclip.copy(output)

def to_latin():
    text = entry_bottom.get()
    output = ""

    for character in text:
        if character.isalpha():
            output += mapping2.get(character, character)
        else:
            output += character

    entry_top.delete(0, tk.END)
    entry_top.insert(0, output)
    pyperclip.copy(output)

root = tk.Tk()
root.title("Rigsravien Translator - Rigret Dialect")
root.geometry("400x350")
root.configure(bg="#F3F4F6")

# --- 1. Editable Top Box ---
frame_top = tk.Frame(root, bg="#3B82F6", bd=2)
frame_top.pack(pady=(40, 10), padx=20)

entry_top = tk.Entry(frame_top, font=("Helvetica", 14), bg="#FFFFFF", fg="#1F2937", bd=5, relief="flat")
entry_top.pack()

# --- 2. Uneditable Bottom Box ---
frame_bottom = tk.Frame(root, bg="#9CA3AF", bd=2)
frame_bottom.pack(pady=10, padx=20)

entry_bottom = tk.Entry(frame_bottom, font=("Helvetica", 14), bg="#E5E7EB", fg="#6B7280", bd=5, relief="flat")
entry_bottom.pack()

# --- 3. Action Button to Read the Text ---
submit_btn = tk.Button(
    root, 
    text="Convert to Rigsravien", 
    command=to_rigsravien, # Runs the function above when clicked
    font=("Helvetica", 11, "bold"),
    bg="#3B82F6",
    fg="white",
    padx=10,
    pady=5,
    relief="flat"
)
submit_btn.pack(pady=20)

submit_btn = tk.Button(
    root, 
    text="Convert to Latin", 
    command=to_latin, # Runs the function above when clicked
    font=("Helvetica", 11, "bold"),
    bg="#3B82F6",
    fg="white",
    padx=10,
    pady=5,
    relief="flat"
)
submit_btn.pack(pady=20)

root.mainloop()
