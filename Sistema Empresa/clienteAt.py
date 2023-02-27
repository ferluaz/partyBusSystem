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
from dataclasses import dataclass


root = customtkinter.CTk()

class Relatorios():
     def printCliente(self):
        webbrowser.open("cliente.pdf")
     def geraRelatClient(self):
        self.c = canvas.Canvas("cliente.pdf")
        
        self.codigoRel = self.codigoEntry.get()
        self.nomeRel = self.nomeEntry.get()
        self.telefoneRel = self.telefoneEntry.get()
        self.cidadeRel = self.cidadeEntry.get()
        if len(self.codigoRel) >=1:
            self.c.setFont("Helvetica-Bold", 24)
            self.c.drawString(200, 790, 'Ficha do Cliente')

            self.c.setFont("Helvetica-Bold", 18)
            self.c.drawString(50, 700, f"Codigo: ")
            self.c.drawString(50, 670, f"Nome: ")
            self.c.drawString(50, 640, f"Telefone: ")
            self.c.drawString(50, 610, f"Cidade: ")
        
            self.c.setFont("Helvetica", 18)
            self.c.drawString(150, 700, self.codigoRel)
            self.c.drawString(150, 670, self.nomeRel)
            self.c.drawString(150, 640, self.telefoneRel)
            self.c.drawString(150, 610, self.cidadeRel)
         #rect(distancia direita, altura, distancia esquerda,)
            self.c.rect(20, 550, 550, 5, fill= True, stroke= False)
            self.c.showPage()
            self.c.save()
        
            self.printCliente()
        else:
            print("Error")

