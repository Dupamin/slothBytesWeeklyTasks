def translateToPigLatin(sentence):
    sylls = ("a", "e", "i", "o", "u")
    inds = []
    words = str.split(sentence)
    for i, word in enumerate(words):
        if word[0] in sylls:
            words[i] = word + "way"
        else:
            for syll in sylls:           
                ind = word.find(syll)
                if ind != -1:
                    inds.append(ind)
            mini = min(inds)
            if mini != -1:
                words[i] = word[mini:] + word[0:mini] + "ay"
                inds.clear()
    return " ".join(words)
                
                
# TESTING TRANSLATION
test_cases = (("this is pig latin","isthay isway igpay atinlay"), ("wall street journal","allway eetstray ournaljay"))
for test in test_cases:
    translated = translateToPigLatin(test[0])
    if translated == test[1]:
        print(f"Hurray!: Test case[{test}], Translated[{translated}]")
    else:
        print(f"No???: Test case[{test}], Translated[{translated}]")