from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
'''### biblioteca para a imagem do botão ###
from PIL import ImageTk, Image
~com base 64 a biblioteca pil pode ser apagada~
### blibioteca para salvar imagem no codigo ###
import base64
'''
from tkinter import tix

root = tix.Tk()

class Relatorios():
     def printCliente(self):
        webbrowser.open("cliente.pdf")
     def geraRelatClient(self):
        self.c = canvas.Canvas("cliente.pdf")
        
        self.codigoRel = self.codigoEntry.get()
        self.nomeRel = self.nomeEntry.get()
        self.telefoneRel = self.telefoneEntry.get()
        self.cidadeRel = self.cidadeEntry.get()

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
    def limpaTela(self):
        self.codigoEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.cidadeEntry.delete(0, END)
    def conectaBd(self):
        self.conn = sqlite3.connect("clientes01.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconectaBd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    def montaTabelas(self):
        self.conectaBd()
        
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes01(
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nomeCliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconectaBd()
    def variaveis(self):
        self.codigo = str(self.codigoEntry.get())
        self.nome = self.nomeEntry.get()
        self.telefone = self.telefoneEntry.get()
        self.cidade = self.cidadeEntry.get()
    def addCliente(self):
        
        self.variaveis()
        self.conectaBd()
        
        
        try:
            self.cursor.execute(""" INSERT INTO clientes01(nomeCliente, telefone, cidade) 
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconectaBd()
            self.selectLista()
            self.limpaTela()
        except:
            print("Error")
            self.desconectaBd()
            self.limpaTela()
    def selectLista(self):
    
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectaBd()
        lista = self.cursor.execute(""" SELECT cod, nomeCliente, telefone, cidade FROM clientes01 
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
        

        # try:
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            print(f"{self.codigo}==>codigo")
            print(f"{self.nome}==>nome")
            print(f"{col1}==>col1")
            print(f"{n}==>n")
            self.cursor.execute("""DELETE FROM clientes01 WHERE cod = ?""",(col1, ))
            self.conn.commit()
            self.desconectaBd()
            self.limpaTela()
            self.selectLista()
            
        # except:
            # print("Error")
            # self.desconectaBd()
            # self.limpaTela()
            # print(f"{self.codigo}==>codigo")
    def alteraCliente(self):
        self.variaveis()
        self.conectaBd()
        self.cursor.execute(""" UPDATE clientes01 SET nomeCliente = ?, telefone = ?, cidade = ?
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
    '''### funcão para imagens no codigo ###
    def imagensBase64(self):
        self.btNovo_base64 = "Usar o site base64.guru para coverter a imagem para base 64 e colar o codigo aqui"      
    '''    

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        '''### chamar a funcão imagensBase64() aqui ###
        self.imagensBase64()
        '''
        self.tela()
        self.framesDaTela()
        self.widgetsFrame1()
        self.listaFrame2()
        self.montaTabelas()
        self.selectLista()
        self.menus()
        root.mainloop()
    def tela(self):
        self.cores()
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= self.cor1)
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 600, height= 500)
    def framesDaTela(self):
        self.frame1 = Frame(self.root, bd= 4, bg= self.cor2, highlightbackground= self.cor3, highlightthickness= 3, 
                            width=100, height=50)
        self.frame1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        
        self.frame2 = Frame(self.root, bd= 4, bg=self.cor2, highlightbackground=self.cor3, highlightthickness= 3)
        self.frame2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgetsFrame1(self):
        
        self.canvasBt = Canvas(self.frame1, bd=0, bg= self.cor4, highlightbackground= self.cor5, highlightthickness= 3)
        self.canvasBt.place(relx= 0.19, rely= 0.08, relwidth= 0.219, relheight= 0.19)


        self.btLimpar = Button(self.frame1, text="Limpar", bd= 2, bg = self.cor6, fg= self.cor7, 
                                activebackground= self.cor8, activeforeground= 'white'
                                ,font= ('verdana', 8, 'bold'), command= self.limpaTela)
        self.btLimpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        self.btBuscar = Button(self.frame1, text="Buscar", bd= 2, bg = self.cor6, fg= self.cor7, 
                                activebackground= self.cor8, activeforeground= 'white'
                                ,font= ('verdana', 8, 'bold'), command=self.buscaCliente)
        self.btBuscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        self.balaoBuscar = tix.Balloon(self.frame1)
        self.balaoBuscar.bind_widget(self.btBuscar, balloonmsg= "Digite no campo 'Nome' o cliente que deseja buscar.")
        
        '''### Ajustes imagem 64 ###
        self.bt_novo = PhotoImage(data=base64.b64decode(self.btNovo_base64))
            
            #### Botão personalizado ###
        self.imgNovo = PhotoImage(file= 'nomeFotoDoBotao.gif')
        ~Com a foto salva no codigo essa variavel deve ser apagada~
        ~O arquivo de imagem salvo na pasta tambem pode ser apagado~

            ###codigo para ajustar tamanho do botão ###
        self.imgNovo = self.imgNovo.subsample(2, 2)
        ~com a imagem no codigo isso deve ser alterado~
        ->self.bt_novo = self.bt_novo.subsample(2, 2)

            ### Ajustando o estilo do botão ###
        self.style = ttk.style()
        self.style.configure("BW.TButton", relwidth=1, relheight=1, foreground="gray",
                            borderwidth=0, bordercolor="gray", background = "mesma cor do frame",
                            image = self.imgNovo)
        ~Com a imagem no codigo o style tambem deve ser apagado~

            ### Alterações necessarias no botão ###
        self.btNovo = ttk.Button(self.frame1, style = "BW.TButton", command= self.addCliente)
        self.btNovo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        self.btNovo.config(image = self.imgNovo)
        ~com a imagem no codigo isso tambem deve ser alterado~
        -> self.btNovo = Button(self.frame1,bd = 0, image = self.bt_novo , command= self.addCliente)
        self.btNovo.place(relx= 0.58, rely= 0.1, width= 60, height= 30)
        

        '''
        
        self.btNovo = Button(self.frame1, text="Novo", bd= 2, bg = self.cor6, fg= self.cor7, 
                            activebackground= self.cor8, activeforeground= 'white'
                            ,font= ('verdana', 8, 'bold'), command= self.addCliente)
        self.btNovo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        self.btAlterar = Button(self.frame1, text="Alterar", bd= 2, bg = self.cor6, 
                                activebackground= self.cor8, activeforeground= 'white'
                                ,fg= self.cor7, font= ('verdana', 8, 'bold'), command=self.alteraCliente)
        self.btAlterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        self.btApagar = Button(self.frame1, text="Apagar", bd= 2, bg = self.cor6, 
                               activebackground= self.cor8, activeforeground= 'white'
                               ,fg= self.cor7, font= ('verdana', 8, 'bold'), command=self.deletaCliente)
        self.btApagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        self.lbCodigo = Label(self.frame1, text = "Código", bg= self.cor2)
        self.lbCodigo.place(relx= 0.05, rely=0.05)

        self.codigoEntry = Entry(self.frame1, bg= self.cor9, fg= self.cor7)
        self.codigoEntry.place(relx= 0.05, rely=0.15, relwidth=0.07)

        self.lbNome = Label(self.frame1, text = "Nome", bg= self.cor2, fg= self.cor7)
        self.lbNome.place(relx= 0.05, rely=0.35)

        self.nomeEntry = Entry(self.frame1, bg= self.cor9, fg= self.cor7)
        self.nomeEntry.place(relx= 0.05, rely=0.45, relwidth=0.8)

        self.lbTelefone = Label(self.frame1, text = "Telefone", bg= self.cor2, fg= self.cor7)
        self.lbTelefone.place(relx= 0.05, rely=0.6)

        self.telefoneEntry = Entry(self.frame1, bg= self.cor9, fg= self.cor7)
        self.telefoneEntry.place(relx= 0.05, rely=0.7, relwidth=0.4)

        self.lbCidade = Label(self.frame1, text = "Cidade", bg= self.cor2, fg= self.cor7)
        self.lbCidade.place(relx= 0.5, rely=0.6)

        self.cidadeEntry = Entry(self.frame1, bg= self.cor9, fg= self.cor7)
        self.cidadeEntry.place(relx= 0.5, rely=0.7, relwidth=0.4)
    def listaFrame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, column=("col1","col2","col3","col4"))
        self.listaCli.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

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

        
        
        self.scrooLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrooLista.set)
        self.scrooLista.place(relx= 0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.onDoubleClick)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatórios", menu= filemenu2)

        filemenu.add_command(label="sair", command= quit)
        filemenu.add_command(label= "Limpa cliente", command= self.limpaTela)

        filemenu2.add_command(label= "Ficha do cliente", command= self.geraRelatClient)

#Ultima aula assistida: 19
#canal:RfZorzi
#codigo para criar executavel: pyinstaller --onefile --noconsole --windowed cdstTk01.py
        


Application()







