**1. что такое Load Average?** 
- (стоит освежить что это и как работает на одноядерных и многоядерных серверах, мочь объяснить суть своими словами)

  - to understand the Load Average in Linux, we need to know what do we define as load.
  - in a Linux system, the load is a measure of CPU utilization at any given moment.

  - is a metric that is used by Linux users to keep track of (observe) system resources. 
  - it also helps you monitor how the system resources are engaged.
  - it refers to **the number of processes** which are either currently **being executed by the CPU** or are **waiting for execution**.
  - an idle system has a load of **0**. 
  - if each process that is **being executed** or is **on the waitlist**, the load increases by **1**.


1. Какие состояния процессов есть в Linux? 
- (стоит освежить знания по Systemd)

1. Как проверить сетевую доступность между EC2 и RDS, если на  EC2 установлена минимальная сборка Linux? - (Разобраться какие команды могут использоваться кроме telnet, в том числе как использовать echo)****