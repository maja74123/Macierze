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

    def __repr__(self):
        return f"Macierz o wymiarach {self.number_of_rows} na {self.number_of_columns}"

    def print_matrix(self):
        """
        Wypisuje macierz.
        """
        print(self.data_to_string())

    def print_element(self, i, j):
        """
        Wypisuje element macierzy o indeksach i, j.
        i - indeks wiersza, j - indeks kolumny
        Uwaga. Indeksowanie od 1 tak jak na algebrze.
        """
        print(self.data[i - 1][j - 1])
        print()

    def print_row(self, i):
        """
        Wypisuje i-ty wiersz macierzy.
        """
        for element in self.data[i - 1]:
            print(element, end=' ')
        print("\n")

    def print_column(self, j):
        """
        Wypisuje j-tą kolumnę macierzy.
        """
        for i in range(0, self.number_of_rows):
            print(self.data[i][j - 1])
        print()

    def copy(self):
        """
        Zwraca nowy obiekt typu Matrix, zawierający prawdziwą kopię danych, a nie alias do nich
        """
        data_copy = [] # pusta macierz
        for i in range(self.number_of_rows):
            data_copy.append([])  # dodajemy pusty wiersz
            for j in range(self.number_of_columns):
                data_copy[i].append(self.data[i][j])  # dodajemy (kopię) każdego elementu do wiersza
        return Matrix(data_copy)

    def add_elementwise(self, other):
        """
        Zwraca nowy obiekt typu Matrix, będący wynikiem dodania do siebie odpowiadających elementów dwóch macierzy (self i other).
        """
        if self.number_of_rows != other.number_of_rows or self.number_of_columns != other.number_of_columns:
            raise ValueError("Dodawanie jest możliwe tylko gdy macierze mają jednakowe wymiary.")
        new_matrix = self.copy()
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                new_matrix.data[i][j] += other.data[i][j]
        return new_matrix

    def __add__(self, other):
        return self.add_elementwise(other)

    def multiply_by_scalar(self, scalar):
        """
        Zwraca nowy obiekt typu Matrix, będący wynikiem pomnożenia macierzy (czyli self) przez skalar.
        """
        scalar = float(scalar)
        new_matrix = self.copy()
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                new_matrix.data[i][j] *= scalar
        return new_matrix

    def multiply_by_matrix(self, other):
        """
        Zwraca nowy obiekt typu Matrix, będący wynikiem pomnożenia macierzy (czyli self) przez drugą macierz (czyli other).
        """
        if self.number_of_columns != other.number_of_rows:
            raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")

        result = [[0] * other.number_of_columns for _ in range(self.number_of_rows)]

        for i in range(self.number_of_rows):
            for j in range(other.number_of_columns):
                for k in range(self.number_of_columns):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def __mul__(self, other):
        # print(type(self), type(other))
        if isinstance(other, Matrix):
            return self.multiply_by_matrix(other)
        else:
            return self.multiply_by_scalar(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def determinant(self):
        """
        Oblicza i zwraca wyznacznik macierzy kwadratowej lub informuje, że wyznacznik nie istnieje.
        """
        if self.number_of_rows != self.number_of_columns:
            raise ValueError("Wyznacznik jest określony tylko dla macierzy kwadratowych.")

        if self.number_of_rows == 1:
            return self.data[0][0]

        if self.number_of_rows == 2:
            det = self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
            return det

        det = 0
        for j in range(self.number_of_columns):
            sign = (-1) ** j
            submatrix = []
            for i in range(1, self.number_of_rows):
                row = self.data[i][:j] + self.data[i][j + 1:]
                submatrix.append(row)
            sub_det = Matrix(submatrix).determinant()
            det += sign * self.data[0][j] * sub_det
        return det

    def inverse(self):
        """
        Zwraca nowy obiekt typu Matrix, będący odwrotnością macierzy (self) lub informuje użytkownika, że macierz jest osobliwa i odwrotność nie istnieje
        """
        if self.number_of_rows != self.number_of_columns:
            raise ValueError("Macierz odwrotna jest określona tylko dla macierzy kwadratowych, których wyznacznik jest różny od 0.")
        if self.determinant() == 0:
            raise ValueError("Nie można obliczyć odwrotności, ponieważ macierz jest osobliwa (wyznacznik macierzy jest równy 0)")

        inverted_matrix = self.copy()
        # TODO zaimplementować obliczanie odwrotności
        from warnings import warn
        warn("To nie jest macierz odwrotna, ta funkcjonalność nie jest jeszcze zaimplementowana")
        return inverted_matrix

    def transpose(self):
        """
        Zwraca nowy obiekt typu Matrix, będący transpozycją macierzy (self).
        """
        transposed = [[0] * self.number_of_rows for _ in range(self.number_of_columns)]
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                transposed[j][i] = self.data[i][j]
        return Matrix(transposed)

    def orthogonal(self, tolerance=0.000001):
        """
        Zwraca True, jeśli macierz jest ortogonalna lub False, jeśli nie jest ortogonalna.
        """
        transposed = self.transpose()
        AAT = (self * transposed).data
        ATA = (transposed * self).data
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):  
                if i == j:
                    if abs(AAT[i][j] - 1) > tolerance or abs(ATA[i][j] - 1) > tolerance:
                        return False
                else:
                    if abs(AAT[i][j]) > tolerance or abs(ATA[i][j]) > tolerance:
                        return False
        return True

    def trace(self):
        """
        Oblicza i zwraca ślad macierzy kwadratowej lub informuje, że ślad nie istnieje.
        """
        if self.number_of_rows != self.number_of_columns:
            raise ValueError("Ślad macierzy jest określony tylko dla macierzy kwadratowych.")
        tr = 0
        for i in range(self.number_of_rows):
            tr += self.data[i][i]
        return tr


    @staticmethod
    def validate_row(row, number_of_columns=None):
        row = list(map(lambda x: x.replace(",", "."), row))
        try:
            row = list(map(float, row))
        except ValueError:
            raise ValueError("Wszystkie elementy muszą być liczbami rzeczywistymi.")

        if number_of_columns is not None:
            if len(row) != number_of_columns:
                raise ValueError(f"Wiersz musi zawierać {number_of_columns} elementów.")
        return row

    @staticmethod
    def from_file(path):
        data = []
        with open(path, 'r') as file:
            for line in file:
                row = Matrix.validate_row(line.split())
                data.append(row)
        number_of_columns = len(data[0])
        for row in data:
            if len(row) != number_of_columns:
                raise ValueError("Każdy wiersz musi zawierać taką samą liczbę elementów.")
        return Matrix(data)

    @staticmethod
    def from_user():
        # wczytywanie wymiarów macierzy
        while True:
            try:
                number_of_rows, number_of_columns = list(map(int, input("Podaj wymiary macierzy w formacie liczba wierszy liczba kolumn (dodatnie liczby naturalne oddzielone spacją): ").split()))
                if number_of_rows <= 0 or number_of_columns <= 0:
                    print("Macierz musi mieć co najmniej 1 wiersz i 1 kolumnę.", end=" ")
                else:
                    break
            except ValueError:
                print("Niepoprawny format wymiarów macierzy.", end=" ")

        # wczytywanie elementów macierzy wiersz po wierszu
        print("Wpisuj kolejno wiersze macierzy składające się z liczb rzeczywistych oddzielonych spacją. Po wpisaniu całego wiersza naciśnij ENTER")
        data = []
        for _ in range(number_of_rows):
            while True:
                try:
                    row = Matrix.validate_row(input().split(), number_of_columns)
                    data.append(row)
                    break
                except ValueError as e:
                    print(e, "Wpisz ponownie ten wiersz macierzy")

        return Matrix(data)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join([str(element) for element in row]))
                file.write('\n')
        print(f"Zapisano macierz do pliku {filename}")


# Poniżej testowanie działania różnych metod.

if __name__ == "__main__":
    A = Matrix([
        [1.0, 2.1, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.7, 9.0]
    ])

    A.print_matrix()
    A.print_row(3)
    A.print_column(1)
    A.print_element(2, 2)
    print("Wyznacznik macierzy A:", A.determinant())

    print("Test wczytywania macierzy z pliku")
    B = Matrix.from_file("Macierz_3x4.txt")
    print(B)

    print("Test dodawania macierzy")
    print(A + A + A)

    print("Test mnożenia macierzy")
    print(A)
    print(A * 6)
    print(A * A)
    print(B)
    print(A * B)

    print("Test wczytywania macierzy z konsoli (od użytkownika)")
    print(Matrix.from_user())

    help(Matrix)
