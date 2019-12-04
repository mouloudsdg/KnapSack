from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import KnapSack
import random

lv = []
lw = []
weight_max = [0]


def add_obj():
    lv.append(int(sp_gain.get()))
    lw.append(int(sp_poid.get()))
    tree.insert("","end", text="Objet_"+str(len(lv)), values=(lw[len(lw)-1],lv[len(lv)-1]))
    nb_objets.configure(text="Nb_objets : "+str(len(lv)))

    

def add_nbobj_rand():
    for i in range(0,int(sp_nbobj.get())):
        lv.append(random.randint(1,100))
        lw.append(random.randint(1,100))
        tree.insert("","end", text="Objet_"+str(len(lv)), values=(lw[len(lw)-1],lv[len(lv)-1]))
        nb_objets.configure(text="Nb_objets : "+str(len(lv)))

def add_weight_max():
    weight_max[0] = int(sp_pmax.get())
    w_m.configure(text="Poids_max : "+str(weight_max[0]))

def excute():
    res = KnapSack.knapsack(len(lv),lw,lv,weight_max[0])
    res[1].reverse()
    showinfo("Resultat","La valeur max = "+str(res[0])+"\n"+"Les objets pris sont = "+str(res[1]))
def reinit():
    lv.clear()
    lw.clear()
    weight_max[0]=0
    tree.delete(*tree.get_children())
    nb_objets.configure(text="Nb_objets : "+str(len(lv)))
    w_m.configure(text="Poids_max : "+str(weight_max[0]))


win = Tk()
win.title("KnapSack")
win.minsize(width=600,height=350)
win.maxsize(width=600,height=350)

#-----------------TreeView----------
tree = Treeview(win,columns=('poids','gain'))
tree.place(x=10,y=10)

tree.heading('poids',text='poids')
tree.heading('gain',text='gain')
tree.column('#0',width=150)
tree.column('poids',width=120)
tree.column('gain',width=120)
vsb = Scrollbar(win, orient="vertical", command=tree.yview)
vsb.place(x=402, y=10, height=220)
tree.configure(yscrollcommand=vsb.set)
#-----------------//

#--------------Label Objet-----------
lb_object=LabelFrame(win,text="Objet").place(x=10,y=240,height=100,width=200)

l_poid = Label(lb_object,text="poid").place(x=30, y=260)
sp_poid = Spinbox(lb_object,from_=1,to=100)
sp_poid.place(x=70, y=260, width=100)
l_gain = Label(lb_object,text="gain").place(x=30, y=285)
sp_gain = Spinbox(lb_object,from_=1,to=100)
sp_gain.place(x=70, y=285, width=100)
bt_obj=Button(lb_object, text="Ajouter",command=add_obj).place(x=125, y=310,width=70,height=25)
#-----------------//

#--------------Label Aléatoire-----------
lb_rand=LabelFrame(win,text="Aléatoire").place(x=205,y=240,height=100,width=200)

l_nbobj = Label(lb_rand,text="nb_objets").place(x=215, y=273)
sp_nbobj = Spinbox(lb_rand,from_=1,to=100)
sp_nbobj.place(x=285, y=273, width=100)
bt_rand=Button(lb_rand, text="Ajouter",command=add_nbobj_rand).place(x=320, y=310,width=70,height=25)
#------------------//

#--------------Label---------------------
lb=LabelFrame(win).place(x=400,y=240,height=100,width=190)

l_pmax = Label(lb,text="poid_max").place(x=410, y=273)
sp_pmax = Spinbox(lb,from_=1,to=100)
sp_pmax.place(x=480, y=273, width=100)
bt=Button(lb, text="Entrer", command=add_weight_max).place(x=510, y=310,width=70,height=25)
#------------------//

#---------------Button exec et reinit----------------
bt_1=Button(win, text="Executer", command=excute).place(x=445, y=125,width=120,height=40)
bt_2=Button(win, text="Réinitialiser", command=reinit).place(x=445, y=175,width=120,height=40)
#------------------//


lb_txt=LabelFrame(win).place(x=445,y=30,height=80,width=120)
nb_objets = Label(lb_txt,text="Nb_objets : "+str(len(lv)))
nb_objets.place(x=455,y=50)
w_m= Label(lb_txt,text="Poids_max : "+str(weight_max[0]))
w_m.place(x=455,y=75)



win.mainloop()