class Solution:
    def toGoatLatin(self, S):

        def starts_with_vowel(s):
            return s[0] in "aeiouAEIOU"
        def starts_with_consonant(s):
            return not starts_with_vowel(s)

        def vowel_transform(s,i):
            return s + "ma" + "a"*(i+1)
        def consonant_transform(s,i):
            return s[1:] + s[0] + "ma" + "a"*(i+1)
        
        sentence = []
        
        for i, word in enumerate(S.split()):
            sentence.append(vowel_transform(word,i) if starts_with_vowel(word) else consonant_transform(word,i))
            
        return ' '.join(sentence)
