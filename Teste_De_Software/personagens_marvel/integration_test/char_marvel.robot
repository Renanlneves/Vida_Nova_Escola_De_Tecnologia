*** Settings ***
Library  RequestsLibrary
Variables  config.py

*** Variables ***


*** Test Cases *** 
Testar API Characters da Marvel
    Configurar nossa autorizacao para API
    Realizar a requisicao para API
    Fazer a validacao dos campos necessarios


*** Keywords ***
Configurar nossa autorizacao para API
    ${URL}  Set Variable   

Realizar a requisicao para API
    Create Session  requisicao_char  ${BASE_URL}  headers=${HEADERS}
    ${response_char}=  Get On Session  requisicao_char  url=${URL_CHAR}?apikey=${API_KEY}
    Log To Console  ${response_char}
    Set Test Variable  ${response_char}


Fazer a validacao dos campos necessarios
    Request Should Be Successful  ${response_char}
    Should Not Be Empty  ${response_char.json()}[data]