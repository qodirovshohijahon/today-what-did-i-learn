**Nagios** 
- is one of the monitoring tools that is used for Continuous monitoring of 
  - systems, 
  - applications, 
  - services, 
  - and business processes etc. in a DevOps culture. 

- **In the event of a failure**, Nagios can alert technical staff of the problem, allowing them to begin remediation processes before outages affects business processes, end-users, or customers. With Nagios you don’t have to explain why an unseen infrastructure outage affect your organization’s bottom line.

**By using Nagios you can:**

- **Plan** for infrastructure upgrades before outdated systems cause failures.
- **Respond** to issues at the first sign of a problem.
- **Automatically** fix problems when they are detected.
- **Coordinate** technical team responses.
- **Ensure** your organization’s SLAs are being met.
- **Ensure** IT infrastructure outages have a minimal effect on your organization’s bottom line.
- **Monitor** your entire infrastructure and business processes.

**How does Nagios work?**
- Nagios runs on a server, usually as a daemon or service.
- Nagios periodically runs plugins residing on the same server, they contact hosts or servers on your network or on the internet.
- One can view the status information using the web interface.
- You can also receive email or SMS notifications if something happens.
- The Nagios daemon behaves like a scheduler that runs certain scripts at certain moments.
- It stores the results of those scripts and will run other scripts if these results change. Refer the diagram below:

**What is the difference between Active and Passive check in Nagios?**


- **The major difference between **Active and Passive checks** is that** 
  - Active checks are initiated and performed by Nagios, 
  - while passive checks are performed by external applications.
  - Passive checks are useful for monitoring services that are:
  - Asynchronous in nature and cannot be monitored effectively by polling their status on a regularly scheduled basis.
  - Located behind a firewall and cannot be checked actively from the monitoring host.

- **The main features of Actives checks are as follows:** 
- Active checks are initiated by the Nagios process. 
- Active checks are run on a regularly scheduled basis.

Monitoring Network - Nagios Core
Services:
- HTTP
- PING
- SMTP

Monitoring Host Resources - Nagios Core
- Diks Usage
- CPU Load
- RAM usage


**Architechture**
Nagios Interface
Nagios Server
Host - Linux Server