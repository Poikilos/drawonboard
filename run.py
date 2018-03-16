#from tkinter import *

#try:
#    import Tkinter as tk     ## Python 2.x
#except ImportError:
#    import tkinter as tk     ## Python 3.x

try:
    from Tkinter import *     ## Python 2.x
except ImportError:
    from tkinter import *     ## Python 3.x

from random import randint
#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/
class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.toolsThickness = 3
        self.rgb = "#%02x%02x%02x" % (0, 0, 0)

        self.pack()
        self.createWidgets()

        master.bind('=', self.thicknessPlus)
        master.bind('+', self.thicknessPlus)
        master.bind('-', self.thicknessMinus)

    def getDotList(self, posA, posB):
        posA = list(posA)
        posB = list(posB)
        results = []
        deltas = list((0, 0))

        dirs = list((1, 1))
        for axis_i in range(0,2):
            deltas[axis_i] = posB[axis_i] - posA[axis_i]
            if posB[axis_i] < posA[axis_i]:
                dirs[axis_i] = -1

        loop_axis_i = 0
        off_axis_i = 1
        if deltas[1] > deltas[0]:
            loop_axis_i = 1
            off_axis_i = 0

        this_pos = list((posA[0], posA[1]))
        # walk_i = posA[loop_axis_i]
        rel_i = 0
        # walk_diff = posB[loop_axis_i] - posA[loop_axis_i]
        # off_diff = posB[off_axis_i] - posA[off_axis_i]
        iteration_count_max = 10000
        iteration_count = 0
        while True:
            progress = 0
            if deltas[loop_axis_i] != 0:
                progress = float(rel_i) / float(deltas[loop_axis_i])
            this_pos[off_axis_i] = posA[off_axis_i] + progress * deltas[off_axis_i]
            results.append((this_pos[0], this_pos[1]))
            if this_pos[loop_axis_i] == posB[loop_axis_i]:
                break
            # if walk_i == posB[loop_axis_i]:
                # break
            # walk_i += 1
            this_pos[loop_axis_i] += dirs[loop_axis_i]
            rel_i += dirs[loop_axis_i]
            iteration_count += 1
            if iteration_count > iteration_count_max:
                print(
                    "ERROR in getDotList: maximum iterations reached"
                    + "{"
                    + "this_pos["+str(loop_axis_i)+"]: " + str(this_pos[loop_axis_i]) + "; "
                    + "this_pos["+str(off_axis_i)+"]: " + str(this_pos[off_axis_i]) + "; "
                    + "posA: " + str(posA) + "; "
                    + "posB: " + str(posB) + "; "
                    + "dirs["+str(loop_axis_i)+"]: " + str(dirs[loop_axis_i]) + "; "
                    + "dirs["+str(off_axis_i)+"]: " + str(dirs[off_axis_i]) + "; "
                    + "progress: " + str(progress) + "; "
                )
                break
        return results

    def createWidgets(self):
        self.myCanvas = Canvas(self, width = 1200,
                                height = 800, relief=RAISED, borderwidth=0)
        self.myCanvas.pack(side = LEFT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setFirstXY)
        #-----------------------------------------------

        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

        self.leftFrame = Frame(self, bg = tk_rgb)
        self.leftFrame.pack(side = RIGHT, fill = Y)

        self.label = Label(self.leftFrame, text = "choose a RGB color: ")
        self.label.grid(row = 0, column = 0, sticky = NW, pady = 2, padx = 3)
        #-----------------------------------------------
        self.entryFrame = Frame(self.leftFrame)
        self.entryFrame.grid(row = 1, column = 0,
                              sticky = NW, pady = 2, padx = 3)

        self.myEntry1 = Entry(self.entryFrame, width = 5, insertwidth = 3)
        self.myEntry1.pack(side = LEFT, pady = 2, padx = 4)

        self.myEntry2 = Entry(self.entryFrame, width = 5)
        self.myEntry2.pack(side = LEFT, pady = 2, padx =4)

        self.myEntry3 = Entry(self.entryFrame, width = 5)
        self.myEntry3.pack(side = LEFT, pady = 2, padx = 4)
        #----------------------------------------------
        self.bttn1 = Button(self.leftFrame,
                             text = "accept", command = self.setColor)
        self.bttn1.grid(row = 2, column = 0, pady = 2, padx = 3, sticky = NW)

        self.labelThickness = Label(
                            self.leftFrame,
                            text = "drawing tools' thickness:")
        self.labelThickness.grid(row = 3,
                                 column = 0, pady = 2, padx = 3)

        self.myScale = Scale(
                            self.leftFrame, from_ = 1, to = 25,
                            orient = HORIZONTAL,
                            command = self.setThickness
                            )
        self.myScale.set(self.toolsThickness)
        #self.toolsThickness = 2
        self.myScale.grid(
                          row = 4, column = 0,
                          pady = 2, padx = 3, sticky = S,
                          )

        self.labelTools = Label(
                                self.leftFrame,
                                text = "chose a drawing tool:",
                                )
        self.labelTools.grid(
                             row = 5, column = 0,
                             pady = 2, padx = 3,
                             sticky = NW
                             )

        Radiobutton(self.leftFrame,
                    text = "line",
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = 3, pady = 2,
                                    row = 6, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftFrame,
                    text = "line2",
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = 3, pady = 2,
                                    row = 7, column = 0,
                                    sticky = NW
                                    )

        Radiobutton(self.leftFrame,
                    text = "flowers tool",
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = 3, pady = 2,
                                    row = 8, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftFrame,
                    text = "spray",
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = 3, pady = 2,
                                    row = 9, column = 0,
                                    sticky = NW,
                                    )
        Radiobutton(self.leftFrame,
                    text = "cosmos",
                    variable = self.radiobuttonValue,
                    value = 5).grid(padx = 3, pady = 2,
                                    row = 10, column = 0,
                                    sticky = NW,
                                    )

        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.deleteAll)
        self.buttonDeleteAll.grid(padx = 3, pady = 2,
                                    row = 11, column = 0,
                                    sticky = NW)

