import requests
import time
import socket
import socks
from stem import Signal
from stem.control import Controller

# Adres SOCKS proxy dla lokalnej instancji Tor
TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051

# Funkcja do zmiany adresu IP przez bezpośredni SOCKS proxy
def change_tor_circuit():
    try:
        with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
            controller.authenticate()  # Uwierzytelnianie przy użyciu kontroli Tor
            controller.signal(Signal.NEWNYM)  # Wysyłanie sygnału do zmiany obwodu
            print("New Tor circuit created.")
    except Exception as e:
        print(f"Error: {e}")
        print("Unable to change Tor circuit.")

# Funkcja do wykonania zapytania HTTP przez Tor
def make_tor_request(url, max_content_lines=10):
    session = requests.session()
    session.proxies = {'http': f'socks5h://localhost:{TOR_SOCKS_PORT}',
                       'https': f'socks5h://localhost:{TOR_SOCKS_PORT}'}

    try:
        start_time = time.time()
        response = session.get(url, timeout=10)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Status Code: {response.status_code}")
        print(f"Elapsed Time: {elapsed_time:.2f}")

        try:
            local_ip = session.get("http://httpbin.org/ip").json()["origin"]
            peer_ip = response.raw._fp.fp.raw._sock.getpeername()[0]
            print(f"Local IP Address: {local_ip}")
            print(f"Peer IP Address: {peer_ip}")
        except AttributeError:
            print("Unable to retrieve IP Address.")

        # Wyłączono wydruk treści odpowiedzi
        # content_lines = response.text.split('\n')[:max_content_lines]
        # content_preview = '\n'.join(content_lines)
        # print(f"Content Preview:\n{content_preview}")

        with open('results.txt', 'a') as file:
            file.write(f"Success - Status Code: {response.status_code}, Elapsed Time: {elapsed_time:.2f}, Local IP Address: {local_ip if 'local_ip' in locals() else 'N/A'}, Peer IP Address: {peer_ip if 'peer_ip' in locals() else 'N/A'}, URL: {url}\n")

    except requests.exceptions.Timeout:
        print("Error: Connection timed out.")

        with open('results.txt', 'a') as file:
            file.write(f"Failure - Error: Connection timed out, URL: {url}\n")

    except Exception as e:
        print(f"Error: {e}")

        with open('results.txt', 'a') as file:
            file.write(f"Failure - Error: {e}, URL: {url}\n")

    finally:
        session.close()

# Przykładowe użycie
if __name__ == "__main__":
    try:
        num_iterations = int(input("Podaj liczbę iteracji (zmian adresu IP): "))
        for _ in range(num_iterations):
            change_tor_circuit()
            time.sleep(5)
            make_tor_request("https://www.nytimesn7cgmftshazwhfgzm37qxb44r64ytbb2dj3x62d2lljsciiyd.onion/")

    except KeyboardInterrupt:
        pass
