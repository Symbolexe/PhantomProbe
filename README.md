# PhantomProbe: Web Pentest Framework
## Overview
PhantomProbe is a powerful web pentest framework designed to assist security professionals in performing comprehensive security assessments of web applications. Developed by Yasin Saffari Founder & CEO of OxyopesLab, PhantomProbe offers a wide range of tools and functionalities for subdomain enumeration, reconnaissance, vulnerability scanning, and more.
## Tools
PhantomProbe provides a wide range of tools categorized into different sections. Here's a detailed overview of each category and the tools within them:
### Subdomain Enumeration
- [x] Sublist3r: A subdomain enumeration tool that utilizes various techniques to discover subdomains.
- [x] Subfinder: Another subdomain enumeration tool focusing on providing fast and comprehensive results.
- [x] Assetfinder: A tool specialized in discovering subdomains from a given domain.
- [x] Cero: A subdomain enumeration tool designed to uncover hidden subdomains efficiently.
- [x] Xorn: A subdomain discovery tool capable of finding subdomains using different methods.
### Reconnaissance
- [x] Csprecon: A reconnaissance tool that extracts endpoints and sensitive information from a given URL.
- [x] Lazyrecon: An automated reconnaissance tool that performs various reconnaissance tasks efficiently.
- [x] Arjun: A parameter discovery tool that helps in finding hidden parameters in URLs.
- [x] Dnsrecon: A tool for DNS reconnaissance, providing detailed information about DNS records.
- [x] Dnsenum: Another DNS reconnaissance tool focused on discovering DNS information.
### Scanning
- [x] Nmap: A versatile network scanning tool for discovering open ports, services, and vulnerabilities.
- [x] Wafdetect: A tool for detecting web application firewalls (WAFs) and their characteristics.
- [x] Naabu: A fast port scanner designed for discovering open ports and services.
- [x] Whatweb: A web scanner that identifies technologies used by web applications.
- [x] Httpx: A tool for probing HTTP and HTTPS servers, providing detailed information about web services.
### Email Harvesting
- [x] TheHarvester: An email harvesting tool capable of extracting email addresses from various sources.
### Vulnerability Analysis
- [x] Https Smuggling: A tool for detecting HTTP request smuggling vulnerabilities in web applications.
- [x] Sqlinjection: A tool for detecting and exploiting SQL injection vulnerabilities.
- [x] Command Injection: A tool for identifying and exploiting command injection vulnerabilities.
- [x] WordPress: A tool for scanning WordPress websites for known vulnerabilities.
### Miscellaneous Tools
- [x] Waybackurls: A tool for fetching URLs from the Wayback Machine archive.
- [x] Gdork: A Google dorking tool for finding sensitive information on Google.
- [x] SecretFinder: A tool for discovering sensitive information hidden in web applications.
## Installation
To install PhantomProbe, follow these steps:
Clone the repository:

  ```git clone https://github.com/OxyopesLab/PhantomProbe.git```

Navigate to the PhantomProbe directory:

```cd PhantomProbe```

Run the installation script:

```./install.sh```

Follow any additional instructions prompted during the installation process.
## Usage
### Basic Commands
- use <tool_name>: Select a tool to use.
- set <parameter> <value>: Set parameter values, e.g., domain, URL, etc.
- run: Run the selected tool with the configured parameters.
- back: Deselect the current tool and return to the main prompt.
- help: Display the help message with a list of available commands.
- exit: Exit the PhantomProbe framework.
### Tool Selection
To select a tool, use the use command followed by the desired tool's name. For example:

```use subenum/sublist3r```
### Setting Parameters <a name="setting-parameters"></a>
Set parameters using the set command followed by the parameter name and its value.

```set domain example.com```
### Running Tools
Once a tool is selected and parameters are set, use the run command to execute the tool.

```run```
### Navigating the Framework
You can navigate through the framework using the ```back``` command to return to the main prompt.
### System Commands
You can also execute system commands directly within PhantomProbe by typing the command
## Contributing
PhantomProbe is an open-source project, and contributions from the community are highly appreciated. If you'd like to contribute to the project, you can:
1. Submit bug reports or feature requests on the GitHub repository.
2. Fork the repository, make your changes, and submit pull requests for review.
3. Help improve the documentation or provide translations for non-English speakers.
## Credits
PhantomProbe is developed and maintained by Yasin Saffari (symbolexe) founder & CEO of OxyopesLab. Special thanks to all contributors and supporters who have helped make this project possible.
