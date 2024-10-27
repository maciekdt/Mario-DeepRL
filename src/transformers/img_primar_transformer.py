import numpy as np

class ImgPrimarTransformer:
    
    def transform(self, np_img):
        reduced_img = np_img[::8, ::8, :]
        mono_img = np.mean(reduced_img, axis=2)
        
        left = 2
        right = 2
        top = 1
        bottom = 1
        
        cropped_img = mono_img[top:-bottom, left:-right]
        normalized_img = cropped_img / 255.0
        
        return normalized_img
        #return np.mean(np_img[::8, ::8, :], axis=2)[1:-1, 2:-2] / 255.0   for ultra fast computing