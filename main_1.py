texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
"""
projekt_1.py: první projekt do Engeto Online Python Akademie:

author: Radek Doleček
email: radek.dolecek@gmail.com
discord: Radek
discord user: radek0913
"""
# import knihovny
import string
import re
import getpass
import time
from collections import defaultdict

# uvítání uživatele
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# přivitání užívatele
# kontrola, zda uživatel existuje v seznamu + ošetření psaní velkými písmeny uživatelem
user = input("Write your name: ").lower()
if user not in users:
    print(f"username '{user}'")
else:
    pass
        
# zadání hesla uživatelem
password = getpass.getpass("Write your password: ")
print(f"Password was proceeded:'{password}'.")

# podmínka, která ověřuje zadané přihlašovací údaje, v tomto případě heslo
if users.get(user) == password:
    print(f"Password for the '{user}' is correct.")
    print("-" * 35)
    print(f"Welcome to the app, {user.capitalize()}!\nWe have 3 texts to be analyzed.")
    print("-" * 35)
else:
    print("-" * 24)
    print(f"username:'{user}'")
    print(f"password:'{password}'")
    print("Unregistered user, terminating the program...")
    exit()

# kontrola vstupu uživatele
index = [1, 2, 3]

# kontrola, zda uživatel zadal platné číslo
while True:
    vyber_textu = input("Choose:\n1 - for the first text\n2 - for the second text\n3 - for the third text\nto start the analysis: ")
    if vyber_textu.isdigit() and int(vyber_textu) in index:
        print("-" * 38)
    else: 
        print("Unregistered user, terminating the program...")
        exit()

    print(f"Analysis of the text is being run", end="", flush=True)
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)  # pauza 
    print()  # nový řádek po dokončení
    print("-" * 38)
    break  # Exit the loop after processing the input

# výběr textu podle uživatelského vstupu
text = texts[int(vyber_textu) - 1] 

# zadání proměnných
pocet_not_cislo = []
pocet_z_velka = []
pocet_velka = []
pocet_is_cislo = []
pocet_mala = []

# Rozdělení textu na jednotlivá slova, odstranění interpunkce
words = text.split()

# výpis jednotlivých znaků za jednotlivá slova za celý odstavec bez interpunkce 
letter_count = defaultdict(int)  # Initialize as a dictionary
for word in words:
        clean_word = word.strip(string.punctuation)
        count = sum(1 for sign in clean_word if sign.isalpha())
        if count > 0:
            letter_count[count] += 1

# výpis počtu slov (kolik písmen, tolik * ve slově, řazeno sestupně)
for length in sorted(letter_count.keys()):
        stars = "*" * length
        count = letter_count[length]
        #print(stars, f"{length} | {count}x")
                                   
# proměnné pro počet slov v textu bez čísel  
sum_cislo = 0
num = 0

# smyčka pro součet všech číslic, které jsou obsaženy ve vybraném odstavci
for word in words:
    word = word.strip(string.punctuation)
    if not word.isdigit():
        pocet_not_cislo.append(word)
    else:
        pocet_is_cislo.append(word)
        num = int(word)
        sum_cislo += num

# získání součtu všech slov v textu včetně číselných hodnot
    sum_soucet = []
    sum_soucet = pocet_is_cislo + pocet_not_cislo
# výpis počtu slov v textu s velkým písmenem na začátku slova
    if word[0].isupper() and word.istitle():
        pocet_z_velka.append(word)
# výpis počtu slov v textu s velkým písmenem
    if word.isupper():
        pocet_velka.append(word)
# výpis počtu slov v textu s malým písmenem
    if word.islower():
        pocet_mala.append(word)

# získání součtu všech slov v textu
sum_pocet = [] 

# přidání počtu slov do celkového součtu zadaných textů
for text in texts:
    words = text.split()
    # odstranění interpunkce a čísel ze slov
    for word in words:
        if not word.isdigit():
            word = word.strip(string.punctuation)
            # přidání slova do celkového součtu
            sum_pocet.append(word)

# vytisknutí výsledků na obrazovku 
line = "-" * 70

print(line)
print(f"{'The number of words that do not contain a digit:':54}{len(pocet_not_cislo):>16}")
print(f"{'The number of words with first capital letter:':54}{len(pocet_z_velka):>16}")
print(f"{'The number of words written in capital letters:':54}{len(pocet_velka):>16}")
print(f"{'The number of words written in lowercase:':54}{len(pocet_mala):>16}")
print(f"{'The number of words including digits:':54}{len(pocet_is_cislo):>16}")
print(line)
print(f"{'Total number of words in all paragraphs:':54}{len(sum_pocet):>16}")
print(f"{'Total number of words in the paragraph, numbers':54}{len(sum_soucet):>16}")
print(f"{'Total sum of all numbers in the selected paragraph(' + str(vyber_textu) + '):':54}{sum_cislo:>16}")
print(line)

# Šířky sloupců
col1_width = 6  # Délka
col2_width = 6  # Počet
col3_width = 12 # Hvězdy
sorted_letter_count = sorted(letter_count.items())

# Funkce pro ohraničovací řádek
def print_line():
    print("+" + "-" * (col1_width + 2) +
          "+" + "-" * (col2_width + 2) +
          "+" + "-" * (col3_width + 2) + "+")

# Hlavička tabulky
print_line()
print(f"| {'Length':^{col1_width}} | {'Number':^{col2_width}} | {'Stars':^{col3_width}} |")
print_line()

# Data řádky
for length, count in sorted_letter_count:
    print(f"| {length:^{col1_width}} | {count:^{col2_width}} | {'*' * length:<{col3_width}} |")

# Spodní čára
print_line()

                