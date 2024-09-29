# Tor_ip_tester

## About the project

 This project is the subject of my engineering thesis under the title **Algorithm of dinamic change of ip addresses in tor network in the context of service availability testing**. Its main goal is to check whether the use of dynamically assigned ip addresses when using Internet services, which positively affects the security and anonymity of users, would have a significant impact on the availability and efficiency of the services provided.

 ## Testing methodology

 This project uses the tor network and the dynamic ip address change algorithm to compare the different types of services for dynamic ip addresses and static ip addresses. 

 It collects data for both cases and, based on these data, creates statistics to enable comparison of effectiveness for both types of tests.

 ## Project structure

 ### functions.py
 
 This file contains the functions necessary to conduct research for dynamically assigned and static ip addresses. The functions that test the various services are:  

- **make_pings -**
Pings a webpage and records response times.

- **check_first_image_download_time -**
Downloads the first image from a webpage and records download times.

- **download_file -**
Downloads a sample text file from a webpage and records download times.

- **test_jsonplaceholder_get -**
Sends GET requests to the JSONPlaceholder API and records response times.

- **fetch_webpage -**
Fetches a webpage and records response times.

- **test_mongodb_find -**
Queries MongoDB and records query times.

- **test_dns_resolution -**
Resolves DNS for a hostname and records resolution times.

- **test_websocket_connection -**
Establishes WebSocket connections and records connection times.
  
### statistics.py

This file is used to create statistics based on the generated data

### utils.py

This file contains auxiliary functions used when running tests

### config.py

This file contains config parameters for functions used when running tests


  



