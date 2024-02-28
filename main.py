import pygame as pg
from settings import *
from boid import BoidPix
from surface import SurfaceArray

def main():
    pg.init()
    pg.display.set_caption("PixelBoids")
    try: pg.display.set_icon(pg.image.load("nboids.png"))
    except: print("FYI: nboids.png icon not found, skipping..")

    if FLLSCRN:
        currentRez = (pg.display.Info().current_w, pg.display.Info().current_h)
        screen = pg.display.set_mode(currentRez, pg.SCALED)
        pg.mouse.set_visible(False)
    else:
        screen = pg.display.set_mode((WIDTH, HEIGHT))

    cur_w, cur_h = screen.get_size()
    screenSize = (cur_w, cur_h)

    drawLayer = SurfaceArray(screenSize)
    boidList = [BoidPix(n, drawLayer) for n in range(BOIDZ)]

    clock = pg.time.Clock()
    if SHOWFPS: font = pg.font.Font(None, 30)

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                return

        dt = clock.tick(FPS) / 100
        screen.fill(0)

        for boid in boidList:
            boid.update(dt, SPEED, WRAP)

        drawImg = drawLayer.update(dt)
        rescaled_img = pg.transform.scale(drawImg, (cur_w, cur_h))
        screen.blit(rescaled_img, (0, 0))

        if SHOWFPS:
            screen.blit(font.render(str(int(clock.get_fps())), True, [0, 200, 0]), (8, 8))

        pg.display.update()

if __name__ == '__main__':
    main()
    pg.quit()
