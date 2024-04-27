while True:
    alphabet = []
    for i in range(26):
        alphabet.append(chr(ord('a') + i))
    s = input("Plz enter a single character: ")
    for i in range(len(s):


                   
        for i in range(len(alphabet)):
            if alphabet[i] == s:
                print(alphabet[(i + 3)% 26])
                break

