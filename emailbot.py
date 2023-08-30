import smtplib # Biblioteca de envio de emails 
#Simple mail transfer protocol
from email.mime.multipart import MIMEMultipart # Serve para criar uma msg multipart
# Mime = Norma de envio de emails 
from email.mime.text import MIMEText #Cria um objeto para envio de mensagens de texto
from email.mime.base import MIMEBase #Serve para enviarmos coisas em anexo
from email import encoders #Serve para codigicar mensagens


fromaddr = "giovanni@gmail.com"
toaddr = "bazim@gmail.com"

msg = MIMEMultipart()


msg["From"] = fromaddr 
# Variavel do responsavel do  envio
msg["To"] = toaddr #Variavel do remetente
msg["Subject"] = "Hello world" #Titulo

html = """

<html>
    <head>
        <style>
            p{
                font-family:Georgia, 'Times New Roman', Times, serif;
            }
        </style>

    </head>
    <body>
            <p>Hello world</p>
    </body>
</html>

"""
part1 = MIMEText(html, "html") #Passa variavel html e a linguagem que estamos usando (html)
msg.attach(part1)
#usar o agendador de tarefas do windows para disparar automatico ao 12:00

s = smtplib.SMTP('smtp.gmail.com', 587) 
#Servidor do gmail

s.starttls() # Fazer uma conexão segura 

s.login(fromaddr, "senha") 
#Responsavel por fazer login
#Senha do app (Segurança)

print("Enviando email...")
text = msg.as_string() #Transforma tudo em string
s.sendmail(fromaddr, toaddr, text) #Envia o email
s.quit() #Fechar a conexao com o servidor
print("Email enviado...")
