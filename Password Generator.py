import random, string, time

s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)

while (True):
    try:
        pwlen = input('\nEnter lentgh of your Password or press "q" to quit : ')

        if pwlen.lower() == "q":
            print("Thaks for using password generator.")
            time.sleep(2)
            exit()

        elif pwlen != "q":
            pwlen = int(pwlen)
            random.shuffle(s)
            print("\nYour password is : ")
            print("".join(random.sample(s, int(pwlen))))

    except Exception as e:
        again = True

        while again:
            a = input("\nPassword length should be number! Try again (Y/N) ? : ")

            if a.lower() == "y":
                break
            elif a == "n":
                print("Thaks for using password generator.")
                time.sleep(2)
                exit()
            else:
                print("Invalid Choice!")
