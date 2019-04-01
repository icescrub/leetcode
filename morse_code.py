class Solution:
    def uniqueMorseRepresentations(self, words):
        import string
        list_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

	# create 1-1 relation between letters and their morse codes.
        dict_morse = dict(zip(string.ascii_lowercase, list_morse))

	# convert each word to its morse code equivalent. Output is an array of characters, so next line joins characters to become words.
        words_converted = [[dict_morse[letter] \
                            for letter in word] for word in words]
        words_conv2 = [''.join(word_array) for word_array in words_converted]

	# make list into set (only unique vals allowed), then get the length.
        answer = len(set(words_conv2))
        return answer
