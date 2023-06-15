from tkinter import *
import openai
import os
import random
import pywhatkit

BG_COLOR = "#1f2833"
TEXT_COLOR = "#66fcf1"

FONT = "Helvetica 15"
FONT_BOLD = "Helvetica 13 bold"
botName="Saber"

openai.api_key="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"


class ChatApp:
    def __init__(self):
        self.win = Tk()
        # calling setup function in constructor to initilize when app is start
        self._setup_main_window()

    def run(self):
        # slef is similer to super in java i.e it call variable of class
        self.win.mainloop()

    def _setup_main_window(self):
        self.win.title = "Saber"
        self.win.geometry("800x550")
        self.win.configure(bg=BG_COLOR)

        # label
        l1 = Label(self.win, text="Welcome", bg=BG_COLOR,
                   fg=TEXT_COLOR, font=FONT_BOLD, pady=20)
        l1.place(relheight=0.12,relwidth=1)
        

        
        #TextBox
        #tBox is instance variable here as we need it in other function
        self.tBox=Text(self.win,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,
                  border=5,font=FONT,padx=5,pady=5)
        # relheight=0.75 means tbox wedgit will take 75% heigh of hight of whole appliaction
        #imagaine rely=0.1 =10% margin from top(parent of tBox which is win)
        self.tBox.place(relheight=0.75,relwidth=1,rely=0.1)
        self.tBox.configure(cursor="arrow",state=DISABLED)

        #scrollBar
        scrollBar=Scrollbar(self.tBox)
        # here parent of scrollbar is tbox 
        # we want scrollBar at right side so relx=97%
        scrollBar.place(relheight=1,relx=0.99)

        #bottom label
        bottom_label=Label(self.win,height=80)
        bottom_label.place(relwidth=1,rely=0.825)

        #message box(instance variable)
        self.msg_entry=Entry(bottom_label,bg="#2c3e50",font=FONT,fg=TEXT_COLOR)
        self.msg_entry.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self.onEnterPressed)

        #button
        btn=Button(bottom_label,text="Send",font=FONT_BOLD,width=20,
                   command=lambda:self.onEnterPressed(None))  
        btn.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)  

    def search(self,ques):
        model1="text-davinci-003"
         
        if "exit" in ques:
            exit()
        completion = openai.Completion.create(
            model=model1,
            prompt=ques,
            max_tokens = 1024,
            temperature = 0.5,
            n=3,
            stop=None
            )

        response=completion.choices[0].text

        return response
    
   

    def onEnterPressed(self,event):
    
        msg=self.msg_entry.get()
        

        if 'play music' in msg:
            music_dir="C:\\Users\\Brain Box\\Music\\music"
            song=os.listdir(music_dir)
            n=len(song)
            r=random.randrange(0,n)
            os.startfile(os.path.join(music_dir,song[r]))

        elif 'youtube' in msg:
            query = msg.replace("youtube", " ")
            pywhatkit.playonyt(query)   

        ans=self.search(msg)

        self.insertMssg(msg,"You",ans)

    

    def insertMssg(self,msg,sender,ans):
        if not msg:
            return

        #from 0 to end we want text then show it
        self.msg_entry.delete(first=0,last=END) 
        msg1=f"{sender} : {msg}\n\n"
        #fisrt eble tbox then insert output text then again disable it
        self.tBox.configure(state=NORMAL)
        self.tBox.insert(END,msg1)
        self.tBox.configure(state=DISABLED)

        msg2=f"{botName} : {ans}\n\n"
        #fisrt eble tbox then insert output text then again disable it
        self.tBox.configure(state=NORMAL)
        self.tBox.insert(END,msg2)
        self.tBox.configure(state=DISABLED)

    def defualtMssg(self):
        msg="Saber : Hii There!,I am Saber,I am here to help you,Type any question in below text Area\nExample:\ni)To Play Music <SONG_NAME>\nii)To open vedio on Youtube \nii)Search Any querry\n\n"
        #fisrt eble tbox then insert output text then again disable it
        self.tBox.configure(state=NORMAL)
        self.tBox.insert(END,msg)
        self.tBox.configure(state=DISABLED)
    




# main method
if __name__ == "__main__":
    # calling mainloop functoin
    app = ChatApp()  # at the time of object creation consturctor is call which will inkove two function then mainloop will start
    app.defualtMssg()
    app.run()
