# Chaining Plugins using "USE" in a Promptbook

Required Plugin(s): _Incident Analysis, MDTI, IP-API custom plugin, WHOIS custom plugin_

To expose a _threat based on an Incident_ in an environment using Copilot for Security, you could use the following series of prompts:

1. Summarize a Defender Incident:
   ```
   Summarize Defender Incident <IncidentID>. Include the Incident ID, category, and impacted assets.
   ```

2. Use MDTI to research any existing threats based on the Incident details:
   ```
   Use the last response as context and use Microsoft Defender Threat Intelligence to tell me if there are any existing threats that might match.
   ```

3. Get information about the IP address of the impacted assets:
   ```
   Use IP-API and tell me where the IP address is located.
   ```

4. Get information about the domain used in the Incident:
   ```
   Use WHOIS to tell me about the domain of the impacted user.
   ```

These prompts are designed to guide Copilot for Security through a _threat based on an Incident_ within an environment, from initial identification to detailed reporting. Remember to tailor these prompts to fit the specific context and systems of your organization.
