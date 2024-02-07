import subprocess
import requests
import time
import os

# Pełna ścieżka do pliku tor.exe
TOR_EXE_PATH = r'D:\\Tor\\tor\\tor.exe'

# Adres SOCKS proxy dla lokalnej instancji Tor
TOR_SOCKS_PORT = 9050

# Ścieżka do pliku kontrolnego, który jest używany do autoryzacji
CONTROL_AUTH_COOKIE_PATH = r'D:\\Tor\\tor\\data\\control_auth_cookie'

# Funkcja do zmiany adresu IP przez zrestartowanie procesu Tor
def change_tor_ip():
    stop_tor()
    start_tor()

# Funkcja do uruchamiania Tor
def start_tor():
    subprocess.run([TOR_EXE_PATH, "--quiet", "--hash-password", "", "--controlport", str(TOR_SOCKS_PORT)])

# Funkcja do zatrzymywania Tor
def stop_tor():
    subprocess.run([TOR_EXE_PATH, "--quiet", "--hash-password", "", "--controlport", str(TOR_SOCKS_PORT), "--pidfile", "kill"])

# Funkcja do wykonania zapytania HTTP przez Tor
def make_tor_request(url, max_content_lines=10):
    session = requests.session()
    session.proxies = {'http': f'socks5h://localhost:{TOR_SOCKS_PORT}',
                       'https': f'socks5h://localhost:{TOR_SOCKS_PORT}'}

    try:
        response = session.get(url, timeout=5)
        print(f"Status Code: {response.status_code}")

        # Wyświetl tylko kilka pierwszych linii odpowiedzi
        content_lines = response.text.split('\n')[:max_content_lines]
        content_preview = '\n'.join(content_lines)
        print(f"Content Preview:\n{content_preview}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

# Przykładowe użycie
if __name__ == "__main__":
    try:
        # Uruchom proces Tor w tle
        start_tor()

        # Poczekaj chwilę przed zapytaniem
        time.sleep(5)

        # Zapytanie HTTP przez Tor
        make_tor_request("https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/")

        # Poczekaj przed zmianą adresu IP
        time.sleep(5)

        # Zmiana adresu IP
        change_tor_ip()

        # Poczekaj przed kolejnym zapytaniem
        time.sleep(5)

        # Zapytanie po zmianie adresu IP
        make_tor_request("https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/")

    finally:
        # Zatrzymaj Tor po zakończeniu
        stop_tor()
