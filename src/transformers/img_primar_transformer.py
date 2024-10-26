import numpy as np

class ImgPrimarTransformer:
    
    def transform(self, np_img):
        
        reduced_img = np_img[::8, ::8, :]
        mono_img = np.mean(reduced_img, axis=2)
        
        left = 4
        right = 1
        top = 6
        bottom = 3
        
        cropped_img = mono_img[top:-bottom, left:-right]
        normalized_img = cropped_img / 255.0
        
        return normalized_img