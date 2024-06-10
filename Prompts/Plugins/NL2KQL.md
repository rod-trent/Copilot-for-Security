Prompts on this page require the Natural Language to KQL plugin to work.
<br><br>
```
Explain the following KQL query to me: EmailEvents | extend GeoInformation = parse_json(geo_info_from_ip_address(SenderIPv4)) | extend NwMsgId_Recipient = strcat(NetworkMessageId, "_", RecipientEmailAddress) | summarize dcount(NwMsgId_Recipient) by tostring(GeoInformation.country)
```
---
```
Create a KQL query to use to locate users with more than 5 incorrect logins in 10 minutes.
```
