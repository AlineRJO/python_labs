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