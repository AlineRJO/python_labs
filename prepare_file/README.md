#Explicação do código

## read_file

* o mecanismo try-except e abra o arquivo de nome predeterminado (text.txt no nosso caso)
* tente ler o primeiro caractere do arquivo (<code>char = stream.read(1)</code>)
* caso seja bem-sucedido (comprovado pelo resultado positivo da verificação da condição while), o caractere será mostrado (observe o argumento <code>end=</code> pois é importante! Não queremos pular para uma nova linha após cada caractere!);
* atualize também o contador (<code>counter</code>);
* tente ler o próximo caractere e o processo se repetirá.

## readline_file

Para tratar o conteúdo do arquivo como um conjunto de linhas e não um monte de caracteres, o método readline() irá ajudar você com isso.

## write_file

A sequência a ser gravada consiste na palavra linha, seguida do número da linha. Decidimos escrever o conteúdo da string caractere por caractere (isso é feito pelo loop for interno), mas você não tem a obrigação de fazer dessa maneira.

## Lab 1 - Histograma de frequência de caracteres classificados

Sua tarefa é fazer algumas alterações, que geram os seguintes resultados:

o histograma de saída será classificado com base na frequência dos caracteres (o contador maior deve ser apresentado primeiro)
o histograma deverá ser enviado para um arquivo com o mesmo nome do arquivo de entrada, mas com o sufixo '.hist' (deverá ser concatenado ao nome original)
Supondo que o arquivo de entrada contenha apenas uma linha preenchida com: cBabAa
a saída esperada deve ser a seguinte:

a -> 3
b -> 2
c -> 1

Obs: use um lambda para alterar a ordem de classificação.

## Lab 2 - Avaliação dos resultados dos alunos

O Professor Jekyll dá aulas com os alunos e regularmente faz anotações em um arquivo de texto. Cada linha do arquivo contém três elementos: o primeiro nome do aluno, o sobrenome do aluno e o número de pontos que o aluno recebeu durante determinadas aulas.

Os elementos são separados por espaços em branco. Cada aluno pode aparecer mais de uma vez dentro do arquivo do Professor Jekyll.

O arquivo pode ter a seguinte aparência:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5

Sua tarefa é criar um programa que:

* pede ao usuário o nome do arquivo do Professor Jekyll;
* lê o conteúdo do arquivo e conta a soma dos pontos recebidos por cada aluno;
* imprime um relatório simples (mas classificado), como este:

Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0

Observação:


* seu programa deve estar totalmente protegido contra todas as falhas possíveis: a inexistência do arquivo, o arquivo vazio ou quaisquer falhas de dados de entrada; encontrar qualquer erro de dados deve causar o encerramento imediato do programa, e o erro deve ser apresentado ao usuário;
* implemente e use sua própria hierarquia de exceções – nós a apresentamos no editor; a segunda exceção deve ser gerada quando uma linha errada for detectada e a terceira quando o arquivo de origem existir, mas estiver vazio.

Dica: use um dicionário para armazenar os dados dos alunos.