import tkinter as tk
import math

class areaSelector:
    root = tk.Tk()
    
    # root(window) configs
    # root.geometry("1000x600")
    root.wm_attributes('-alpha', 0.7)
    root.configure(bg="black")
    root.minsize(500,500)
    root.title("Capture Area selection Widget")
    root.update_idletasks()

    # screen cordinates for bunk-inator
    areaStartX = 0
    areaStartY = 0
    areaWidth = 1920
    areaHeight = 1080
    
    def __init__(self):
        instructions = '''
        Bunk-inator capture area selection widget (BICASW)
        -------------------------------------------------
        \n\n\n\n\n\n
        Cover the area you wish to capture with this window
        including window title bar and hit enter when done
        \n\n\n\n\n\n
        
        -------------------------
        This is not accurate to the pixel, screenshot
        might be 10-20 pixels away from covered area
        '''
        tk.Label(self.root,text=instructions,font=("Arial", 13),bg="black",fg="white").place(relx=0.5,rely=0.5,anchor="center")
        self.root.bind("<Configure>", self.configureHandler)
        self.root.bind("<Return>", lambda _ : self.root.destroy())
        self.root.mainloop()
    
    def configureHandler(self,e):
        '''for updating cordinates each time window is resized or repositioned''' 
        self.areaStartX=self.root.winfo_x()+8
        self.areaStartY=self.root.winfo_y()+8
        self.areaWidth=self.root.winfo_width()+(96*(math.ceil(self.root.winfo_width()/480)))
        self.areaHeight=self.root.winfo_height()+(29*(math.floor(self.root.winfo_height()/75)))
        
    def getCaptureArea(self):
        '''for fetching cordinates in bunk-inator'''
        return({
            "x":self.areaStartX,
            "y":self.areaStartY,
            "width":self.areaWidth,
            "height":self.areaHeight,
        })