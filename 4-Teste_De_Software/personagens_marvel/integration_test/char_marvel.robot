*** Settings ***

Resource  char_marvel.resource 
Suite Setup  Configurar nossa autorizacao para API  


*** Test Cases *** 
Testar API Characters da Marvel
    Configurar nossa autorizacao para API
    Realizar a requisicao para API
    Fazer a validacao dos campos necessarios

