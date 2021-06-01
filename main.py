def reverse_words_order_and_swap_cases(sentence):
    result = ""
    if all(x.isalpha() or x.isspace() for x in sentence):
        if sentence[0].isalpha() and sentence[-1].isalpha():
            total_words = sentence.split()

            if (sentence.count(' ')) == (len(sentence.split()) - 1):

                if len(total_words) <= 10:
                    for i in range(len(total_words)):
                        if len(total_words[i]) <= 10:
                            word = total_words[i]
                            for ch in word:
                                if ch.isupper():
                                    result += ch.lower()
                                elif ch.islower():
                                    result += ch.upper()

                        result += ' '

        word_list = result.split()
        reversed_list = word_list[:: -1]
        reversed_sentence = " ".join(reversed_list)

        return reversed_sentence



reverse_words_order_and_swap_cases('aWESOME is cODING')