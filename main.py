import tkinter
from tkinter import *
from win32com.client import Dispatch
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
from googletrans import Translator,LANGUAGES
import speech_recognition as sr

# ********************************************************************************************************************************
#  -----------------------------------------   function of File Menu   ----------------------------------------------------------
#  -----------------------------------------   newfile function   ---------------------
def newFile():
    global file
    root.title("*Untitle -AutoText")
    file=None
    TextArea.delete(1.0,END)
#  -----------------------------------------   open function   ------------------------
def openFile():
    global file
    if file == None or file!=None:
        file = askopenfilename(defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + "-AutoText")
            TextArea.delete(1.0,END)
            f=open(file,"r")
            TextArea.insert(1.0,f.read())
            f.close()
#  -----------------------------------------   save function   ---------------------
def saveFile():
    global file
    try:
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt',
                                 defaultextension=".txt",filetypes=[("Text Documents","*.txt"),("All Files","*.*")])
            if file == "":
                file=None
            else:
                # save as new file
                f=open(file,"w")
                f.write(TextArea.get(1.0,END))
                root.title(os.path.basename(file) + "-AutoText")
                print("file saved")
        else:
            # save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
    except:
        print('some error with file saving...')

#  -----------------------------------------   saveAs function   ---------------------
def saveAsFile():
    global file
    try:
        file = asksaveasfilename(defaultextension=".txt",
                                 filetypes=[("Text Documents","*.txt"),("All Files","*.*")])
        data = TextArea.get(1.0, END)
        file .write(data)
        file.close()
    except:
         print('some error about file save as file ')

# -----------------------------------print current file------------------------
def printFile():
    try:
        win32api.ShellExecute(0,'print', file, None, ".", 0)
    except:
        messagebox.showerror("Print Error","Please Save File!")
        saveFile()

#----------------------------------------2 function of edit menu------------------------------------------------------------------
def cutFile():
    TextArea.event_generate("<<Cut>>")
def copyFile():
    TextArea.event_generate("<<Copy>>")
def pasteFile():
    TextArea.event_generate("<<Paste>>")
def select_All():
        TextArea.event_generate("<<SelectAll>>")
def deleteFile():
    TextArea.delete(1.0,END)
#   --------------------------------dropdown.--------------------------------------------------------------------------------------
def text_translator():
    try:
        inputData=TextArea.get("1.0",END)
        translater = Translator()
        out = translater.translate(inputData,dest="hi")

        TextArea.delete('1.0',END)
        TextArea.insert("1.0",out.text)
    except:
      messagebox.showinfo("Error",'please check network!')
#     ------------------------------------------------Typing By Voice---------------------------------------------------------------
def text_by_voice():
    r=sr.Recognizer()
    try:
        inputData = len(TextArea.get("1.0", END))
        messagebox.showinfo('speak', 'please speak...')
        with sr.Microphone() as source:
            audio = r.listen(source)
            messagebox.showinfo("Loading...", 'Recognizing...')
            text=r.recognize_google(audio)
            if inputData==1:
                TextArea.insert('1.0', '{}'.format(text))
            else:
                TextArea.insert(END,'{}'.format(" "+text))
    except:
            messagebox.showerror('Recognition Error',"sorry!, check net connection and \n Try agian!")

def speak_by_machine():
    inputData = TextArea.get("1.0", END)
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(inputData)
# -----------------------------------View Theme Functions--------------------------------------------------------------------------------

def choose_LightTheme():
    TextArea.config(bg='white',fg='black',insertbackground='black')

def choose_DarkTheme():
    TextArea.config(bg='black',fg='white',insertbackground='white')


# -----------------------------------About function--------------------------------------------------------------------------------
def about():
    messagebox.showinfo("About","Hello user this Automate Text Editor Developed by @mangesh")

#  -----------------------------------Help Function--------------------------------------------------------------------------------
def help():
    # bg=PhotoImage(file="icon//")
    # bg_label=Label(root,image=bg).pack()
    # text_label=Label(root,text="")
    import Help
    try:
        Help.help_windows_handler()
    except:
        messagebox.showerror('call back error','call back error')
        print('call back error!')

    # messagebox.showinfo("Help","Welcome To Automate Text Editor!\n"
    #                            "Here Some Scope of this App:\n"
    #                            "1.File Operation\n"
    #                            "2.Text Translator\n"
    #                            "3.Speech Recognization\n"
    #                            "4.Theme Changing etc")
#     ----------------------------------------pop menu---------------------------------------------
def pop_menu(event):
    sub_menu.tk_popup(event.x_root,event.y_root)
# =================================================================================================================================
#                                                     Driver code
# ----------------------------------------------------------------------------------------------------------------------------------


