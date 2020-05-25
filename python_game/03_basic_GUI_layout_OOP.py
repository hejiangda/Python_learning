import tkinter as tk

class Game(tk.Frame):
    def __init__(self,master):
        super(Game,self).__init__(master)
        self.lives=3
        self.width=610
        self.height=400
        self.canvas=tk.Canvas(self,bg='#aaaaff',
                              width=self.width,
                              height=self.height)
        self.canvas.pack()
        self.pack()
class GameObject(object):
    def __init__(self,canvas,item):
        self.canvas=canvas
        self.item=item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self,x,y):
        self.canvas.move(self.item,x,y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self,canvas,x,y):
        self.radius=10
        self.direction=[1,-1]
        self.speed=10
        item=canvas.create_oval(x-self.radius,y-self.radius,
                                x+self.radius,y+self.radius,
                                fill='white')
        super(Ball,self).__init__(canvas,item)

if __name__=='__main__':
    root=tk.Tk()
    root.title('Hello,Pong!')
    game=Game(root)
    # game.canvas.create_rectangle(250,300,330,320,fill='blue',tags='paddle')
    # item=game.canvas.create_rectangle(10,10,100,80,fill='green')
    # game_object=GameObject(game.canvas,item)
    # print(game_object.get_position())
    # game_object.move(20,-10)
    # print(game_object.get_position())
    # game_object.delete()
    # ball=Ball(game.canvas,20,20)

    game.mainloop()