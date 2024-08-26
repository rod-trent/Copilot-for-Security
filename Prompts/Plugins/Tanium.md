Prompts on this page require the Tanium plugin and Tanium specific solutions to work.

Want more? Check out the <a href="https://help.tanium.com/bundle/ug_connect_cloud/page/connect/ms_copilot_security.html#using_skills" target="_blank">Microsoft Copilot for Security Integration Reference</a> page on Tanium's site.

## Tanium Copilot Prompts Legend 

Synonyms:
*	List / Show / Show me
* Endpoint(s) / Device(s) / Computer(s)
# Incident Response Process Prompts:
```
[List|Show] the endpoints that are running a process with the [process name|file name] <name>
```
---
```
[List|Show] the child processes of <process name> [on endpoint <endpoint>].  
```
---
```
[List|Show] the processes that have been run by user <username> [on endpoint <endpoint>].  Show results in a table format.
```
---
```
[List|Show] all processes connected to IP address X.X.X.X.  Show results in a table format.
```
---
```
[Show me the|How many] different versions of <executable> [are] [present] on my endpoints.  Show results in a table.
```
# Vulnerability Prompts:
```
[List|Show] the endpoints that have vulnerability <CVE-YYYY-XXXXX>. Show results in a table format.
```
---
```
[List|Show] the endpoints that have a software package for <package name>. show results in a table format.
```
---
```
[How many|Which] endpoints have <application name> and <version number> [installed]? Show results in a table format. 
---
```
# Promptbook flow example:
```
Show me the details of Defender Incident 43
```
```
  What are the main issues or indicators to investigate?
```
```
        Analyze the suspicious powershell script    
```
```
            Deobfuscate the url
```
```
                Use Tanium to tell me all of the machines that are currently connected to the malicious ip address
```
---
# General Prompts:

```
Tell me what computers are affected by CVE-2023-36805 and what patches are required. Group them by OS platform in table format
```
---
```
What is the status of patch deployment for computer Win11-x64?
```
---
```
Show me the systems that have log4j in their SBOM report, present the findings in a table
```
---
```
Get Logged In User
```
---
```
Get Real-time Data from Endpoints
```
---
```
Count Endpoints Having Package Version
```
---
```
List Endpoints Having Package
```
---
```
List Process SHA-256 Hashes and Versions
```
---
```
Get Vulnerability Test Results
```
---
```
List Endpoints Vulnerable To CVE
```
---
```
View Endpoint Processes
```
---
```
List Service Module Details
```
---
```
List Service Process Details
```
---
```
List WMI Event Consumers
```
---
```
List File Details
```
---
```
List Child Processes for Process File
```
---
```
List Endpoints with Process Command
```
---
```
List Endpoints with Process Name
```
---
```
List Endpoints with Process MD5 Hash
```
---
```
List Endpoints with Process MD5 Hash
```
---
```
List Processes Connected To IPv4 Address
```
---
```
List Process Ran As User
```
---


