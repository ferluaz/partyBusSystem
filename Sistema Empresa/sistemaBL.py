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
from tkcalendar import *
from Relatorio import Relatorios
from Funcoes import Funcs

root = customtkinter.CTk()

class Application(Funcs, Relatorios):
    def __init__(self):
        super().__init__()
        self.root = root
        self.tela()
        self.framesDaTela()
        self.swichAltera()
        self.widgetsFrame1()
        self.widgetsTabview1()
        #self.checkFunc()
        self.listaFrame2()
        self.montaTabelas()
        self.selectLista()
        self.menus()
        root.mainloop()
    def tela(self):
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.root.title("Cadastro de clientes")
        self.root.geometry(f"{950}x{550}") #widht x hight
        #self.root.maxsize(width= 800, height= 600)
        self.root.minsize(width= 600, height= 500)
        
        self.root.grid_columnconfigure((0, 1), weight=2)
        self.root.grid_rowconfigure((0), weight=2)
    def framesDaTela(self):
        self.frame1 = customtkinter.CTkFrame(self.root, corner_radius=15,
                                            border_width=4, border_color= "#400000", 
                                            fg_color="transparent",width=475, height=550)
        self.frame1.grid(row=0, column=0, pady=5,padx=1.5, sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(self.root, corner_radius=15,
                                            border_width=4, border_color= "#400000",
                                             fg_color="transparent",width=475, height=550)
        self.frame2.grid(row=0, column=1, pady= 5, padx=1.5, sticky="nsew")

        '''self.frame3 = customtkinter.CTkFrame(self.frame1, corner_radius=15,
                                            border_width=4, border_color= "#400000")
        self.frame3.place(relx= 0.03, rely= 0.81, relwidth= 0.93, relheight= 0.17)'''
    def swichAltera(self):
        self.switchVar = customtkinter.StringVar(value="Light")
        self.switchMode = customtkinter.CTkSwitch(self.frame1,
                                                text="Baladeiro",
                                                font= ('verdana', 11, 'bold'),  
                                                command=self.change_appearance_mode_event, 
                                                variable= self.switchVar, onvalue="Dark", offvalue="Light")
        self.BeL= list()
        self.Bala = str()
        self.Limou = str()
        '''if self.switchMode.get() == "Dark":
            self.BeL.clear()
            self.Bala = "Baladeiro"
            self.BeL.append(self.Bala)
        elif self.switchMode.get() == "Light":
            self.BeL.clear()
            self.Limou = "Limousine"
            self.BeL.append(self.Limou)'''

        
        self.switchMode.place(relx=0.7, rely=0.95)
        self.switchMode.select()
    def widgetsFrame1(self):
        self.btNovo = customtkinter.CTkButton(self.frame1, text="Novo",font= ('verdana', 13, 'bold'), 
                                              border_width=2, corner_radius= 20, fg_color=("#004d87"),
                                              border_color= "#005b96",
                                              command= self.addCliente)
        self.btNovo.place(relx= 0.28, rely= 0.15, relwidth= 0.16, relheight= 0.06)

        self.btBuscar =customtkinter.CTkButton(self.frame1, text="Buscar",
                                               font= ('verdana', 12, 'bold'),
                                               border_width=2, fg_color=("#004d87"),
                                                corner_radius= 20, border_color= "#005b96",
                                               command=self.buscaCliente)
        self.btBuscar.place(relx= 0.45, rely= 0.15, relwidth= 0.16, relheight= 0.06)

        self.btAlterar = customtkinter.CTkButton(self.frame1, text="Alterar",
                                                border_width=2, fg_color=("#004d87"),
                                                corner_radius= 20, border_color= "#005b96",
                                                font= ('verdana', 12, 'bold'), command= self.alteraCliente)
        self.btAlterar.place(relx= 0.62, rely= 0.15, relwidth= 0.16, relheight= 0.06)

        self.btApagar = customtkinter.CTkButton(self.frame1, text="Apagar", 
                                                border_width=2,
                                                hover_color="#93000b",
                                                corner_radius= 20, border_color= "#800000",
                                                fg_color='#740001', font= ('verdana', 12, 'bold'), 
                                                command= self.deletaCliente)
        self.btApagar.place(relx= 0.8, rely= 0.06, relwidth= 0.17, relheight= 0.07)
        
        entryText = StringVar()
        def characterLimit(entryText):
            if len(entryText.get()) > 0:
                entryText.set(entryText.get()[:11])
        entryText2 = StringVar()
        def characterLimit2(entryText2):
            if len(entryText2.get()) > 0:
                entryText2.set(entryText2.get()[:8])
        entryText3 = StringVar()
        def characterLimit3(entryText3):
            if len(entryText3.get()) > 0:
                entryText3.set(entryText3.get()[:1])       

        self.lbCodigo = customtkinter.CTkLabel(self.frame1, text = "Código", font= ('verdana', 12, 'bold'), anchor="center")
        self.lbCodigo.place(relx= 0.05, rely=0.09)
        self.codigoEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 20,
                                                 state="normal")
        self.codigoEntry.place(relx= 0.05, rely=0.15, relwidth=0.16, relheight= 0.06)

        self.lbNome = customtkinter.CTkLabel(self.frame1, text = "Nome", font= ('verdana', 12, 'bold'))
        self.lbNome.place(relx= 0.05, rely=0.25)
        self.nomeEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 20,
                                                font= ('verdana', 12))
        self.nomeEntry.place(relx= 0.05, rely=0.31, relwidth=0.85, relheight= 0.06)
        
        self.lbLocal = customtkinter.CTkLabel(self.frame1, text = "Local", font= ('verdana', 12, 'bold'))
        self.lbLocal.place(relx= 0.05, rely=0.4)
        self.localEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 20)
        self.localEntry.place(relx= 0.05, rely=0.45, relwidth=0.85,  relheight= 0.06)

        self.lbTelefone = customtkinter.CTkLabel(self.frame1, text = "Telefone", font= ('verdana', 12, 'bold'))
        self.lbTelefone.place(relx= 0.05, rely=0.54)
        self.telefoneEntry = customtkinter.CTkEntry(self.frame1, border_width=3, 
                                                    corner_radius= 20, textvariable= entryText)
        self.telefoneEntry.place(relx= 0.05, rely=0.59, relwidth=0.4, relheight= 0.06)
        entryText.trace("w", lambda *args: characterLimit(entryText))

        self.lbData = customtkinter.CTkLabel(self.frame1, text = "Data", font= ('verdana', 12, 'bold'))
        self.lbData.place(relx= 0.5, rely=0.54)
        self.dataEntry = customtkinter.CTkEntry(self.frame1, border_width=3, 
                                                    corner_radius= 20, textvariable= entryText2)
        self.dataEntry.place(relx= 0.5, rely=0.59, relwidth=0.2, relheight= 0.06)
        entryText2.trace("w", lambda *args: characterLimit2(entryText2))
        self.sel= tkinter.StringVar()
        self.date = DateEntry(self.frame1, selectmode="day", year=2022, month=12, textvariable=self.sel)
        self.date.place(relx= 0.5, rely=0.59, relwidth=0.2, relheight= 0.06)

        self.lbDura = customtkinter.CTkLabel(self.frame1, text = "Duração", font= ('verdana', 12, 'bold'))
        self.lbDura.place(relx= 0.78, rely=0.54)
        self.duraEntry = customtkinter.CTkEntry(self.frame1, border_width=3, 
                                                    corner_radius= 20, textvariable= entryText3)
        self.duraEntry.place(relx= 0.78, rely=0.59, relwidth=0.12, relheight= 0.06)
        entryText3.trace("w", lambda *args: characterLimit3(entryText3))
        
        self.lbhrInicio = customtkinter.CTkLabel(self.frame1, text = "Horario", font= ('verdana', 12, 'bold'))
        self.lbhrInicio.place(relx= 0.05, rely=0.68)
        self.hrInicioEntry = customtkinter.CTkEntry(self.frame1, border_width=3, 
                                                    corner_radius= 20)
        self.hrInicioEntry.place(relx= 0.05, rely=0.73, relwidth=0.2, relheight= 0.06)

        self.lbValor = customtkinter.CTkLabel(self.frame1, text = "Valor", font= ('verdana', 12, 'bold'))
        self.lbValor.place(relx= 0.6, rely=0.68)
        self.valorEntry = customtkinter.CTkEntry(self.frame1, border_width=3, 
                                                    corner_radius= 20)
        self.valorEntry.place(relx= 0.6, rely=0.73, relwidth=0.3, relheight= 0.06)

        self.lbPg = customtkinter.CTkLabel(self.frame1, text = "Totalmente Pago", font= ('verdana', 12, 'bold'))
        self.lbPg.place(relx= 0.05, rely=0.82)
        self.radioVar = tkinter.IntVar(value=0)
        self.pagoStr = ""
        def radiofunc():
            if self.radioVar.get() == 1:
                try:
                    self.pagoStr = "sim"; print(self.pagoStr)
                except:
                    print("deu ruim no if")
            else:
                try:
                    self.pagoStr ="não"; print(self.pagoStr)
                except:
                    print("Deu ruim no else")
        
        self.radioButton1= customtkinter.CTkRadioButton(self.frame1,
                                                        text="Sim",command= radiofunc,
                                                        value=1,
                                                        variable= self.radioVar 
                                                        )
        self.radioButton2= customtkinter.CTkRadioButton(self.frame1,
                                                        text="Não",command= radiofunc,
                                                        value=2,
                                                        variable= self.radioVar 
                                                        )

        self.radioButton1.place(relx=0.05, rely=0.87)
        self.radioButton2.place(relx=0.2, rely=0.87)
    def widgetsTabview1(self):
        self.tabview = customtkinter.CTkTabview(self.frame2, border_width=0, corner_radius=20)
        self.tabview.place(relx= 0.05, rely= 0.69, relwidth= 0.9, relheight= 0.29)
        self.tabview.add("Extras")
        self.tabview.add("Pago")
        self.chekList = list()
        for r in self.chekList:
            if len(self.chekList) > 5:
                            self.chekList= self.chekList[:5]
                            print(f"{self.chekList} -- self.chekList# ")
        '''def checkFunc(self):
            if self.chekRosk.get() != "off":
                self.chekList.remove(self.chekRosk.get())
                self.chekList.append(self.chekRosk.get());print(self.chekList)
            elif self.checkAni.get() != "off":
                self.chekList.remove(self.checkAni.get())
                self.chekList.append(self.checkAni.get());print(self.chekList)
            elif self.checkInst.get() != "off":
                self.chekList.remove(self.checkInst.get())
                self.chekList.append(self.checkInst.get());print(self.chekList)
            elif self.checkBuf.get() != "off":
                self.chekList.remove(self.checkBuf.get())
                self.chekList.append(self.checkBuf.get());print(self.chekList)
            elif self.checkCerv.get() != "off":
                self.chekList.remove(self.checkCerv.get())
                self.chekList.append(self.checkCerv.get()); print(self.chekList)
            else:
                print("deu ruim check box")'''


        self.checkRosk = customtkinter.CTkCheckBox(self.tabview.tab("Extras"), text="Roskeiro", 
                                                    onvalue="Roskeiro", offvalue="off", command=self.checkFunc,
                                                    fg_color="#400000", font= ('verdana', 11),
                                                    hover=False)
        self.checkRosk.place(relx= 0.0, rely=0.0, relwidth= 0.24, relheight= 0.48)
        
        self.checkAni = customtkinter.CTkCheckBox(self.tabview.tab("Extras"), text="Animador", 
                                                    onvalue="Animador", offvalue="off",command=self.checkFunc2,
                                                    fg_color="#400000", font= ('verdana', 11),
                                                    hover=False)
        self.checkAni.place(relx= 0.25, rely=0.0, relwidth= 0.24, relheight= 0.48)

        self.checkInst = customtkinter.CTkCheckBox(self.tabview.tab("Extras"), text="Instrutor", 
                                                    onvalue="Instrutor", offvalue="off",command=self.checkFunc3,
                                                    fg_color="#400000", font= ('verdana', 11),
                                                    hover=False)
        self.checkInst.place(relx= 0.0, rely=0.6, relwidth= 0.24, relheight= 0.48)

        self.checkBuf = customtkinter.CTkCheckBox(self.tabview.tab("Extras"), text="Buffet", 
                                                    onvalue="Buffet", offvalue="off",command=self.checkFunc4,
                                                    fg_color="#400000", font= ('verdana', 11),
                                                    hover=False)
        self.checkBuf.place(relx= 0.25, rely=0.6, relwidth= 0.24, relheight= 0.48)

        self.checkCerv = customtkinter.CTkCheckBox(self.tabview.tab("Extras"), text="Cerveja", 
                                                    onvalue="Cerveja", offvalue="off",command=self.checkFunc5,
                                                    fg_color="#400000", font= ('verdana', 11),
                                                    hover=False)
        self.checkCerv.place(relx= 0.5, rely=0.0, relwidth= 0.24, relheight= 0.48)

    def listaFrame2(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure('Treeview',
                        background = "#9ba7ba",
                        foreground= "white",
                        rowheight=25,
                        fieldbackground="white" ,   
                        )
        self.style.configure('Treeview.Heading',
                        background = "#444444",
                        foreground= "white",
                        fieldbackground="#444444" ,   
                        relief= "flat"   
                        )
        
        self.style.map("Treeview.Heading", background=[('active', "#444444")])
                        
        self.style.map('Treeview',
                 background=[('selected', '#693a3a')]
                 )
                
        self.scrooLista = customtkinter.CTkScrollbar(self.frame2, orientation='vertical')
        self.scrooLista2 = customtkinter.CTkScrollbar(self.frame2, orientation='horizontal')
        self.scrooLista.place(relx= 0.96, rely=0.02, relheight=0.65, relwidth=0.03)
        self.scrooLista2.place(relx= 0.015, rely=0.67, relheight=0.03, relwidth=0.9)
        
        self.listaCli = ttk.Treeview(self.frame2,column=("col1","col2","col3","col4","col5",
                                                        "col6","col7","col8","col9","col10", "col11"))
        self.listaCli.place(relx= 0.015, rely= 0.02, relwidth= 0.9, relheight= 0.65)
        #self.listaCli.pack(fill="both")
        
        self.listaCli.heading("#0", text="", anchor=W)
        self.listaCli.heading("#1", text="Codigo", anchor=W)
        self.listaCli.heading("#2", text="Nome", anchor=W)
        self.listaCli.heading("#3", text="Telefone", anchor=W)
        self.listaCli.heading("#4", text="Local", anchor=W)
        self.listaCli.heading("#5", text="Data", anchor=W)
        self.listaCli.heading("#6", text="Valor total", anchor=W)
        self.listaCli.heading("#7", text="Duração", anchor=W)
        self.listaCli.heading("#8", text="Extras", anchor=W)
        self.listaCli.heading("#9", text="Hora de inicio", anchor=W)
        self.listaCli.heading("#10", text="Completamente Pago", anchor=W)
        self.listaCli.heading("#11", text="Baladeiro ou limou", anchor=W)

        self.listaCli.column("#0", width=1, minwidth=25, stretch=NO)
        self.listaCli.column("#1", width=50, minwidth=0, stretch=NO)
        self.listaCli.column("#2", width=200, minwidth=0, stretch=NO)
        self.listaCli.column("#3", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#4", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#5", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#6", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#7", width=50, minwidth=0, stretch=NO)
        self.listaCli.column("#8", width=200, minwidth=0, stretch=NO)
        self.listaCli.column("#9", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#10", width=100, minwidth=0, stretch=NO)
        self.listaCli.column("#11", width=150, minwidth=0, stretch=NO)
    
        self.listaCli.configure(yscrollcommand=self.scrooLista.set, xscrollcommand=self.scrooLista2.set)
        self.scrooLista.configure(command=self.listaCli.yview)
        self.scrooLista2.configure(command=self.listaCli.xview)
        #self.listaCli.configure(xscrollcommand=self.scrooLista2.set)
        self.listaCli.bind("<Double-1>", self.onDoubleClick)
    def menus(self):
        def quit(): self.root.destroy()
        
        self.filemenu2 = customtkinter.CTkOptionMenu(self.frame1, values=["Opções:","Ficha do cliente","Relatório ano",
                                                                        "Relatório mês", "Limpar Tela", "Sair"], 
                                                    button_color=("#444444"),
                                                    fg_color=("#444444"),
                                                    button_hover_color=("gray"),
                                                    dropdown_hover_color=("#693a3a"),
                                                    dropdown_font=('verdana', 11),
                                                    corner_radius=20, 
                                                    font=('verdana', 12,'bold'),
                                                    anchor=("w"),
                                                    dynamic_resizing=True,
                                                    command=self.listaComand)
        self.filemenu2.place(relx= 0.01, rely= 0.01, relwidth= 0.3, relheight= 0.05)


Application()
