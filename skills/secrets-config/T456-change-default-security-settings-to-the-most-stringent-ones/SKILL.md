---
name: t456-change-default-security-settings-to-the-most-stringent-ones
description: Follow these instructions to decrease the possibility of exploits through excessive capabilities: - Change the default/basic security settings to the most stringent settings available for the device, application, container or component in u
---

# T456: Change default security settings to the most stringent ones and disable unnecessary services and modules

**Category:** CODE_FIX  
**SD Elements:** [T456](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T456/)  
**Priority:** 6  
**Domain:** secrets-config

## Affected Areas in This Repository

auth.py (JWT_SECRET), docker-compose.yml and .env.example (DB_PASSWORD), database.py (seeded admin/admin123), app.py (Flask debug=True via start.sh)

## Required Fix

Move all secrets to environment variables/a secret manager, remove default accounts and passwords, and ship secure-by-default configuration (debug disabled).

## Implementation Guidance (SD Elements)

Follow these instructions to decrease the possibility of exploits through excessive capabilities:
 
- Change the default/basic security settings to the most stringent settings available for the device, application, container or component in use. This will help to reduce the attack surface of the system or software. For example, basic security settings for a device might enable Bluetooth connectivity by default, which can make the device vulnerable to different types of attacks.
 
 - Maintain a list of system components and server modules, including all available functions, services, protocols, and ports. You can refer to the framework/device/component documentation to help compile the list, which you should review periodically.
 
 - In addition to listing capabilities manually, use scanning tools to identify unnecessary modules, open ports, and available services, and then add those findings to the list of system components and server modules.
 
 - Configure the system and all its components to provide only necessary functionality, disabling all inessential modules, functions, services, protocols, and ports. For example, a directory listing module, HTTP or FTP protocols, or JTAG and USB ports. Disable any unnecessary ports to ensure operation with a minimum number of open ports.  
 
 - If it is feasible, limit the functionality of system components to a single function per component/device. For example, do not run a file sharing server on the same host as a DNS server.

### Secure the use of USB ports when they are enabled

Follow these guidelines to decrease the threats of enabled ports: 

- Set the USB port as a dedicated charging port by default. Ensure that a device plugged in is enumerated as a Dedicated Charging Port (DCP) by default.
- Protect USB mounting for upload or download with a console password. That is, change the enumeration mode to Charging Downstream Port (CDP) only after entering the correct password.

## Success Criteria

- The control "Change default security settings to the most stringent ones and disable unnecessary services and modules" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
