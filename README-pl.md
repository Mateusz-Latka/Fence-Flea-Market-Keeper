# Fence-Flea-Market-Keeper

Fence-Flea-Market-Keeper to bot Discord zaprojektowany, aby dostarczać informacji o przedmiotach z gry Escape from Tarkov (EFT) i ich aktualnych cenach rynkowych. Bot korzysta z API Tarkov, aby pobierać dane o przedmiotach i obliczać ich ceny.

## Funkcje
- `/price [item_name]`: Pobierz aktualną cenę rynkową i poziom przedmiotu z EFT.
- `/tier`: Wyświetl poziomy łupów na podstawie identyfikacji cen slotów.
- `/how2use`: Dowiedz się, jak korzystać z bota i dostępnych komend.

## Wymagania
- Python 3.x
- Biblioteka `discord.py`
- Biblioteka `requests`
- Biblioteka `python-dotenv`

Możesz zainstalować wymagane biblioteki za pomocą:
```bash
pip install -r requirements.txt
```

## Instalacja
1. Sklonuj to repozytorium na swój komputer lokalny.
2. Utwórz konto bota Discord na [Discord Developer Portal](https://discord.com/developers/applications).
3. Wygeneruj token bota i skopiuj go.
4. Zmień nazwę pliku `.env.example` na `.env`.
5. Zamień placeholder `YOUR_BOT_TOKEN` w pliku `.env` na wygenerowany token bota.
6. Zaproś bota na swój serwer Discord, używając wygenerowanego URL z Discord Developer Portal.
7. Otwórz terminal lub wiersz polecenia, przejdź do katalogu projektu i uruchom plik `bot.py`.

## Użycie
1. Upewnij się, że bot działa i jest połączony z Twoim serwerem Discord.
2. Wpisz `/how2use` na dowolnym kanale tekstowym, aby uzyskać instrukcję obsługi bota i dostępnych komend.
3. Użyj komendy `/price [item_name]`, aby pobrać aktualną cenę rynkową i poziom przedmiotu z EFT.
4. Użyj komendy `/tier`, aby zobaczyć poziomy łupów na podstawie identyfikacji cen slotów.

## Przykłady
- `/price AK-47`: Pobiera aktualną cenę rynkową i poziom przedmiotu AK-47.
- `/tier`: Wyświetla poziomy łupów.

## Podziękowania
- [Discord.py Library](https://github.com/Rapptz/discord.py)
- [Escape from Tarkov API](https://tarkov.dev/api/)

## Wkład
Jeśli znajdziesz jakiekolwiek problemy lub masz sugestie dotyczące ulepszenia bota, śmiało otwórz zgłoszenie (issue) lub zgłoś pull request.

## Licencja
Ten projekt jest licencjonowany na warunkach licencji MIT - szczegóły znajdziesz w pliku LICENSE.

## Kontakt
W razie pytań lub uwag, prosimy o otwarcie zgłoszenia (issue) lub kontakt z właścicielem repozytorium.