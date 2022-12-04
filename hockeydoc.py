import pygame as pg
import pandas as pd

pg.init() # start game
dimensions = (850, 750)
clock = pg.time.Clock()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
BLUE = pg.Color('dodgerblue1')

background_img = pg.Surface(screen.get_size())
background_img.fill((30, 30, 30))

# Ice surface
game_surf = pg.Surface(dimensions)
ice = pg.image.load("ice.png").convert()
ice = pg.transform.scale(ice, dimensions)
game_surf.blit(ice, (0,0))

# stats surface
stats_surf = pg.Surface((400, 750), pg.SRCALPHA)
stats_surf.fill((255, 255, 255))

stats_font = pg.font.SysFont("Arial", 18, 1, 1)

# dots
arrow_img = pg.Surface((12, 12), pg.SRCALPHA)
pg.draw.circle(arrow_img, BLUE, (6,6), 6)

pos = []  # Position of the dots.
data = {"Position":[]}
df = pd.DataFrame(data)

done = False
while not done:
    # Blit the background to clear the screen.
    screen.blit(background_img, (0, 0))
    background_img.blit(game_surf, (20,40))
    background_img.blit(stats_surf, (1000, 40))
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos.append(event.pos)
            print(event.pos)
            
            df = pd.concat([df, pd.DataFrame({"Position": [event.pos]})], ignore_index=True)
            print(df)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                done = True
            
    # Blit the arrow.
    for j in pos:
        i = list(j)
        i[0] = i[0] - 20
        i[1] = i[1] - 40
        position = tuple(i)
        game_surf.blit(arrow_img, position)

    for row in df.index:
        height = (int(row) + 1) * 20
        stats_surf.blit(stats_font.render(str(df.Position.iloc[row]), False, (0, 0, 0)), (20, height))

    pg.display.update()

    pg.display.flip()

pg.quit()
exit()