---
name: t1468-encrypt-sensitive-data-at-rest-in-the-browser
description: Avoid using browser-based storage mechanisms to store sensitive data. However, if you can justify storing data in the browser, that data needs to be encrypted. The mechanism for encrypting data in the browser is driven by the requirement to
---

# T1468: Encrypt sensitive data at rest in the browser

**Category:** CODE_FIX  
**SD Elements:** [T1468](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1468/)  
**Priority:** 9  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Required Fix

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

## Implementation Guidance (SD Elements)

Avoid using browser-based storage mechanisms to store sensitive data. However, if you can justify storing data in the browser, that data needs to be encrypted.

The mechanism for encrypting data in the browser is driven by the requirement to gain access to the data while the application is offline (i.e., a Progressive Web App). 


__When offline access is not a requirement__, follow these steps:

* Authenticate the user against the backend system
* Request a salt from the client (see notes below)
* Use the salt to generate a symmetric encryption key
* Send the key to the client (see notes below)
* Use the client key to encrypt and decrypt data at rest.
* To regain access to encrypted data, follow these steps again using the existing salt.	 

	__*Note:*__ More detail is available in the How-To section of this countermeasure (Encrypt using a key obtained from the server).

__When offline access is a requirement__, follow these steps:

* Generate or retrieve a salt on the client (see notes below)
* Prompt the user for a passphrase to initialize the encryption/decryption key
* Use the user's passphrase and salt to generate a symmetric encryption key
	* Passphrases can be turned into cryptographic keys using a Password-Based Key Derivation Function (PBKDF)
		* PBKDF2 is a widely supported function that achieves this.
* Use the key to encrypt and decrypt data at rest.
* To regain access to encrypted data, follow these steps again using the existing salt.

	__*Note:*__ More detail is available in the How-To section of this countermeasure (Encrypt using a key generated from a user passphrase).
	__*Note:*__ The steps here only concern access to encrypted data. User authentication against backend systems is a crucial part of a PWA running in online mode.


__*Additional Notes*__

* The key is derived using a per-client salt
	* Use unique keys per client. An example of a client instance is a specific browser.
	* Key uniqueness is guaranteed by using a per-client salt.
	* Randomly generate the salt by the client and store it in the browser. When an existing salt is available, it should be reused.
	* The salt can be stored in Local Storage in plain text
* The key is used in the browser to encrypt and decrypt locally stored data
	* Keep the key in memory on the client. Do not store the key in the browser.
	* When the client's browsing context is closed, the key will be dismissed.
* The implementation of the encryption/decryption logic must be centralized
	* In an Angular application, these features are typically implemented using an application-wide service. Only this service handles the keys.

## Success Criteria

- The control "Encrypt sensitive data at rest in the browser" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
