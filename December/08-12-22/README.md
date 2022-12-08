**1. Как дать доступ к Endpoint из on-prem? (Нужно разобраться в деталях Site-to-site VPN, Virtual Private Gateway, Route table, Endpoints, DNS resolver)**


**:one: Connect Your Data Center to AWS (Direct Connect)**

   ![](./../img/1.connect-data-center-to-aws2.jpg)

   - **AWS Direct Connect** enables you to securely connect your AWS environment to your on-premises data centre 

   - over a standard **1Gb** or **10Gb** Ethernet fibre-optic connection. 

   - AWS Direct Connect offers dedicated **high speed**, l**ow latency** connection, which bypasses internet service providers in your network path. 

   - an AWS Direct Connect location provides access to Amazon Web Services in the region it is associated with, as well as access to other US regions. 

   - AWS Direct Connect allows you to logically partition the fibre-optic connections into multiple logical connections called Virtual Local Area Networks (VLAN). 

   - you can take advantage of these logical connections to improve security, differentiate traffic, and achieve compliance requirements.

**:two: Using Site-to-Site VPN, between the on-premises network and AWS**

   ![](./../img/2.vpn-how-it-works-tgw.png)

   - this solution is much quicker to implement providing that already you have a pair of **Firewalls** or **Routers** (with VPN accelerator hardware) in **High-Availability** mode connected to the Internet, usually at your Extranet Block.
   
   - by default, instances that you launch into an Amazon **VPC can’t communicate** with your own (remote) network. 
   - you can enable access to your remote network from your **VPC** by creating an **AWS Site-to-Site** VPN (**Site-to-Site VPN**) connection, and configuring **routing** to pass traffic through the connection.
   
   - although the term VPN connection is a general term, in this documentation, a **VPN connection** refers to the connection between your **VPC** and your **own on-premises network**. 
   - **Site-to-Site VPN** supports **Internet Protocol security** (**IPsec**) VPN connections. 
   
   - a **Site-to-Site VPN** connection offers two (`Active/Standby`) VPN tunnels between a virtual private gateway or a transit gateway on the AWS side, and a customer gateway on the remote (on-premises) side. 