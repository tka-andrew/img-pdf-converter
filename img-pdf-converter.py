import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
# from pdf2image import convert_from_path, convert_from_bytes
# from pdf2image.exceptions import (
#     PDFInfoNotInstalledError,
#     PDFPageCountError,
#     PDFSyntaxError
# )

class ImgPdfConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Img-Pdf-Converter App")
        self.geometry('800x300')

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        # buttons
        self.img2pdf_button = ttk.Button(self, text='Convert Images To PDF')
        self.img2pdf_button['command'] = self.img_to_PDF
        self.img2pdf_button.pack(**options)

        self.pack(**options)

    # REFERENCE: https://datatofish.com/images-to-pdf-python/
    def img_to_PDF(self):
        
        files = filedialog.askopenfilenames(filetypes=(("image files", "*.png *.jpg *.jpeg"), ("jpeg files", "*.jpeg *jpg"), ("png files", "*.png")))
        if len(files) == 0:
            return
        
        StorePDFPath = filedialog.askdirectory()
        if StorePDFPath == "":
            return
        
        SelectedImageStringList = list(files) #these are automatically sorted according to name
        SelectedImageList = []
        for imgString in SelectedImageStringList:
            SelectedImageList.append(Image.open(imgString).convert('RGB'))
        im1 = SelectedImageList[0]
        SelectedImageList.pop(0)
        im1.save(StorePDFPath + '/ProcessedPDF.pdf', save_all=True, append_images=SelectedImageList)
        PopUpText="Processed PDF saved to: " + StorePDFPath
        self.popupmsg(PopUpText)
    
    def popupmsg(self,msg):
        popup = tk.Tk()
        popup.wm_title("Saving info")
        NORM_FONT = ("Helvetica", 10)
        label = tk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

if __name__=="__main__":
    app = ImgPdfConverterApp()
    mainFrame = MainFrame(app)
    app.mainloop()