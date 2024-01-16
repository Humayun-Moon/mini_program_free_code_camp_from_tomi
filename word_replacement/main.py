def word_replacment():
    str = "Hello, world this the program of word replacement"
    word_replace = input("Enter the word to replace: ")
    word_replacment = input("Enter the word replacement: ")
    result = str.replace(word_replace, word_replacment)
    print(result)
word_replacment()    