Prompts on this page require the Natural Language to KQL plugin to work.
<br><br>
```
Use the following information to generate a proper KQL query for Microsoft Sentinel.

Table = <tablename>
Date range = <time range>
Query = <query processing example: the top medium severity alert and the number of times is shows up in the data>
Display = <how the results are displayed example: just the alert name and the times it shows up>
```
---
For a Promptbook
```
Use the following information to generate a proper KQL query for <PRODUCT_NAME>.

Table = <TABLE_NAME>
Date range = <TIME_RANGE>
Query = <QUERY_RESULT>
Display = <RESULTS_DISPLAY>
```
---
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
