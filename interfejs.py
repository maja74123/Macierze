# Oto taki pierwowzór interfejsu. I to baaaardzo odległy pierwowzór, wersja v0.03 xD
# wszystko to, aby wyświetlało okno na środku
import tkinter as tk  # importuje pakiet tkinker
from tkinter import font  # importuje funkcję zmiany czcionek

liczba_klikniec = 0  # zmienna liczby kliknięć do przycisku

def klikniecie():  # definuję funkcję przycisku
    global liczba_klikniec  # globalna zmienna (czyli poza definicją) licząca kliknięcia
    liczba_klikniec += 1  # iteracja
    print(f"Kliknięto orzycisk {liczba_klikniec} razy!")  # f-string tworzący napis

def otworzOkno():  # definicja funkcji otwierania okna (początkowo to był cały kod, ale jako funkcja jest poręczniejszy)
    okno = tk.Tk()  # tworzy okno o nazwie "okno"
    okno.configure(bg="black")  # dzięki temu okno jest czarne

    okno_height = 600  # ustala wysokość okna na 600px
    okno_width = 600  # ustala szerokość okna na 600px

    screen_width = okno.winfo_screenwidth()  # zmienna która ustala rozmiar
    screen_height = okno.winfo_screenheight()  # też zmienna która ustala rozmiar

    x = (screen_width // 2) - (okno_width // 2)  # pozycja okna na ekranie
    y = (screen_height // 2) - (okno_height // 2)  # też pozycja okna na ekranie

    okno.geometry(f"{okno_width}x{okno_height}+{x}+{y}")  # generalnie ustala geometrie okna

    czcionka_tytulowa = font.Font(family="Comic Sans MS", size=48)  # ustawienie czcionki tytułu na Comic Sans MS oraz rozmiaru na 48
    czcionka_przyciskowa = font.Font(family="Comic Sans MS", size=24)  # ustawianie czcionki na przycisk
    czcionka_detaliczna = font.Font(family="Comic Sans MS", size=12)  # ustawianie czcionki na rozmaite detale(jak napisy w rogach)

    tytul = tk.Label(okno, text="Macierze", font=czcionka_tytulowa, fg="white", bg="black", )  # tworzy napis na oknie o treści "Macierze" o białym kolorze
    napis_wersji = tk.Label(okno, text="wersja 0.03 (10.05.2023)", font=czcionka_detaliczna, fg="white", bg="black")  # tworzy napis o najnowszej wercji programu
    napis_nw = tk.Label(okno, text="Projekt na algorytmy :)", font=czcionka_detaliczna, fg="white", bg="black")  # tworzy napis na górnym-lewym rogu okna

    napis_wersji.pack(side="bottom", anchor="se")  # w zasadzie pokazuje napis o wersji
    napis_nw.pack(side="top", anchor="nw")  # w zasadzie pokazuje napis w górnym-lewym rogu
    tytul.pack(pady=120)  # w zasadzie daje nasz napis na środek (i przesunięcie napisu o 150px w dół)

    przycisk = tk.Button(okno, text="kliknij mnie", font=czcionka_przyciskowa, command=klikniecie, width=15, height=1, fg="white", bg="black")  # wymiary i parametry przycisku (oraz komenda, którą spełnia)
    przycisk.pack()  # wyświetla przycisk

    okno.title("Macierze")  # tytuł na pasku
    okno.mainloop()  # wyświetla okno (by nie znikało)

otworzOkno()  # wywołuje funkcję otwierającą okno