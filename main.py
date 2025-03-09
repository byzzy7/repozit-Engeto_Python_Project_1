from collections import Counter
'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author = Lukáš Bystroň
email: lbystron@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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

# převod na pomocný list
text = list()

# oddělovač a podtržítko v textu
znak = "-" *40
hvezda = "*"

# přihlášení do programu
username = input("username:")
password = input("password:")
print(znak)

# registrováni uživatele
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# kontrola ověření hesla a jména
if uzivatele.get(username) == password:
    print("Welcome to the app,", username,"\n","We have 3 texts to be analyzed.","\n",znak)
    try:
        vyber_textu = input("Enter a number btw. 1 and 3 to select: ")
        text = TEXTS[int(vyber_textu) - 1].split() #vyber odstavce uzivatelem
        print(znak)
    except ValueError:
        print("You have made a wrong selection. The program ends.") #ukončeního programu, když nevyberé uživatel text 1 - 3
        exit()
else: 
    print("Unregistered user, terminating the program..") 
    exit() #ukončení když není uživatel registrován

# rozdělení textu podle zadání
velka_pismena = 0
zacinaji_velkym_pismem = 0
mala_pismena = 0
cisla = 0
pocet_slov = len(text)
total_sum = 0

for slovo in text:
    if slovo.islower():
        mala_pismena += 1
    elif slovo[0].isalpha():
        zacinaji_velkym_pismem += 1
    elif slovo.isnumeric():
        total_sum += int(slovo)
        cisla += 1
    elif slovo.isupper():
        velka_pismena += 1


# rozdělení na slova bez čárek a teček a pomlček
pocet_pismen = []
for slovo in text:
    pocet_pismen.append(len((slovo.replace('.', '').replace(',', '').replace('-', ''))))

# vypis podle zadání
print(f'''There are {pocet_slov} words in the selected text.
There are {zacinaji_velkym_pismem} titlecase words.
There are {velka_pismena} uppercase words.
There are {mala_pismena} lowercase words.
There are {cisla} numeric strings.
The sum of all the numbers {total_sum}\n''', znak
)

# tabulka s počtem stejně dlouhých slov
tabulka = Counter(sorted(pocet_pismen))
print("LEN|\tOCCURENCES","{:^15}".format("|NR."))
for key in tabulka:
    if key < 10: #zarovnani označených řádků - jednociferných
       print("",key,"|",tabulka[key] * hvezda,(17 - tabulka[key]) * " ","|",tabulka[key])
    else: #zarovnani označených řádků - dvouciferných
        print(key,"|",tabulka[key] * hvezda,(17 - tabulka[key]) * " ","|",tabulka[key])
