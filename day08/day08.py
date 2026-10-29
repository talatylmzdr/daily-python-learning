customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
    
}

print(customer.get("birthdate", "Jan 1 1980"))

#phone = input("Phone: ")
#digits_mapping = {
    
 #   "1": "One",
 #   "2": "Two",
 #   "3": "Three",
 #   "4": "Four",
  #  "5": "Five",
   # "6": "Six",
    #"7": "Seven",
    #"8": "Eight",
   # "9": "Nine",
  #  "0": "Zero"
#}#

#output = ""
#for ch in phone:
 #   output += digits_mapping.get(ch, "!") + ""
#print(output)


message = input(">")
words = message.split(" ")
print(words)

emojis = {
    
    ":)" : "😀",
    ":(" : "🙄"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

ogrenci_bilgileri = {
    "ad" : "Talat",
    "soyad": "Yılmazdere",
    "şehir": "İstanbul"
}

ogrenci_bilgileri = ogrenci_bilgileri.items()
print(ogrenci_bilgileri)