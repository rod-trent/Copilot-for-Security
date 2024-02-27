# Microsoft 365 Defender incident investigation

Required Plugin(s): *Microsoft 365 Defender, Intune*

To create a *Microsoft 365 Defender incident investigation* in an environment using Copilot for Security, you could use the following series of prompts:

1. **Summarize a 365 Defender incident**:
   ```
   Summarize Defender incident <DEFENDER_INCIDENT_ID>.
   ```

2. **Report on the entities captured in the incident**:
   ```
   Tell me about the entities associated with that incident.
   ```

3. **Prioritize impact of associated IP addresses**:
   ```
   What are the reputation scores for the IPv4 addresses on that incident?
   ```

4. **Determine how users authenticated with the network**:
   ```
   Show the authentication methods setup for each user involved in that incident. Especially indicate whether they have MFA enabled.
   ```

5. **Identify the devices a user has had access to**:
   ```
   If a user is listed in the incident details, show which devices they have used recently and indicate whether they are compliant with policies.
   ```

6. **Check if devices are up-to-date with security updates**:
   ```
   If any devices are listed in the previous output, show details from Intune on the one that checked in most recently. Especially indicate if it is current on all operating system updates.
   ```

7. **Provide a report**:
   ```
   Write an executive report summarizing this investigation. It should be suited for a non-technical audience.
   ```

These prompts are designed to guide Copilot for Security through a *Microsoft 365 Defender incident investigation* within an environment, from initial identification to detailed reporting. Remember to tailor these prompts to fit the specific context and systems of your organization.
