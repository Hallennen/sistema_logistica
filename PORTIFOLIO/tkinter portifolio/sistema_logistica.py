from tkinter import * 
from tkinter import ttk as tk
from tkinter import messagebox
import psycopg2




nome_sistema = 'HN-Logistica' 
cor_de_fundo =   'light grey' #'#704F92'
cor_Labels = 'light grey'   #'#E8A604'   #'#BAA3CE' 
cor_da_faixa = '#996bc7'
linhas= []
contador = 1
base_contrato = 'HN0000'

class sistema:
    def __init__(self):
        self.retorno_num_contrato()
        self.tela_principal()


        return

    def retorno_num_contrato(self):
        busca_num = ''' SELECT max(contratos) FROM CONTRATOS'''
        execução = conexao_banco.busca(self,busca_num)
        self.inteirocontrato = int(execução[0])+1
        self.numero_contrato = base_contrato+str(self.inteirocontrato)
        return self.inteirocontrato

    def tela_principal(self):
        self.janela = Tk()
        self.janela.title('Distribuição')
        self.janela.geometry('800x600+250+50')
        self.janela.configure(background= cor_de_fundo)
    

        #barra de ferramentas
        self.barra_ferramentas = Menu(self.janela, tearoff=False)
        self.janela.config(menu=self.barra_ferramentas)
        self.arquivo= Menu(self.barra_ferramentas,tearoff=False)
        self.arquivo.add_command(label="Categorias",command=self.catagorias)
        self.arquivo.add_command(label="Distribuição",command=self.distribuicao)
        self.arquivo.add_command(label="Gerar Contrato",command=self.gerar_contrato)
        self.arquivo.add_command(label="Fechar",command=self.fechar)
        self.barra_ferramentas.add_cascade(label='Arquivo',menu=self.arquivo)

        #faixa 
        self.faixa = tk.Label(self.janela, background=cor_da_faixa)
        self.faixa.place(relx=0 , rely=0, relheight= 0.15 , relwidth=1)

        self.titulo_sistema = tk.Label(self.faixa, text=nome_sistema, font=('arial',25), background=cor_da_faixa)
        self.titulo_sistema.place(rely=0.28, relx=0.42)

        self.label1 = LabelFrame(self.janela, text='Opções',relief='raised', border=4)#bg=cor_Labels)
        self.label1.place(rely=0.16, relx=0.01,relwidth=0.30, relheight=0.83)

        #opções
        self.opcoesbtn = tk.Button(self.label1, text='CATEGORIAS', command=self.catagorias)
        self.opcoesbtn.place(rely=0.1 , relx=0.01, relwidth=0.98, relheight=0.07)
        self.opcoesbtn = tk.Button(self.label1, text='DISTRIBUIÇÃO',command=self.distribuicao)
        self.opcoesbtn.place(rely=0.17 , relx=0.01, relwidth=0.98, relheight=0.07)
        self.opcoesbtn = tk.Button(self.label1, text='GERAR CONTRATO',command=self.gerar_contrato)
        self.opcoesbtn.place(rely=0.24 , relx=0.01, relwidth=0.98, relheight=0.07)
        self.opcoesbtn = tk.Button(self.label1, text='ESTADOS - BRASIL')
        self.opcoesbtn.place(rely=0.31 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes3.place(rely=0.38 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes2 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes2.place(rely=0.45 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes3.place(rely=0.52 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes3.place(rely=0.59 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes3.place(rely=0.66 , relx=0.01, relwidth=0.98, relheight=0.07)
        # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
        # self.opcoes3.place(rely=0.73 , relx=0.01, relwidth=0.98, relheight=0.07)
        self.opcoes3 = tk.Button(self.label1, text='FECHAR CONTEUDO',command=self.fechar)
        self.opcoes3.place(rely=0.80 , relx=0.01, relwidth=0.98, relheight=0.07)

        
        return Tk.mainloop(self.janela)

    #funções dos botoes
    def cria_conteudo_lateral(self):
        self.conteudo_lateral= LabelFrame(self.janela, text='alo',highlightcolor='blue' ,highlightthickness=1,relief='raised', border=4)
        self.conteudo_lateral.place(rely=0.16, relx=0.32, relheight=0.83, relwidth=0.67)
        self.conteudo_lateral.focus_set()


#funções:

    #consulta categorias
    def catagorias(self):
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok')

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='CATEGORIAS')

        self.rolagem = Scrollbar(self.conteudo_lateral)
        self.rolagem.pack(side=RIGHT, fill=Y)

        self.tecnologia = LabelFrame(self.conteudo_lateral,text='Tecnologia')
        self.setores = Label(self.tecnologia, text='40 - Informática \n\n51 - Tablet', justify='left')
        # flat, groove, raised, ridge, solid, or sunken
        self.setores.place(relx= 0.15, rely=0.05)
        self.tecnologia.place(relx= 0.10, rely=0.05, relheight=0.4 , relwidth=0.3)

        self.eletrodomesticos = LabelFrame(self.conteudo_lateral,text='Eletromesticos')
        self.setores = Label(self.eletrodomesticos, text="21 - Eletroportateis \n\n22 - Utensilios \n\n46 - Beleza", justify='left')
        self.setores.place(relx=0.15 , rely=0.05)
        self.eletrodomesticos.place(relx= 0.60, rely=0.05, relheight=0.4 , relwidth=0.3)
        
        self.linhaBranca = LabelFrame(self.conteudo_lateral,text='Linha Branca')
        self.setores = Label(self.linhaBranca, text="25 - Queimadores \n\n26 - Refrigeradores \n\n27 - Lavadoras", justify='left')
        self.setores.place(relx=0.15 , rely=0.05)
        self.linhaBranca.place(relx= 0.10, rely=0.52, relheight=0.4 , relwidth=0.3)
        
        self.moveis = LabelFrame(self.conteudo_lateral,text='Moveis')
        self.setores = Label(self.moveis, text="\n31 - Moveis de Quarto \n\n32 - Moveis Sala de Jantar \n\n33 - Moveis de Cozinha \n\n34 - Estofados \n\n35 - Colchoes \n\n36 - Moveis de Escritorio ", justify='left',height=10)
        self.setores.place(relx=0.06 , rely=0.05)
        self.moveis.place(relx= 0.60, rely=0.52, relheight=0.4 , relwidth=0.3)


        pass

    #realizar distribuição do contrato
    def distribuicao(self):
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok')

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='DISTRIBUIÇÃO')
 

        #campo contrato
        self.label_distribuição = Label(self.conteudo_lateral, text='Contrato:',font=('Georgia', 11))
        self.label_distribuição.place(relx= 0.1 , rely= 0.20)
        script = ''' SELECT contratos FROM contratos GROUP BY contratos ORDER BY CONTRATOS ASC'''
        
        contratoteste = conexao_banco.conecta_bd(self,script)
        lista = []
        for i in range(len(contratoteste)):
            lista.append(contratoteste[i])
        
      
        self.inform_contratos = tk.Combobox(self.conteudo_lateral,values=lista)
        self.inform_contratos.place(relx= 0.35 , rely=0.21, relheight=0.04, relwidth=0.45 )
        print('deu certo')

        #campo quantidade
        self.btn_distribuição = Button(self.conteudo_lateral, text='Buscar', font=('Georgia', 11), command=self.busca_contrato)
        self.btn_distribuição.place(relx= 0.85 , rely= 0.19)

        self.regiao = Checkbutton(self.conteudo_lateral,text='Parcial')
        self.regiao.place(relx=0.40, rely=0.255)

        self.regiao = Checkbutton(self.conteudo_lateral,text='Full')
        self.regiao.place(relx=0.60, rely=0.255)

        #campo destino
        self.label_distribuição = Label(self.conteudo_lateral, text='Destino:', font=('Georgia', 11))
        self.label_distribuição.place(relx= 0.1 , rely= 0.30)
        Destinos = ["AC","AL","AP","AM","BA","CE","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","DF"]
        self.infor_estados = tk.Combobox(self.conteudo_lateral,values=Destinos)
        self.infor_estados.place(relheight=0.04 , relwidth=0.45, relx=0.35, rely=0.31)

        self.btn_distribuir= Button(self.conteudo_lateral,text='Distribuir',width=30)
        self.btn_distribuir.pack(side='bottom',pady=15)
        self.btn_distribuição.bind('<Return>',self.busca_contrato)
        self.inform_contratos.focus_force()


        #criar o treeview para o contrato selecionado
        self.tabela_distribuição = tk.Treeview(self.conteudo_lateral,columns=['Contrato','Id_produto','ds_produto','QNTD'],show='headings')
        self.tabela_distribuição.heading('Contrato',text='Contrato')
        self.tabela_distribuição.column('Contrato',minwidth=10,anchor='center',width=15)
        self.tabela_distribuição.heading('Id_produto',text='Id_produto')
        self.tabela_distribuição.column('Id_produto',minwidth=5,anchor='center',width=10)
        self.tabela_distribuição.heading('ds_produto',text='ds_produto')
        self.tabela_distribuição.column('ds_produto',minwidth=20,anchor='center',width=50)
        self.tabela_distribuição.heading('QNTD',text='QNTD')
        self.tabela_distribuição.column('QNTD',minwidth=10,anchor='center',width=15)
        self.tabela_distribuição.place(relx= 0.05, rely= 0.4 , relwidth= 0.80, relheight=0.50)

        self.qnt_libera = Entry(self.conteudo_lateral)
        self.qnt_libera.place(relx=0.87 , rely=0.50, width=40)


        pass


    #busca itens pelo numero do contrato
    def busca_contrato(self,event=None):
        
        try: 
            for linha in self.tabela_distribuição.get_children():
                self.tabela_distribuição.delete(linha)
        except:
            print('tabela limpa')

        sintaxe = '''SELECT * FROM contratos WHERE contratos = '{}' '''.format(self.inform_contratos.get())
        retorno = conexao_banco.conecta_bd(self,sintaxe)
        for i in range(len(retorno)):
            self.tabela_distribuição.insert('','end',values=(retorno[i][0],retorno[i][1],retorno[i][2]))
            print(retorno)
        self.tabela_distribuição.update()

        return



    #geração do contrato
    def gerar_contrato(self):
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok')

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='GERAR CONTRATO')

        #campo informar SKU do produto
        self.label_codigo= Label(self.conteudo_lateral, text='COD.PRODUTO:')
        self.label_codigo.place(relx=0.08 , rely=0.2)
        self.entry_codigo= Entry(self.conteudo_lateral,border=1, highlightthickness=1)
        self.entry_codigo.place(relwidth=0.10, rely=0.2, relx=0.35)
        self.descrição_codigo= Label(self.conteudo_lateral, text=' - ', relief='groove', bd=3, background='light gray')
        self.botao_busca = Button(self.conteudo_lateral, text='Buscar', command=self.busca_descricao)
        self.descrição_codigo.place(relx= 0.50 , rely=0.20, relwidth=0.45)
        Entry.focus(self.entry_codigo)
        self.entry_codigo.bind('<Return>', self.busca_descricao)


        #campo qntd comprada
        self.qnt_pedido= Label(self.conteudo_lateral, text='Qntd contratada:')
        self.qnt_pedido.place(relx= 0.08 , rely=0.3)
        self.entry_qnt = Entry(self.conteudo_lateral, bd=1, highlightthickness=1)
        self.entry_qnt.place(relx=0.35 , rely=0.3)
        self.entry_qnt.bind('<Return>', self.inserirlinha)
        self.butao_confirmar = Button(self.conteudo_lateral, text='Confirmar', command=self.inserirlinha)
        self.butao_confirmar.place(relx= 0.65 , rely=0.29)

        self.style = tk.Style()
        self.style.configure("Treeview", highlightthickness=2, bd=4, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("Treeview.heading",background='PowderBlue', font=('Calibri', 10,'bold'))

        self.tabela = tk.Treeview(self.conteudo_lateral,selectmode='browse',columns=('id_produto','Ds_produto','QNTD','Preço','TOTAL'),show='headings',style='Treeview')
        self.tabela.column('id_produto',minwidth=  10 , width=30,anchor=CENTER)
        self.tabela.heading('id_produto', text='Id_produto')
        self.tabela.column('Ds_produto',minwidth=  30 , width=100, anchor=CENTER)
        self.tabela.heading('Ds_produto', text='Ds_produto')
        self.tabela.column('QNTD',minwidth=  10 , width=30, anchor=CENTER)
        self.tabela.heading('QNTD', text='QNTD')
        self.tabela.column('Preço',minwidth=  15 , width=30, anchor=CENTER)
        self.tabela.heading('Preço', text='Preço')
        self.tabela.column('TOTAL',minwidth=  50 , width=30, anchor=CENTER)
        self.tabela.heading('TOTAL', text='TOTAL')
      
        
        self.tabela.place(relx=0.05 , rely=0.4, relwidth=0.90,relheight=0.49)
        self.btngerar_contrato = Button(self.conteudo_lateral,text='Gerar contrato', command=self.btn_gerar_contrato)
        self.btngerar_contrato.pack(side='bottom',pady=15)

    #função busca descrição do sku para o contrato
    def busca_descricao(self, event=None):   
        try:
            self.produto = conexao_banco.fun_conexao(self,self.entry_codigo.get())
            self.descrição_codigo.config(anchor=W,text=self.produto[1])
            Entry.focus(self.entry_qnt)
        except:
            TypeError=messagebox.showwarning(title='Alert', message='Codigo não cadastrado')
            self.entry_codigo.delete(0,END)
        return

    #função insere a linha na tabela
    def inserirlinha(self, event = None):
        listinha = self.produto[1]
        linhas.append(listinha)
        print(linhas)
        try:
            self.subtotal = float(self.produto[2])*int(self.entry_qnt.get())

            self.tabela.insert('',index='end',values=(self.produto[0],self.produto[1],self.entry_qnt.get(),self.produto[2],self.subtotal))
            self.descrição_codigo.config(text=' - ',anchor='center')
            self.entry_codigo.delete(0,END)
            self.entry_qnt.delete(0, END)
            Entry.focus(self.entry_codigo)
        except:
            messagebox.showerror(title='ERROR',message='Preencha os dois campos.')


        return

    #função botão gerar o contrato e o txt
    def btn_gerar_contrato(self):
        self.retorno_num_contrato()

    #geração do txt do contrato
        file = open('itens contrato.txt', 'a+')
        itens_contrato=[]
        file.write('ID;DESCRICAO;QTD;PRECO;TOTAL\n')
        for a in range (len(self.tabela.get_children())):
            itens =self.tabela.item(self.tabela.get_children()[a],'values')
            itens_contrato.append(itens)
            for i in range(0,5):
                palavra = itens_contrato[a][i]
                file.write(palavra+';')
            file.write('\n')
        file.close()
    
    #INSERE NO BANCO DE DADOS LINHA POR LINHA 
        for i in range(len(self.tabela.get_children())):
            campos_tabela = self.tabela.item(self.tabela.get_children()[i],'values')
            inserir_dado_banco =  " INSERT INTO contratos (contratos, id_produto, ds_produtos) VALUES ('{}','{}','{}') ".format(self.inteirocontrato,campos_tabela[0],campos_tabela[1])
            conexao_banco.insere(self,inserir_dado_banco)
        print('passou aqui poraa')
    
    #LIMPA O TREEVIEW
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        self.contrato = messagebox.showinfo(title='contrato',message='contrato HN0000'+str(self.inteirocontrato) + ' gerado!')




    #função fechar conteudo
    def fechar(self):
        self.conteudo_lateral.destroy()
        self.janela.update()









class conexao_banco:
    def fun_conexao(self,valor):

        try:
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.sintaxe = " SELECT * FROM produtos WHERE id_produto = '{}' ".format(valor)
            self.cursor.execute(self.sintaxe)
            self.retorno = self.cursor.fetchone()
        
        except:
            print('codido invalido')

        return self.retorno

    def conecta_bd(self,sintaxe):
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            self.retorno = self.cursor.fetchall()
            self.conecta.commit()
            self.conecta.close()

            return self.retorno

    def insere(self,sintaxe):
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            # self.retorno = self.cursor.fetchone()
            self.conecta.commit()
            self.conecta.close()

            return self.retorno

    def busca(self,sintaxe):
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            self.retorno = self.cursor.fetchone()
            self.conecta.close()

            return self.retorno


sistema()