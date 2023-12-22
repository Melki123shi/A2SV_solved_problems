class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, im in enumerate(image):
            im = im[::-1]
            im = [1 - i for i in im]
            image[i] = im
        return image
        