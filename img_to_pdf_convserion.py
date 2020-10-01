import os
import datetime
import img2pdf
from tkinter import messagebox,filedialog, Button
import tkinter as tk

        
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
        
    def create_widgets(self):
        self.img_to_pdf = Button(self, text = "Convert image to pdf", command = self.file_opener)
        self.img_to_pdf.pack(side='top')
        self.quit = Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def file_opener(self):
        input = filedialog.askopenfilenames(initialdir="/", title = "Select Image")
        file_name = os.path.join(filedialog.askdirectory(), str(datetime.datetime.now().date()).replace('-', '')+'_'+ str(datetime.datetime.now().time()).replace(':','').replace('.', '')+'.pdf')
        try:
            with open(file_name, 'wb') as f:
                layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297)))
                f.write(img2pdf.convert(list(input), layout_fun = layout))
                messagebox.showinfo("info",'Successfully Saved at '+file_name)
        except:
            messagebox.showerror("Error", 'Could not convert')
                    
root = tk.Tk()

app = Application(master=root)
app.master.title("Img_to_pdf")
app.mainloop()
            
        
        
        
    
            
    
        
        
    
        
    


