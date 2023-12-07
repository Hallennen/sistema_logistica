from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
import psycopg2
# from sistema_logistica import sistema


retorno_xyz = False

class tela_login_logistica1:
    def __init__(self) :
        self.tela_login()
        pass

        #CRIAÇÃO DA TELA DE LOGIN
    def tela_login(self) :
        self.tela = Tk()
        self.tela.title('Acess')
        self.tela.geometry('400x500+450+150')

        self.user = Label(self.tela, text='Usuario: ', font=('Arial Black', 15))
        self.user.place(relx=0.39, rely= 0.25)
        self.user_entry = Entry(self.tela, font=('Arial', 15))
        self.user_entry.place(relx= 0.2 , rely=0.33 , relwidth= 0.6, relheight=0.06)


        self.senha = Label(self.tela, text='Senha: ', font=('Arial Black', 15))
        self.senha.place(relx= 0.41 , rely= 0.45)
        self.senha_entry = Entry(self.tela,font=('Arial', 15), show='*')
        self.senha_entry.place(relx= 0.2 , rely=0.53 , relwidth= 0.6, relheight=0.06)


        self.btn_entrar = Button(self.tela,text='Logar', command=self.button) #command=sistema
        self.btn_entrar.place(relx=0.4 , rely= 0.7, relwidth=0.2 )

        self.user_entry.focus_force()
        self.senha_entry.bind('<Return>', self.button)
        self.btn_entrar.bind('<Return>', self.button)
        
        
        return Tk.mainloop(self.tela)

        #FUNÇÃO BOTÃO LOGAR
    def button(self, event=None):
        global retorno_xyz,nome_user,permissao_user

        #BUSCA OS USUARIOS E SENHAS NO BANCO DE DADOS
        script = '''SELECT nome, senha, permissao FROM logins '''
        retorno = conexao.busca_fetchall(self,script)


        #VALIDA SE O USUARIO E SENHA ESTÃO OK 
        try:
            for i in range(len(retorno)):
                if self.user_entry.get().capitalize() in retorno[i] and self.senha_entry.get() in retorno[i]:
                    print('logado')

                    nome_user = retorno[i][0]
                    permissao_user = retorno[i][2]

                    retorno_xyz = True

                    self.tela.destroy()
                else: 
                    pass
        except:
            pass

        # print("usuario / senha invalidos")

        try: 
            self.senha_entry.delete(0, END)
            self.error = messagebox.showerror(title='Acesso Negado',message="usuario / senha invalidos")
            self.user_entry.delete(0, END)
            print("usuario / senha invalidos")   
            self.user_entry.focus_force()  
        except:
            pass
        return 



    #CLASSE CONEXÃO DO BANCO
class conexao():
    def busca_fetchall(self,script):
        self.connect =psycopg2.connect(database='user',user='postgres',password='1804')
        self.cursor= self.connect.cursor()
        self.cursor.execute(script)
        self.retorno_banco = self.cursor.fetchall()
        
        return self.retorno_banco


tela_login_logistica1()