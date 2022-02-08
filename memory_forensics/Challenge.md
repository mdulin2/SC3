## Setup 1
The Security Operations Center (SOC) has indicated some suspicious behavior on an endpoint and have sent you the Windows Security and PowerShell event logs to identify the Indicators of Compromise and any additional information. The two files are CTF_Security.evtx & CTF_Windows PowerShell.evtx.

- What IP address is contained within the malicious PowerShell Script? 
    - HINT: Use an event log viewing tool for EVTX files. 'Windows Event Viewer' will do this by default. 
    - HINT: Look for outgoing connections that use powershell
- What User account was able to log into the system from the system identified in the PowerShell script?
    - HINT: Use an event log viewing tool for EVTX files. 
    - HINT: What's the event code for LOGINs on Windows?


## Setup 2 


The SOC has also forward potential malware sample to you for evaluation. They have sent you a 7Zip folder with the file name CTF_Spokane2022.7z with the password “infected”. The SOC manager is requesting the following information concerning the payload. 


- What is the SHA-256 Value of the Payload?:
    - HINT: Just hash the whole file
- What IP address does the script establish a connection with?
    - HINT: Base64 decode the powershell script before execution. 
    - HINT: Decode the binary that gets executed in the powershell script
- What has Microsoft identified this file as?
    - HINT: Use Virus Total
- What tool produced this script? 
    - HINT: Use Virus Total