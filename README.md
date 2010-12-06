#Gerenciador de Memória
##Autores
[Rafaelo Pinheiro](mailto:rafaelo.pinheiro1988@gmail.com)

[Eduardo Veiga](mailto:kluwe@softwarelivre.org)

[Harlan Maas Martins](mailto:hmaas00@hotmail.com)




##Descrição
Este trabalho tem como objetivo simular um autômato de pilha através de uma
Máquina de Turing. O algoritmo, implementado em Python, recebe como parâmetro o
nome de um arquivo que contém dados referentes à construção de um autômato de
pilha, como o estado inicial, o conjunto de estados finais, o alfabeto, o conjunto de
estados, o número de estados e as regras de transição. 

O algoritmo inicialmente
pergunta ao usuário qual palavra ele quer verificar se é ou não aceita pelo autômato
de pilha simulado na Máquina de Turing. Após isso, ele abre o arquivo, enviado por
parâmetro, e faz uma leitura do mesmo, jogando cada dado contido no arquivo para
uma variável definida. Assim, por exemplo, o valor do estado inicial vai para uma
variável relacionada, o conjunto de estados vai para outra variável, as regras vão para
outra variável, e assim por diante.

 Após essa etapa, começa a fase de mapeamento
através de uma função, denominada converte, que recebe como parâmetro a variável
que contém as regras do autômato de pilha. Essa função lê as regra do autômato, e
converte em regras da Máquina de Turing, através de condições de seleção. Essa
conversão é feita com base no estado atual, na posição da palavra lida e no conteúdo
da pilha. Para isso funcionar, teve-se que pesquisar todos os possíveis casos que
poderiam ocorrer em uma regra do autômato de pilha. 

Assim, percebeu-se que
existiam quatro casos possíveis: leitura da pilha sem escrever nada nela, escrita na
pilha sem ler nada nela, leitura e escrita na pilha e sem realizar escrita e leitura na
pilha. Para fazer a simulação de uma pilha, foi inserido um caractere ($) no final da
palavra, recebida pelo usuário, que serve para indicar o começo da pilha. Para cada
regra de um autômato de pilha que façam uma manipulação na pilha, tem-se um
conjunto de regras da Máquina de Turing que se move até o final da palavra, passando
pelo caractere que representa o começo da pilha ($), para assim realizar a
manipulação.

 A próxima etapa é a da execução das regras da Máquina de Turing.
Nessa fase, a execução foi realizada por meio de uma função que recebe como
parâmetros o estado atual, a posição do cabeçote de leitura e todo o conjunto de
regras da Máquina, para daí então fazer uma varredura nesse conjunto até encontrar
uma regra que tenha valores no estado atual e no cabeçote igual aos valores passados
por parâmetros. 

Quando essa regra é encontrada, o algoritmo faz a escrita do valor
indicado pela regra na posição atual da fita, faz a troca de estados e move o cabeçote
para a nova posição, repetindo esse processo até que se alcance um estado de
aceitação ou de rejeição, indicando ao usuário se a palavra que ele queria verificar foi
aceita ou não pela Máquina de Turing.