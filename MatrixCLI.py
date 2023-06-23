from Matrix import Matrix

"""
UWAGI:
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
}


def get_matrix():
    while True:
        matrix_name = input("Podaj nazwę macierzy: ").strip()
        if matrix_name == "":
            continue
        elif matrix_name in memory:
            break
        else:
            print(f"Nie znaleziono macierzy '{matrix_name}' w pamięci programu.")
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

def get_yes_no_answear():
    while True:
        answear = input("Wpisz 'tak' lub 'nie': ").strip().lower()
        if answear == "tak":
            return True
        elif answear == "nie":
            return False

def get_object_name(question):
    while True:
        new_matrix_name = input(question).strip()
        if new_matrix_name == "":
            print("Nazwa nie może być pusta")
        elif not new_matrix_name[0].isalpha():
            print("Nazwa musi zaczynać się od litery")
        elif new_matrix_name in memory:
            print("Macierz o takiej nazwie już istnieje. Czy chcesz ją nadpisać?", end=" ")
            if get_yes_no_answear():
                return new_matrix_name
        else:
            return new_matrix_name

def get_filename():
    while True:
        filename = input("Podaj nazwę (lub kompletną ścieżkę) pliku, do którego chcesz zapisać tę macierz: ").strip()
        if filename == "":
            print("Nazwa pliku nie może być pusta")
        else:
            # sztuczka pozwalająca na sprawdzenie, czy plik istnieje bez używania zewnętrznych bibliotek
            try:
                with open(filename, 'r') as file_that_should_not_exist:
                    # udało nam się otworzyć plik, więc plik o takiej nazwie istnieje,
                    # nie chcemy nadpisywać istniejących plików,
                    # użytkownik mógłby sobie zrobić krzywdę (nadpisać ważny dokument albo plik systemowy)
                    print(f"Plik o nazwie {filename} istnieje, podaj inną nazwę")
            except FileNotFoundError:
                # plik o takiej nazwie jeszcze nie istnieje, możemy bezpiecznie zapisywać pod taką nazwą
                return filename


def get_index(question):
    while True:
        try:
            index = int(input(question))
            return index
        except ValueError:
            continue


user_manual = """
Instrukcja

Tutaj możesz zapoznać się z poleceniami, których możesz użyć, aby wykonywać proste operacje na macierzach. Na końcu tej instrukcji znajdziesz podsumowanie, które będzie zawierało nazwę operacji i możliwe polecenia, które wywołają działanie danej metody. Mogą być one pomocne, kiedy już zapoznasz się z działaniem poszczególnych metod i będziesz potrzebować tylko skrótowej nazwy oraz poleceń. Masz do wyboru kilka poleceń, w tym słowa polskie i angielskie, więc możesz łatwiej zapamiętać swoje ulubione i później go używać :)
Jeśli program będzie wymagał od Ciebie wprowadzenia jakichś danych, np. aby utworzyć nową macierz, informacja o tym pojawi się na ekranie. Kiedy coś wpiszesz, zatwierdź to, używając ENTER.

> Wczytywanie z konsoli
    Jeśli chcesz podać nową macierz, wpisz jedno z następujących poleceń ["readcmd", "read cmd", "read from cmd", "read from command line", "enter matrix", "wczytaj z konsoli", "wpisz macierz", "wpisz"]. Następnie postępuj zgodnie z instrukcjami pojawiającymi się na ekranie (podaj wymiary macierzy, a następnie jej elementy oraz nazwę, pod którą chcesz zapisać tę macierz w pamięci).
> Wczytywanie z pliku
    Możesz wczytywać macierz nie tylko z konsoli, ale również z pliku. Osobny plik z macierzą zawiera kolejne wiersze w kolejnych liniach, a elementy w wierszu są oddzielone spacjami. Na końcu znajduje się pusta linia. Aby użyć opcji wczytywania z pliku, wpisz jedno z następujących poleceń ["readfile", "read file", "read from file", "wczytaj plik", "wczytaj z pliku", "z pliku"]. Podaj nazwę pliku (np. nazwa_pliku.txt), a następnie nazwę, pod jaką chcesz przechowywać wczytywaną macierz.
