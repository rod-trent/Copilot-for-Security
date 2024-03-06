Prompts on this page require the Tanium plugin to work.

# General Prompts:
```
Tell me what computers are affected by CVE-2023-36805 and what patches are required. Group them by OS platform in table format
```
---
```
Please patch affected windows systems
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