global root
root=Tk()
root.title("*Untitle -AutoText")
root.wm_iconbitmap("icon//automate.ico")#-------set Icon-----------
root.geometry("900x500+200+100")

# ---------------------------------------------- -add textArea-----------------------------------------------------------
global TextArea
TextArea=Text(root,font='georgia 15',undo=True)
TextArea.pack(expand=True,fill=BOTH)
TextArea.config(bg='silver')
file = None

#-----------------------------------------------------------add scroll bar---------------------------------------------------------
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

# ------------------------------------------------add menubar------------------------------------------------------------

MenuBar=Menu(root)
#------------------------------------------------1 add menu on menubar
FileMenu=Menu(MenuBar,tearoff=0)

# -------------------------open new file
# new_icon=root.PhotoImage(file="icon//new_file.ico")
FileMenu.add_command(label="New",accelerator="Ctr+n",command=newFile)
#------------------------- open existing file
FileMenu.add_command(label="Open", accelerator="Ctr+o",command=openFile)
# -------------------------save current file
FileMenu.add_command(label="Save",accelerator="Ctr+s", command=saveFile)
# -------------------------save current file
FileMenu.add_command(label="SaveAs", accelerator="Ctr+alt+s", command=saveAsFile)
# --------------------------print current file
FileMenu.add_command(label="Print",accelerator="Ctr+p",command=printFile)
FileMenu.add_separator()#---------------add seperator
# ---------------------------exist editor
FileMenu.add_command(label="Exit",command=root.destroy)
# -------------------------------------------------add File Menu
MenuBar.add_cascade(label="File",menu=FileMenu)

# -------------------------------------------------2.Add Edit menu on Menubar
EditMenu=Menu(MenuBar,tearoff=0)

# ----------------------------undo content file
EditMenu.add_command(label="Undo", accelerator="Ctr+z", command=TextArea.edit_undo)
# ----------------------------Redo content file
EditMenu.add_command(label="Redu", accelerator="Ctr+y", command=TextArea.edit_redo)
# ----------------------------cut content file
EditMenu.add_command(label="Cut",accelerator="Ctr+x",command=cutFile)
# ----------------------------copy content file
EditMenu.add_command(label="Copy",accelerator="Ctr+c", command=copyFile)
# ----------------------------paste content file
EditMenu.add_command(label="Paste",accelerator="Ctr+v", command=pasteFile)
EditMenu.add_separator()
# ---------------------------- Delete editor
EditMenu.add_command(label="Delete",accelerator="delete",command=deleteFile)
MenuBar.add_cascade(label="Edit", menu=EditMenu)

#----------------------------------------------------3 Translator menu on menubar
TranslatorMenu=Menu(MenuBar,tearoff=0)
 # --translate content of file--
TranslatorMenu.add_command(label="Translate", command=text_translator)
MenuBar.add_cascade(label="Translate", menu=TranslatorMenu)


 #-----------------------------------------------------4 Speak menu add on menubar
SpeakMenu = Menu(MenuBar, tearoff=0)
SpeakMenu.add_command(label="Speak", command=text_by_voice)

SpeakMenu.add_command(label="Read", command=speak_by_machine)

MenuBar.add_cascade(label="Speak", menu=SpeakMenu)

#------------------------------------------------------5 View menu add on menubar

ViewMenu = Menu(MenuBar, tearoff=0)

ViewMenu.add_command(label='light mode',command=choose_LightTheme)
ViewMenu.add_command(label='Dark mode',command=choose_DarkTheme)

MenuBar.add_cascade(label="View", menu=ViewMenu)

#------------------------------------------------------6 About menu add on menubar
AboutMenu = Menu(MenuBar, tearoff=0)
AboutMenu.add_command(label="About", command=about)
MenuBar.add_cascade(label="About", menu=AboutMenu)

#-------------------------------------------------------7 Help manu add on menubar
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="Help", command=help)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
# -------------------------------------------------------add menues on menubar-------------------------------------------
root.config(menu=MenuBar)


# ============================================================sub menu in textArea=========================================================

sub_menu=Menu(TextArea,tearoff=0,bg="black",fg='white')
# menu option
sub_menu.add_command(label="Cut",accelerator='ctr+x',command=cutFile)
sub_menu.add_command(label="Copy",accelerator='ctr+c',command=copyFile)
sub_menu.add_separator()
sub_menu.add_command(label="Paste",accelerator='ctr+v',command=pasteFile)
sub_menu.add_command(label="Select All",accelerator="ctr+a",command=select_All)
TextArea.bind("<Button - 3>",pop_menu)

# ============================================================mainloop=========================================================

root.mainloop()


