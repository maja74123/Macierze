from Matrix import Matrix

"""
UWAGI:
- projekt wymaga Pythona w wersji co najmniej 3.8 (w tej wersji wprowadzono operator := ), można oczywiście przerobić kod i zrezygnować z :=
- polecenia są case insensitive, nazwy obiektów w pamięci są case sensitive (można to łatwo zmienić)
- ans przechowuje wynik ostatniego działania, nie jest zapisywana w słowniku memory, nie można jej użyć do dalszych działań (można to łatwo zmienić)
- jeśli ans będzie zapisywane w pamięci, to przy operacjach trzeba będzie dodać sprawdzanie, czy obiekt jest macierzą,
  żeby użytkownik nie próbował czasem obliczyć wyznacznika / odwrotności dla int'a/float'a, które nie mają takich metod, przez co program by się wysypał
"""

# TODO pomysły na dodatkową funkcjonalność:
# tworzenie macierzy zeros, ones, identity, wypełnionej konkretną wartością (analogicznie do np.zeros, np.ones, np.identity, np.full)
# transponowanie macierzy - łatwe
# sprawdzanie czy macierz jest ortogonalna - banalne, jeśli mamy zaimplementowane mnożenie macierzy i transponowanie macierzy
# znajdowanie min, max w całej macierzy / wybranym wierszy kolumnie - łatwe
# obliczanie śladu macierzy (sumy elementów na głównej przekątnej macierzy kwadratowe) - łatwe
# obliczanie normy Frobeniusa - łatwe

memory = {}

# TODO wywalić  poniższe memory przed wysłaniem projektu, to jest do testów, żeby za każdym uruchomieniem nie wpisywać poleceń wczytujących
memory = {
    "demo": Matrix.from_file("demo_matrix.txt"),
    "kw": Matrix.from_file("square_matrix.txt"),
    "liczba": 5,
}


def get_matrix():
    while (matrix_name := input("Podaj nazwę macierzy: ")) not in memory:
        print(f"Nie znaleziono macierzy '{matrix_name}' w pamięci programu")
    matrix = memory[matrix_name]
    if isinstance(matrix, Matrix):
        return matrix
    else:
        print(f"Obiekt o nazwie {matrix_name} nie jest macierzą, wybierz inny obiekt.")
        return get_matrix()


def get_matrix_or_float():
    while True:
        argument = input("Podaj nazwę macierzy lub liczbę rzeczywistą: ").strip()
        if argument == "":
            continue
        try:
            real_number = float(argument)
            return real_number
        except ValueError:
            if argument in memory:
                return memory[argument]
            else:
                print(f"Nie znaleziono macierzy {argument} w pamięci programu")


def get_name(question):
    while True:
        new_matrix_name = input(question).strip()
        if new_matrix_name == "":
            print("Nazwa nie może być pusta")
        elif not new_matrix_name[0].isalpha():
            print("Nazwa musi zaczynać się od litery")
        else:
            return new_matrix_name


def get_index(question):
    while True:
        try:
            index = int(input(question))
            return index
        except ValueError:
            continue


user_manual = """
Tutaj będzie poradnik dla nowego użytkownika, m.in. lista komend i co one robią, info że CTRL-D pozwala wrócić do menu głównego
"""