class Funcs():
    def cores(self):
        self.cor1  = '#04578e'
        self.cor2  = '#bcd6ef'
        self.cor3  = '#97bad9'
        self.cor4  = '#191970'
        self.cor5  = '#4682B4'   
        self.cor6  = '#ebcad9'
        self.cor7  = '#002f51'
        self.cor8  = '#7393B3'
        self.cor9  = '#f8f4f4'
        self.cor10 = '#'
        self.cor11 = '#'
        self.cor12 = '#'
    def listaComand(self, comand):
        if self.filemenu2.get() == "Ficha do cliente":
            self.geraRelatClient()
            print('estou na op gerar clientes',comand)
            time.sleep(1)
            self.filemenu2.set("Opções:")
            
        elif self.filemenu2.get() == "Sair":
            print("estou na op sair",comand)
            quit()
        elif self.filemenu2.get() == "Limpar Tela":
            print("estou no limpa tela")
            self.limpaTela()
            time.sleep(1)
            self.filemenu2.set("Opções:")             
    def alteraCores(self):
                            #Frames#
        self.frame1.configure(corner_radius=15,
                             border_width=4, border_color= "#28889c", 
                             fg_color="transparent",width=700, height=250)
        self.frame2.configure(corner_radius=15,
                             border_width=4, border_color= "#28889c", 
                             fg_color="transparent",width=700, height=250)
                            #Botões#            
        self.filemenu2.configure(button_color=("#999fa1"),
                                fg_color=("#999fa1"),
                                text_color=("white"),
                                button_hover_color=("#999fa1"),
                                dropdown_hover_color=("#76b3ec"))
                
        self.btLimpar.configure( fg_color= ("#0075cd"))
        self.btBuscar.configure( fg_color= ("#0075cd"))                       
        self.btNovo.configure(fg_color= ("#0075cd"))
        self.btAlterar.configure( fg_color= ("#0075cd"))
        self.btApagar.configure( fg_color= ("#c3010c"))
                            #Switch#
        self.switchMode.configure(button_color="#0075cd",
                                 border_width=2,
                                 border_color="#005b96", 
                                 fg_color="white",
                                 button_hover_color="#0075cd",
                                 text="Dark Mode off")
                            #Treeview#
        self.style.configure('Treeview',
                        background = "white",
                        foreground= "black",
                        rowheight=25,
                        fieldbackground="#9ba7ba" ,   
                        )
        self.style.configure('Treeview.Heading',
                        background = "#999fa1",
                        foreground= "white",
                        fieldbackground="#999fa1" ,   
                        relief= "flat",   
                        ) 
        self.style.map('Treeview',
                      background=[('selected', '#76b3ec')])
        self.style.map('Treeview.Heading',
                       background=[('selected', '#999fa1')])   
    def desalteraCores(self):    
                            #Frames#
        self.frame1.configure(corner_radius=15,
                             border_width=4, border_color= "#400000", 
                             fg_color="transparent",width=700, height=250)
        self.frame2.configure(corner_radius=15,
                             border_width=4, border_color= "#400000", 
                             fg_color="transparent",width=700, height=250)                       
                            #Botões#
        self.filemenu2.configure(button_color=("#444444"),
                                fg_color=("#444444"),
                                text_color=("white"),
                                button_hover_color=("#444444"),
                                dropdown_hover_color=("#693a3a")) 
        self.btLimpar.configure(fg_color= ("#004d87"))
        self.btNovo.configure(fg_color= ("#004d87")) 
        self.btAlterar.configure(fg_color= ("#004d87")) 
        self.btBuscar.configure(fg_color= ("#004d87")) 
        self.btApagar.configure(fg_color= ("#740001")) 
                            #Switch#
        self.switchMode.configure(button_color="#004d87",
                                 border_width=2,
                                 border_color="#005b96",
                                 fg_color="gray",
                                 progress_color="#444444",
                                 button_hover_color="#004d87",
                                 text="Dark Mode on")
                            #Treeview#
        self.style.configure('Treeview',
                        background = "#9ba7ba",
                        foreground= "white",
                        rowheight=25,
                        fieldbackground="#9ba7ba" ,   
                        )
        self.style.configure('Treeview.Heading',
                        background = "#444444",
                        foreground= "white",
                        fieldbackground="#444444" ,   
                        relief= "flat"   
                        )
        self.style.map('Treeview',
                 background=[('selected', '#693a3a')]
                 )      
    def limpaTela(self):
        self.codigoEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.cidadeEntry.delete(0, END)
    def conectaBd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconectaBd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    def montaTabelas(self):
        self.conectaBd()
        
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nomeCliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectaBd()
    def variaveis(self):
        self.codigo = self.codigoEntry.get()
        self.nome = self.nomeEntry.get()
        self.telefone = self.telefoneEntry.get()
        self.cidade = self.cidadeEntry.get()
    def addCliente(self):
        
        self.variaveis()
        self.conectaBd()
        
        
        if len(self.nome) >= 1:
            self.cursor.execute(""" INSERT INTO clientes(nomeCliente, telefone, cidade) 
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconectaBd()
            self.selectLista()
            self.limpaTela()
        else:
            print("Error")
            self.desconectaBd()
            self.limpaTela()
    def selectLista(self):
    
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectaBd()
        lista = self.cursor.execute(""" SELECT cod, nomeCliente, telefone, cidade FROM clientes 
            ORDER BY nomeCliente ASC; """)

        for i in lista:
            self.listaCli.insert("", END, values=i)

        self.desconectaBd()
    def onDoubleClick(self, event):
        self.limpaTela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigoEntry.insert(END, col1)
            self.nomeEntry.insert(END, col2)
            self.telefoneEntry.insert(END, col3)
            self.cidadeEntry.insert(END, col4)
    def deletaCliente(self):
        self.variaveis()
        self.conectaBd()
        '''#  self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo))
        self.conectaBd()
        self.itemSelec= self.listaCli.selection()[0]
        self.curItem = self.listaCli.focus(self.itemSelec)
        # self.dicSelect = list(self.curItem.item())
        # rs=self.cursor.execute("""DELETE FROM clientes WHERE cod=?""", (self.itemSelec))
        # self.conn.commit()
        # if(rs.rowcount==1):
        #     self.listaCli.delete(self.itemSelec)
        print(f"{self.codigo}===> codigo//{self.itemSelec.items()}===>item selec")
        # self.itemSelec= self.listaCli.selection()[0]
        # self.listaCli.delete(self.itemSelec)
        self.desconectaBd()
        # self.limpaTela()
        # self.selectLista()'''
        if len(self.codigo) >= 1:
                self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo))
                self.conn.commit()
                self.desconectaBd()
                self.limpaTela()
                self.selectLista()
        else:
            print("Error")
            self.desconectaBd()
            self.limpaTela()
    def alteraCliente(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute(""" UPDATE clientes SET nomeCliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,(self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconectaBd()
        self.selectLista()
        self.limpaTela()
    def buscaCliente(self):
        self.conectaBd()
        
        self.listaCli.delete(*self.listaCli.get_children())

        self.nomeEntry.insert(END, "%")
        nome = self.nomeEntry.get()
        self.cursor.execute(""" SELECT cod, nomeCliente, telefone, cidade 
            FROM clientes WHERE nomeCliente LIKE '%s' ORDER BY nomeCliente 
            ASC """ % nome)
        buscaNomeCli = self.cursor.fetchall()
        
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values= i)
        
        self.limpaTela()
        self.desconectaBd()
    def change_appearance_mode_event(self):
            if self.switchMode.get() == "Light":
                customtkinter.set_appearance_mode(self.switchMode.get())
                self.alteraCores()
            elif self.switchMode.get() == "Dark":
                customtkinter.set_appearance_mode(self.switchMode.get())
                self.desalteraCores()

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        super().__init__()
        self.cores()
        self.tela()
        self.framesDaTela()
        self.swichAltera()
        self.widgetsFrame1()
        self.listaFrame2()
        self.montaTabelas()
        self.selectLista()
        self.menus()
        self.alteraCores()
        self.desalteraCores()
        
        
        root.mainloop()
    def tela(self):
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.root.title("Cadastro de clientes")
        self.root.geometry(f"{700}x{500}")
        #self.root.maxsize(width= 800, height= 600)
        self.root.minsize(width= 600, height= 500)
        
        self.root.grid_columnconfigure((0), weight=2)
        self.root.grid_rowconfigure((0, 1), weight=2)
    def framesDaTela(self):
        self.frame1 = customtkinter.CTkFrame(self.root, corner_radius=15,
                                            border_width=4, border_color= "#400000", 
                                            fg_color="transparent",width=700, height=250)
        self.frame1.grid(row=0, column=0, pady=10, sticky="nsew")

        self.frame2 = customtkinter.CTkFrame(self.root, corner_radius=15,
                                            border_width=4, border_color= "#400000",
                                             fg_color="transparent",width=700, height=250)
        self.frame2.grid(row=1, column=0, sticky="nsew")        
    def swichAltera(self):
        self.switchVar = customtkinter.StringVar(value="Light")
        self.switchMode = customtkinter.CTkSwitch(self.frame1,
                                                text="Dark Mode on",
                                                font= ('verdana', 11, 'bold'),  
                                                command=self.change_appearance_mode_event, 
                                                variable= self.switchVar, onvalue="Dark", offvalue="Light")
        self.switchMode.place(relx=0.7, rely=0.85)
        self.switchMode.select()
    def widgetsFrame1(self):
        self.btLimpar = customtkinter.CTkButton(self.frame1, text="Limpar",
                                                font= ('verdana', 12, 'bold'),border_width=2, 
                                                corner_radius= 20, border_color= "#005b96",
                                                fg_color=("#004d87"),
                                                command= self.limpaTela)
        self.btLimpar.place(relx= 0.335, rely= 0.1, relwidth= 0.11, relheight= 0.15)

        self.btBuscar =customtkinter.CTkButton(self.frame1, text="Buscar",
                                               font= ('verdana', 12, 'bold'),
                                               border_width=2, fg_color=("#004d87"),
                                                corner_radius= 20, border_color= "#005b96",
                                               command=self.buscaCliente)
        self.btBuscar.place(relx= 0.45, rely= 0.1, relwidth= 0.11, relheight= 0.15)

        self.btNovo = customtkinter.CTkButton(self.frame1, text="Novo",font= ('verdana', 11, 'bold'), 
                                              border_width=2, corner_radius= 20, fg_color=("#004d87"),
                                              border_color= "#005b96",
                                              command= self.addCliente)
        self.btNovo.place(relx= 0.585, rely= 0.1, relwidth= 0.11, relheight= 0.15)

        self.btAlterar = customtkinter.CTkButton(self.frame1, text="Alterar",
                                                border_width=2, fg_color=("#004d87"),
                                                corner_radius= 20, border_color= "#005b96",
                                                font= ('verdana', 11, 'bold'), command= self.alteraCliente)
        self.btAlterar.place(relx= 0.7, rely= 0.1, relwidth= 0.11, relheight= 0.15)

        self.btApagar = customtkinter.CTkButton(self.frame1, text="Apagar", 
                                                border_width=2,
                                                hover_color="#93000b",
                                                corner_radius= 20, border_color= "#800000",
                                                fg_color='#740001', font= ('verdana', 12, 'bold'), 
                                                command= self.deletaCliente)
        self.btApagar.place(relx= 0.85, rely= 0.05, relwidth= 0.12, relheight= 0.12)
        
        self.lbCodigo = customtkinter.CTkLabel(self.frame1, text = "Código", font= ('verdana', 11))
        self.lbCodigo.place(relx= 0.05, rely=0.05)
        self.codigoEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 10)
                                                  #,state="disabled")
        self.codigoEntry.place(relx= 0.05, rely=0.15, relwidth=0.07)
        self.lbNome = customtkinter.CTkLabel(self.frame1, text = "Nome", font= ('verdana', 11))
        self.lbNome.place(relx= 0.05, rely=0.35)
        self.nomeEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 10)
        self.nomeEntry.place(relx= 0.05, rely=0.45, relwidth=0.85)
        
        self.lbTelefone = customtkinter.CTkLabel(self.frame1, text = "Telefone", font= ('verdana', 11))
        self.lbTelefone.place(relx= 0.05, rely=0.6)
        self.telefoneEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 10)
        self.telefoneEntry.place(relx= 0.05, rely=0.7, relwidth=0.4)

        self.lbCidade = customtkinter.CTkLabel(self.frame1, text = "Cidade", font= ('verdana', 11))
        self.lbCidade.place(relx= 0.5, rely=0.6)
        self.cidadeEntry = customtkinter.CTkEntry(self.frame1, border_width=3, corner_radius= 10)
        self.cidadeEntry.place(relx= 0.5, rely=0.7, relwidth=0.4)

        '''def Dark(): customtkinter.set_appearance_mode("Dark")
        def Light(): customtkinter.set_appearance_mode("Light")
        self.radioVar = tkinter.IntVar(value=0)

        self.radioButton1= customtkinter.CTkRadioButton(master=self.frame1, text="Dark Mode",
                                                        value=1,
                                                        command=Dark,
                                                        variable= self.radioVar 
                                                        )
        self.radioButton2= customtkinter.CTkRadioButton(master=self.frame1, text="Light Mode",
                                                        value=2,
                                                        command= Light,
                                                        variable= self.radioVar 
                                                        )
        self.radioButton1.place(relx=0.7, rely=0.3)
        self.radioButton2.place(relx=0.5, rely=0.3)'''                   
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

        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1","col2","col3","col4"))
        self.listaCli.place(relx= 0.012, rely= 0.1, relwidth= 0.97, relheight= 0.85)
        

        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=200)

        
        
        self.scrooLista = customtkinter.CTkScrollbar(self.frame2, orientation='vertical')
        self.listaCli.configure(yscroll=self.scrooLista.set)
        self.scrooLista.place(relx= 0.97, rely=0.1, relheight=0.85, relwidth=0.027)
        self.listaCli.bind("<Double-1>", self.onDoubleClick)
    def menus(self):
        def quit(): self.root.destroy()
        
        
        self.filemenu2 = customtkinter.CTkOptionMenu(self.frame1, values=["Opções:","Ficha do cliente","Limpar Tela", 
                                                                         "Sair"], 
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
        
        #filemenu.place(relx=0.2, rely=0.1, relwidth= 0.12, relheight= 0.12)
        self.filemenu2.place(relx=0.16, rely=0.1, relwidth= 0.15, relheight= 0.15)
          
Application()
#codigo executavel: pyinstaller --noconfirm --onedir --windowed --add-data "c:/users/ferna/appdata/local/programs/python/python38/lib/site-packages/customtkinter;customtkinter/" clienteAt.py