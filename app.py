from tkinter import *
from chat import get_response, bot_name

BG_GRAY = "#122742"
BG_COLOR = "#bafacb"
TEXT_COLOR = "#122742"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chatbot")
        # self.window.iconbitmap("chat_icon.ico")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=470,height=550,bg=BG_COLOR)
        
        #head label
        head_label = Label(self.window,bg = BG_COLOR, fg =TEXT_COLOR,
                              text = "Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
                
        
        #tiny divider
        line = Label(self.window,width=450,bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07,relheight=0.012)
        
        #text widget
        self.text_widget = Text(self.window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,
                                font=FONT,padx=5,pady=5)
        
        self.text_widget.place(relheight = 0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)
        
        #scroll bar
        scrollbar = Scrollbar(self.text_widget,)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        #bottom label
        bottom_label = Label(self.window, bg = BG_GRAY, height=80)
        bottom_label.place(relwidth=1,rely=0.825)
        
        #message entry box
        self.msg_entry = Entry(bottom_label,bg="#122742",fg="#bafacb",font=FONT)
        self.msg_entry.place(relwidth=0.60,relheight=0.06,rely=0.008,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)
        
        #clear button
        clear_button = Button(bottom_label, text="Clear Chat", font=FONT_BOLD, width=20, bg=BG_COLOR,
                      command=lambda: self._clear_chat())
        clear_button.place(relx=0.55, rely=0.008, relheight=0.06, relwidth=0.22)
        
        #button widget
        send_button = Button(bottom_label, text="Send",font=FONT_BOLD,width=20,bg=BG_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
        
    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _clear_chat(self):
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete('1.0', END)
        self.text_widget.configure(state=DISABLED)
        
    def _insert_message(self,msg,sender):
        if not msg:
            return 
        
        self.msg_entry.delete(0,END)
        
        msg1=f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1, ('sender'))
        self.text_widget.configure(state=DISABLED)
    
        msg2=f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2, ('bot'))
        self.text_widget.configure(state=DISABLED)
        
        # configure tags for alignment and other properties
        self.text_widget.tag_config('sender', foreground='#122742')
        self.text_widget.tag_config('bot', foreground='#163c00')
            
        self.text_widget.see(END)
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()