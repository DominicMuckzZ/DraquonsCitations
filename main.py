import tkinter as tk

class mainApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("550x145")
        self.root.config(padx=5,pady=5)
        self.root.title("Draquon's Citation Generator")
        self.root.resizable(False,False)

        self.cNameLabel = tk.Label(self.root,text="Case Name:")
        self.reporterLabel = tk.Label(self.root,text="Reporter:")
        self.pnLabel = tk.Label(self.root,text="Page Number:")
        self.courtLabel = tk.Label(self.root,text="Court:")
        self.yearLabel = tk.Label(self.root,text="Year:")

        self.cNameEntry = tk.Entry(self.root,width=24)
        self.reporterEntry = tk.Entry(self.root,width=24)
        self.pnEntry = tk.Entry(self.root,width=24)
        self.courtEntry = tk.Entry(self.root,width=24)
        self.yearEntry = tk.Entry(self.root,width=24)

        self.outputEntry = tk.Entry(self.root,width=50)
        self.outputEntry.config(state='disabled')
        
        self.submitButton = tk.Button(self.root,text="Create Citation",command=self.createCitation)

        self.cNameLabel.grid(row=0,column=0)
        self.reporterLabel.grid(row=1,column=0)
        self.pnLabel.grid(row=2,column=0)
        self.courtLabel.grid(row=3,column=0)
        self.yearLabel.grid(row=4,column=0)

        self.cNameEntry.grid(row=0,column=1)
        self.reporterEntry.grid(row=1,column=1)
        self.pnEntry.grid(row=2,column=1)
        self.courtEntry.grid(row=3,column=1)
        self.yearEntry.grid(row=4,column=1)

        self.submitButton.grid(row=5,columnspan=2)
        self.outputEntry.grid(row=5,column=3)

    def createCitation(self):
        self.outputEntry.config(state='normal')
        self.outputEntry.delete(0,tk.END)
        
        output = self.getOutput()
        self.root.clipboard_clear()
        self.root.clipboard_append(output)

        self.outputEntry.insert(0,output)
        
        self.outputEntry.config(state='disabled')
        
    def getOutput(self):
        caseName = self.cNameEntry.get()
        reporter = self.reporterEntry.get()
        pageNumber = self.pnEntry.get()
        court = self.courtEntry.get()
        year = self.yearEntry.get()
        
        output = f"*{caseName}; {reporter} {pageNumber} ({court} {year})"
        return output


if __name__ == "__main__":
    mainApp()
