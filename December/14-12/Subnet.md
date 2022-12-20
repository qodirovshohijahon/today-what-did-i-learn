### What is a subnet?
- a subnet, or subnetwork, is a network inside a network. 
- subnets make networks more efficient. 
- through subnetting, network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination.


**Why is subnetting necessary?**
As the previous example illustrates, the way IP addresses are constructed makes it relatively simple for Internet routers to find the right network to route data into. However, in a Class A network (for instance), there could be millions of connected devices, and it could take some time for the data to find the right device. This is why subnetting comes in handy: subnetting narrows down the IP address to usage within a range of devices.

Because an IP address is limited to indicating the network and the device address, IP addresses cannot be used to indicate which subnet an IP packet should go to. Routers within a network use something called a subnet mask to sort data into subnetworks.


**What is a subnet mask?**
A subnet mask is like an IP address, but for only internal usage within a network. Routers use subnet masks to route data packets to the right place. Subnet masks are not indicated within data packets traversing the Internet — those packets only indicate the destination IP address, which a router will match with a subnet.

Suppose Bob answers Alice's letter, but he sends his reply to Alice's place of employment rather than her home. Alice's office is quite large with many different departments. To ensure employees receive their correspondence quickly, the administrative team at Alice's workplace sorts mail by department rather than by individual employee. After receiving Bob's letter, they look up Alice's department and see she works in Customer Support. They send the letter to the Customer Support department instead of to Alice, and the customer support department gives it to Alice.

In this analogy, "Alice" is like an IP address and "Customer Support" is like a subnet mask. By matching Alice to her department, Bob's letter was quickly sorted into the right group of potential recipients. Without this step, office administrators would have to spend time laboriously looking for the exact location of Alice's desk, which could be anywhere in the building.

For a real-world example, suppose an IP packet is addressed to the IP address 192.0.2.15. This IP address is a Class C network, so the network is identified by "192.0.2" (or to be technically precise, 192.0.2.0/24). Network routers forward the packet to a host on the network indicated by "192.0.2."

Once the packet arrives at that network, a router within the network consults its routing table. It does some binary mathematics using its subnet mask of 255.255.255.0, sees the device address "15" (the rest of the IP address indicates the network), and calculates which subnet the packet should go to. It forwards the packet to the router or switch responsible for delivering packets within that subnet, and the packet arrives at IP address 192.0.2.15 (learn more about routers and switches).