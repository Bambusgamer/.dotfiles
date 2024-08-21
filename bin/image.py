from __future__ import division
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

total = len(sys.argv)-1
if (total < 1):
    print ("Usage: IMG")
    sys.exit(1)

# Parsing args one by one
IMG = str(sys.argv[1])

def demo(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(
                  screen, IMG, 
                  screen.height-2,
                  uni=screen.unicode_aware,
                  dither=screen.unicode_aware),
                  0,
                  stop_frame=200
            )
    ]
    scenes.append(Scene(effects))
    screen.play(scenes, stop_on_resize=True)


# capture ctrl+c and exit nicely
import signal
import sys
def signal_handler(sig, frame):
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            #Screen.wrapper(demo, catch_interrupt=True)
            sys.exit(0)
        except ResizeScreenError:
            sys.exit(0)
