from tkinter import * 
from tkinter import ttk as tk
from tkinter import messagebox
import psycopg2
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from maskedentry import MaskedWidget
from tela_login_logistica import tela_login_logistica1
from tela_login_logistica import retorno_xyz, nome_user, permissao_user




nome_sistema = 'HN-Logistica' 
cor_de_fundo =   'light grey' #'#704F92'
cor_Labels = 'light grey'   #'#E8A604'   #'#BAA3CE' 
cor_da_faixa = '#996bc7'
base_contrato = 'HN0000'
Destinos = ["AC","AL","AP","AM","BA","CE","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","DF"]

class sistema:
    def __init__(self):
        self.retorno_num_contrato()
        self.descrição_produtos()
        conexao_banco.busca_informacoes_personalizado(conexao_banco)
        self.tela_principal()


        return

    def retorno_num_contrato(self):
        busca_num = ''' SELECT max(contratos) FROM CONTRATOS'''
        execução = conexao_banco.busca_fetchone(self,busca_num)
        self.inteirocontrato = int(execução[0])+1
        self.numero_contrato = base_contrato+str(self.inteirocontrato)
        return self.inteirocontrato

    def tela_principal(self): 
        # tela_login_logistica1
        print(retorno_xyz)

        #******************** VALIDA PERMISSÃO ************************
        teste = False
        try:
            if retorno_xyz == True:

                self.janela = Tk()
                self.janela.title('Distribuição')
                self.janela.geometry('800x600+250+50')
                self.janela.configure(background= cor_de_fundo)
                # self.relatorio()

                #estilo do tkinter
                estilo = tk.Style()
                estilo.theme_use('default')
            

                #barra de ferramentas
                self.barra_ferramentas = Menu(self.janela, tearoff=False)
                self.janela.config(menu=self.barra_ferramentas)
                self.arquivo= Menu(self.barra_ferramentas,tearoff=False)
                self.arquivo.add_command(label="Categorias",command=self.catagorias)
                self.arquivo.add_command(label="Gerar Contrato",command=self.gerar_contrato)
                self.arquivo.add_command(label="Distribuição",command=self.distribuicao)
                self.arquivo.add_command(label="Contratos pendentes",command=self.contratos_pendentes)
                self.arquivo.add_command(label="Contratos distribuidos",command=self.contratos_distribuidos)
                self.arquivo.add_command(label="Fechar",command=self.fechar)
                self.arquivo.add_cascade(label='Deslogar',command=self.sair_do_sistema)
                self.barra_ferramentas.add_cascade(label='Arquivo',menu=self.arquivo)

                #faixa 
                self.faixa = tk.Label(self.janela, background=cor_da_faixa)
                self.faixa.place(relx=0 , rely=0, relheight= 0.15 , relwidth=1)

                self.titulo_sistema = tk.Label(self.faixa, text=nome_sistema, font=('arial',25), background=cor_da_faixa)
                self.titulo_sistema.place(rely=0.28, relx=0.42)

                self.label1 = LabelFrame(self.janela, text='Opções',relief='raised', border=4)#bg=cor_Labels)
                self.label1.place(rely=0.16, relx=0.01,relwidth=0.30, relheight=0.83)
                
                nome_user1 = 'Olá, '+ nome_user
                self.nome_usuario = Label(self.label1, text=nome_user1, font=('arial',17))
                self.nome_usuario.place(rely=0.01 , relx=-0.15, relwidth=0.98, relheight=0.07)

                #opções
                self.opcoesbtn = tk.Button(self.label1, text='CATEGORIAS', command=self.catagorias)
                self.opcoesbtn.place(rely=0.1 , relx=0.01, relwidth=0.98, relheight=0.07)

                self.opcoesbtn = tk.Button(self.label1, text='GERAR CONTRATO',command=self.gerar_contrato)
                self.opcoesbtn.place(rely=0.17 , relx=0.01, relwidth=0.98, relheight=0.07)

                self.opcoesbtn = tk.Button(self.label1, text='DISTRIBUIÇÃO',command=self.distribuicao)
                self.opcoesbtn.place(rely=0.24 , relx=0.01, relwidth=0.98, relheight=0.07)

                self.opcoesbtn = tk.Button(self.label1, text='CONTRATOS - PENDENTES',command=self.contratos_pendentes)
                self.opcoesbtn.place(rely=0.31 , relx=0.01, relwidth=0.98, relheight=0.07)

                self.opcoesbtn = tk.Button(self.label1, text='CONTRATOS DISTRIBUIDOS', command= self.contratos_distribuidos)
                self.opcoesbtn.place(rely=0.38 , relx=0.01, relwidth=0.98, relheight=0.07)

                self.opcoes3 = tk.Button(self.label1, text='FECHAR CONTEUDO',command=self.fechar)
                self.opcoes3.place(rely=0.80 , relx=0.01, relwidth=0.98, relheight=0.07)


                #SE USUARIO POSSUI PERMISSÃO ADM
                if permissao_user == 'admin':
                    self.opcoes2 = tk.Button(self.label1, text='CRIAR USUÁRIO',command=self.criar_usuario)
                    self.opcoes2.place(rely=0.45 , relx=0.01, relwidth=0.98, relheight=0.07)
                    self.opcoes3 = tk.Button(self.label1, text='GERAR RELATÓRIO',command= self.relatorio)
                    self.opcoes3.place(rely=0.52 , relx=0.01, relwidth=0.98, relheight=0.07)

                    self.gerencia = Menu(self.barra_ferramentas,tearoff=False)
                    self.gerencia.add_command(label='Criar Usuario',command=self.criar_usuario)
                    self.barra_ferramentas.add_cascade(label='Gerencia',menu=self.gerencia)
                # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
                # self.opcoes3.place(rely=0.59 , relx=0.01, relwidth=0.98, relheight=0.07)
                # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
                # self.opcoes3.place(rely=0.66 , relx=0.01, relwidth=0.98, relheight=0.07)
                # self.opcoes3 = tk.Button(self.label1, text='PRIMEIRA OPÇÃO',)
                # self.opcoes3.place(rely=0.73 , relx=0.01, relwidth=0.98, relheight=0.07)
            
                
            return Tk.mainloop(self.janela)
        except:
            print('Tela fechada')

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

        self.rolagem = Scrollbar(self.conteudo_lateral,orient='vertical')   
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


    #*********geração do contrato********

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

        #BARRA DE ROLAGEM
        rolagem = Scrollbar(self.tabela,command=self.tabela.yview)
        rolagem.pack(side='right',fill='y')
        self.tabela.config(yscrollcommand=rolagem.set)

        #PERSONALIZAÇÃO DA TABELA
        self.tabela.tag_configure('normal', background='lightgray')
        self.tabela.tag_configure('gray',background='white')
        self.tag_tabela = 'normal'
        
        self.tabela.place(relx=0.05 , rely=0.4, relwidth=0.90,relheight=0.49)
        self.btngerar_contrato = Button(self.conteudo_lateral,text='Gerar contrato', command=self.btn_gerar_contrato)
        self.btngerar_contrato.pack(side='bottom',pady=15)

    #função busca descrição do sku para o contrato
    def busca_descricao(self, event=None):   
        try:
            sintaxe = '''SELECT * FROM produtos WHERE id_produto = {} '''.format(int(self.entry_codigo.get()))
            self.produto = conexao_banco.busca_fetchone(self,sintaxe)
            self.descrição_codigo.config(anchor=W,text=self.produto[1])
            Entry.focus(self.entry_qnt)
        except:
            TypeError=messagebox.showwarning(title='Alert', message='Codigo não cadastrado')
            self.entry_codigo.delete(0,END)

        return


    #função insere a linha na tabela
    def inserirlinha(self, event = None):
        try:
            self.subtotal = float(self.produto[2])*int(self.entry_qnt.get())

            if len(self.tabela.get_children()) % 2==0:
                self.tag_tabela ='normal'
            else:
                self.tag_tabela ='gray'

            self.tabela.insert('',index='end',values=(self.produto[0],self.produto[1],self.entry_qnt.get(),self.produto[2],self.subtotal), tags=(self.tag_tabela))
            self.descrição_codigo.config(text=' - ',anchor='center')
            self.entry_codigo.delete(0,END)
            self.entry_qnt.delete(0, END)
            Entry.focus(self.entry_codigo)
        except:
            messagebox.showerror(title='ERROR',message='Preencha os dois campos.')


        return


    #função botão gerar o contrato e o txt
    def btn_gerar_contrato(self):
        if len(self.tabela.get_children()) <1 :
            messagebox.showinfo(title='Erro na geração do contrato',message='Informe os campos obrigátorio')


        else:
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
                inserir_dado_banco =  " INSERT INTO contratos (contratos, id_produto, ds_produtos,qntd_item) VALUES ('{}','{}','{}',{}) ".format(self.inteirocontrato,campos_tabela[0],campos_tabela[1],campos_tabela[2])
                conexao_banco.insere(self,inserir_dado_banco)
            print('passou aqui poraa')
        
        #LIMPA O TREEVIEW
            for linha in self.tabela.get_children():
                self.tabela.delete(linha)

            self.contrato = messagebox.showinfo(title='contrato',message='contrato HN0000'+str(self.inteirocontrato) + ' gerado!')

        pass






    #********DISTRIBUIÇÃO********

    #realizar distribuição do contrato
    def distribuicao(self):
        global parcial, full, lista
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok')

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='DISTRIBUIÇÃO')
 

        #campo contrato
        self.label_distribuição = Label(self.conteudo_lateral, text='Contrato:',font=('Georgia', 11))
        self.label_distribuição.place(relx= 0.1 , rely= 0.20)

        script = '''SELECT contratos FROM contratos
                        LEFT JOIN contratos_distribuidos ON contratos = id_contrato
                            WHERE id_contrato is null
                                GROUP BY 1
                                    ORDER BY contratos DESC'''
        
        contratoteste = conexao_banco.busca_fetchall(self,script)
        lista = []
        for i in range(len(contratoteste)):
            lista.append(contratoteste[i])
        
      
        self.inform_contratos = tk.Combobox(self.conteudo_lateral,values=lista)
        self.inform_contratos.place(relx= 0.35 , rely=0.21, relheight=0.04, relwidth=0.45 )

        #campo quantidade
        self.btn_distribuição = Button(self.conteudo_lateral, text='Buscar', font=('Georgia', 11), command=self.busca_contrato)
        self.btn_distribuição.place(relx= 0.85 , rely= 0.19)

        parcial=IntVar()
        self.btn_parcial = Checkbutton(self.conteudo_lateral,text='Parcial',variable=parcial)
        self.btn_parcial.place(relx=0.40, rely=0.255)

        full=IntVar()
        self.btn_full = Checkbutton(self.conteudo_lateral,text='Full',variable=full)
        self.btn_full.place(relx=0.60, rely=0.255)

        #campo destino
        self.label_distribuição = Label(self.conteudo_lateral, text='Destino:', font=('Georgia', 11))
        self.label_distribuição.place(relx= 0.1 , rely= 0.30)
        self.infor_estados = tk.Combobox(self.conteudo_lateral,values=Destinos)
        self.infor_estados.place(relheight=0.04 , relwidth=0.45, relx=0.35, rely=0.31)

        self.btn_distribuir= Button(self.conteudo_lateral,text='Distribuir',width=30,command= self.distribuir_contrato)
        self.btn_distribuir.pack(side='bottom',pady=15)
        self.btn_distribuição.bind('<Return>',self.busca_contrato)
        self.inform_contratos.focus_force()


        #TABELA para o contrato selecionado
        self.tabela_distribuição = tk.Treeview(self.conteudo_lateral,columns=['Contrato','Id_produto','ds_produto','QNTD'],show='headings')
        self.tabela_distribuição.heading('Contrato',text='Contrato')
        self.tabela_distribuição.column('Contrato',minwidth=10,anchor='center',width=15)
        self.tabela_distribuição.heading('Id_produto',text='Id_produto')
        self.tabela_distribuição.column('Id_produto',minwidth=5,anchor='center',width=10)
        self.tabela_distribuição.heading('ds_produto',text='ds_produto')
        self.tabela_distribuição.column('ds_produto',minwidth=20,anchor='center',width=50)
        self.tabela_distribuição.heading('QNTD',text='QNTD')
        self.tabela_distribuição.column('QNTD',minwidth=10,anchor='center',width=15)
        self.tabela_distribuição.place(relx= 0.05, rely= 0.4 , relwidth= 0.85, relheight=0.50)

        rolagem = Scrollbar(self.tabela_distribuição, orient='vertical')
        rolagem.config(command=self.tabela_distribuição.yview)
        rolagem.pack(side='right', fill='y')
        self.tabela_distribuição.config(yscrollcommand=rolagem.set)

        #PERSONALIZAÇÃO DA TABELA
        self.tabela_distribuição.tag_configure('gray', background= 'lightgray')
        self.tabela_distribuição.tag_configure('normal', background= 'white')
        self.tag = 'normal'


        pass


    #busca itens pelo numero do contrato
    def busca_contrato(self,event=None):
        try: 
            for linha in self.tabela_distribuição.get_children():
                self.tabela_distribuição.delete(linha)
        except:
            print('tabela limpa')


        try:
            sintaxe = '''SELECT * FROM contratos WHERE contratos = '{}' '''.format(self.inform_contratos.get())
            retorno = conexao_banco.busca_fetchall(self,sintaxe)

            for i in range(len(retorno)):
                if self.tag == 'normal':
                    self.tag= 'gray'
                else:
                    self.tag= 'normal'

                self.tabela_distribuição.insert('','end',values=(retorno[i][0],retorno[i][1],retorno[i][2],retorno[i][3]),tags = (self.tag))
                print(retorno)
            self.tabela_distribuição.update()
        except:
            messagebox.showerror(title='Error na busca', message='Contrato invalido ou não informado!')

        return



    # FUNÇÃO DO BOTÃO DISTRIBUIR CONTRATO DA TELA DE DISTRIBUIÇÃO (vai no BD e salva o contrato distribuido)
    def distribuir_contrato(self):

        if self.infor_estados.get() not in Destinos :
            messagebox.showwarning(title='Alert', message='Estado não informado ou inválido, Verifique! ')         

    
        if full.get() == 1:
            
            script = "SELECT SUM(qntd_item) FROM contratos WHERE contratos = {}".format(self.inform_contratos.get())
            self.total_por_contrato = conexao_banco.busca_fetchone(self,sintaxe=script)

            # O self.total_por_contrato não está modificando 
            if self.total_por_contrato[0] == 'None': self.total_por_contrato[0] = 0
            sintaxe = '''INSERT INTO contratos_distribuidos (id_contrato, qtnd_produto_total, uf_estado)
                            VALUES ('{}', '{}', '{}')'''.format(self.inform_contratos.get(),self.total_por_contrato[0],self.infor_estados.get())

            self.insere_contrato_distribuido = conexao_banco.insere(self,sintaxe)

            print('Salvo no BD')   
            messagebox.showinfo(title='Distribuição', message='Contrato distribuido com êxito!')    

            for linha in self.tabela_distribuição.get_children():
                self.tabela_distribuição.delete(linha)
            self.inform_contratos.delete(0,END)
            self.infor_estados.delete(0,END)
            self.inform_contratos.focus_force()
        
        else:
            messagebox.showinfo(title='Geração do contrato',message='Contrato não é full, não foi gerado!')
            

        return






    #FUNÇÃO CONTRATOS DISTRIBUIDOS

    def contratos_distribuidos(self):
        global filtros_estado, filtros_produto, ds_produtos
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok, tela limpa')
        
        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='CONTRATOS DISTRIBUIDOS')


        sintaxe = '''SELECT * FROM contratos_distribuidos ORDER BY id_contrato ASC'''
        self.lista_contratos_distribuidos = conexao_banco.busca_fetchall(self, sintaxe)
 

        self.texto_informativo = Label(self.conteudo_lateral,text='Para filtrar informe alguns dos campos abaixo.', font=('Georgia', 11))
        self.texto_informativo.pack(side='top',pady=30)

        self.inform_do_filtro = Label(self.conteudo_lateral,text='Filtrar por: ', font=('Arial', 10 ))
        self.inform_do_filtro.place(relx=0.1 , rely=0.15)

        filtros_estado = IntVar()
        filtros_produto = IntVar()
        self.selecao_filtro = Checkbutton(self.conteudo_lateral, text='Estado', variable=filtros_estado)
        self.selecao_filtro.place(relx=0.35 , rely=0.15 )
        self.selecao_filtro = Checkbutton(self.conteudo_lateral, text='Produto', variable=filtros_produto)
        self.selecao_filtro.place(relx=0.55 , rely=0.15 )

        self.filtro_estado = Label(self.conteudo_lateral,text='UF do estado: ', font=('Arial', 10))
        self.filtro_estado.place(relx= 0.10 , rely=0.22)
        self.filtro_estado_entry = tk.Combobox(self.conteudo_lateral,values= Destinos)
        self.filtro_estado_entry.place(relx=0.35 , rely=0.22, relheight=0.05 , relwidth=0.12)

        self.filtro_descricao = Label(self.conteudo_lateral,text='Nome do produto: ', font=('Arial', 10))
        self.filtro_descricao.place(relx= 0.10 , rely=0.3)
        self.filtro_descricao_entry = tk.Combobox(self.conteudo_lateral, values= ds_produtos)
        self.filtro_descricao_entry.place(relx=0.35 , rely=0.30, relheight=0.05 , relwidth=0.30)


        self.btn_filtro = Button(self.conteudo_lateral, text='Aplicar filtro', command=self.filtro_busca)
        self.btn_filtro.place(relx=0.7 , rely= 0.22)
        self.btn_filtro = Button(self.conteudo_lateral, text='Limpar filtro', command=self.limpar_tudo)
        self.btn_filtro.place(relx=0.7 , rely= 0.30)


        
        self.tabela_contrato_distribuido = tk.Treeview(self.conteudo_lateral,columns=['CONTRATO','QNTD_TOTAL_PRODUTO','ESTADO'],show='headings')
        self.tabela_contrato_distribuido.heading('CONTRATO',text='CONTRATO')
        self.tabela_contrato_distribuido.column('CONTRATO',minwidth=10,anchor='center',width=15)
        self.tabela_contrato_distribuido.heading('QNTD_TOTAL_PRODUTO',text='QNTD_TOTAL_PRODUTO')
        self.tabela_contrato_distribuido.column('QNTD_TOTAL_PRODUTO',minwidth=5,anchor='center',width=60)
        self.tabela_contrato_distribuido.heading('ESTADO',text='ESTADO')
        self.tabela_contrato_distribuido.column('ESTADO',minwidth=20,anchor='center',width=15)
        self.tabela_contrato_distribuido.place(relx= 0.05, rely= 0.4 , relwidth= 0.88, relheight=0.50)
        rolagem = Scrollbar(self.tabela_contrato_distribuido,orient='vertical')
        rolagem.pack(side='right',fill='y')
        rolagem.config(command=self.tabela_contrato_distribuido.yview)
        self.tabela_contrato_distribuido.config(yscrollcommand=rolagem.set)

        

        self.tabela_contrato_distribuido.tag_configure('normal', background='lightgray')
        self.tabela_contrato_distribuido.tag_configure('gray', background='white')
        tag = 'normal'

        for i in range(len(self.lista_contratos_distribuidos)):
            if tag == 'gray':
                tag = 'normal'
            else:
                tag = 'gray'

            self.tabela_contrato_distribuido.insert('','end',values=(self.lista_contratos_distribuidos[i][0],self.lista_contratos_distribuidos[i][1],self.lista_contratos_distribuidos[i][2]),tags=(tag))
                
        
        
        return

    def descrição_produtos(self):
        global ds_produtos
        sintaxe = '''SELECT name_produto FROM produtos order by name_produto ASC'''
        retorno = conexao_banco.busca_fetchall(self, sintaxe)
        ds_produtos = []
        for i in retorno:
            ds_produtos.append(i[0])

        return ds_produtos



    def filtro_busca(self):

        self.tabela_contrato_distribuido.tag_configure('normal', background='lightgray')
        self.tabela_contrato_distribuido.tag_configure('gray', background='white')

        tag = 'normal'

        if filtros_estado.get() == 0 and filtros_produto.get() == 0:
            messagebox.showerror(message='Informe o tipo de filtro')
                
        elif filtros_estado.get() == 1 and filtros_produto.get() == 1:
            messagebox.showerror(message='favor selecionar um tipo de filtro, dupla-seleção indisponivel até o momento')
            
        
        elif filtros_produto.get() == 1 :    

            for linha in self.tabela_contrato_distribuido.get_children():
                self.tabela_contrato_distribuido.delete(linha)


            if self.filtro_descricao_entry.get() in ds_produtos:
                sintaxe = ''' SELECT * FROM contratos WHERE ds_produtos = '{}' AND qntd_item IS NOT null ''' .format(self.filtro_descricao_entry.get())
                retorno = conexao_banco.busca_fetchall(self,sintaxe)
                print(retorno)
            
                for i in range (len(retorno)):
                    if tag == 'normal':
                        tag = 'gray'
                    else:
                        tag = 'normal'

                    script =   '''SELECT uf_estado FROM contratos 
                                    INNER JOIN contratos_distribuidos on contratos = id_contrato 
                                        WHERE id_contrato = '{}' GROUP by id_contrato '''.format(retorno[i][0])
                    busca_estado = conexao_banco.busca_fetchall(self,script)
                    self.tabela_contrato_distribuido.insert('','end',values=(retorno[i][0],retorno[i][3],busca_estado[0][0]),tags=(tag))
            else:
                messagebox.showerror(message='Item invalido')


        else:

            if self.filtro_estado_entry.get() in Destinos:
                sintaxe = ''' SELECT * FROM contratos_distribuidos WHERE uf_estado = '{}' ''' .format(self.filtro_estado_entry.get())
                retorno = conexao_banco.busca_fetchall(self,sintaxe)
                print(retorno)

                for linha in self.tabela_contrato_distribuido.get_children():
                    self.tabela_contrato_distribuido.delete(linha)
                

                for i in range (len(retorno)):
                    
                    if tag == 'normal':
                        tag = 'gray'
                    else:
                        tag = 'normal'

                    script = '''SELECT id_contrato, qtnd_produto_total, uf_estado FROM contratos 
	                                INNER JOIN contratos_distribuidos ON contratos = id_contrato 
		                                WHERE id_contrato =	{} '''.format(retorno[i][0])
                    busca_estado = conexao_banco.busca_fetchall(self,script)
                    self.tabela_contrato_distribuido.insert('','end',values=(busca_estado[0][0],busca_estado[0][1],busca_estado[0][2]),tags=(tag))
            else:


                error_Estado = messagebox.showerror(title='Erro filtro estado', Text='filtre um estado da listagem!')


          
        pass



    def limpar_tudo(self):
        self.filtro_estado_entry.delete(0, END)
        self.filtro_descricao_entry.delete(0, END)

        return print('Tudo limpo')





    #####  FUNÇÃO CONTRATOS PENDENTES   #####

    def contratos_pendentes(self):

        try:
            self.conteudo_lateral.destroy()
        except:
            print()

        script= '''SELECT contratos, SUM(qntd_item) FROM contratos
                    LEFT JOIN contratos_distribuidos ON contratos = id_contrato
                        WHERE id_contrato is null
                            GROUP BY 1'''

        self.retorno_contratos_pendentes = conexao_banco.busca_fetchall(self,script)
        
        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='CONTRATOS PENDENTES')
        

        self.tabela_pendentes = tk.Treeview(self.conteudo_lateral, columns= ['contrato', 'qntd_total_produtos'],show='headings')
        self.tabela_pendentes.heading('contrato',text='CONTRATOS')
        self.tabela_pendentes.column('contrato', anchor='center',width= 50,)
        self.tabela_pendentes.heading('qntd_total_produtos',text='QNTD_TOTAL_PRODUTOS')
        self.tabela_pendentes.column('qntd_total_produtos', anchor='center', width=50)
        self.tabela_pendentes.place(relheight=0.70 , relwidth=0.88 , relx= 0.05 , rely=0.2)
        
        #estilo para as linhas da tabela
        self.tabela_pendentes.tag_configure('normal', background='lightgray')
        self.tabela_pendentes.tag_configure('gray', background='white')
        tag = 'normal'

        for i in range(len(self.retorno_contratos_pendentes)):
            if tag == 'gray':
                tag = 'normal'
            else:
                tag = 'gray'

            self.tabela_pendentes.insert('',index='end', values=(self.retorno_contratos_pendentes[i][0],self.retorno_contratos_pendentes[i][1]),tags= (tag))               



        
        return


    def criar_usuario(self):
        try:
            self.conteudo_lateral.destroy()
        except:
            print()

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='CRIAÇÃO DE USUÁRIO')


        ####  campos de cadastro  ####
        self.titulo_cria_usuario = Label(self.conteudo_lateral, text='Formulario usuario',font=('calibri', 15))
        self.titulo_cria_usuario.pack(anchor='center',side='top')




        #### Label informações ####
        self.label_info_cria_usuario = LabelFrame(self.conteudo_lateral, text="Pessoais")
        self.label_info_cria_usuario.place(relheight=0.25  , relwidth=0.95, relx= 0.025, rely=0.10)


        # nome
        self.nome_cria_usuario = Label(self.label_info_cria_usuario, text=('Nome:'),font=('Arial' , 12))
        self.nome_cria_usuario.place(rely=0.08,relx= 0.05)
        self.nome_cria_usuario_entry = Entry(self.label_info_cria_usuario,justify=CENTER)
        self.nome_cria_usuario_entry.place(relx= 0.27 , rely=0.08, relwidth=0.50 )
        self.nome_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')
        self.nome_cria_usuario_entry.focus_force()

        # idade
        self.idade_cria_usuario =Label(self.label_info_cria_usuario, text=('Idade:'),font=('Arial' , 12))
        self.idade_cria_usuario.place(rely=0.35,relx=0.05)
        self.idade_cria_usuario_entry = Entry(self.label_info_cria_usuario,justify=CENTER)
        self.idade_cria_usuario_entry.place(relx=0.27 , rely=0.35, relwidth=0.50 )
        self.idade_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')

        # cpf
        self.cpf_cria_usuario =Label(self.label_info_cria_usuario, text=('CPF:'),font=('Arial' , 12))
        self.cpf_cria_usuario.place(relx= 0.05, rely=0.62)
        self.cpf_cria_usuario_entry = Entry(self.label_info_cria_usuario,justify=CENTER)
        self.cpf_cria_usuario_entry.place(relx=0.27 , rely=0.62, relwidth=0.50 )
        self.cpf_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')


        ##### label contatos ######
        self.label_contatos_cria_usuario = LabelFrame(self.conteudo_lateral, text="Contato/Endereço")
        self.label_contatos_cria_usuario.place(relheight=0.30  , relwidth=0.95, relx= 0.025, rely=0.355)


        # cidade
        self.cidade_cria_usuario =Label(self.label_contatos_cria_usuario, text=('Cidade:'),font=('Arial' , 12))
        self.cidade_cria_usuario.place(rely=0.06, relx= 0.05)
        self.cidade_cria_usuario_entry = Entry(self.label_contatos_cria_usuario,justify=CENTER)
        self.cidade_cria_usuario_entry.place(relx=0.25 , rely=0.06, relwidth=0.42 )
        self.cidade_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')


        # rua 
        self.rua_cria_usuario =Label(self.label_contatos_cria_usuario, text=('Endereço:'),font=('Arial' , 12))
        self.rua_cria_usuario.place(relx= 0.05, rely=0.25)
        self.rua_cria_usuario_entry = Entry(self.label_contatos_cria_usuario,justify=CENTER)
        self.rua_cria_usuario_entry.place(relx=0.25 , rely=0.25, relwidth=0.42 )
        self.rua_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')


        # telefone
        self.telefone_cria_usuario =Label(self.label_contatos_cria_usuario, text=('Telefone:'),font=('Arial' , 12))
        self.telefone_cria_usuario.place(relx= 0.05, rely=0.45)
        self.telefone1_cria_usuario_entry = Entry(self.label_contatos_cria_usuario,justify='center')
        self.telefone1_cria_usuario_entry.place(relx=0.25 , rely=0.45, relwidth=0.05 )
        self.telefone1_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')
        self.telefone2_cria_usuario_entry = Entry(self.label_contatos_cria_usuario, justify='center')
        self.telefone2_cria_usuario_entry.place(relx=0.30 , rely=0.45, relwidth=0.18 )
        self.telefone2_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')
        self.telefone3_cria_usuario_entry = Entry(self.label_contatos_cria_usuario, justify='center')
        self.telefone3_cria_usuario_entry.place(relx=0.49 , rely=0.45, relwidth=0.18 )
        self.telefone3_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')


        # email
        self.email_cria_usuario =Label(self.label_contatos_cria_usuario, text=('E-mail:'),font=('Arial' , 12))
        self.email_cria_usuario.place(relx= 0.05, rely=0.65)
        self.email_cria_usuario_entry = Entry(self.label_contatos_cria_usuario, justify=CENTER)
        self.email_cria_usuario_entry.place(relx=0.25 , rely= 0.65, relwidth=0.42)
        self.email_cria_usuario_entry.config(highlightthickness= 2,highlightcolor='lightblue')

        # permissao
        self.permissao_cria_usuario =Label(self.label_contatos_cria_usuario, text=('Permissão:'),font=('Arial' , 12))
        self.permissao_cria_usuario.place(relx= 0.68, rely=0.36)
        self.permissao_admin_cria_usuario = IntVar()
        self.check_permissao_cria_usuario = Checkbutton(self.label_contatos_cria_usuario, text='Admin', variable=self.permissao_admin_cria_usuario)
        self.check_permissao_cria_usuario.place(relx= 0.86 , rely=0.28)
        self.permissao_padrao_cria_usuario = IntVar()
        self.check_permissao_cria_usuario = Checkbutton(self.label_contatos_cria_usuario, text='Padrão', variable=self.permissao_padrao_cria_usuario )
        self.check_permissao_cria_usuario.place(relx= 0.86 , rely=0.48)


        
        #### Label ACESSO ####
        
        self.label_senha_cria_usuario = LabelFrame(self.conteudo_lateral, text='Acesso')
        self.label_senha_cria_usuario.place(relx=0.025, rely=0.66, relheight=0.25  , relwidth= 0.95 )
        
        # senha
        self.senha_cria_usuario =Label(self.label_senha_cria_usuario, text=('Senha:'),font=('Arial' , 12))
        self.senha_cria_usuario.place(relx=0.05  , rely= 0.20 )
        self.senha_cria_usuario_entry = Entry(self.label_senha_cria_usuario, show='*',justify=CENTER)
        self.senha_cria_usuario_entry.place(relx=0.27  , rely= 0.20 , relwidth= 0.50 )
        self.senha_cria_usuario_entry.config(highlightthickness =2, highlightcolor='lightblue')   


        self.confirmacao_cria_usuario =Label(self.label_senha_cria_usuario, text=('Confirmação:'),font=('Arial' , 12))
        self.confirmacao_cria_usuario.place(relx=0.05  , rely= 0.50 )
        self.confirmacao_cria_usuario_entry = Entry(self.label_senha_cria_usuario, show='*',justify=CENTER)
        self.confirmacao_cria_usuario_entry.place(relx=0.27  , rely= 0.50 , relwidth= 0.50 )
        self.confirmacao_cria_usuario_entry.config(highlightthickness =2, highlightcolor='lightblue')      

        self.botao_cadastrar_usuario = Button(self.conteudo_lateral,default='active', text='Cadastrar Usuário', command=self.valida_campos_formulario)
        self.botao_cadastrar_usuario.pack(anchor='center', side= BOTTOM, pady=8 ) 
        self.botao_cadastrar_usuario.bind('<Return>', self.valida_campos_formulario)

        

        return

    def valida_campos_formulario(self, event= None):
        self.validacao = True
        # cpf = self.cpf_cria_usuario_entry.get()
        # cpf = cpf[:3]+'.'+ cpf[3:6]+'.'+ cpf[6:9]+'.'+ cpf[9:]
        # self.cpf_cria_usuario_entry.config(show=cpf)


        if len(self.cpf_cria_usuario_entry.get()) != 11:
            self.cpf_cria_usuario_entry.focus_force()
            self.cpf_cria_usuario_entry.config(highlightcolor='red')
            messagebox.showinfo('Erro de Preenchimento', message='CPF Invalido.')
            self.validacao = False
        
        if len(self.telefone1_cria_usuario_entry.get()) != 2:
            self.telefone1_cria_usuario_entry.focus_force()
            self.telefone1_cria_usuario_entry.config(highlightcolor='red')
            messagebox.showinfo('Erro de Preenchimento', message='DDD brasileiro Invalido')
            self.validacao = False

        if len(self.telefone2_cria_usuario_entry.get()) != 5:
            self.telefone2_cria_usuario_entry.focus_force()
            self.telefone2_cria_usuario_entry.config(highlightcolor='red')
            messagebox.showinfo('Erro de Preenchimento', message='Número Invalido')
            self.validacao = False


        if len(self.telefone3_cria_usuario_entry.get()) != 4:
            self.telefone3_cria_usuario_entry.focus_force()
            self.telefone3_cria_usuario_entry.config(highlightcolor='red')
            messagebox.showinfo('Erro de Preenchimento', message='Número Invalido')
            self.validacao = False
            

        if len(self.senha_cria_usuario_entry.get()) < 3:
            self.senha_cria_usuario_entry.focus_force()
            self.senha_cria_usuario_entry.config(highlightcolor='red')
            messagebox.showinfo('Erro de Preenchimento', message='Minimo de 3 caracteres para a senha.')
            self.validacao = False

        return self.cadastrar_usuario()




    def cadastrar_usuario(self, event=None):

        if self.validacao == True:    

            if self.senha_cria_usuario_entry.get() == self.confirmacao_cria_usuario_entry.get():
                print(self.nome_cria_usuario_entry.get(), self.idade_cria_usuario_entry.get(), self.cpf_cria_usuario_entry.get())
                nome = self.nome_cria_usuario_entry.get().capitalize()
                idade = int(self.idade_cria_usuario_entry.get())
                cidade = self.cidade_cria_usuario_entry.get().capitalize()
                rua = self.rua_cria_usuario_entry.get()
                cpf = self.cpf_cria_usuario_entry.get()
                cpf = cpf[:3]+'.'+ cpf[3:6]+'.'+ cpf[6:9]+'.'+ cpf[9:]
                telefone = self.telefone1_cria_usuario_entry.get() + ' ' + self.telefone2_cria_usuario_entry.get() + '-' + self.telefone3_cria_usuario_entry.get()
                email = self.email_cria_usuario_entry.get()
                senha = self.senha_cria_usuario_entry.get()
                if self.permissao_admin_cria_usuario.get() == 1 and self.permissao_padrao_cria_usuario == 1:
                    messagebox.showwarning(title='Erro na escolha', message='Favor atribuir apenas uma permissão ao usuário.')
                    
                elif self.permissao_admin_cria_usuario.get() == 1:
                    permissao = 'admin'
                elif self.permissao_padrao_cria_usuario.get() == 1:
                    permissao = 'padrão'
                
                num_maximo_user =conexao_banco.busca_fetchone(self, sintaxe='SELECT max(user_id) FROM logins')
                id_user = num_maximo_user[0]+1


                script = '''INSERT INTO logins (user_id, nome, idade, cidade, rua, cpf, telefone, email, senha, permissao)
                                VALUES('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )'''.format(id_user, nome,idade,cidade, rua, cpf, telefone, email, senha, permissao)


                conexao_banco.insere(self, script)

                print('cadastro ok')
                messagebox.showinfo(title='Cadastro de usuário', message='Usuario Cadastrado com Exito')

                self.nome_cria_usuario_entry.delete(0,END)
                self.idade_cria_usuario_entry.delete(0,END)
                self.cidade_cria_usuario_entry.delete(0,END)
                self.rua_cria_usuario_entry.delete(0,END)
                self.cpf_cria_usuario_entry.delete(0,END)
                self.telefone1_cria_usuario_entry.delete(0,END)
                self.telefone2_cria_usuario_entry.delete(0,END)
                self.telefone3_cria_usuario_entry.delete(0,END)
                self.email_cria_usuario_entry.delete(0,END)
                self.senha_cria_usuario_entry.delete(0,END)

                self.confirmacao_cria_usuario_entry.delete(0,END)
                self.nome_cria_usuario_entry.focus_force()
                



            else:

                print('Senha não está igual.')
                messagebox.showinfo(title='Cadastro de usuário', message='Verificar preenchimento')








        return









    ##### FUNÇÃO RELATORIO #####
    def relatorio(self):
        global tipo_relatorio
        try:
            self.conteudo_lateral.destroy()
        except:
            print('ok')

        self.cria_conteudo_lateral()
        self.conteudo_lateral.config(text='RELATÓRIO')

        self.tipo_de_relatorio_label = Label(self.conteudo_lateral,text='Buscar por: ', font=('arial', 12))
        self.tipo_de_relatorio_label.place(relx=0.10  , rely=0.18)

        tipo_relatorio = ['PENDENTES','DISTRIBUIDOS','GERAL','PERSONALIZADO']
        self.tipo_de_relatorio = tk.Combobox(self.conteudo_lateral,values=tipo_relatorio)
        self.tipo_de_relatorio.place(relx=0.4  , rely=0.19)
        self.tipo_de_relatorio.bind('<<ComboboxSelected>>', self.escolha)
        self.tipo_de_relatorio.focus_force()

        self.frame_relatorio = LabelFrame(self.conteudo_lateral, text='Informações adicionais')
        self.frame_relatorio.place(rely=0.45, relheight=0.47, relx=0.02, relwidth=0.96)


        self.nome_relatorio = Label (self.frame_relatorio, text='Nome do relatório: ', font=('arial', 12))
        self.nome_relatorio.place(rely=0.15, relx= 0.02)
        self.nome_relatorio_entry = Entry(self.frame_relatorio)
        self.nome_relatorio_entry.place(rely= 0.17 , relx=0.33, relwidth=0.55)


        self.formato_relatorio = Label (self.frame_relatorio, text='Formato do relatório: ', font=('arial', 12))
        self.formato_relatorio.place(rely=0.40, relx= 0.02)
        self.valor_csv_relatorio = IntVar()
        self.formato_checkbox1 = Checkbutton(self.frame_relatorio, text='CSV', variable=self.valor_csv_relatorio)
        self.formato_checkbox1.place(rely= 0.42 , relx=0.43)
        self.valor_txt_relatorio = IntVar()
        self.formato_checkbox2 = Checkbutton(self.frame_relatorio, text='TXT', variable=self.valor_txt_relatorio)
        self.formato_checkbox2.place(rely= 0.42 , relx=0.63)

        self.button_relatorio = Button(self.frame_relatorio,text='Gerar Relatorio', command=self.func_button_relatorio)
        self.button_relatorio.place(rely= 0.75 , relx= 0.45)

        self.button_relatorio_grafico = Button(self.frame_relatorio,text='Gerar Gráfico', command=self.func_button_grafico,default='normal')
        self.button_relatorio_grafico.place(rely= 0.75 , relx= 0.25)

        return

    def escolha(self, event=None):
        if self.tipo_de_relatorio.get() == 'PERSONALIZADO':
            self.tipo_de_relatorio_label.place(relx=0.05  , rely=0.07)
            self.tipo_de_relatorio.place(relx= 0.30 , rely=0.08)

            self.estado_relatorio = Label(self.conteudo_lateral,text='Estado: ', font=('arial', 12))
            self.estado_relatorio.place(relx=0.05 , rely=0.14)
            self.estado_relatorio_entry = tk.Combobox(self.conteudo_lateral,values=Destinos, state='disabled')
            self.estado_relatorio_entry.place(relx= 0.27  , rely= 0.15, relwidth= 0.55)
            self.valida_estado = IntVar()
            self.check1 = Checkbutton(self.conteudo_lateral ,variable=self.valida_estado)
            self.check1.place(relx=0.85 , rely=0.14)
            self.check1.bind('<Button-1>', self.bind_checkbutton_estado)


            self.contrato_relatorio = Label(self.conteudo_lateral, text='Contrato: ', font=('arial', 12))
            self.contrato_relatorio.place(relx= 0.05 , rely=0.21 )
            self.contrato_relatorio_entry = tk.Combobox(self.conteudo_lateral,values=conexao_banco.busca_informacoes_personalizado(conexao_banco),state='disabled')
            self.contrato_relatorio_entry.place(relx=0.27 , rely=0.22, relwidth= 0.55)
            self.valida_contrato = IntVar()
            self.check2 = Checkbutton(self.conteudo_lateral ,variable=self.valida_contrato)
            self.check2.place(relx=0.85 , rely=0.21)
            self.check2.bind('<Button-1>', self.bind_checkbutton_contrato)

            self.produto_relatorio = Label(self.conteudo_lateral, text='Produto: ', font=('arial', 12))
            self.produto_relatorio.place(relx=0.05 , rely=0.28 )
            self.produto_relatorio_entry = tk.Combobox(self.conteudo_lateral, values= ds_produtos, state='disabled')
            self.produto_relatorio_entry.place(relx=0.27 , rely=0.29, relwidth= 0.55)
            self.valida_produto = IntVar()
            self.check3 = Checkbutton(self.conteudo_lateral ,variable=self.valida_produto)
            self.check3.place(relx=0.85 , rely=0.28)
            self.check3.bind('<Button-1>', self.bind_checkbutton_produto)



            # script = '''SELECT * FROM contratos
	        #                 ORDER BY 1 asc'''
            # self.cabeçalho = 'ID_CONTRATO;ID_PRODUTO;DS_PRODUTO;QNTD_ITEM\n'
            self.button_relatorio_grafico.config(state='disabled')
        
        elif self.tipo_de_relatorio.get() == 'PENDENTES':
            self.button_relatorio_grafico.config(state='active')
            self.corrige_posicao()

            script=  '''SELECT contratos, SUM(qntd_item) FROM contratos 
                            left JOIN contratos_distribuidos on contratos = id_contrato
                                WHERE id_contrato is null
                                    GROUP BY contratos'''
            self.cabeçalho = 'CONTRATOS;QNTD_PRODUTO_TOTAL_CONTRATO\n'

        elif self.tipo_de_relatorio.get() == 'DISTRIBUIDOS':
            self.button_relatorio_grafico.config(state='active')
            self.corrige_posicao()

            script =    '''SELECT * FROM contratos_distribuidos
                            ORDER BY id_contrato ASC'''
            self.cabeçalho = 'ID_CONTRATO;QNTD_PRODUTO_TOTAL;UF_ESTADO\n'

        elif self.tipo_de_relatorio.get() == 'GERAL':
            self.button_relatorio_grafico.config(state='active')
            self.corrige_posicao()

            script = '''SELECT * FROM contratos
	                        ORDER BY 1 asc'''
            self.cabeçalho = 'ID_CONTRATO;ID_PRODUTO;DS_PRODUTO;QNTD_ITEM\n'
            
        try:
            self.retorno_relatorio = conexao_banco.busca_fetchall(self, script)
        except:
            print('Foi personalizado')

        return 

    def bind_checkbutton_estado(self, event=None):
        
        # se : estado, não busco por contrato (pode combinar com produto)
        
        if self.valida_estado.get() == 0:
            self.estado_relatorio_entry.config(state='normal')
            self.check2.config(state='disabled')
            print(self.valida_estado.get())
        else:
            self.estado_relatorio_entry.config(state='disabled')
            self.check2.config(state='normal')
            print(self.valida_estado.get())

    def bind_checkbutton_contrato(self, event=None):

        # # se : contrato não busco por produto  estado
        if self.valida_contrato.get() == 0:
            self.contrato_relatorio_entry.config(state='normal')
            self.check1.config(state='disabled')
            self.check3.config(state='disabled') 
        else:
            self.contrato_relatorio_entry.config(state='disabled') 
            self.check1.config(state='normal')
            self.check3.config(state='normal') 

    def bind_checkbutton_produto(self, event=None):

        if self.valida_produto.get() == 0:
            self.produto_relatorio_entry.config(state='normal')
            self.check2.config(state='disabled')
        else:
            self.produto_relatorio_entry.config(state='disabled')
            self.check2.config(state='normal')


    def relatorio_personalizado(self): 
        print(self.valida_contrato.get())


        if self.valida_contrato.get() == 1:
            script ='''SELECT * FROM contratos
                            WHERE contratos = {} '''.format(int(self.contrato_relatorio_entry.get()))
            self.cabeçalho = 'contrato;id_produto;ds_produto;qntd_item\n'

        elif self.valida_estado.get() == 1:
            script =''' SELECT * FROM contratos_distribuidos
                            WHERE uf_estado = '{}' '''.format(self.estado_relatorio_entry.get())
            self.cabeçalho = 'id_contrato;qntd_produto_total;uf_estado\n'


        elif self.valida_produto.get() == 1:
            script = '''SELECT contratos,uf_estado FROM contratos 
                            INNER JOIN contratos_distribuidos on contratos = id_contrato
                                WHERE ds_produtos = '{}' '''.format(self.produto_relatorio_entry.get().upper())
            self.cabeçalho = 'contrato;uf_estado\n'

        
        self.retorno_relatorio = conexao_banco.busca_fetchall(self, script)

        print(self.retorno_relatorio)            


        print('testando, passou aqui')
        
        return self.cabeçalho,self.retorno_relatorio



    def corrige_posicao(self):
        try:
            self.estado_relatorio.destroy()
            self.estado_relatorio_entry.destroy()
            self.contrato_relatorio.destroy()
            self.contrato_relatorio_entry.destroy()
            self.produto_relatorio.destroy()
            self.produto_relatorio_entry.destroy()
            self.tipo_de_relatorio_label.place(relx=0.10  , rely=0.18)
            self.tipo_de_relatorio.place(relx=0.4  , rely=0.19)
            self.check1.destroy()
            self.check2.destroy()
            self.check3.destroy()

        except:
            TypeError
            
        return


    def func_button_relatorio(self):
        try:
            self.relatorio_personalizado()
        except:
            print('Não foi personalizado')
      
        if self.valor_txt_relatorio.get() == 1: 
            print("TXT")
 

            file = open(self.nome_relatorio_entry.get()+'.txt','a+')
            file.write(self.cabeçalho)
            for i in range(len(self.retorno_relatorio)):
                texto = self.retorno_relatorio[i]
                file.write(str(texto))
                file.write('\n')
            file.close()


            print('arquivo criado com sucesso')
            self.nome_relatorio_entry.delete(0,END)



        if self.valor_csv_relatorio.get() == 1: print("CSV") 
        
        return


    def gera_grafico(self, extracao, titulo, pos_x, pos_y, tipo_grafico=['barra','linha','barra_deitada']):
        lista= []
        numeros= []
        
        for i in range(len(extracao)):
            x = extracao[i][int(pos_x)]
            y = extracao[i][int(pos_y)]
            lista.append(x)
            numeros.append(y)
        fig, ax = plt.subplots()
        ax.set_title(titulo,loc='center')
        if tipo_grafico == 'barra': 
            ax.bar(lista, numeros,tick_label=lista)
        elif tipo_grafico == 'linha':
            ax.plot(lista, numeros)
        elif tipo_grafico == 'barra_deitada':
            ax.barh(lista, numeros)


        return plt.show()
    

    def func_button_grafico(self):
        if self.tipo_de_relatorio.get() == 'PENDENTES':

            self.gera_grafico(self.retorno_relatorio,titulo='CONTRATOS PENDENTES',pos_x=0, pos_y=1,tipo_grafico= 'barra')



        if self.tipo_de_relatorio.get() == 'DISTRIBUIDOS':
            
            script = '''SELECT uf_estado, count(id_contrato) as contagem FROM contratos_distribuidos
	                        GROUP BY uf_estado'''
            self.dados_grafico = conexao_banco.busca_fetchall(self, script)
            print(self.dados_grafico)

            self.gera_grafico(self.dados_grafico,titulo='CONTRATOS DISTRIBUIDOS',pos_x=0, pos_y=1,tipo_grafico='barra')

        if self.tipo_de_relatorio.get() == 'GERAL':

            script= '''SELECT contratos, count(id_produto) as "QNTD_ITEM_CONTRATO" FROM contratos
	                        GROUP BY contratos
		                        ORDER BY contratos ASC'''
            self.dados_grafico = conexao_banco.busca_fetchall(self,script)
            print(self.dados_grafico)

            self.gera_grafico(self.dados_grafico,titulo= 'GERAL - ITENS POR CONTRATO',pos_x=0, pos_y=1,tipo_grafico= 'barra')            


        pass

    #função fechar conteudo
    def fechar(self):
        self.conteudo_lateral.destroy()
        self.janela.update()

    
    def sair_do_sistema(self):
        self.janela.destroy()
        

        tela_login_logistica1()
        return









class conexao_banco:
    def busca_fetchall(self,sintaxe):  #ok
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            self.retorno = self.cursor.fetchall()
            self.conecta.close()

            return self.retorno

    def insere(self,sintaxe):
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            self.conecta.commit()
            self.conecta.close()

            return self.retorno

    def busca_fetchone(self,sintaxe): #ok
            self.conecta = psycopg2.connect(database='user', user='postgres', password='1804')
            self.cursor= self.conecta.cursor()
            self.cursor.execute(sintaxe)
            self.retorno = self.cursor.fetchone()
            self.conecta.close()

            return self.retorno

    def busca_informacoes_personalizado(self):
        script = ''' SELECT contratos FROM contratos GROUP BY contratos ORDER BY CONTRATOS DESC'''
        
        contratoteste = conexao_banco.busca_fetchall(self,script)
        self.lista_contratos = []
        for i in range(len(contratoteste)):
            self.lista_contratos.append(contratoteste[i])

        return self.lista_contratos


sistema()