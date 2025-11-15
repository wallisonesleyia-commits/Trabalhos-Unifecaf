# **Sistema de Controle de Qualidade Industrial (QC) em Python**

Protótipo de um sistema interativo de terminal (CLI) para automação do controle de qualidade e gerenciamento de produção em uma linha de montagem industrial.

**Status:** Protótipo Funcional

## **⚙️ Como Funciona**

Este sistema atua como um "Assistente de Produção" digital, permitindo que um operador de linha gerencie o fluxo de peças fabricadas através de um menu interativo.

O sistema armazena o estado da produção (peças cadastradas, caixas fechadas) em memória enquanto está em execução.

### **Lógica de Negócio**

O núcleo do sistema é a função de **Avaliação (QC)**. Cada peça cadastrada é instantaneamente validada contra os seguintes critérios:

* **Peso:** Deve estar entre 95g e 105g (inclusive).  
* **Cor:** Deve ser "azul" ou "verde" (não sensível a maiúsculas/minúsculas).  
* **Comprimento:** Deve estar entre 10cm e 20cm (inclusive).

Se uma peça falhar em *qualquer* um dos critérios, ela é marcada como **REPROVADA** e o motivo da falha é registrado.

### **Funcionalidades do Menu**

1. **Cadastrar nova peça:** Solicita ao usuário os dados (ID, peso, cor, comprimento) e realiza a avaliação.  
   * Se **Aprovada**, a peça é adicionada à caixa\_atual.  
   * Se a caixa\_atual atingir a capacidade (10 peças), ela é "fechada" e uma nova é iniciada.  
   * Se **Reprovada**, é armazenada para fins de relatório.  
2. **Listar peças:** Exibe *todas* as peças já cadastradas, separadas em "Aprovadas" e "Reprovadas", mostrando os detalhes e motivos de falha.  
3. **Remover peça:** Permite ao operador remover uma peça do sistema usando seu ID (para corrigir erros de digitação, por exemplo).  
4. **Listar caixas fechadas:** Mostra um histórico de todas as caixas que atingiram a capacidade máxima (10/10) e seu conteúdo.  
5. **Gerar relatório final:** Exibe um sumário completo da produção atual, incluindo totais, detalhamento de falhas e contagem de caixas.

## **🚀 Como Rodar**

### **Pré-requisitos**

* Você precisa ter o **Python 3.x** instalado em sua máquina.

### **Passo a Passo**

1. **Clone ou baixe o repositório:**  
   git clone \[https://github.com/seu-usuario/seu-repositorio.git\](https://github.com/seu-usuario/seu-repositorio.git)](https://github.com/wallisonesleyia-commits/Trabalhos-Unifecaf/tree/c7d0235436d22cc7f9ae6c439bfd290b1ee6833c/L%C3%B3gica%20e%20Programa%C3%A7%C3%A3o)

   *(Ou baixe o ZIP e extraia os arquivos)*  
2. **Navegue até a pasta do projeto:**  
   cd seu-repositorio

3. **Execute o script Python:**  
   * (Assumindo que o arquivo se chama main.py ou similar)

python main.py

4. **Use o menu interativo** que aparecerá no seu terminal. Para encerrar o programa, escolha a opção "Sair".

## **📊 Exemplos de Uso**

### **1\. Menu Principal**

```
Ao executar o script, você verá o menu de controle:

\=============================================  
      ⚙️ SISTEMA DE CONTROLE DE QUALIDADE ⚙️  
\=============================================  
 (Peças na caixa atual: 0/10)

1\. Cadastrar nova peça  
2\. Listar peças (Aprovadas/Reprovadas)  
3\. Remover peça cadastrada  
4\. Listar caixas fechadas  
5\. Gerar relatório final  
6\. Sair  
\---------------------------------------------  
Escolha uma opção (1-6): 

```

### **2\. Cadastrando uma Peça APROVADA**

```
Escolha uma opção (1-6): 1

\--- 1\. Cadastrar Nova Peça \---  
   ID da Peça (ex: 'p001'): p001  
   Peso (g): 102  
   Cor: azul  
   Comprimento (cm): 15

   ➡️ RESULTADO: Peça p001 APROVADA.

\=============================================  
      ⚙️ SISTEMA DE CONTROLE DE QUALIDADE ⚙️  
\=============================================  
 (Peças na caixa atual: 1/10)  
...
```

### **3\. Cadastrando uma Peça REPROVADA**

```
Escolha uma opção (1-6): 1

\--- 1\. Cadastrar Nova Peça \---  
   ID da Peça (ex: 'p001'): p002  
   Peso (g): 110  
   Cor: vermelho  
   Comprimento (cm): 12

   ➡️ RESULTADO: Peça p002 REPROVADA. (Motivos: Peso, Cor)

\=============================================  
      ⚙️ SISTEMA DE CONTROLE DE QUALIDADE ⚙️  
\=============================================  
 (Peças na caixa atual: 1/10)  
...
```

### **4\. Listando Peças (Opção 2\)**

```
Escolha uma opção (1-6): 2

\--- 2\. Listagem de Peças \---

\--- Peças Aprovadas \---  
  \[ID: p001\] | ✅ APROVADA  
     (Peso: 102.0g, Cor: azul, Comp: 15.0cm)

\--- Peças Reprovadas \---  
  \[ID: p002\] | ❌ REPROVADA (Motivos: Peso, Cor)  
     (Peso: 110.0g, Cor: vermelho, Comp: 12.0cm)

Pressione ENTER para voltar ao menu...
```

### **5\. Gerando o Relatório Final (Opção 5\)**

```
Escolha uma opção (1-6): 5

\========================================  
     📊 RELATÓRIO DE PRODUÇÃO ATUAL 📊  
\========================================

✅ Total de Peças APROVADAS: 1  
❌ Total de Peças REPROVADAS: 1

\--- Detalhes da Reprovação \---  
   Falhas por Peso:         1  
   Falhas por Cor:          1  
   Falhas por Comprimento:  0

\--- Logística \---  
📦 Total de Caixas Utilizadas: 1  
   (Sendo 0 caixas cheias e 1 caixa atual com 1 peças)

\========================================  
Pressione ENTER para voltar ao menu...  
