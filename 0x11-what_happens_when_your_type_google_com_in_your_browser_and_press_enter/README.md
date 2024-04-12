#### What happens when you type google.com in your browser and press Enter ####

### DNS request: ###
When you type a URL into your browser, the first thing that happens is a DNS (Domain Name System) request. The browser sends a request to a DNS server to translate the human-readable domain name (like "google.com") into an IP address, which is needed to locate the server on the internet.

### TCP/IP: ###
Once the DNS server returns the IP address, the browser initiates a TCP (Transmission Control Protocol) connection with the server using the IP address obtained. TCP ensures that data packets are transmitted reliably and in the correct order over the internet. IP (Internet Protocol) handles the routing of these packets across networks.

Firewall: A firewall acts as a barrier between the browser and the internet to monitor and control incoming and outgoing network traffic based on predetermined security rules. It helps protect the system from unauthorized access and malicious attacks.

### HTTPS/SSL: ###
If the website uses HTTPS (Hypertext Transfer Protocol Secure), the browser establishes a secure connection with the server using SSL/TLS (Secure Sockets Layer/Transport Layer Security) encryption. This ensures that the data exchanged between the browser and the server is encrypted and secure from eavesdropping or tampering.

### Load balancer: ###
In the case of large websites like Google, multiple servers are typically deployed to handle incoming requests. A load balancer distributes incoming traffic across these servers to ensure optimal resource utilization, improve responsiveness, and prevent overload on any single server.

### Web server: ###
The web server (e.g., Apache, Nginx) receives the HTTP request from the browser, processes it, and generates an appropriate response. It serves web pages, files, or other resources requested by the client.

### Application server: ###
In some cases, especially for dynamic web applications, an application server (e.g., Tomcat, Node.js) is used to execute application logic and interact with databases or other external services. It generates dynamic content based on user inputs or other factors.

### Database: ###
If the request involves retrieving or storing data, the application server communicates with the database server (e.g., MySQL, PostgreSQL) to perform database operations. The database stores and manages structured data, such as user information, product catalogs, or session data.
