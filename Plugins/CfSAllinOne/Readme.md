# Copilot for Security Plugin: CfSAllinOne

See the <a href="https://rodtrent.substack.com/i/144250833/version-history" target="_blank">version history</a>

### **This plugin combines previous plugins into a single, all-in-one effort to capture and respond with Copilot for Security activity. This plugin will be updated as additional monitoring activity is made available and identified.**

### Pre-requisites

-   [Copilot for Security Enabled](https://learn.microsoft.com/en-us/security-copilot/get-started-security-copilot#onboarding-to-microsoft-security-copilot)
-   [Access to upload custom plugins](https://learn.microsoft.com/en-us/security-copilot/manage-plugins?tabs=securitycopilotplugin#managing-custom-plugins)
-   [Microsoft Sentinel Workspace](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) created.
-   Parameters for KQL Plugin - Microsoft Sentinel Workspace Name, Subscription ID, Resource Group Name and Entra Tenant ID

### Instructions

#### Upload the Custom Plugin

1.  Obtain the file CfSAllinOne.yaml from this directory.
2.  Modify the yaml file to specify your specific Entra TentantId, SubscriptionId, ResourceGroupName and WorkspaceName for your Sentinel instance.
3.  <a href="https://learn.microsoft.com/en-us/copilot/security/manage-plugins?tabs=securitycopilotplugin#add-custom-plugins" target="_blank">Upload the custom plugin</a>



