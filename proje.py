meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "XD": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            "OK":"onaylamak",
            }
word = input("Hepsini büyük harflerle yazın! ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("bu kelime eşleşmiyor")
