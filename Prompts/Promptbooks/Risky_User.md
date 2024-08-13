# Risky User

Required Plugin(s): *General*

To expose a *Risky User* in an environment using Copilot for Security, you could use the following series of prompts:

1. **Identify if a user is risky or not**:
   ```
   Check if <USER_UPN> is a risky user?
   ```

2. **Why is the user risky?**:
   ```
   Give detailed context as to why the user is risky
   ```

3. **Is the user's device part of the risk?**:
   ```
   Does the user have a risky sign in device?
   ```

4. **Provide more investigation recommendations**:
   ```
   Suggest how we can investigate further this risky user?
   ```

5. **Request additional methods to help secure the environment**:
   ```
   What additional security methods can be invoked to take down the user from the risky user list?
   ```

These prompts are designed to guide Copilot for Security through a *Risky User* within an environment, from initial identification to detailed reporting. Remember to tailor these prompts to fit the specific context and systems of your organization.
