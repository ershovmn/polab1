from tkinter import *
import random

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="#f2ff38")

class Snake(object):
    def __init__(self, segments):    
        self.segments = segments
        self.courses = {
            "Down": (0, 1), 
            "Up": (0, -1),
            "Left": (-1, 0), 
            "Right": (1, 0)
            }
        
        self.current_couse = self.courses["Right"]
     
    def move(self):
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                x1 + self.current_couse[0] * SEG_SIZE,
                y1 + self.current_couse[1] * SEG_SIZE,
                x2 + self.current_couse[0] * SEG_SIZE,
                y2 + self.current_couse[1] * SEG_SIZE)
     
    def change_direction(self, event): 
        if event.keysym in self.courses:
            if self.current_couse[0] + self.courses[event.keysym][0] == 0 and self.current_couse[1] + self.courses[event.keysym][1]  == 0:
                return
            self.current_couse = self.courses[event.keysym]
 
    def add_segment(self):
        last_seg = c.coords(self.segments[0].instance)
        
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        
        self.segments.insert(0, Segment(x, y)) 

def create_block():
    global BLOCK
    posx = SEG_SIZE * (random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE))
    posy = SEG_SIZE * (random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE))

    BLOCK = c.create_oval(posx, posy,
            posx + SEG_SIZE,
            posy + SEG_SIZE,
            fill="#ff3877")

class Game:
    def __init__(self):
        
        self.root = Tk()
        self.root.title('Tehnarenok snake')
    
    def initGame(self):
        global c, s
        self.IN_GAME = True
        c = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='#38ff6d')
        c.grid()
        c.focus_set()
        segments = [Segment(SEG_SIZE, SEG_SIZE),
                Segment(SEG_SIZE*2, SEG_SIZE),
                Segment(SEG_SIZE*3, SEG_SIZE)]
        s = Snake(segments)
        create_block()
        c.bind("<KeyPress>", s.change_direction)
        self.main()
        self.root.mainloop()

    def main(self):
        if self.IN_GAME:
            s.move()
            head_coords = c.coords(s.segments[-1].instance)
            block_coords = c.coords(BLOCK)
            xx1, yy1, xx2, yy2 = block_coords
            x1, y1, x2, y2 = head_coords
            if x1 < 0 or x2 > WIDTH or y1 < 0 or y2 > HEIGHT:
                self.IN_GAME = False 
            elif xx1 == x1 and yy1 == y1 and xx2 == x2 and yy2 == y2:
                s.add_segment()
                c.delete(BLOCK)
                create_block()
            else:
                for index in range(len(s.segments)-1):
                    if c.coords(s.segments[index].instance) == head_coords:
                        self.IN_GAME = False
            self.root.after(100, self.main)
        else:
            c.create_text(WIDTH/2, HEIGHT/2,
                    text="GAME OVER!",
                    font="Arial 20",
                    fill="#ff0000")

if __name__ == '__main__':
    game = Game()    
    game.initGame()


    