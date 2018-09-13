# Log Report

### Overview
Projeto #3 apresentado no curso Nanodegree Fullstack Web Developer

### Criar VIEWS necessárias

1. Criar view errodata:
  ```
    create view errodata as select cast(time as date) as data, cast(count(*) as float) as errodia 
	from log 
	where status like '%404%' group by data;
  ```
2. Create view errototal using:
  ```
    create view errototal as select cast(time as date) as data,  cast(count(*) as float) as errototal 
	from log group by data;
  ```

  
#### Executando:
  1. Após a criação das VIEWS, executar utilizando:
  ```
    $ python projetolog.py
  ```
  

