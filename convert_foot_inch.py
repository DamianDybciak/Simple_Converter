# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:06:38 2021

@author: Damian Dybciak
"""



import tkinter as tk

import codecs



class CM:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Zmien na cm ')
        self.root.geometry('300x200')
        self.text1 = tk.StringVar()
        self.text2 = tk.StringVar()
        
        self.label1 = tk.Label(self.root, text='stopy: ')
        self.label1.grid(column=0, row=0)
        
        self.label2 = tk.Label(self.root, text='cale: ')
        self.label2.grid(column=0, row=1)
        
        self.entry1 = tk.Entry(self.root, textvariable=self.text1)
        self.entry1.grid(column=1, row=0)
        
        self.entry2 = tk.Entry(self.root, textvariable=self.text2)
        self.entry2.grid(column=1, row=1)
        
        
        
        self.button = tk.Button(self.root, text='Zmień na cm ', command=self.na_cm)  
        self.button.grid(column=1, row=2, columnspan=2)
        
        
        
    def na_cm(self):
        dane1 = int(self.text1.get())
        dane2 = int(self.text2.get())
        if dane1 <0 or dane2<0:
            
            tk.messagebox.showinfo('Błąd','niepoprawne dane  ')
            
        else:
            cm = round(((dane2*2,54)+(dane1*30,48)),0)
            tk.messagebox.showinfo('centymetry',cm)
            
            
            
            
    
  
    def run(self):
        
        self.root.mainloop()
        '''
        mainloop obsługuje wszystkie czynnosci w okienku
        '''
        
        
        
        
        
if __name__ == '__main__':
    zmiana = CM()
    zmiana.run()