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
import tkinter.messagebox
import time

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
            print('estou na op gerar clientesBL',comand)
            self.filemenu2.set("Opções:")
        elif self.filemenu2.get() == "Sair":
            print("estou na op sair",comand)
            quit()
        elif self.filemenu2.get() == "Limpar Tela":
            print("estou no limpa tela")
            self.limpaTela()
            self.filemenu2.set("Opções:")   
        elif self.filemenu2.get() == "Relatório ano":
            print("estou no Relatório do ano")
            self.dialog = customtkinter.CTkInputDialog(text="Digite o ano:", title="Relatório ano")
            self.conectaBd()
            SelectVal = self.cursor.execute(""" SELECT valor FROM clientesBL""")
            listaVal = list()
            for valores in SelectVal:
                for v in valores:
                    listaVal.append(v)
                    print(f"{v}-- V")
                print(f"{valores}--valores")
            somaVal = sum(listaVal) 
            print(f"{listaVal}--lista val")
            print(f"{somaVal}--soma")
            self.desconectaBd() 

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
                                 text="Limousine")
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
                                 text="Baladeiro")
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
        self.localEntry.delete(0, END)
        self.dataEntry.delete(0, END)
        self.duraEntry.delete(0, END)
        self.hrInicioEntry.delete(0, END)
        self.valorEntry.delete(0, END)
        self.checkRosk.deselect()
        self.checkAni.deselect()
        self.checkInst.deselect()
        self.checkBuf.deselect()
        self.checkCerv.deselect()
        self.Bala = "Baladeiro"
        self.switchMode.select()
        self.change_appearance_mode_event()
    def conectaBd(self):
        self.conn = sqlite3.connect("clientesBL.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconectaBd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    def montaTabelas(self):
        self.conectaBd()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientesBL(
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nomeCliente VARCHAR(40) NOT NULL,
                telefone VARCHAR(20),
                local VARCHAR(40),
                data VARCHAR(15),
                valor FLOAT(15),
                duracao INTEGER(5),
                extras VARCHAR(200),
                hora VARCHAR(10),
                pago VARCHAR(10),
                qual VARCHAR(20)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectaBd()
    def variaveis(self):
                     #entry
        self.codigo   = self.codigoEntry.get()
        self.nome     = self.nomeEntry.get()
        self.telefone = self.telefoneEntry.get()
        self.local    = self.localEntry.get()
        # self.data     = self.dataEntry.get()
        self.data     = self.sel.get()
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
        for r in self.chekList:
            if len(self.chekList) > 5:
                            self.chekList= self.chekList[:5]
                            print(f"{self.chekList} -- self.chekList# ")
        self.ListExt  = str(self.chekList)
        self.chekList2 = self.ListExt.split(",")
        c = "x"
        while c == "x":
            self.ListExt = self.ListExt.replace("[","")
            self.ListExt = self.ListExt.replace("]","")
            self.ListExt = self.ListExt.replace("'","")
            self.ListExt = self.ListExt.replace(" ","")
            c="y"
    def addCliente(self):
        
        self.variaveis()
        self.conectaBd()
        
        
        if len(self.nome) >= 1:
            self.cursor.execute(""" INSERT INTO clientesBL(nomeCliente, telefone, local, data,
                                                         valor, duracao, extras, hora, pago, qual) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.telefone, self.local,
                                                                            self.data, self.valor, self.dura, 
                                                                            self.ListExt, self.hrInicio, self.pago,
                                                                            self.qual))
            self.conn.commit()
            self.desconectaBd()
            self.selectLista()
            self.limpaTela()
        else:
            print("Error")
            self.desconectaBd()
            self.limpaTela()
    def selectLista(self):
        print("###=-==--=-//ESTOU NO SELECT LISTA//-=-=-=-###")
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectaBd()
        lista = self.cursor.execute(""" SELECT cod, nomeCliente, telefone, local, data,
                                    valor, duracao, extras, hora, pago, qual
                                    FROM clientesBL 
                                    ORDER BY nomeCliente ASC; """)

        # for i in lista:
        #     self.listaCli.insert("", END, values=i)
        # selectDate = self.cursor.execute(""" SELECT data, strftime('%Y',data) as 'Year', strtime('%m',data) as 'Month',
        #                                 strtime('%d',data) as 'Day'
        #                                 FROM clientesBL; """)
        # for d in selectDate:
        #     print(d)

        self.desconectaBd()
    def onDoubleClick(self, event):
        self.variaveis()
        self.limpaTela()
        self.listaCli.selection()
        for n in self.listaCli.selection():
            col1, col2, col3, col4, col5,col6,col7,col8,col9,col10,col11=self.listaCli.item(n, 'values')
            self.codigoEntry.insert(END, col1)
            self.nomeEntry.insert(END, col2)
            self.telefoneEntry.insert(END, col3)
            self.localEntry.insert(END, col4)
            self.dataEntry.insert(END, col5)
            self.valorEntry.insert(END, col6)
            self.duraEntry.insert(END, col7)
            print("\n###=-=-=-=-//ESTOU NO DOUBLE CLICK//=-=-=-=-###")
            if len(col8)>1:
                print(f"{len(col8)} --> tamanho col8")
                # self.conectaBd()
                # self.cursor.execute(""" UPDATE clientesBL SET extras = ?
                #                     WHERE cod = ? """,(col8, col1))
                # self.conn.commit()
                self.chekList2= col8.split(",")
                self.chekList.clear()
                for item in self.chekList2:
                    self.chekList.append(item)
                # for n in self.chekList:
                #     if n not in self.chekList2:
                #         self.chekList.remove(n)
                #         print(f"{self.chekList} -- {n} removido self.checklist")
                self.ListExt  = str(self.chekList)
                c = "x"
                while c == "x":
                    self.ListExt = self.ListExt.replace("[","")
                    self.ListExt = self.ListExt.replace("]","")
                    self.ListExt = self.ListExt.replace("[","")
                    self.ListExt = self.ListExt.replace("'","")
                    self.ListExt = self.ListExt.replace(" ","")
                    c="y"

                print(f"{col8} -- col8 ")
                print(f"{self.ListExt} -- self.ListExt ")
                print(f"{len(self.ListExt)} -- Tamanho self.ListExt ")
                print(f"{self.chekList} -- self.chekList ")
                print(f"{self.chekList2} -- self.chekList2 ")
                print(f"{self.listaCli.selection()}\n---->ListaCli selection")
                if len(self.chekList) > 5:
                            self.chekList= self.chekList[:5]
                            print(f"{self.chekList} -- self.chekList ")
                self.checkRosk.deselect()
                self.checkAni.deselect()
                self.checkInst.deselect()
                self.checkBuf.deselect()
                self.checkCerv.deselect()
                # for i in range (6):
                while len(self.chekList2)>0:
                
                    try:
                        print("Estou no Entrando nos if/elif")
                        if 'Roskeiro' in self.chekList2 and len(self.chekList2) > 0: 
                            try:
                                #print(f"Posição [{i}]-- {self.chekList2}-- tem {self.chekList2[i]}")
                                print(f"-- Deu bom0 --")
                                # self.chekList.remove('Roskeiro')
                                self.chekList2.remove('Roskeiro')
                                self.checkRosk.select()
                                self.checkRosk.togle()
                                print(f"//{self.chekList} check list")
                                print(f"//{self.chekList2} check list 2")

                            except:
                                print("Nada a remover")
                        if "Animador" in self.chekList2 and len(self.chekList2) > 0:
                                try:
                                    #print(f"Posição [{i}]-- {self.chekList2}-- tem {self.chekList2[i]}")
                                    print(f" -- Deu bom1 --")
                                    # self.chekList.remove("Animador")
                                    self.chekList2.remove("Animador")
                                    self.checkAni.select()
                                    self.checkAni.togle()
                                    print(f"//{self.chekList} check list")
                                    print(f"//{self.chekList2} check list 2")
                                    
                                except:
                                    print("Nada a remover")
                        if "Instrutor" in self.chekList2 and len(self.chekList2) > 0: 
                                try:
                                    #print(f"Posição [{i}]-- {self.chekList2}-- tem {self.chekList2[i]}")
                                    print(f"-- Deu bom2 --")
                                    # self.chekList.remove("Instrutor")
                                    self.chekList2.remove("Instrutor")
                                    self.checkInst.select()
                                    self.checkInst.togle()
                                    print(f"//{self.chekList} check list")
                                    print(f"//{self.chekList2} check list 2")
                                    continue
                                except:
                                    print("Nada a remover")
                        if "Buffet" in self.chekList2 and len(self.chekList2) > 0:
                                try:
                                    #print(f"Posição [{i}]-- {self.chekList2}-- tem {self.chekList2[i]}")
                                    print(f"-- Deu bom3 --")
                                    # self.chekList.remove("Buffet")
                                    self.chekList2.remove("Buffet")
                                    self.checkBuf.select()
                                    self.checkBuf.togle()
                                    print(f"//{self.chekList2} check list 2")
                                    print(f"//{self.chekList} check list")
                                except:
                                    print("Nada a remover")
                        if "Cerveja" in self.chekList2 and len(self.chekList2) > 0: 
                                try:
                                    #print(f"Posição [{i}]-- {self.chekList2}-- tem {self.chekList2[i]}")
                                    print(f"-- Deu bom4 --")
                                    # self.chekList.remove("Cerveja")
                                    self.chekList2.remove("Cerveja")
                                    self.checkCerv.select()
                                    self.checkCerv.togle()
                                    print(f"//{self.chekList} check list")
                                    print(f"//{self.chekList2} check list 2")
                                except:
                                    print("Nada a remover")
                                            
                    # if len(self.chekList2)<=0:
                    #     print(f"{self.chekList}---Estou no elif col8")
                    #     self.checkRosk.deselect()
                    #     self.checkAni.deselect()
                    #     self.checkInst.deselect()
                    #     self.checkBuf.deselect()
                    #     self.checkCerv.deselect()
                        
                        #print(f"Posição [{i}]-- item {self.chekList2[i]}//Não tem {self.chekList2[i]} -- estou no primeiro else")
                    except:
                        print(f"-- Deu muito ruim na col8 --")
                    self.chekList.clear()
                    self.chekList2.clear()     
                    print(f"Estou fora do while {self.chekList2}-checklist 2 // {self.chekList}-checklist" )

            self.hrInicioEntry.insert(END, col9)          
            for t in range(2):
                print(f"\nestou no for da cl10 ---> {col10}")
                if col10== "sim":
                    print(f"bt {col10} -- if {t}")
                    self.pagoStr.replace("Sim","")
                    self.radioButton1.select()
                    break
                if col10=="não":
                    self.pagoStr.replace("Não","")
                    print(f"bt {col10} -- if {t+1}")
                    self.radioButton2.select()      
            print(f"{col11} ---col11")
            self.qual = str(self.BeL)
            c00 = "x"
            while c00 == "x":
                self.qual = self.qual.replace("[","")
                self.qual = self.qual.replace("]","")
                self.qual = self.qual.replace("'","")
                c00="y"
            
            print(f"{self.qual}---self.qual//{self.BeL}---self.BeL")
            if col11 == "Baladeiro":
                print(f"\n{col11} --- estou na col11 if//{self.qual}//")
                self.Bala = "Baladeiro"
                self.switchMode.select()
                self.change_appearance_mode_event()
                #self.desalteraCores()
            elif col11 == "Limousine":
                print(f"\n{col11} --- estou na col11 elif//{self.qual}//")
                self.Limou = "Limousine"
                self.switchMode.deselect()
                self.change_appearance_mode_event()
            else:
                print(f"{col11} --- Estou  no inicio else da col11//{self.qual}")
                self.Bala = "Baladeiro"
                self.switchMode.select()
                self.BeL.append(self.Bala)
                self.change_appearance_mode_event()
                print(f"{col11} --- Estou no fim do else da col11//{self.qual}")
                #self.alteraCores()

            print(f"\n{col11}--- valor col11")           
            # self.selectLista()
    def deletaCliente(self):
        self.variaveis()
        self.conectaBd()
        # if len(self.nome) >= 1:
        try:
            self.cursor.execute("""DELETE FROM clientesBL WHERE cod = ?""", (self.codigo, ))
            self.conn.commit()
            self.desconectaBd()
            self.limpaTela()
            self.selectLista()
        except:
            print("Erro no deleta cliente")
            self.desconectaBd()
            self.limpaTela()
    def alteraCliente(self):
        print("####=-=-=-=-=-//ESTOU NO ALTERA CLI//-=-=-=-=-==-=-##")
        self.variaveis()
        # self.onDoubleClick(self)
        self.conectaBd()
        self.cursor.execute(""" UPDATE clientesBL SET nomeCliente = ?, telefone = ?, local = ?, data = ?,
                                valor = ?, duracao = ?, extras = ?, hora = ?, pago = ?, qual =? 
                                WHERE cod = ? """,(self.nome, self.telefone, self.local,
                                self.data, self.valor, self.dura, 
                                self.ListExt, self.hrInicio, self.pago,
                                self.qual, self.codigo))
        self.conn.commit()
        self.desconectaBd()
        self.selectLista()
        self.limpaTela()
    def buscaCliente(self):
        self.conectaBd()
        
        self.listaCli.delete(*self.listaCli.get_children())

        self.nomeEntry.insert(END, "%")
        nome = self.nomeEntry.get()
        self.cursor.execute(""" SELECT cod, nomeCliente, telefone, local, data,
                            valor, duracao, extras, hora, pago, qual 
                            FROM clientesBL WHERE nomeCliente LIKE '%s' ORDER BY nomeCliente 
                            ASC """ % nome)
        buscaNomeCli = self.cursor.fetchall()
        
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values= i)
        
        self.limpaTela()
        self.desconectaBd()
    def change_appearance_mode_event(self):
            print("-=-=-=-##//estou no change_appearance_mode_event//##-=-=-=-=")
            self.BeL   = list()
            self.Bala  = str()
            self.Limou = str()
            print(f"{self.BeL}---->self.BeL//\n{self.Bala}---->self.Bala//\n{self.Limou}---->self.Limou")
            self.variaveis()
            if self.switchMode.get() == "Light":
                self.BeL.clear()
                self.Limou = "Limousine"
                self.BeL.append(self.Limou)
                customtkinter.set_appearance_mode(self.switchMode.get())
                self.checkRosk.configure(state = tkinter.DISABLED)
                self.checkAni.configure(state = tkinter.DISABLED)
                self.checkInst.configure(state = tkinter.DISABLED)
                self.checkBuf.configure(state = tkinter.DISABLED)
                self.checkCerv.configure(state = tkinter.DISABLED)
                self.alteraCores()
                print("Estou no Switch mode dark")
                print(f"{self.BeL}---->self.BeL//\n{self.Bala}---->self.Bala//\n{self.Limou}---->self.Limou")
            elif self.switchMode.get() == "Dark":
                self.BeL.clear()
                self.Bala = "Baladeiro"
                self.BeL.append(self.Bala)
                customtkinter.set_appearance_mode(self.switchMode.get())
                self.checkRosk.configure(state = tkinter.NORMAL)
                self.checkAni.configure(state = tkinter.NORMAL)
                self.checkInst.configure(state = tkinter.NORMAL)
                self.checkBuf.configure(state = tkinter.NORMAL)
                self.checkCerv.configure(state = tkinter.NORMAL)
                self.desalteraCores()
                print("Estou no Switch mode dark")
                print(f"{self.BeL}---->self.BeL//\n{self.Bala}---->self.Bala//\n{self.Limou}---->self.Limou")
            else:
                self.Bala = "Baladeiro"
                self.BeL.append(self.Bala)
                print(f"{self.BeL}---->self.BeL//\n{self.Bala}---->self.Bala//\n{self.Limou}---->self.Limou")
    def checkFunc(self):
        self.variaveis();
        def new_method():
            self.chekList.remove("Roskeiro");print(f"{self.rosk} removido")

        if self.rosk == "Roskeiro" and self.rosk !="off":
                self.chekList.append(self.rosk);print(self.chekList); print("nada a remover")
        else:
            try:
                new_method()
            except:
                print("rolou não")
    def checkFunc2(self):
        self.variaveis();
        def new_method():
            self.chekList.remove("Animador");print(f"{self.ani} removido")

        if self.ani == "Animador" and self.ani !="off":
                self.chekList.append(self.ani);print(self.chekList); print("nada a remover")
        else:
            try:
                new_method()
            except:
                print("rolou não")
    def checkFunc3(self):
        self.variaveis();
        def new_method():
            self.chekList.remove("Instrutor");print(f"{self.inst} removido")

        if self.inst == "Instrutor" and self.inst !="off":
                self.chekList.append(self.inst);print(self.chekList); print("nada a remover")
        else:
            try:
                new_method()
            except:
                print("rolou não")
    def checkFunc4(self):
        self.variaveis();
        def new_method():
            self.chekList.remove("Buffet");print(f"{self.buf} removido")

        if self.buf == "Buffet" and self.buf !="off":
                self.chekList.append(self.buf);print(self.chekList); print("nada a remover")
        else:
            try:
                new_method()
            except:
                print("rolou não")
    def checkFunc5(self):
        self.variaveis();
        def new_method():
            self.chekList.remove("Cerveja");print(f"{self.cerv} removido")

        if self.cerv == "Cerveja" and self.cerv !="off":
                self.chekList.append(self.cerv);print(self.chekList); print("nada a remover")
        else:
            try:
                new_method()
            except:
                print("rolou não")

        