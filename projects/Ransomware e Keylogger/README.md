# 🛡️ Simulações de Malware com Python (Ambiente Controlado e Educacional)

Este projeto faz parte de um estudo prático sobre **Segurança da Informação**, com foco em entender — de forma **segura e ética** — como funcionam dois tipos comuns de malware:

- 🔐 Ransomware (simulado)
- 🎹 Keylogger (simulado)

Todo o conteúdo aqui tem caráter **exclusivamente educacional** e roda apenas em **ambiente controlado**.  
Nenhum dos scripts causa dano real, não se replica, não se oculta e não executa operações destrutivas.

---

# 📁 Estrutura do Repositório

# 🔐 1. Ransomware Simulado (Educacional)

Este exemplo demonstra:

- Como criptografar arquivos usando Python e a biblioteca `cryptography`
- Como gerar uma mensagem de “resgate” (somente ilustrativa)
- Como descriptografar os arquivos com a chave correta

### ⚠️ Observações importantes
- Este projeto é *inofensivo* e só funciona na pasta de teste criada pelo usuário.
- Não apaga, danifica ou sequestra dados reais.

---

## ▶️ Como usar:

### 1. Crie alguns arquivos dentro de `/ransomware_simulado/arquivos_teste/`

Exemplo:  
teste1.txt
teste2.txt

shell
Copiar código

### 2. Execute o script de criptografia:
python encrypt.py


Isso irá:

- Gerar uma chave
- Criptografar o conteúdo dos arquivos
- Criar a mensagem de resgate (simulada)

### 3. Para reverter:
python decrypt.py


---

# 🎹 2. Keylogger Simulado (Educacional)

Este exemplo demonstra:

- Captura simples de teclas com a biblioteca `pynput`
- Registro em arquivo `.txt`
- Possibilidade de envio por e-mail **somente para conta de testes**

### ⚠️ Segurança e Ética
- Não roda oculto  
- Não se instala sozinho  
- Todos os arquivos gerados são visíveis  
- Só deve ser executado pelo próprio aluno em ambiente de estudo  

---

# 📦 3. Como Executar os Scripts

### Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


### Instale as dependências:
pip install cryptography pynput


---

# 🛡️ 4. Medidas de Prevenção e Defesa (Reflexão)

### 🔒 Antivírus
- Detectam comportamentos suspeitos, como criptografia em massa ou captura de teclas.

### 🧱 Firewall
- Impede conexões externas não autorizadas.
- Pode bloquear keyloggers que tentem enviar dados.

### 📦 Sandbox
- Permite analisar arquivos suspeitos sem risco ao sistema real.

### 👤 Conscientização do Usuário
- A maioria dos ataques depende de engenharia social.
- Entender como malwares funcionam é essencial.

---

# 🎓 5. Conclusão

Este projeto ajudou a compreender:

- Como funcionam basicamente ransomwares e keyloggers
- Como vulnerabilidades humanas são exploradas
- Como aplicar Python em simulações controladas
- Como se defender melhor de ataques reais

---

# 🔗 Recursos

- Python Docs  
- Cryptography (Fernet)  
- pynput  
- smtplib

