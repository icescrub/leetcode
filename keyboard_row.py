# The different rows of the keyboard.

row1 = 'qwertyuiopQWERTYUIOP'
row2 = 'asdfghjklASDFGHJKL'
row3 = 'zxcvbnmZXCVBNM'
rows = [row1,row2,row3]

# For each word, see if ALL letters of the word are in ONE row, for ANY of the three rows of the keyboard. Gives true and false.
# Should really put that complex logic into a function by its own, and filter the words through that function.

answer = [any(all(letter in row for letter in word) for row in rows) for word in words]

# Associates each word with whether it passed the test. Returns only the words that passed the test.

x = list(zip(answer,words))
return [x[i][1] for i in range(len(x)) if x[i][0]]
