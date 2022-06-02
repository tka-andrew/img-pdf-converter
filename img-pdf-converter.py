from sys import platform
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from pdf2image import convert_from_path

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
        self.img2pdf_button = ttk.Button(self, text='Convert images To PDF')
        self.img2pdf_button['command'] = self.img_to_PDF
        self.img2pdf_button.pack(**options)

        self.pdf2img_button = ttk.Button(self, text="Convert PDF to images")
        self.pdf2img_button['command'] = self.PDF_to_img
        self.pdf2img_button.pack(**options)

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
        if platform == "linux" or platform == "linux2":
            im1.save(StorePDFPath + '/ProcessedPDF.pdf', save_all=True, append_images=SelectedImageList)
        elif platform == "win32":
            im1.save(StorePDFPath + '\ProcessedPDF.pdf', save_all=True, append_images=SelectedImageList)
        PopUpText="Processed PDF saved to: " + StorePDFPath
        self.popupmsg(PopUpText)

    def PDF_to_img(self):
        FILEOPENOPTIONS = dict(defaultextension=".pdf",
                               filetypes=[('pdf file', '*.pdf')])
        PDFpath = filedialog.askopenfilename(**FILEOPENOPTIONS)
        print("PDFpath", PDFpath)
        self.PDF_name = PDFpath.split("/")[-1]
        if PDFpath:
            if len(PDFpath) > 0:
                pil_images = convert_from_path(PDFpath)
                self.save_images(pil_images)
    
    def save_images(self, pil_images):
        # This method helps in converting the images in PIL Image file format to the required image format
        index = 1
        StoreImagePath = filedialog.askdirectory()
        if StoreImagePath == "":
            return
        for image in pil_images:
            if platform == "linux" or platform == "linux2":
                image.save(StoreImagePath + "/page_" + str(index) + ".png")
            elif platform == "win32":
                image.save(StoreImagePath + "\page_" + str(index) + ".png")
            index += 1
        #self.save_info.configure(text="Save as: \t"  +StoreImagePath + "\page_" + str(index) + ".png")
        PopUpText="Images saved to: " + StoreImagePath
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