ans = "Nie wykonano jeszcze żadnych obliczeń więc wynik `ans` jest pusty"
print("Witaj w naszym programie. Jeśli nie wiesz co robić wpisz help")
while True:
    try:
        command = input(">> ").lower().strip()

        # użytkownik nie nie wpisał (albo tylko białe znaki) i nacisnął ENTER
        if command == "":
            print("Z pustego [polecenia] i Salomon nie naleje")
            continue

        # zamykanie programu
        elif command in ["stop", "end", "exit", "quit", "koniec", "zamknij", "zakończ"]:
            break

        # TODO do wywalenia, potrzebne tylko do testowania
        elif command == "error":
            raise ValueError("to jest testowy błąd wywoływany poleceniem error")

        elif command == "help":
            print(user_manual)

        # wyświetla wynik ostatniej operacji arytmetycznej/macierzowej
        elif command == "ans":
            print(ans)
        # wyświetla informację o wszystkich obiektach zapisanych w pamięci programu
        elif command in ["ls", "dir"]:
            for key, value in memory.items():
                print(f"{key.ljust(5)}: {repr(value)}")

        # wczytywanie macierzy od użytkownika (z konsoli)
        elif command in ["rcmd", "readcmd", "read cmd", "read from cmd", "read from command line", "enter matrix", "wczytaj z konsoli", "wpisz macierz"]:
            data = Matrix.from_user()
            object_name = get_name("Wpisz nazwę, pod którą chcesz przechowywać tą macierz w pamięci programu: ")
            memory[object_name] = Matrix(data)

        # DODATKOWA FUNKCJONALNOŚĆ wczytywanie macierzy z pliku
        elif command in ["rfile", "readfile", "read file", "read from file", "wczytaj plik", "wczytaj z pliku"]:
            data = None
            while not data:
                path = input("Podaj nazwę pliku: ")
                try:
                    data = Matrix.from_file(path)
                except FileNotFoundError:
                    print(f"Plik {path} nie istnieje")
                except ValueError as e:
                    print(e, "Popraw plik i spróbuj ponownie.")
            object_name = get_name("Wpisz nazwę, pod którą chcesz przechowywać tą macierz w pamięci programu: ")
            memory[object_name] = Matrix(data)

        # DODATKOWA FUNKCJONALNOŚĆ zapis macierzy do pliku
        elif command in ["save", "save matrix", "save matrix to file", "zapisz", "zapisz macierz", "zapisz do pliku"]:
            matrix_to_save = get_matrix()
            path = get_name("Podaj nazwę (lub kompletną ścieżkę) pliku, do którego chcesz zapisać tą macierz: ")
            # sztuczka pozwalająca na sprawdzenie, czy plik istnieje bez używania zewnętrznych bibliotek
            try:
                with open(path, 'r') as file_that_should_not_exist:
                    # udało nam się otworzyć plik, więc plik o takiej nazwie istnieje,
                    # nie chcemy nadpisywać istniejących plików,
                    # użytkownik mógłby sobie zrobić krzywdę (nadpisać ważny dokument albo plik systemowy)
                    print(f"Plik o nazwie {path} istnieje, podaj inną nazwę")
            except FileNotFoundError:
                # plik o takiej nazwie jeszcze nie istnieje, możemy bezpiecznie zapisysać
                matrix_to_save.save_to_file(path)  # TODO zaimplementować metodę zapisującą do pliku

        # wyświetlanie całej macierzy
        elif command in ["display", "show", "print", "wyświetl", "pokaż", "wypisz"]:
            matrix = get_matrix()
            print(matrix)

        # wyświetlanie wybranego wiersza macierzy
        elif command in ["sr", "display row", "show row", "print row", "wyświetl wiersz", "pokaż wiersz", "wypisz wiersz"]:
            matrix = get_matrix()
            row_index = get_index("Podaj numer wiersza (liczbę całkowitą): ")
            try:
                matrix.print_row(row_index)
            except IndexError:
                print(f"Macierz posiada tylko {matrix.number_of_rows} wierszy")

        # wyświetlanie wybranej kolumny macierzy
        elif command in ["sc", "display column", "show column", "print column", "wyświetl kolumnę", "pokaż kolumnę", "wypisz kolumnę"]:
            matrix = get_matrix()
            column_index = get_index("Podaj numer kolumny (liczbę całkowitą): ")
            try:
                matrix.print_column(column_index)
            except IndexError:
                print(f"Macierz posiada tylko {matrix.number_of_columns} kolumn")

        # wyświetlanie jednego wybranego elementu macierzy
        elif command in ["se", "display element", "show element", "print element", "wyświetl element", "pokaż element", "wypisz element"]:
            matrix = get_matrix()
            row_index = get_index("Podaj numer wiersza (liczbę całkowitą): ")
            column_index = get_index("Podaj numer kolumny (liczbę całkowitą): ")
            try:
                matrix.print_element(row_index, column_index)
            except IndexError:
                print(f"Macierz posiada tylko {matrix.number_of_rows} wierszy {matrix.number_of_columns} kolumn")

        # obliczanie wyznacznika macierzy
        elif command in ["det", "determinant", "wyznacznik"]:
            matrix = get_matrix()
            try:
                ans = matrix.determinant()
                print(f"Wyznacznik macierzy jest równy {ans}")
            except ValueError as e:
                print(e)

        # obliczanie odwrotności macierzy
        elif command in ["inv", "inverse", "odwrotność"]:
            matrix = get_matrix()
            try:
                print(f"Macierz odwrotna to:")
                ans = matrix.inverse()
                print(ans)
            except ValueError as e:
                print(e)

        # dodawanie dwóch macierzy
        # TODO można ewentualnie dodać DODATKOWĄ FUNKCJONALNOŚĆ: dodawanie skalara do każdego elementu macierzy
        elif command in ["+", "add", "add matrices", "dodaj", "dodaj macierze", "dodawanie", "dodawanie macierzy"]:
            first_matrix = get_matrix()
            second_matrix = get_matrix()
            try:
                ans = first_matrix + second_matrix
                print("Wynik dodawania to:", ans)
            except ValueError as e:
                print(e)

        # mnożenie: macierzy przez macierz, macierzy przez skalar, dwóch skalarów
        # TODO można oczywiście rzucać błąd gdy użytkownik poda dwa skalary, ale po co ...
        elif command in ["*", "mul", "multiply", "multiplication", "pomnóż", "mnożenie"]:
            first_argument = get_matrix_or_float()
            second_argument = get_matrix_or_float()
            try:
                ans = first_argument * second_argument
                print("Wynik mnożenia to:", ans)
            except ValueError as e:
                print(e)

        # jeśli żadna dotychczasowa komenda nie pasowała, to sprawdzamy, czy użytkownik nie wpisał przypadkiem nazwy obiektu, jeśli tak to go wyświetlamy
        elif command in memory:
            print(f"Nie rozpoznano komendy, ale znaleziono w pamięci programu obiekt o nazwie {command}")
            print(command, "to:", memory[command])

        # tekst wpisany przez użytkownika nie jest poprawną komendą ani nazwą obiektu w pamięci
        else:
            print(f"Nie rozpoznano komendy `{command}`")

    except EOFError:  # użytkownik wcisnął CTRL-D
        print("Wracam do menu głównego")
        continue
    except KeyboardInterrupt:  # użytkownik wcisnął CTRL-C
        print()
        break
    # TODO przez wysłaniem projekty odkomentować poniższy ogólny except, łapiący wszystkie wyjątki, a więc także te niewychwycone w czasie testowania
    except BaseException as e:
        print("Wystąpił nieoczekiwany błąd, skontaktuj się z autorami programu. Przekaż im poniższą treść błędu:\n", e)

print("Dziękujemy za skorzystanie z naszego programu :)")
