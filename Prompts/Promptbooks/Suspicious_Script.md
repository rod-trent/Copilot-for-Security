# Suspicious script analysis

Required Plugin(s): -General-

To expose a -Suspicious script analysis- in an environment using Copilot for Security, you could use the following series of prompts:

1. **Supply the script snippit and request information about it**:
   ```
   The following script was found as part of a potential security incident. Explain what this script does step by step and infer the intent. Also note any actions expressed that could be malicious in nature, including destructive activities, stealing of information, or changing of sensitive settings: <SNIPPET>
   ```

2. **Determine if the script is malicious or not**:
   ```
   Is this script malicious?
   ```

3. **Get reputation of associated IPs or devices**:
   ```
   Provide the reputation of any IPs or hostnames found.
   ```

4. **Determine if any existing intelligence exists**:
   ```
   Are there any threat intelligence articles that reference the IOCs that were found?
   ```

5. **Identify threat actors**:
   ```
   Show me the profiles of any threat actors referenced.
   ```

6. **Find out how to protect against the script's payload**:
   ```
   If this script was malicious, what are the recommended policy changes to protect against it?
   ```

6. **Provide a final report**:
   ```
   Write me a report that summarizes the findings from the investigation. It should be suitable for a non-technical audience.
   ```

These prompts are designed to guide Copilot for Security through a -Suspicious script analysis- within an environment, from initial identification to detailed reporting. Remember to tailor these prompts to fit the specific context and systems of your organization.
