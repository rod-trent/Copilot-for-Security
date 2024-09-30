Prompts on this page require the <a href="https://github.com/rod-trent/Copilot-for-Security/tree/main/Plugins/CfSAllinOne" target="_blank">Copilot for Security Activity (all-in-one)</a> plugin to work.
<br><br>
```
//SLIDE 20 - where EXAMPLE
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4624 // Successful logon
| where AccountType =~ "user" // case insensitive
```
---
```
//SLIDE 23 - count EXAMPLE
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4624
| count 
```
---
```
//SLIDE 25 - limit/take EXAMPLE

SecurityEvent
| limit 10

SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4624
| where AccountType =~ "user" 
| take 10
```
---
```
//SLIDE 27 - top EXAMPLE
SecurityEvent
| where TimeGenerated > ago(1h)
| where EventID == 4624
| summarize count() by Account
| top 10 by _count
```
---
```
//SLIDE 29 - distinct EXAMPLE
SecurityEvent
| where EventID = 4625
| distinct Computer

ThreatIntelligenceIndicator
| where ThreatType contains “BotNet”
| distinct NetworkSourceIP
```
---
```
//SLIDE 32 - summarize EXAMPLE
//Logons with clear text password by target account
SecurityEvent
| where EventID == 4624 and Logontype == 8
| summarize count() by TargetComputer
```
---
```
//SLIDE 35 - project EXAMPLE
Perf
| where CounterName == "Free Megabytes" 
| extend FreeKB = CounterValue * 1024
| extend FreeGB = CounterValue / 1024
| extend FreeMB = CounterValue 
| project Computer, CounterName, FreeGB, FreeMB, FreeKB 
```
---
```
//SLIDE 37 - extend EXAMPLE
Perf
| where CounterName == "Free Megabytes" 
| extend FreeKB = CounterValue * 1024
| extend FreeGB = CounterValue / 1024
| extend FreeMB = CounterValue 
| project Computer, CounterName, FreeGB, FreeMB, FreeKB  
```
---
```
//SLIDE 40 - bin and render EXAMPLE
SecurityEvent 
| where TimeGenerated > ago(7d)
| summarize count() by bin(TimeGenerated, 1d)
| render barchart  
```
---
```
//SLIDE 42 - let STATEMENT EXAMPLE
let suspiciousAccounts = datatable(account: string) [
	@"\administrator", 
	@"NT AUTHORITY\SYSTEM“
];
SecurityEvent | where Account in (suspiciousAccounts)  
```
---
```
//SLIDE 45 - union EXAMPLE
SecurityEvent
| union Heartbeat 
| summarize count() by Computer  
```
---
```
//SLIDE 47 - join EXAMPLE
SecurityEvent
| join Heartbeat on Computer
| where EventID == "4688"
| project Computer, OSType, OSMajorVersion, Version  
```
---
```
//LAB 1
// Find the count of failed logins by Account Name
// run parts of the query, adding a line at the time, to learn more
SecurityEvent
| where TimeGenerated <= ago(7d)
| where EventID == 4625 
| summarize count() by TargetAccount, Computer  
```
---
```
//LAB 2
// Find all Windows logon events starting 2 weeks ago until 1 week ago that occurred on a computer with name which starts with “App”

SecurityEvent | limit 100 // Find relevant fields: Activity, EventID, Computer

SecurityEvent | summarize by Activity // find the Event signaling login

SecurityEvent
| where TimeGenerated between (ago(14d)..ago(7d)) 	// start with the time filter
| where EventID == "4624"
| where Computer startswith "App" // case insensitive
	// This is the solution, but there are so many results

SecurityEvent 
| where TimeGenerated between (ago(14d)..ago(7d))
| where EventID == "4624"
| where Computer startswith "App"
| summarize count() by Computer
	// so let’s count per computer  
```
---
```
//LAB 3
// Find how many times each process ran per computer

SecurityEvent | summarize by Activity // Let’s find the event that includes process names

SecurityEvent | where EventID == "4688" | limit 10 
	// find the relevant field, in this case "Process" 

SecurityEvent
| where EventID == "4688"
| summarize count() by Process, Computer  
```
---
```
//LAB 4
// Chart the rate of process creation on all domain controllers.

SecurityEvent
| where Computer startswith "DC"
| where EventID == "4688" | summarize count() by Computer, bin(TimeGenerated, 1h) 
| render timechart  
```
---
```
//LAB 5
// Find the encoded PowerShell command that was ran on a computer that endswith 3EX for the past 60 days.

VMProcess| where TimeGenerated >= ago(90d)
| where Computer endswith “CSK”
| where CommandLine contains “encoded”  
```
---
```
//LAB 6
// Render graph of successful vs failed logons over the last 30 days, use alias for the legend (“Success”, “Failed”)
// run parts of the query, adding a line at the time, to learn more
SecurityEvent
| where TimeGenerated > ago(30d)
| summarize 
	Success=countif(EventID == 4624), 
	Failed=countif(EventID == 4625) 
	by bin(TimeGenerated, 1h)
| render timechart  
```
---
```
//LAB 7
//Find the missing critical security updates for the VM that starts with CH1. Update
| where Classification == "Security Updates" and UpdateState == "Needed" and MSRCSeverity == "Critical"
| where Resource startswith "CH1"  
```
---
```
//LAB 8
//You need to know what user account was used to sign in and what country they signed in from in the past 60 days.  
union SigninLogs, AADNonInteractiveUserSignInLogs
| where TimeGenerated >= ago(60d)
| where Status_dynamic contains "User did not pass the MFA challenge."
| where AppDisplayName contains "Azure Portal“| project TimeGenerated, Status_dynamic, AppDisplayName  
```
---
```
//LAB 9
// Find the top 3 source IP addresses which were blocked by your firewall. 
AzureNetworkAnalytics_CL
| where FlowStatus_s == "D"
| where FlowDirection_s == "I"
| where isnotempty(SrcIP_s)
| summarize count() by SrcIP_s  
```
---
