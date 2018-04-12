from threading import Thread, Event, local
import pygame
#import pygame.gfxdraw
#import pygame.freetype
#import logging
import pygame.math

from basicPatterns import *

class doDraw(Thread):
        def __init__(self, surface, exiting):
                self.surf = surface
                self.exiting = exiting
                #self.font = pygame.freetype.SysFont(
                #        pygame.freetype.get_default_font(),25)
                super(doDraw, self).__init__( args = (self) )
        def run(self):
                loc = local()
                loc.xy = self.surf.get_size()
                loc.state = 0
                while not self.exiting.isSet():
                        if pygame.event.peek(pygame.VIDEORESIZE):
                                loc.state += 1
                                ev = pygame.event.get(pygame.VIDEORESIZE)[0]
                                loc.xy = ev.size
                                self.surf = pygame.display.set_mode(loc.xy, pygame.RESIZABLE)
                                print("resize happened", loc.state)
                                sierpinski(self.surf, loc.xy)
                        pygame.display.flip()
                print("ded") #cut the thread; killed it dead

if __name__ == '__main__':
        pygame.init()
        kill = Event()
        surf = pygame.display.set_mode((512,512), pygame.RESIZABLE)
        pixelChecker(surf, (512,512))
        dd=doDraw(surf,kill)
        dd.start()
        try:
                state = 0
                while 1:
                        event = pygame.event.poll()
                        if event.type == pygame.QUIT:
                                break
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                        break
                        elif event.type == pygame.VIDEORESIZE:
                                state += 1
                                print("caught resize", state)
        finally:
                kill.set()
                pygame.quit()
        
