Prompts on this page require the Natural Language to KQL plugin to work.
<br><br>
```
What Hunting measures can I take to identify an increase in activity for <insert holiday name>?
```
---
```
Write a KQL query that shows a table of devices that are enrolled in Microsoft Intune. Add the device health score and the compliance status for each device using the lookup operator to join the devices table with a table of device health data and a table of device compliance data, based on the device ID.
```
---
```
Explain the following KQL query to me: EmailEvents | extend GeoInformation = parse_json(geo_info_from_ip_address(SenderIPv4)) | extend NwMsgId_Recipient = strcat(NetworkMessageId, "_", RecipientEmailAddress) | summarize dcount(NwMsgId_Recipient) by tostring(GeoInformation.country)
```
---
```
Create a KQL query to use to locate users with more than 5 incorrect logins in 10 minutes.
```
