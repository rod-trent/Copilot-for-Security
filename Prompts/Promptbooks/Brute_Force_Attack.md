# Brute Force Attack

Required Plugin(s): *Entra, Natural Language to Defender 365 KQL, Natrural Language to Sentinel KQL*

To expose a brute force attack in an environment using Copilot for Security, you could use the following series of prompts:

1. **Monitor Access Attempts**:
   ```
   Show me all failed access attempts within the last 24 hours.
   ```

2. **Check for IP Anomalies**:
   ```
   List all IP addresses with excessive login failures and compare them against known malicious IPs.
   ```

3. **Evaluate Login Patterns**:
   ```
   Highlight any unusual login patterns or times that deviate from the norm.
   ```

4. **Assess Password Complexity**:
   ```
   Review password strength policies and report any accounts with passwords that do not meet the required complexity standards.
   ```

These prompts are designed to help identify potential brute force attack vectors by analyzing login data, account lockouts, and password policies. It's important to regularly monitor and adjust these prompts based on the evolving nature of cyber threats.

