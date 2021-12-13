from tkinter import *
# from tkinter import ttk
def help_windows_handler():
    help_root = Tk()
    help_root.title("Help")
    help_root.wm_iconbitmap("icon//automate.ico")
    help_root.geometry("700x400+300+180")
    help_root.config(bg='silver')


#----------------------------------- add TextArea----------------------------
# global HelpTextArea
    HelpTextArea=Text(help_root,font='georgia 15')
    HelpTextArea.pack(expand=True,fill=BOTH)

# #----------------------------------- add scroll bar----------------------------
    Scroll = Scrollbar(HelpTextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=HelpTextArea.yview)


    content='''\t\t\bAutoText Editor  \b

* Scope of Application *
   1.Create a new file 
   2.General file operations
   3.Text translator
   4.Speech recognition
   5.Switching mode of theme
   6.about
   7.help

   How to use these features:-
   
    1.Create a new file:
       -click on file menu bar
       -click in new file tab
        alt
       * new file opened by default
       
    2.General file operations:
      -user can perform all file operations
       like-create,open,delete,save,print
       cut,copy,paste.
              
    3.Text translator:
      -In this feature user can able to translte english
       text in to any of the language which is choosed by
       user.
       steps for use:
        -click on translator tab
        -choose the destination of language
        -click on translate button
    
    4.Speech Recognition:
      -In this feature user can able to typing by their 
       voice.
       steps for use:
        -click on speak tab
        -system will notify to user 
         ready for getting voice 
        -click on ok and then speak out.   
        
    5.Switching the Themes:
      -In this feature user can change theme of AutoText
       Editor.
      -there are only two mode of theme 
       1.dark mode
       2.light mode
    
    6.About:
      -It shows information about AutoText Editor.     
       
'''

    HelpTextArea.insert(END,content)
    HelpTextArea.config(yscrollcommand=Scroll.set, bg='silver',state='disable')

# formating of title of editor
    HelpTextArea.tag_add("start", "1.3", "1.18")
# configuring a tag called start
    HelpTextArea.tag_config("start", background="cyan",font="georgia 25 bold",
                foreground="green")



# ------------------- ----------Tank you button -------------------------------------
    button=Button(help_root,text="Thank You",bg="magenta",activebackground="green",
                 width="10",height="1",command=help_root.destroy)

    button.place(x=300, y=350)
    help_root.resizable(False,False)
    help_root.mainloop()