> Zapisywanie do pliku
    Jeśli chcesz zapisać macierz do pliku, wpisz jedno z następujących poleceń ["save", "save matrix", "save matrix to file", "zapisz", "zapisz macierz", "zapisz do pliku"].
> Obiekty w pamięci
    Jeśli chcesz zobaczyć, jakie obiekty zostały dotychczas zapisane w pamięci, wpisz jedno z następujących poleceń ["list", "ls", "dir", "pokaż pamięć", "pamięć"]. Po wpisaniu polecenia zobaczysz informację zawierającą nazwę macierzy oraz jej wymiary.
> Wyświetlanie macierzy
    Jeśli chcesz wyświetlić wcześniej wprowadzoną macierz, wpisz jedno z następujących poleceń ["display", "show", "print", "wyświetl", "pokaż", "wypisz"].
> Wyświetlanie wiersza
    Jeśli chcesz wyświetlić jeden z wierszy wprowadzonej wcześniej macierzy, wpisz jedno z następujących poleceń ["display row", "show row", "print row", "row", "wyświetl wiersz", "pokaż wiersz", "wypisz wiersz", "wiersz"].
> Wyświetlanie kolumny
    Jeśli chcesz wyświetlić jedną z kolumn wprowadzonej wcześniej macierzy, wpisz jedno z następujących poleceń ["display column", "show column", "print column", "column", "wyświetl kolumnę", "pokaż kolumnę", "wypisz kolumnę", "kolumna"].
> Wyświetlanie elementu
    Jeśli chcesz wyświetlić jeden z elementów wprowadzonej wcześniej macierzy, wpisz jedno z następujących poleceń ["display element", "show element", "print element", "wyświetl element", "pokaż element", "wypisz element", "element"].
> Dodawanie
    Jeśli chcesz dodać do siebie dwie macierze o tych samych wymiarach, wpisz jedno z następujących poleceń ["add", "add matrices", "dodaj", "dodaj macierze", "dodawanie", "dodawanie macierzy"].
> Mnożenie
    Jeśli chcesz pomnożyć macierz przez inną macierz lub przez skalar, wpisz jedno z następujących poleceń ["mul", "multiply", "multiplication", "pomnóż", "mnożenie"]. Pamiętaj, że aby pomnożyć przez siebie dwie macierze, muszą mieć one odpowiednie wymiary (pierwsza macierz musi mieć tyle kolumn, co druga wierszy).
>  Wyznacznik
    Jeżeli chcesz obliczyć wyznacznik macierzy, wpisz jedno z następujących poleceń ["det", "determinant", "wyznacznik"].
> Odwrotność
    Jeśli chcesz obliczyć odwrotność  macierzy, wpisz jedno z następujących poleceń ["inv", "inverse", "odwrotność"].
> Transpozycja
    Jeśli chcesz transponować macierz, wpisz jedno z następujących poleceń ["tranpose", "transpozycja", "macierz transponowana", "transponuj"].
> Wynik ostatniej operacji
    Jeśli chcesz wyświetlić wynik ostatniej przeprowadzonej operacji, wpisz jedno z następujących poleceń ["ans", "ostatni wynik"].
> Zapisywanie wyniku ostatniej operacji
    Jeśli chcesz zapisać wynik ostatniej operacji w pamięci, aby później móc go użyć do dalszych obliczeń, możesz to zrobić, wpisując jedno z następujących poleceń ["save ans", "zapisz ostatni wynik"].
> Wyjście
    Jeśli chcesz zakończyć korzystanie z programu, wpisz jedno z następujących poleceń ["stop", "end", "exit", "quit", "koniec", "zamknij", "zakończ"].
_____________________________
Instrukcja – wersja skrócona

