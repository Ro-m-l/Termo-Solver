# Termo-Solver
Um trecho de código em python feito como um exemplo de engenharia reversa para decodificar as respostas do jogo termo (https://term.ooo/), utilizando apenas informações obtidas no código frontend do website.

## Explicação do código
O objetivo do jogo é acertar a palavra dadas as dicas fornecidas. Funciona com uma lista de palavras, da qual um grupo de palavras é atualizado como resposta diariamente. 
Através da análise do código-fonte, identificou-se que o jogo opera inteiramente no frontend, sem requisições de validação ao backend. Nota-se, também, que a lógica do código do jogo depende inteiramente de cálculo temporal.
O modo termo (de uma palavra) depende, assim como todos outros, da diferença de tempo entre um dia configurado como base e o dia atual (no fuso horário de São Paulo), além de outro cálculo envolvendo o tamanho da lista e a quantidade de respostas.
Não obstante a similaridade, para a escolha de palavras nos modos de duas e quatro palavras (dueto e quarteto, respectivamente), são utilizadas duas strings previamente codificadas em base64 para cada uma das situações. Uma vez decodificadas, têm seus elementos iterados e utilizados como index para a lista de palavras.
Assim, as três opções obtém seus resultados, em um processo matemático inteiramente reproduzível sem acesso ao servidor.
O script desenvolvido leva em consideração e replica todos esses fatores para obter as respostas.

## Exemplo


## Considerações futuras
Apesar de sua eficiência, e de apresentar o funcionamento de modo simples e entendível, o método atual não comporta resiliência para mudanças futuras na lógica do código.
Utilizar Playwright como fallback seria uma opção para ter mais consistência e facilidade em encontrar a resposta, permitindo a extração dinâmica de dados diretamente da memória do navegador. Entretanto, além de menos eficiente, dada a possibilidade de mudanças de nomes de variáveis e ofuscações do código, o resultado ficaria sujeito a depender do conhecimento do usuário em relação ao sistema.
