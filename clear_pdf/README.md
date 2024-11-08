# 📄 PDF to LLM Training Data

Este repositório contém uma aplicação que permite o upload de documentos PDF, inclusive com imagens, para processamento e preparação como dados de treinamento para Modelos de Linguagem Grande (LLM). Ideal para projetos que envolvem modelos baseados em NLP (Processamento de Linguagem Natural), onde é essencial extrair e formatar textos e conteúdos para aprendizado de máquina.

---

## 🎯 Funcionalidades

- **Upload de PDF**: Permite o upload de arquivos PDF, suportando documentos com texto e imagens.
- **Extração de Texto e Imagens**: Processa o PDF para extrair texto e imagens de cada página.
- **Pré-processamento para LLM**: Formata o conteúdo extraído, estruturando-o em um formato adequado para ser usado como dado de treinamento em modelos de linguagem.
- **Exportação de Dados**: Salva o conteúdo processado em um formato estruturado (JSON, CSV, ou outro formato escolhido), pronto para ser integrado ao pipeline de treinamento do modelo.

---

## 🛠️ Tecnologias Usadas

- **Python**: Linguagem principal para manipulação de PDFs e pré-processamento.
- **Bibliotecas**:
  - `PyMuPDF` ou `pdfplumber`: Para extração de texto e imagens do PDF.
  - `NLTK` ou `spaCy`: Para pré-processamento de texto, como remoção de stopwords e tokenização, se desejado.

---

## 🚀 Como Usar

1. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
2. Execute a aplicação:
  ``` python app.py```
Acesse a aplicação: Abra seu navegador e vá para http://localhost:5000.

Faça o upload do PDF:

    No painel principal, selecione um arquivo PDF para fazer o upload.
    Clique em "Processar".

Obtenha o resultado:

    O conteúdo extraído e processado será exibido, e você poderá baixá-lo em um formato estruturado para usar no treinamento do LLM.
📂 Estrutura do Repositório
.
├── app.py                # Arquivo principal da aplicação
├── requirements.txt      # Dependências da aplicação
├── README.md             # Documentação
├── templates/            # Templates HTML para interface
├── static/               # Arquivos estáticos (CSS, JS)
└── uploads/              # Diretório para armazenar PDFs carregados

⚙️ Configurações

    Formato de Exportação: Por padrão, a aplicação exporta os dados em JSON. Este comportamento pode ser configurado em app.py.
    Pré-processamento: Personalize o nível de pré-processamento, como normalização e tokenização, editando o script principal.

📬 Contato

Em caso de dúvidas ou sugestões, entre em contato comigo:

🌐 Entre em Contato


<p align="center"> <a href="mailto:cassio.matematica@gmail.com"> <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"> </a> <a href="https://wa.me/5511965133956"> <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"> </a> <a href="https://www.linkedin.com/in/cassio-matematica"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"> </a> </p>
