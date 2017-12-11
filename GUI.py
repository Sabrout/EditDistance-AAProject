import tkinter
import EditDistance as ed
root= tkinter.Tk()

l1 = tkinter.Label(root, text="Enter String S1")
l1.pack(anchor=tkinter.W)
e1 = tkinter.Entry(root, bd =5)
df= "dsghdsf"
e1.pack(anchor= tkinter.W)
s1= e1.get()
print (e1)
l1 = tkinter.Label(root, text="Enter String S2")
l1.pack(anchor= tkinter.W)
e2 = tkinter.Entry(root, bd =5)
dsg= "efsdgfg"
e2.pack(anchor= tkinter.W)
s2=e2.get()
print (e2)

#################################################################################
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
var = tkinter.IntVar()
R1 = tkinter.Radiobutton(root, text="Classic Dynamic Algorithm", variable=var, value=1,
                  command=sel)
R1.pack(anchor= tkinter.W)

R2 = tkinter.Radiobutton(root, text="Divide And Conquer Algorithm", variable=var, value=2,
                  command=sel)
R2.pack(anchor= tkinter.W)

R3 = tkinter.Radiobutton(root, text="Pure Recursive Algorithm", variable=var, value=3,
                  command=sel)
R3.pack(anchor= tkinter.W)
R4 = tkinter.Radiobutton(root, text="Branch and Bound Algorithm", variable=var, value=4,
                  command=sel)
R4.pack(anchor= tkinter.W)
###########################################
L5 = tkinter.Label(root, text="Cost for Branch and Bound")
L5.pack(anchor= tkinter.W)
E5 = tkinter.Spinbox(root, from_=0 , to= 20, bd =5)
E5.pack(anchor=tkinter.W)

#L6 = tkinter.Label(root, text="Bound for Branch and Bound")
#L6.pack(anchor= tkinter.W)
#E6 = tkinter.Spinbox(root, from_=0 , to= 20, bd =5)
#E6.pack(anchor=tkinter.W)

##############################################################################3

def selt():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
R5 = tkinter.Radiobutton(root, text="K-Strip Algorithm", variable=var, value=5,
                  command=selt)
R5.pack(anchor= tkinter.W)
#################################################################################

L3 = tkinter.Label(root, text="Enter the value for k")
L3.pack(anchor= tkinter.W)
E3 = tkinter.Spinbox(root, from_=0 , to= 20, bd =5)
k= E3.get()
E3.pack(anchor= tkinter.W)

#var = tkinter.DoubleVar()
#button = tkinter.Button(root, text="Select the value of k for K-Strip algorithm", command=selt)
#button.pack(anchor= tkinter.CENTER)
#scale = tkinter.Scale( root, variable = var, orient= tkinter.HORIZONTAL )
#scale.pack(anchor= tkinter.CENTER)
#label = tkinter.Label(root)
#label.pack()




##############################################################################

R6 = tkinter.Radiobutton(root, text="Approximated Greedy Algorithm", variable=var, value=6,
                  command=sel)
R6.pack(anchor= tkinter.W)
L4 = tkinter.Label(root, text="Lookahead for Greedy Algorithm")
L4.pack(anchor= tkinter.W)
E4 = tkinter.Spinbox(root, from_=0, to=200, bd =5)
E4.pack(anchor= tkinter.W)
#############################################################################
var2 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var2, width=300 )


label.pack()
var3 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var3, width=300 )


label.pack()
var4 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var4, width=600, justify= tkinter.RIGHT, relief= tkinter.RAISED )


label.pack()
var5 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var5, width=600, justify= tkinter.RIGHT, relief= tkinter.RAISED )


label.pack()
var6 = tkinter.StringVar()
label = tkinter.Message( root, textvariable=var6, width=600, justify= tkinter.RIGHT, relief= tkinter.RAISED )


label.pack()
    

def callback():
    if var.get()==1:
       
        result = (ed.calc_runtime_md(ed.med_classic_gui, e1.get(),e2.get()))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        var4.set(result[2])
        var5.set(result[3])
        var6.set(result[4])
        #print("RUNNING TIME :  %s seconds" % result[0])
       # print(var2.set(ed.calc_runtime(ed.med_classic, )))
    if var.get()==2:
    
        result1= ed.hirschberge(e1.get(),e2.get())
        result = (ed.calc_runtime_md(ed.calcByRow, e1.get(),e2.get()))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        var4.set(result1[0])
        var5.set(result1[1])
        var6.set(result1[2])
    if var.get()==3:
        result = (ed.calc_runtime_md(ed.med_recursive, e1.get(),e2.get()))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        
    if var.get()==4:
       
        result = (ed.calc_runtime_md(ed.med_branch, e1.get(),e2.get(), int(E5.get()), abs(len(e1.get()) - len(e2.get())) + 1))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
    if var.get()==5:
        
        result = (ed.calc_runtime_md(ed.med_k_gui, e1.get(),e2.get(), E3.get()))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        var4.set(result[3])
        var5.set(result[4])
        var6.set(result[5])
    if var.get()==6:
        
        result = (ed.calc_runtime_md(ed.med_greedy, e1.get(), e2.get(), int(E4.get())))
        var2.set("RUNNING TIME :  %s seconds" % result[0])
        var3.set("{} {}".format("MINIMUM EDIT DISTANCE :", result[1]))
        


B = tkinter.Button(root, text ="Go", command = callback)
B.pack()


label = tkinter.Label(root)
label.pack()
root.mainloop()

########################################################################
#if var.get()==1:
    #top = tkinter.Tk()
    #top = tkinter.tk(command=callback)
    #top.mainloop()