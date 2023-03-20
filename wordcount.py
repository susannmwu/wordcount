"""Count words in file."""



def get_word_count(file):

    file = open("test.txt")
    word_count = {}

    for line in file: 
        # this would put each word in the line into a list
        line = line.split(" ")
        # print(line)
        for word in line:
            word_count[word] = word_count.get(word,0) + 1 

    for word in word_count.items():
        # print out of tuples
        print(word)
    return word_count


print(get_word_count("test.txt"))       


