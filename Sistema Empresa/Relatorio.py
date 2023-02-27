from tkinter import *
import tkinter
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import customtkinter
import time

class Relatorios():
   def variaveis(self):
                  #entry
      self.codigo   = self.codigoEntry.get()
      self.nome     = self.nomeEntry.get()
      self.telefone = self.telefoneEntry.get()
      self.local    = self.localEntry.get()
      self.data     = self.dataEntry.get()
      self.dura     = self.duraEntry.get()
      self.hrInicio = self.hrInicioEntry.get()
      self.valor    = self.valorEntry.get()
                  #Radiobuttom
      self.pago     = self.pagoStr
                  #switch
      self.qual     = str(self.BeL)
      c0 = "x"
      while c0 == "x":
         self.qual = self.qual.replace("[","")
         self.qual = self.qual.replace("]","")
         self.qual = self.qual.replace("'","")
         c0="y"
                  #extras checkbox
      self.rosk     = self.checkRosk.get()
      self.ani      = self.checkAni.get()
      self.inst     = self.checkInst.get()
      self.buf      = self.checkBuf.get()
      self.cerv     = self.checkCerv.get()
      self.ListExt  = str(self.chekList)
      self.chekList2 = self.ListExt.split(",")
      c = "x"
      while c == "x":
         self.ListExt = self.ListExt.replace("[","")
         self.ListExt = self.ListExt.replace("]","")
         self.ListExt = self.ListExt.replace("'","")
         self.ListExt = self.ListExt.replace(" ","")
         c="y"
   def printCliente(self):
      webbrowser.open("clienteBL.pdf")
   def geraRelatClient(self):
      self.c = canvas.Canvas("clienteBL.pdf")
      self.variaveis()
      if len(self.codigo) >=1:
         self.c.setFont("Helvetica-Bold", 24)
         self.c.drawString(200, 790, 'Ficha do Cliente')

         self.c.setFont("Helvetica-Bold", 18)
         self.c.drawString(50, 700, f"Codigo: ")
         self.c.drawString(50, 670, f"Nome: ")
         self.c.drawString(50, 640, f"Telefone: ")
         self.c.drawString(50, 610, f"Local: ")
         self.c.drawString(50, 580, f"Data: ")
         self.c.drawString(50, 550, f"Duração: ")
         self.c.drawString(50, 520, f"Hora de inicio: ")
         self.c.drawString(50, 490, f"Extras: ")
         self.c.drawString(50, 460, f"Veiculo: ")
         self.c.drawString(50, 430, f"Pago: ")
         self.c.drawString(50, 400, f"Valor Total: ")
         
         self.listaCli.selection()
         for n in self.listaCli.selection():
            col1, col2, col3, col4, col5,col6,col7,col8,col9,col10,col11=self.listaCli.item(n, 'values')
            self.c.setFont("Helvetica", 18)
            self.c.drawString(200, 700, col1)
            self.c.drawString(200, 670, col2)
            self.c.drawString(200, 640, col3)
            self.c.drawString(200, 610, col4)
            self.c.drawString(200, 580, col5)
            self.c.drawString(200, 550, f"{col7} h")
            self.c.drawString(200, 520, col9)
            self.c.drawString(200, 490, col8)
            self.c.drawString(200, 460, col11)
            self.c.drawString(200, 430, col10)
            self.c.drawString(200, 400, f"R$ {col6}")
            break
      #rect(distancia direita, altura, distancia esquerda,)
         self.c.rect(20, 750, 550, 5, fill= True, stroke= False)
         self.c.rect(20, 350, 550, 5, fill= True, stroke= False)
         self.c.showPage()
         self.c.save()
      
         self.printCliente()
      else:
         print("Erro ===> ficha cliente")