> Wczytywanie z konsoli – ["readcmd", "read cmd", "read from cmd", "read from command line", "enter matrix", "wczytaj z konsoli", "wpisz macierz", "wpisz"].
> Wczytywanie z pliku – ["readfile", "read file", "read from file", "wczytaj plik", "wczytaj z pliku", "z pliku"].
> Zapisywanie do pliku – ["save", "save matrix", "save matrix to file", "zapisz", "zapisz macierz", "zapisz do pliku"].
> Obiekty w pamięci – ["list", "ls", "dir", "pokaż pamięć", "pamięć"].
> Wyświetlanie macierzy – ["display", "show", "print", "wyświetl", "pokaż", "wypisz"].
> Wyświetlanie wiersza – ["display row", "show row", "print row", "row", "wyświetl wiersz", "pokaż wiersz", "wypisz wiersz", "wiersz"].
> Wyświetlanie kolumny – ["display column", "show column", "print column", "column", "wyświetl kolumnę", "pokaż kolumnę", "wypisz kolumnę", "kolumna"].
> Wyświetlanie elementu – ["display element", "show element", "print element", "wyświetl element", "pokaż element", "wypisz element", "element"].
> Dodawanie – ["add", "add matrices", "dodaj", "dodaj macierze", "dodawanie", "dodawanie macierzy"].
> Mnożenie – ["mul", "multiply", "multiplication", "pomnóż", "mnożenie"].
> Wyznacznik – ["det", "determinant", "wyznacznik"].
> Odwrotność – ["inv", "inverse", "odwrotność"].
> Transpozycja – ["tranpose", "transpozycja", "macierz transponowana", "transponuj"].
> Wynik ostatniej operacji – ["ans", "ostatni wynik"].
> Zapisywanie wyniku ostatniej operacji – ["save ans", "zapisz ostatni wynik"].
> Wyjście – ["stop", "end", "exit", "quit", "koniec", "zamknij", "zakończ"].
"""

ans = "Nie wykonano jeszcze żadnych obliczeń więc wynik `ans` jest pusty"
print("Witaj w naszym programie służącym do wykonywania prostych operacji na macierzach. Jeśli nie wiesz, co robić, wpisz help i poznaj możliwości programu.")
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

        # DODATKOWA FUNKCJONALNOŚĆ wyświetla wynik ostatniej operacji arytmetycznej/macierzowej
        elif command in ["ans", "ostatni wynik"]:
            print(ans)

        # DODATKOWA FUNKCJONALNOŚĆ zapisywanie wyniku ostatniej operacji do pamięci
        elif command in ["save ans", "zapisz ostatni wynik"]:
            if isinstance(ans, Matrix):
                object_name = get_object_name("Wpisz nazwę, pod którą chcesz przechowywać ten obiekt w pamięci programu: ")
                memory[object_name] = ans
            else:
                print("Pamięć pozwala przechowywać tylko obiekty będące macierzami.")

        # DODATKOWA FUNKCJONALNOŚĆwyświetla informację o wszystkich obiektach zapisanych w pamięci programu
        elif command in ["list", "ls", "dir", "pokaż pamięć", "pamięć"]:
            for key, value in memory.items():
                print(f"{key.ljust(5)}: {repr(value)}")

        # wczytywanie macierzy od użytkownika (z konsoli)
        elif command in ["readcmd", "read cmd", "read from cmd", "read from command line", "enter matrix", "wczytaj z konsoli", "wpisz macierz", "wpisz"]:
            matrix = Matrix.from_user()
            object_name = get_object_name("Wpisz nazwę, pod którą chcesz przechowywać tę macierz w pamięci programu: ")
            memory[object_name] = matrix

        # DODATKOWA FUNKCJONALNOŚĆ wczytywanie macierzy z pliku
        elif command in ["readfile", "read file", "read from file", "wczytaj plik", "wczytaj z pliku", "z pliku"]:
            matrix = None
            while not matrix:
                path = input("Podaj nazwę pliku: ")
                try:
                    matrix = Matrix.from_file(path)
                except FileNotFoundError:
                    print(f"Plik {path} nie istnieje")
                except ValueError as e:
                    print(e, "Popraw plik i spróbuj ponownie.")
            object_name = get_object_name("Wpisz nazwę, pod którą chcesz przechowywać tę macierz w pamięci programu: ")
            memory[object_name] = matrix

        # DODATKOWA FUNKCJONALNOŚĆ zapis macierzy do pliku
        elif command in ["save", "save matrix", "save matrix to file", "zapisz", "zapisz macierz", "zapisz do pliku"]:
            matrix_to_save = get_matrix()
            path = get_filename()
            if path is not None:
                matrix_to_save.save_to_file(path)

        # wyświetlanie całej macierzy
        elif command in ["display", "show", "print", "wyświetl", "pokaż", "wypisz"]:
            matrix = get_matrix()
            print(matrix)

        # wyświetlanie wybranego wiersza macierzy
        elif command in ["display row", "show row", "print row", "row", "wyświetl wiersz", "pokaż wiersz", "wypisz wiersz", "wiersz"]:
            matrix = get_matrix()
            row_index = get_index("Podaj numer wiersza (liczbę całkowitą): ")
            try:
                matrix.print_row(row_index)
            except IndexError:
                print(f"Macierz posiada tylko {matrix.number_of_rows} wierszy.")

        # wyświetlanie wybranej kolumny macierzy
        elif command in ["display column", "show column", "print column", "column", "wyświetl kolumnę", "pokaż kolumnę", "wypisz kolumnę", "kolumna"]:
            matrix = get_matrix()
            column_index = get_index("Podaj numer kolumny (liczbę całkowitą): ")
            try:
                matrix.print_column(column_index)
            except IndexError:
                print(f"Macierz posiada tylko {matrix.number_of_columns} kolumn.")

        # wyświetlanie jednego wybranego elementu macierzy
        elif command in ["display element", "show element", "print element", "wyświetl element", "pokaż element", "wypisz element", "element"]:
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
        elif command in ["add", "add matrices", "dodaj", "dodaj macierze", "dodawanie", "dodawanie macierzy"]:
            first_matrix = get_matrix()
            second_matrix = get_matrix()
            try:
                ans = first_matrix + second_matrix
                print("Wynik dodawania to:", ans)
            except ValueError as e:
                print(e)

        # mnożenie: macierzy przez macierz, macierzy przez skalar, dwóch skalarów
        # TODO można oczywiście rzucać błąd gdy użytkownik poda dwa skalary, ale po co ...
        elif command in ["mul", "multiply", "multiplication", "pomnóż", "mnożenie"]:
            first_argument = get_matrix_or_float()
            second_argument = get_matrix_or_float()
            try:
                ans = first_argument * second_argument
                print("Wynik mnożenia to:", ans)
            except ValueError as e:
                print(e)

        # DODATKOWA FUNKCJONALNOŚĆ transponowanie macierzy
        elif command in ["tranpose", "transpozycja", "macierz transponowana", "transponuj"]:
            matrix = get_matrix()
            ans = matrix.transpose()
            print(ans)

        # jeśli żadna dotychczasowa komenda nie pasowała, to sprawdzamy, czy użytkownik nie wpisał przypadkiem nazwy obiektu, jeśli tak to go wyświetlamy
        elif command in memory:
            print(f"Nie rozpoznano komendy, ale znaleziono w pamięci programu obiekt o nazwie {command}")
            print(command, "to:", memory[command])

        # tekst wpisany przez użytkownika nie jest poprawną komendą ani nazwą obiektu w pamięci
        else:
            print(f"Nie rozpoznano komendy `{command}`")

    except EOFError:  # użytkownik wcisnął CTRL-D (Linux) lub Ctrl-Z i ENTER (Windows)
        print("Wracam do menu głównego")
        continue
    except KeyboardInterrupt:  # użytkownik wcisnął CTRL-C
        print()
        break
    # TODO przez wysłaniem projekty odkomentować poniższy ogólny except, łapiący wszystkie wyjątki, a więc także te niewychwycone w czasie testowania
    except BaseException as e:
        print("Wystąpił nieoczekiwany błąd, skontaktuj się z autorami programu. Przekaż im poniższą treść błędu:\n", e)

print("Dziękujemy za skorzystanie z naszego programu :)")
