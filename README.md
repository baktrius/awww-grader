# Automatyczny uruchamiacz tester-AWWW

## Sposób użycia

Z Moodla należy pobrać wszystkie rozwiązania (przycisk na prawo góra w liście wszystkich rozwiązań) i rozpakować.

Katalog z rozwiązaniami należy wskazać w `config.py`. W `config.py` należy ustawić również względną ścieżkę do testera AWWW (osobny projekt).

Uruchomienie testów następuje poprzez wykonanie `python3 grade.py <imię> <nazwisko>`. Dodatkowe opcje można zobaczyć w `python3 grade.py --help`.

Ustawienie zmiennej środowiskowej `REPORT=1` spowoduje otworzenie vs code z kodem projektu przed jego przetestowaniem.