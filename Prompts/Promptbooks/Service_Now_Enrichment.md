# Service Now Enrichment

Required Plugin(s): *ServiceNow*

To create a *Service Now Enrichment* in an environment using Copilot for Security, you could use the following series of prompts:

1. **Summarize a Service Now incident**:
   ```
   Analyze Service Now incident <IncidentID>.
   ```

2. **Display all the Service Now incident notes and comments**:
   ```
   Show me the work notes and comments associated with it.
   ```

3. **Prioritize high level Service Now indicents for the time range**:
   ```
   Show me high priority service now incidents created in the past month.
   ```

4. **Compare Service Now incidents to known CVEs**:
   ```
   Are there any CVEs listed in this service now incident, Are there any threat actors known to be associated with this CVE? If so, summarize what we know about them.
   ```

5. **Show authentication methods for users in Service Now incident**:
   ```
   Show the authentication methods setup for user involved in that incident. Especially indicate whether they have MFA enabled.
   ```

6. **Generate report**:
   ```
   Write me an executive summary report about the service now incident, vulnerability, threat actor insights, and recommendations for someone who is less technical.
   ```


These prompts are designed to guide Copilot for Security through a *Service Now Enrichment* within an environment, from initial identification to detailed reporting. Remember to tailor these prompts to fit the specific context and systems of your organization.
