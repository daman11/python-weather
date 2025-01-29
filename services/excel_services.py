from pandas import DataFrame, ExcelWriter
import pandas as pd
import os

def save_to_excel(data):
    try:
        file_path = "weather.xlsx"

        # Sprawdź, czy plik już istnieje
        if os.path.exists(file_path):
            try:
#               Wczytaj istniejące dane z pliku
                existing_data = pd.read_excel(file_path)
                # Konwertuj do DataFrame
                df_existing = DataFrame(existing_data)
            except Exception as e:
                print(f"Błąd podczas odczytu istniejącego pliku: {e}")
                df_existing = DataFrame()  # Pusty DataFrame w razie błędu
        else:
            df_existing = DataFrame()  # Pusty DataFrame, jeśli plik nie istnieje
        # Tworzenie nowego DataFrame z nowymi danymi
        df_new = DataFrame(data, index=[0])

        # Dodaj nowe dane do istniejących
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)

        # Zapisz dane z powrotem do pliku
        df_combined.to_excel(file_path, index=False)

        print("Dane zapisane do pliku Excel.")
    except Exception as error:
        print(f"Wystąpił błąd podczas zapisywania do Excela: {error}")