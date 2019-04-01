class Solution:
    def flipAndInvertImage(self, A):
        A_flip = [x[::-1] for x in A]
        A_invert = [[1 if coordinate == 0 else 0 \
                     for coordinate in vector] \
                    for vector in A_flip]
        return A_invert
