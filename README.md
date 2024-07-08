# ~

---

Scary Chicken is a program designed to use malware defensive techniques to our advantage.
Modern-day malware holds code that can be vital to the survival of the organization distributing such programs. And so they contain safeguards that include preventing malware reverse engineering and research by preventing installation onto machines that have indicators of tools that would be installed onto a VM or a malware researcher's machine.
As a user, we can leverage this to our advantage by creating fake processes, files, fake network indicators, and registry entries to deter malware from even executing the installation.

This is my attempt at an open source cyber scarecrow (https://www.cyberscarecrow.com/).
The nature of Cyber Scarecrow is somewhat shady and is not open source.

---

## Resources
```
https://github.com/mategol/PySilon-malware/blob/main/resources/protections.py
https://symantec-enterprise-blogs.security.com/threat-intelligence/verblecon-sophisticated-malware-cryptocurrency-mining-discord
https://krebsonsecurity.com/2021/05/try-this-one-weird-trick-russian-hackers-hate/
https://symantec-enterprise-blogs.security.com/threat-intelligence/verblecon-sophisticated-malware-cryptocurrency-mining-discord
https://www.sans.org/white-papers/36667/
https://blog.sonicwall.com/en-us/2018/02/6-ways-malware-evades-detection/
https://www.cyberbit.com/endpoint-security/anti-vm-and-anti-sandbox-explained/
https://attack.mitre.org/techniques/T1497/
https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis
```

---

## To do list

- [ ] Fill browser history (VM's come with empty browser history)
- [ ] Modularizing code
- [ ] Make like libraries with a portion of the functions
- [ ] Configure realistic non conflicting processes
- [ ] Make like libraries with a portion of the functions
- [ ] Encrypting code with pyinstaller to make it exe
- [ ] Fake content injection
---
