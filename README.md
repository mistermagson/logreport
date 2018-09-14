# Log Report

### Visão Geral
Este projeto cria uma  ferramenta de relatórios que imprime relatórios (em texto sem formatação) com base nos dados no banco de dados de um site de noticias ficticio.

### Resultados
A ferramenta responde às seguintes questões:
1. Quais são os três artigos mais populares de todos os tempos? 
2. Quem são os autores de artigos mais populares de todos os tempos? 
3. Em quais dias mais de 1% das requisições resultaram em erros? 

###Pre-REquisitos
- Python3
- VirtualBox
- Vagrant

###Configuração do ambiente
Instale o Python3
Instale o VirtualBox
Instale o Vagrant
Configure a VM, A configuração poderá ser baixada em
 ```
	git clone https://github.com/udacity/fullstack-nanodegree-vm
 ```
Clone este repositorio
 ```
	git clone https://github.com/mistermagson/logreport.git
 ```
Baixe e descompacte os dados para popular o banco de dados [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) 
 
###Conectando à Maquina Virtual
1. Execute Vagrant VM de dentro do sub-diretorio onde foi baixado o repositorio fullstack-nanodegree-vm usando o comando:
  
  ```
    $ vagrant up
  ```
  2. Em seguida execute:
  
  ```
    $ vagrant ssh
  ```
  3. Altere o diretório para /vagrant .

###Configuração do Banco
Para carregar os dados, use o comando 
  ```
	psql -d news -f newsdata.sql
  ```
  
  
### Criar VIEWS necessárias

1. Criar view errodata:
  ```
    create view errodata as select cast(time as date) as data, cast(count(*) as float) as errodia 
	from log 
	where status like '%404%' group by data;
  ```
2. Criar view errototal usando:
  ```
    create view errototal as select cast(time as date) as data,  cast(count(*) as float) as errototal 
	from log group by data;
  ```
3. Create view percentualerro usando:
  ```
    create view percentualerro as select a.data,  round(cast((100.0*a.errodia/b.errototal)as numeric),2) as percentual
from errodata a, errototal b where a.data=b.data order by percentual desc;
  ```
  
#### Executando:
  1. Após a criação das VIEWS, executar utilizando:
  ```
    $ python projetolog.py
  ```
  