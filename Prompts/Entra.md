Tell me about Lee Majors most recent failed sign-in

Why was Lee Majors prompted for MFA?

Create a lifecycle workflow for new hires in the Marketing department that sends a welcome email and a TAP and adds them to the All Users group.


1.  `SecurityEvent  `
2.  `| where TimeGenerated > ago(1h) and EventID == 4688  `
3.  `| summarize count() by Process, Computer`
