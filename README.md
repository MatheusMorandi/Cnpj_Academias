# Projeto CNPJ Academias

## Descrição do Projeto

Este projeto tem como objetivo analisar e filtrar dados públicos do Cadastro Nacional da Pessoa Jurídica (CNPJ) para identificar academias ativas no Brasil. A partir dos dados disponibilizados pelo governo federal, o projeto busca extrair informações relevantes sobre empresas que operam no segmento de atividades físicas, utilizando códigos CNAE específicos para filtragem.

Os dados processados podem ser utilizados para análises de mercado, estudos de densidade de academias por região ou até mesmo para identificar tendências no setor de saúde e bem-estar.

---

## Estrutura do Projeto

A estrutura do projeto foi organizada para facilitar a manutenção e colaboração. Abaixo está uma visão geral das pastas e arquivos:
```
Cnpj_Academias/
│
├── data/ # Dados brutos e processados
│ ├── raw/ # Dados brutos originais
│ │ ├── cnpj-metadados.pdf # Metadados do CNPJ
│ │ ├── cnae.csv # Arquivo com códigos CNAE
│ │
│ ├── processed/ # Dados após processamento
│ └── academias_filtradas.csv # Resultado final
│
├── src/ # Código-fonte do projeto
│ ├── scripts/ # Scripts específicos
│ │ ├── filtro.py # Script para filtrar dados
│ │
│ └── main.py # Ponto de entrada principal
│
├── README.md # Este arquivo
│
└── .gitignore # Arquivo para ignorar arquivos desnecessários
```

---

## Fontes de Dados

Os dados utilizados neste projeto foram obtidos do portal [Dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj), que disponibiliza o Cadastro Nacional da Pessoa Jurídica (CNPJ) em formato aberto. Os arquivos contêm informações detalhadas sobre empresas brasileiras, incluindo:

- **Metadados**: Informações sobre a estrutura dos dados (`cnpj-metadados.pdf`).
- **CNAE**: Classificação Nacional de Atividades Econômicas (`cnae.csv`).

Para mais detalhes sobre os dados, consulte a documentação oficial no site do governo:
- [Portal Dados.gov.br - CNPJ](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)

---

## 📢 Conecte-se Comigo!

🔗 **GitHub**: [Matheus Morandi](https://github.com/MatheusMorandi)  
🔗 **LinkedIn**: [Matheus Morandi](https://www.linkedin.com/in/matheusmorandi/)  

Se você gostou deste projeto, deixe uma ⭐ no repositório! 😃