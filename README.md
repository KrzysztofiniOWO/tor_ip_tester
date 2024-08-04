# Tor_ip_tester

## About the project

 This project is the subject of my engineering thesis under the title **Algorithm of dinamic change of ip addresses in tor network in the context of service availability testing**. Its main goal is to check whether the use of dynamically assigned ip addresses when using Internet services, which positively affects the security and anonymity of users, would have a significant impact on the availability and efficiency of the services provided.

 ## Testing methodology

 This project uses the tor network and the dynamic ip address change algorithm to compare the different types of services for dynamic ip addresses and static ip addresses. 

 It collects data for both cases and, based on these data, creates statistics to enable comparison of effectiveness for both types of tests.

 ## Project structure

 ### functions.py
 
 This file contains the functions necessary to conduct research for dynamically assigned and static ip addresses. The functions that test the various services are:  

  - **make_requests -** Tests pinging websites
  
  - **check_first_image_download_time -** Checks the time it takes to find and download the first image file on the page

  - **test_mongodb -** Checks the time it takes to connect to the mongodb database and execute the query

  - **download_file -** Checks the time it takes to download a test text file
  
  - **test_upload_file_ftp -** Checks the time it takes to transfer an image file via ftp
  
  - **test_jsonplaceholder_get -** Test the response time and data fetching from the jsonplaceholder API
  
  - **test_dns_resolution -** Test the DNS resolution time for a given domain
  
  - **test_websocket -** Test WebSocket connections
  
### statistics.py

This file is used to create statistics based on the generated data

### utils.py

This file contains auxiliary functions used when running tests


  



