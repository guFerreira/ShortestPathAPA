# ShortestPathAPA
Repositório do trabalho da disciplina de análise e projeto de algoritmos


## Dependências
Versão do [Python](https://www.python.org/downloads/) utilizada: 3.8

## Para Acesso ao repositório

```

$ git clone https://github.com/guFerreira/ShortestPathAPA.git
pip install requirements.txt

```

## Como Executar

### Para executar e gerar o gráfico em relação ao computador 1 do experimento, siga os seguintes passos:

- Entre no diretório onde o arquivo está pelo terminal.
- Digite o comando "python alg_experimento.py -l pc1 -n 1000 -e 50 --seed 10".

```
python3 alg_experimento.py -l pc1 -n 1000 -e 50 --seed 10

```

- O abrirá a imagem do gráfico e também irá gerar um txt chamado "out_alg_dijkstra.txt", que possui os dados das execuções do algoritmo.

<p align="center">
  <img src="https://github.com/guFerreira/ShortestPathAPA/blob/master/Gr%C3%A1ficosGerados/experimentopc1-n1000.png" height = 350 width=450 />
</p>

### Para executar e gerar o gráfico em relação ao computador 2 do experimento, siga os seguintes passos:

- Entre no diretório onde o arquivo está pelo terminal.
- Digite o comando "python alg_experimento.py -l pc2 -n 1000 -e 50 --seed 10".

```
python3 alg_experimento.py -l pc2 -n 1000 -e 50 --seed 10

```

- O abrirá a imagem do gráfico e também irá gerar um txt chamado "out_alg_dijkstra_pc_2.txt", que possui os dados das execuções do algoritmo.

<p align="center">
  <img src="https://github.com/guFerreira/ShortestPathAPA/blob/master/Gr%C3%A1ficosGerados/experimentopc2-n1000.png"  height = 350 width=450 />
</p>

### Para executar e gerar o gráfico em relação aos dados gerados nos dois computadores:

- Entre no diretório onde o arquivo está pelo terminal.
- Copie as saidas das execuções no computador 1 e 2.
- Digite o comando "python alg_experimento.py -n 1000 -e 50 --seed 10".

```
python alg_experimento.py -n 1000 -e 50 --seed 10

```

- Será gerado o gráfico com os dados gerados através do computador 1 e 2.
<p align="center">
  <img src="https://github.com/guFerreira/ShortestPathAPA/blob/master/Gr%C3%A1ficosGerados/experimento-n1000.png"  height = 350 width=450 />
</p>

## Referências
Utilizamos como base os algoritmos desenvolvidos nos videos:

-[Dijkstra's Algorithm in Python Explained](https://www.youtube.com/watch?v=Ub4-nG09PFw&ab_channel=AmitabhaDey)

-[Implementation of dijkstra in python](https://www.youtube.com/watch?v=IG1QioWSXRI&ab_channel=IanSullivan)
