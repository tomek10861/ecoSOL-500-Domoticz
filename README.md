# Integration of ecoSOL 500 with Domoticz

## Description
This Python script enables the integration of the ecoSOL 500 solar controller with the Domoticz platform. With this script, you can monitor and manage your heating system based on the ecoSOL 500 controller using the Domoticz platform.

## How It Works
The script first fetches data from the ecoSOL 500 controller and then sends this data to Domoticz. Data fetching is done by sending a GET request to the ecoSOL 500 controller and then parsing the JSON response. Sending data to Domoticz is done by sending a GET request with the appropriate parameters.

## Controller Details
- Name: ecoSOL 500
- Module A Version: 003.50
- ecoNET Module Version: 3.2.3731

## Implementation Details
The script uses the `requests` and `json` libraries for communication with ecoSOL 500 and Domoticz. The script first defines the login data for Domoticz and the index mapping for various fields. Then the script fetches JSON data from ecoSOL 500, assigns values from the JSON response to variables, and then sends these values to Domoticz.

## Notes
Ensure that the IP addresses and login data for Domoticz and ecoSOL 500 are correct. Also, ensure that the index mapping is correct for your system.



# Integracja ecoSOL 500 z Domoticz

## Opis
Ten skrypt Pythona umożliwia integrację sterownika solarnego ecoSOL 500 z platformą Domoticz. Dzięki temu skryptowi, możesz monitorować i zarządzać swoim systemem grzewczym opartym na sterowniku ecoSOL 500 za pomocą platformy Domoticz.

## Jak to działa
Skrypt najpierw pobiera dane z sterownika ecoSOL 500, a następnie przesyła te dane do Domoticza. Pobieranie danych odbywa się poprzez wysłanie żądania GET do sterownika ecoSOL 500, a następnie analizę odpowiedzi JSON. Wysyłanie danych do Domoticza odbywa się poprzez wysłanie żądania GET z odpowiednimi parametrami.

## Dane sterownika
- Nazwa: ecoSOL 500
- Wersja modułu A: 003.50
- Wersja modułu ecoNET: 3.2.3731

## Szczegóły implementacji
Skrypt korzysta z bibliotek `requests` i `json` do komunikacji z ecoSOL 500 i Domoticz. Skrypt najpierw definiuje dane logowania do Domoticza oraz mapowanie indeksów dla różnych pól. Następnie skrypt pobiera dane JSON z ecoSOL 500, przypisuje wartości z odpowiedzi JSON do zmiennych, a następnie wysyła te wartości do Domoticza.

## Uwagi
Upewnij się, że adresy IP i dane logowania do Domoticza i ecoSOL 500 są poprawne. Ponadto, upewnij się, że mapowanie indeksów jest poprawne dla Twojego systemu.
