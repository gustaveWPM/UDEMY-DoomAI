#=========================================
# * ... To update (deprecated functions)
#=========================================

# Image Preprocessing

# Importing the libraries
import numpy as np
import cv2
from gym.core import ObservationWrapper
from gym.spaces.box import Box

# Preprocessing the Images

class PreprocessImage(ObservationWrapper):
    
    def __init__(self, env, height = 64, width = 64, grayscale = True, crop = lambda img: img):
        super(PreprocessImage, self).__init__(env)
        self.img_size = (height, width)
        self.grayscale = grayscale
        self.crop = crop
        n_colors = 1 if self.grayscale else 3
        self.observation_space = Box(0.0, 1.0, [n_colors, height, width])

    def observation(self, img):
        img = self.crop(img)
        img = cv2.resize(img, dsize=(80, 80), interpolation=cv2.INTER_CUBIC)
        if self.grayscale:
            img = img.mean(-1, keepdims = True)
        img = np.transpose(img, (2, 0, 1))
        img = img.astype('float32') / 255.
        return img
