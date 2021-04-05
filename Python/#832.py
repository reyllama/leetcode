"""
832. Flipping an Image

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for row in range(n):
            for i in range(0, n//2):
                tmp = image[row][i]
                image[row][i] = 1 - image[row][n-i-1]
                image[row][n-i-1] = 1-tmp
            if n % 2 == 1:
                image[row][n//2] = 1 - image[row][n//2]


        return image

"""
Runtime: 44 ms, faster than 94.30% of Python3 online submissions for Flipping an Image.
Memory Usage: 14.3 MB, less than 56.59% of Python3 online submissions for Flipping an Image.
"""
