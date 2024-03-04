print("""Welcome to great karikalan magic show
Select your choise #1 or #2""")

show = input("> ")

if show == "1":
    print("Welcome to the show!")
    print("1. Ungal anaivarukum vanakkam")
    print("2. Neenga adi poga poringa, asanthu poga poreenga.")
    
    vanakkam = input("> ")

    if vanakkam == "1":
        print("Neeye vechikaa show start pannuyaaa!")
    elif vanakkam == "2":
        print("Summa pesitey irukatha yaa! Seekiram arambi")
    else:
        print("Apo yaro ungaluku already sollitanga! athaney?")

elif show == "2":
    print("Yov! nalla irukumyaa oru thadava vathu nambi vangaya.")
    print("1. Seri evlo?")
    print("2. Ethuku en kasa nee aataya podrathuka?")
    print("3. Illa illaa mudiyathu.")

    sodhanai = input("> ")

    if sodhanai == "1":
        print("Just 50 rupees! vanthu paaru ya gongango")
    elif sodhanai == "2":
        print("Konjamavathu erakam kaatrana paaru kal nenja pudichavan")
    else:
        print("Appo! Katta durai ku kattam seri illa.")

else:
    print("Mandaya polanthuduven! olunga vanthu seru")

