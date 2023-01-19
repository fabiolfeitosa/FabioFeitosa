#!/usr/bin/env python
# coding: utf-8

# In[1]:


#instalando biblioteca
#pip install mysql-connector-python


# In[9]:


#instalando biblioteca para tornar executavel nosso script python
#pip install pyinstaller


# In[1]:


# Importamos a biblioteca:
import mysql.connector


# In[2]:


# Conectando ao database:
conexao = mysql.connector.connect(host='localhost', db= 'db_sp_alagamentos', user='root', passwd='')


# In[3]:


#Testando conexao
if conexao.is_connected():
    db_info = conexao.get_server_info()
    print('Conectado ao servidor Mysql', db_info)
    cursor = conexao.cursor() #cursor é um objeto que permite navegar/manipular db
    cursor.execute('select database();')
    linha = cursor.fetchone() #fetchone retorna apenas uma linha
    print('Conectado ao database : ', linha)


# In[4]:


#Funcao de cadastro das ocorrencias
def reg_ocorrencias():
    banco = mysql.connector.connect(host='localhost', db= 'db_sp_alagamentos', user='root', passwd='')
    cursor = banco.cursor()
    email_user = input('Digite email novamente:')
    cursor.execute("SELECT Id_User from usuario WHERE Email = '{}'".format(email_user))
    id_user_db = cursor.fetchall()
    print(id_user_db[0][0])
   
        
    reg_id = int(id_user_db[0][0])
    reg_rua = input("Insira Rua/Av: ")    
    reg_bairro = input("Insira Bairro: ")    
    reg_cidade = input("Insira Cidade: ")    
    reg_estado = input("Insira Estado: ")    
    reg_intensidade = input("Insira classificacao de intensidade sendo Leve, Moderado ou Grave: )")    
    reg_classificacao = input("Classificacao como Alagamento localizado ou Intransitável: )")    
    cursor.execute("""INSERT INTO ocorrencias(Id_User, Rua, Bairro, Cidade, Estado, Intensidade, Classificacao) VALUES (%s,%s, %s, %s, %s,%s, %s)""",
    (reg_id, reg_rua, reg_bairro, reg_cidade, reg_estado, reg_intensidade,reg_classificacao)) 
    conexao.commit()
    print("Ocorrencia inserido com sucesso!")
    cursor.close()
    banco.close()


# In[5]:


#função de cadastro do usuario
def reg_usuario():

    reg_nome = input(" Insira seu nome completo: ")
    
    reg_email = input("Insira Email: ")
    
    reg_senha = int(input("Insira senha de acesso ao app com 8 digitos numéricos: "))
    
    reg_tel = int(input("Insira telefone com DDD - apenas numeros: )"))
    
    cursor.execute("""INSERT INTO usuario(Nome, Email, Senha, Telefone) VALUES (%s, %s, %s, %s)""", (reg_nome, reg_email, reg_senha, reg_tel)) 
    conexao.commit()
    print("Dados usuario inseridos com sucesso!")


# In[6]:


#funcao de login
def login():
    email_user = input("Digite email de acesso: ")
    senha = input("Digite a senha: ")
    banco = mysql.connector.connect(host='localhost', db= 'db_sp_alagamentos', user='root', passwd='')
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT Senha from usuario WHERE Email = '{}'".format(email_user))
        senha_db = cursor.fetchall()
        print(senha_db[0][0])#remover por segurança a senha
        cursor.execute("SELECT Email from usuario WHERE Email = '{}'".format(email_user))
        email_db = cursor.fetchall()
        banco.close()
    
        if senha == senha_db[0][0] and email_user == email_db[0][0]:
            print("Usuario conectado, faça registro da sua ocorrencia")
            reg_ocorrencias()
         
        elif senha != senha_db[0][0] and email_user == email_db[0][0]:
            print("Senha Invalida!")
        
    except:
        reg_usuario()
        print('Cadastro do usuario inserido!')


# In[8]:


#chamada da função de login
login() 


# In[ ]:


#encerrando conexao
if conexao.is_connected():
    cursor.close()
    conexao.close()
    print('Conexao encerrado')


# In[ ]:


#para executavel não encerrar sozinho após finalizar
input("Pressione <enter> para encerrar!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




