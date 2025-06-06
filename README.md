# Ford-Fulkerson

A teoria dos grafos nos permite calcular algumas previsibilidades comuns no dia a dia, presente em redes sociais, navegação pelo GPS entre outras aplicações que são utilizadas comumente. Pensando em como verificar o fluxo máximo em um grafo, Lester Randolph Ford Jr. e Delbert Ray Fulkerson desenvolveram um algoritmo Max Flow que recebeu o nome de Ford-Fulkerson.

Algoritmos de max flow (fluxo máximo) tem sido utilizado cada vez mais no dia a dia, possibilitando calcular o máximo possível do uso de produtos, armazenamento em estoque, o consumo ideal máximo de matéria prima em produções de produtos das fábricas, bem como outras finalidades. Para que tudo isso fosse possível nos dias atuais Ford e Fulkerson uniram os pensamentos para desenvolver um algoritmo que à partir de um Grafo, uma fonte, um terminal e a capacidade das arestas fosse possível calcular os caminhos possíveis, não obrigando a escolha de um caminho mais curto ou com maiores capacidades, permitindo assim escolha de qualquer um dos caminhos.


O algoritmo de fluxo máximo é uma técnica fundamental na teoria dos grafos que identifica a maior quantidade possível de "material" que pode fluir de uma fonte a um sumidouro em uma rede capacitada. Desenvolvido por Ford e Fulkerson em 1956, o algoritmo funciona através da identificação iterativa de pseudo caminhos aumentadores, onde se busca caminhos não saturados entre a fonte e o sumidouro para incrementar o fluxo. A cada iteração, aument  a-se o fluxo pela capacidade residual do caminho encontrado (o mínimo entre as capacidades disponíveis dos arcos) até que não existam mais caminhos aumentadores. Neste ponto, os arcos saturados formam um corte mínimo que representa o gargalo da rede, e o valor do fluxo máximo é igual à soma das capacidades destes arcos, permitindo otimizar desde redes de distribuição até sistemas de telecomunicações.


O algoritmo precisa do grafo, uma fonte, o final e carga ou capacidade, com essas informações é possível realizar o cálculo algorítmico, que inicia sentando o fluxo global como zero, para cada aresta “E” fluxo é igual a zero, depois começa as verificações, onde o processo se repete enquanto as partes do grafo houverem caminhos a serem percorridos, depois de cada verificação, atualizamos o grafo residual, após a atualização verificamos novamente os caminhos.
Exemplo:
	Fluxo Máximo(G, s, t, c){
		fluxo global = 0
		Para cada e ∈ E
			f(e) = 0
		Enquanto Ǝ Pst no Gf {
			Qualquer Pst # Qualquer caminho Pst
			f’ = Aumentar(f, Pst)
			Atualizar o Grafo residual Gf
		}
	}
Para começar as interações com o Grafo, escolhemos a aresta que possui maior peso ou capacidade, observamos a direção a partir do vértice (nó), usamos o mesmo critério a aresta que possui o maior peso, isso até chegar no final “t”, (ver grafo na figura 1).
Respeitando as interações conforme descrito anteriormente, faremos o primeiro fluxo [s, a, c, b, d e t] e o valor máximo que conseguimos nesta interação é 3, pois a aresta com menor valor está localizada na intersecção c para b. Para atualizarmos o grafo residual, precisamos subtrair 3, o valor encontrado, de cada vértice gerando assim um novo grafo (ver grafo residual 1 figura 2).
A partir do grafo residual repetimos o processo até que não seja possível passar por nenhum caminho, ou seja, até que os possíveis caminhos estejam com peso zero.


 Para a proposta deste trabalho precisa-se desenvolver o grafo sem o uso de bibliotecas que permita a programação realizar o cálculo diretamente, sendo assim, gerando a necessidade de implementação deste cálculo diretamente.
Para comparativo e validação dos acertos, necessitamos de um parâmetro ou um projeto base, pois a partir dele será possível atestar a genuinidade do método e dos cálculos realizados internamente.  


Foi escolhida a linguagem em Python para o desenvolvimento deste trabalho, com ela é possível gerar uma classe do grafo que vai realizar o cálculo de busca do maior fluxo para o valor inserido no código.
O primeiro passo foi definir a classe e estruturar a mesma, pois a partir disto será possível a identificação das arestas e capacidades. Dentro desta estrutura está a função que usa o algoritmo de Ford-Fulkerson para encontrar o fluxo máximo e obter a resposta esperada.
Depois escrevemos o grafo através de uma matriz, que possui o tamanho de acordo com a quantidade de vértices, por exemplo, o grafo encontrado na figura 1, possui 6 nós (arestas), sendo assim a matriz correspondente é 6 x 6 (ver tabela 1 - Matriz grafo)


Para a validação deste projeto utilizamos como base o canal do Youtube de Lucas Mattos, que fez uso do blog Geeks, neste blog tem um exercício que é resolvido através do algoritmo de Ford-Fulkerson, buscando o fluxo máximo do grafo plotado na página.
Conforme o autor o grafo (ver na Figura 6), precisa apresentar o resultado de 23 para o fluxo máximo encontrado, e, quando aplicamos o conhecimento adquirido no item 2.1. Algoritmo podemos chegar ao resultado do fluxo igual a 23. 
Embora o código desenvolvido não gere partes gráficas, ao inserir as informações de capacidade em forma de matriz, o código precisa resultar no valor de 23 como fluxo máximo encontrado (ver retorno do código na Figura 7).


Após a realização dos testes no código em Python do algoritmo de Ford-Fulkerson, obtivemos um resultado satisfatório e que entrega o valor de fluxo máximo calculado pelo algoritmo.
O desafio deste desenvolvimento está em codificar este algoritmo de grafo sem o uso de bibliotecas auxiliares já existentes, uma vez que o uso delas não permitiria o conhecimento passo a passo do que estaria sendo executado nas linhas de código.
Como uma segunda verificação de validação do código, inserimos a matriz equivalente do exemplo utilizado no item 2.1. Algoritmo, que gerou o resultado 9 para o fluxo máximo, que foi calculado previamente (ver resultado na Figura 8).
