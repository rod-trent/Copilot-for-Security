Prompts on this page require the Red Canary plugin to work.<br><br>
Details here: <a href="https://learn.microsoft.com/en-us/copilot/security/plugin-red-canary">Red Canary plugin for Copilot for Security</a>

## Red Canary Investigation - IP Address
_Use the following to create a Promptbook to execute an investigation in Red Canary based on the IP address of an endpoint with promptbookinputs : ip_address_
```
In Red Canary, can you search for ip address <ip_address>? Be sure to return the Endpoint ID in your response if there is a match.
```
```
Can you search Red Canary for that Endpoint ID? If there is a match please return the hostname and any `detections` associated with that hostname. Be sure to include the Detection ID and URL in your response.
```
```
Search Red Canary for that Detection ID and provide a complete overview of the threat
```
```
List all of the threat timeline items for the same Detection ID and provide a brief overview.
```
```
Can you please list the detectors that were involved in this Detection ID and provide a brief overview of them in table format?
```
```
Search Red Canary's external alerts. Do any of the alerts involve the same hostname? If they do be sure to keep that context for your analysis.
```
```
Use your expert security knowledge and the context in this chat to offer recommendations on how to respond to this threat.
```
```
Add the relevant Red Canary activity and comments to a one page write up summarizing this incident and its resolution. The language should be specific but accessible to a less technical audience.
```
```
Add the relevant Red Canary activity and comments to a one page write up summarizing this incident and its resolution. The language should be specific but accessible to a less technical audience.
```
---
## Red Canary Investigation - Hostname
_Use the following to create a Promptbook to execute an investigation in Red Canary based on the hostname of an endpoint with promptbookinputs : hostname_
```
Search the most recent published threats in Red Canary. Did any of the threats involve host <hostname>. Be sure to include the Threat ID in your response.
```
```
Search Red Canary's external alerts. Do any of the alerts involve the same hostname? If they do be sure to keep that context for your analysis.
```
```
Summarize the suspicious threat activity Red Canary has associated with this threat.
```
```
In Red Canary, are there any timeline details for this threat ID under investigation?
```
```
Can you please list the detectors that were involved in this Detection ID and provide a brief overview of them in table format?
```
```
Use your expert security knowledge and the context in this chat to offer recommendations on how to respond to this threat.
```
```
Add the relevant Red Canary activity and comments to a one page write up summarizing this incident and its resolution. The language should be specific but accessible to a less technical audience.
```
