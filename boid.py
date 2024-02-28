# boid.py
from random import randint
import numpy as np
import pygame as pg
from settings import *
from vector import rotate_vector

class BoidPix():
    def __init__(self, boidNum, surfArray):
        self.bnum = boidNum
        self.data = surfArray
        self.maxW = surfArray.surfSize[0]
        self.maxH = surfArray.surfSize[1]
        self.color = pg.Color(0)  # preps color so we can use hsva
        self.color.hsva = (randint(0, 360), 90, 90)
        self.ang = randint(0, 360)  # random start ang and pos
        self.pos = (randint(10, self.maxW - 10), randint(10, self.maxH - 10))
        self.dir = rotate_vector(self.ang)

    def update(self, dt, speed, ejWrap):
        margin = 8
        turnRate = 10 * dt
        turnDir = xvt = yvt = yat = xat = 0
        otherBoids = np.delete(self.data.b_array, self.bnum, 0)
        # Make list of nearby boids, sorted by distance
        array_dists = (self.pos[0] - otherBoids[:,0])**2 + (self.pos[1] - otherBoids[:,1])**2
        closeBoidIs = np.argsort(array_dists)[:7]
        neiboids = otherBoids[closeBoidIs]
        neiboids[:,3] = np.sqrt(array_dists[closeBoidIs])
        neiboids = neiboids[neiboids[:,3] < 48]
        if neiboids.size > 0:  # if has neighbors, do math and sim rules
            yat = np.sum(np.sin(np.deg2rad(neiboids[:,2])))
            xat = np.sum(np.cos(np.deg2rad(neiboids[:,2])))
            # averages the positions and angles of neighbors
            tAvejAng = np.rad2deg(np.arctan2(yat, xat))
            targetV = (np.mean(neiboids[:,0]), np.mean(neiboids[:,1]))
            # if too close, move away from closest neighbor
            if neiboids[0,3] < 4 : targetV = (neiboids[0,0], neiboids[0,1])
            # get angle differences for steering
            tDiff = pg.Vector2(targetV) - self.pos
            tDistance, tAngle = pg.math.Vector2.as_polar(tDiff)
            # if boid is close enough to neighbors, match their average angle
            if tDistance < 16 : tAngle = tAvejAng
            # computes the difference to reach target angle, for smooth steering
            angleDiff = (tAngle - self.ang) + 180
            if abs(tAngle - self.ang) > 1: turnDir = (angleDiff/360 - (angleDiff//360)) * 360 - 180
            # if boid gets too close to target, steer away
            if tDistance < 4 and targetV == (neiboids[0,0], neiboids[0,1]) : turnDir = -turnDir
        if not ejWrap and min(self.pos[0], self.pos[1], self.maxW - self.pos[0], self.maxH - self.pos[1]) < margin:
            if self.pos[0] < margin : tAngle = 0
            elif self.pos[0] > self.maxW - margin : tAngle = 180
            if self.pos[1] < margin : tAngle = 90
            elif self.pos[1] > self.maxH - margin : tAngle = 270
            angleDiff = (tAngle - self.ang) + 180  # if in margin, increase turnRate to ensure stays on screen
            turnDir = (angleDiff / 360 - (angleDiff // 360)) * 360 - 180
            edgeDist = min(self.pos[0], self.pos[1], self.maxW - self.pos[0], self.maxH - self.pos[1])
            turnRate = turnRate + (1 - edgeDist / margin) * (20 - turnRate) #minRate+(1-dist/margin)*(maxRate-minRate)
        # Steers based on turnDir, handles left or right
        if turnDir != 0:
            self.ang += turnRate * abs(turnDir) / turnDir # turn speed 10
            self.ang %= 360  # keeps angle within 0-360
        self.dir = pg.Vector2(1, 0).rotate(self.ang).normalize()
        self.pos += self.dir * dt * (speed + (7 - neiboids.size) / 14)  # forward speed
        # Edge Wrap
        if self.pos[1] < 1 : self.pos[1] = self.maxH - 1
        elif self.pos[1] > self.maxH : self.pos[1] = 1
        if self.pos[0] < 1 : self.pos[0] = self.maxW - 1
        elif self.pos[0] > self.maxW : self.pos[0] = 1
        # Finally, output pos/ang to arrays
        self.data.b_array[self.bnum,:3] = [self.pos[0], self.pos[1], self.ang]
        self.data.img_array[(int(self.pos[0]), int(self.pos[1]))] = self.color[:3]
