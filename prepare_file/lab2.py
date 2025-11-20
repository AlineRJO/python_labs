# Uma classe de exceção base para nosso código:
class StudentsDataException(Exception):
    pass


# Uma exceção para linhas com erro:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# Uma exceção para um arquivo vazio.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# Um dicionário para dados de alunos:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Ler o arquivo inteiro na lista.
    lines = f.readlines()
    f.close()
    # O arquivo está vazio?
    if len(lines) == 0:
        raise FileEmpty()
    # Varre o arquivo linha por linha.
    for i in range(len(lines)):
        # Chegar até a linha i.
        line = lines[i]
        # Divide em colunas.
        columns = line.split()
        # Devem existir 3 colunas - elas estão lá?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Cria uma chave a partir do nome e sobrenome do aluno.
        student = columns[0] + ' ' + columns[1]
        # Obter pontos.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Atualiza o dicionário.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Imprime os resultados.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")
    