#----------------------------------------------------------------------
    def setThickness(self, event):
        # print(self.myScale.get())
        self.toolsThickness = self.myScale.get()

    def setColor(self):
        try:
            val1 = int(self.myEntry1.get())
            val2 = int(self.myEntry2.get())
            val3 = int(self.myEntry3.get())
            if 0 <=(val1 and val2 and val3) <= 255:
                self.rgb = "#%02x%02x%02x" % (val1, val2, val3)
            self.myEntry1.delete(0, END)
            self.myEntry2.delete(0, END)
            self.myEntry3.delete(0, END)

        except ValueError:
            print("ERROR: Could not finish setColor--that's not an int!")
        # set focus to something else, not to mess with pressing keys: a,s
        self.focus()

    def setFirstXY(self, event):
        # print("now")
        self.firstX = event.x
        self.firstY = event.y
        self.previousX = event.x
        self.previousY = event.y
        self.previousDown = [False, False, False]  # mouse buttons

    def draw(self, event):
        # line 1
        if self.radiobuttonValue.get() == 1:
            if self.previousDown[0]:
                dots = self.getDotList((self.previousX, self.previousY), (event.x, event.y))
                for dot in dots:
                    self.myCanvas.create_oval(dot[0] - self.toolsThickness,
                                              dot[1] - self.toolsThickness,
                                              dot[0] + self.toolsThickness,
                                              dot[1] + self.toolsThickness,
                                              fill = self.rgb
                                              )
            else:
                print("(verbose message in draw) was not down")
                self.myCanvas.create_oval(event.x - self.toolsThickness,
                                          event.y - self.toolsThickness,
                                          event.x + self.toolsThickness,
                                          event.y + self.toolsThickness,
                                          fill = self.rgb
                                          )

        #line 2
        elif self.radiobuttonValue.get() == 2:

            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width = self.toolsThickness,
                                      fill = self.rgb)
            self.previousX = event.x
            self.previousY = event.y
        #flowers tool
        elif self.radiobuttonValue.get() == 3:
            tk_rgb = "#%02x%02x%02x" % (randint(140,255), randint(140,225), 40)
            self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width = self.toolsThickness,
                                      fill = tk_rgb)
        # spray tool
        elif self.radiobuttonValue.get() == 4:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)

            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + xrand + self.toolsThickness, event.y + yrand + self.toolsThickness,
                                      fill = self.rgb,
                                      width = 0
                                      )
        # cosmos tool
        elif self.radiobuttonValue.get() == 5:
            if self.toolsThickness < 5:
                multiplier = 6
            else:
                multiplier = 2
            xrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            yrand = randint(-self.toolsThickness * multiplier,
                             +self.toolsThickness * multiplier)
            tk_rgb = "#%02x%02x%02x" % (randint(5,255), randint(10,150), randint(13,255))
            self.myCanvas.create_oval(event.x + xrand, event.y + yrand,
                                      event.x + self.toolsThickness, event.y + self.toolsThickness,
                                      fill = tk_rgb
                                      )
        self.previousX = event.x
        self.previousY = event.y
        self.previousDown[0] = True

    def deleteAll(self):
        self.myCanvas.delete("all")

    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)

    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)

root = Tk()
root.title("Draw on Board")
app = Application(root)
root.mainloop()
