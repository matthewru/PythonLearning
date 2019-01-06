from clsEncoder import Encoder

encoder = Encoder()
for count in range(0, 5):
    letter = input("Letter: ")

    if str.lower(letter) in ["a", "b", "c", "d", "e"]:
        encodedChar = encoder.encodeAToE(letter)
        print("Encoded Letter: %s" % encodedChar)
    elif str.lower(letter) in ["f", "g", "h", "i", "j"]:
        encodedChar = encoder.encodeFToJ(letter)
        print("Encoded Letter: %s" % encodedChar)
    elif str.lower(letter) in ["k", "l", "m", "n", "o"]:
        encoder.encodeKToO(letter)
        encodedChar = encoder.encodeKToO(letter)
        print("Encoded Letter: %s" % encodedChar)
    elif str.lower(letter) in ["p", "q", "r", "s", "t"]:
        encoder.encodePToT(letter)
        encodedChar = encoder.encodePToT(letter)
        print("Encoded Letter: %s" % encodedChar)
    elif str.lower(letter) in ["u", "v", "w", "x", "y", "z"]:
        encoder.encodeUToZ(letter)
        encodedChar = encoder.encodeUToZ(letter)
        print("Encoded Letter: %s" % encodedChar)


