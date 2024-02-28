# surface.py
import pygame as pg
import numpy as np
from settings import *


class SurfaceArray:
    def __init__(self, bigSize):
        self.surfSize = (bigSize[0] // PRATIO, bigSize[1] // PRATIO)
        self.image = pg.Surface(self.surfSize).convert()
        self.img_array = np.array(pg.surfarray.array3d(self.image), dtype=float)
        self.b_array = np.zeros((BOIDZ, 4), dtype=float)

    def update(self, dt):
        self.img_array[self.img_array > 0] -= (
            FADE * (60 / FPS / 1.5) * ((dt / 10) * FPS)
        )
        self.img_array = self.img_array.clip(0, 255)
        pg.surfarray.blit_array(self.image, self.img_array.astype("int"))
        return self.image
