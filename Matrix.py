def validate_row(row):
    # TODO zrobić porządną walidację, sprawdzanie isnumeric
    return list(map(float, row))


def read_matrix_from_file(path):
    # TODO sprawdzanie, czy plik istnieje
    data = []
    with open(path, 'r') as file:
        for line in file:
            row = validate_row(line.split())
            data.append(row)
    number_of_columns = len(data[0])
    for row in data:
        if len(row) != number_of_columns:
            raise ValueError("TODO ładny komunikat")
    return data


def read_matrix_from_user():
    # TODO wczytywanie i walidacja wejścia od użytkownika
    pass


class Matrix:
    def __init__(self, data):
        self.number_of_rows = len(data)
        self.number_of_columns = len(data[0])
        self.data = data

    def data_to_string(self):
        s = ""
        for row in self.data:
            s += " ".join(map(str, row))
            s += "\n"
        return s

    def __str__(self):
        return f"Macierz o wymiarach {self.number_of_rows} na {self.number_of_columns} i elementach:\n" + self.data_to_string()

    def print_matrix(self):
        '''
        Wypisuje macierz.
        '''
        print(self.data_to_string())

    def print_element(self, i, j):
        '''
        Wypisuje element macierzy o indeksach i, j.
        i - indeks wiersza, j - indeks kolumny
        Uwaga. Indeksowanie od 1 tak jak na algebrze.
        '''
        print(self.data[i - 1][j - 1])
        print()

    def print_row(self, i):
        '''
        Wypisuje i-ty wiersz macierzy.
        '''
        for element in self.data[i - 1]:
            print(element, end=' ')
        print("\n")

    def print_column(self, j):
        '''
        Wypisuje j-tą kolumnę macierzy.
        '''
        for i in range(0, self.number_of_rows):
            print(self.data[i][j - 1])
        print()

    def copy(self):
        '''
        Zwraca nowy obiekt typu Matrix, zawierający prawdziwą kopię danych, a nie alias do nich
        '''
        data_copy = []
        for i in range(self.number_of_rows):
            data_copy.append([])
            for j in range(self.number_of_columns):
                data_copy[i].append(self.data[i][j])
        return Matrix(data_copy)

    def add_elementwise(self, other):
        '''
        Zwraca nowy obiekt typu Matrix, będący wynikiem dodania do siebie odpowiadających elementów dwóch macierzy (self i other).
        '''
        new_matrix = self.copy()
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                new_matrix.data[i][j] += other.data[i][j]
        return new_matrix

    def multiply_by_scalar(self, scalar):
        '''
        Zwraca nowy obiekt typu Matrix, będący wynikiem pomnożenia macierzy (czyli self) przez skalar.
        '''
        scalar = float(scalar)
        new_matrix = self.copy()
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                new_matrix.data[i][j] *= scalar
        return new_matrix

    def multiply_by_matrix(self, other):
        if self.number_of_columns != other.number_of_rows:
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")

        multiplied = [[0] * self.number_of_columns for _ in range(self.number_of_rows)]

        for i in range(self.number_of_rows):
            for j in range(other.number_of_columns):
                for k in range(self.number_of_columns):
                    result[i][j] += self[i][k] * other[k][j]
        
        return multiplied
        
        pass

    def determinant(self):
        if self.number_of_rows != self.number_of_columns:
            raise ValueError("Macierz musi być kwadratowa, aby wyznacznik istniał")

        if self.number_of_rows == 2 and self.number_of_columns == 2:
            det = self[0][0] * self[1][1] - self[0][1] * self[1][0]
            return det

        det = 0
        for j in range(self.number_of_columns):
            sign = (-1) ** j
            submatrix = []
            for i in range(1, self.number_of_rows):
                row = self[i][:j] + self[i][j + 1:]
                submatrix.append(row)
            sub_det = determinant(submatrix)
            det += sign * matrix[0][j] * sub_det

        return det
        
        pass

    def inverse(self):
        # TODO zaimplementować, jeśli wyznacznik jest różny od 0, oblicza i zwraca macierz odwrotną, w przeciwnym razie informuje użytkowanika, że macierz jest osobliwa i odwrotność nie istnieje
        pass


# Poniżej testowanie działania różnych metod.

if __name__ == "__main__":
    A = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])

    A.print_matrix()
    A.print_row(3)
    A.print_column(1)
    A.print_element(2, 2)

    B = Matrix(read_matrix_from_file("Macierz_3x3.txt"))
    print(B)

    print(A.multiply_by_scalar(6))

    print(A.add_elementwise(A))

    help(Matrix)
