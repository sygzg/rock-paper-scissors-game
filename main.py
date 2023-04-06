import random
user_choice = input("Lütfen bir seçenek seçiniz:  \n Taş \n Kağıt \n Makas: \n -> ")
secenekler = ["taş", "kağıt", "makas"]
computer_choice = random.choice(secenekler)

while True:

    if user_choice == computer_choice:
        print(f"\n Berabere bir daha oynayın")
    elif user_choice == "taş":
        if computer_choice ==  "kağıt":
            print("Kaybettiniz")
        else:
            print("Kazandınız")
            break
    elif user_choice == "kağıt":
        if computer_choice == "taş":
            print("Kazandınız")
        else:
            print("Kaybettiniz")
            break
    elif user_choice == "makas":
        if computer_choice == "taş":
            print("Kaybettiniz")
        else:
            print("Kazandınız")
    else:
        print("Seçiminiz hatalıdır. Lütfen doğru seçeneği yazınız.")
        break
    print("\nTekrar oynamak isterseniz lütfen bir seçenek seçiniz:  \n Taş \n Kağıt \n Makas: \n ->" )
    cevap = input() .lower
    if cevap == ("makas" and "kağıt" and "taş"):
           break



