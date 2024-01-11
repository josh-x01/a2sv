class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for img in image:
            new_img = []
            for i in range(len(img)-1, -1, -1):
                if img[i] == 1:
                    new_img.append(0)
                else:
                    new_img.append(1)
            result.append(new_img)
        return result