Prompts on this page require the Natural Language to KQL plugin to work.
<br><br>
```
Tell me the intent of the following KQL query: <insert KQL query>
```
---
```
Use the following information to generate a proper KQL query for Microsoft Sentinel.

Table = SecurityAlert
Time/date range = 3 days
Query = the top medium severity alert and the number of times is shows up in the data
Display = just the alert name and the times it shows up
```

The above, but for a Promptbook: https://github.com/rod-trent/Copilot-for-Security/blob/main/Prompts/Promptbooks/KQL_Request.md

---
```
Convert the following yara rule to a Microsoft Sentinel analytics rule:

/*
    This Yara ruleset is under the GNU-GPLv2 license (http://www.gnu.org/licenses/gpl-2.0.html) and open to any user or organization, as long as you use it under this license.
*/

rule Linux_DirtyCow_Exploit {
   meta:
      description = "Detects Linux Dirty Cow Exploit - CVE-2012-0056 and CVE-2016-5195"
      author = "Florian Roth"
      reference = "http://dirtycow.ninja/"
      date = "2016-10-21"
   strings:
      $a1 = { 48 89 D6 41 B9 00 00 00 00 41 89 C0 B9 02 00 00 00 BA 01 00 00 00 BF 00 00 00 00 }

      $b1 = { E8 ?? FC FF FF 48 8B 45 E8 BE 00 00 00 00 48 89 C7 E8 ?? FC FF FF 48 8B 45 F0 BE 00 00 00 00 48 89 }
      $b2 = { E8 ?? FC FF FF B8 00 00 00 00 }

      $source1 = "madvise(map,100,MADV_DONTNEED);"
      $source2 = "=open(\"/proc/self/mem\",O_RDWR);"
      $source3 = ",map,SEEK_SET);"

      $source_printf1 = "mmap %x"
      $source_printf2 = "procselfmem %d"
      $source_printf3 = "madvise %d"
      $source_printf4 = "[-] failed to patch payload"
      $source_printf5 = "[-] failed to win race condition..."
      $source_printf6 = "[*] waiting for reverse connect shell..."

      $s1 = "/proc/self/mem"
      $s2 = "/proc/%d/mem"
      $s3 = "/proc/self/map"
      $s4 = "/proc/%d/map"

      $p1 = "pthread_create" fullword ascii
      $p2 = "pthread_join" fullword ascii
   condition:
      ( uint16(0) == 0x457f and $a1 ) or
      all of ($b*) or
      3 of ($source*) or
      ( uint16(0) == 0x457f and 1 of ($s*) and all of ($p*) and filesize < 20KB )
}
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
