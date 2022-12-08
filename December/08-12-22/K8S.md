
**:one: What Is Kubernetes Deployment?** 

- a deployment is a Kubernetes resource object used for declarative application updates. 

- deployments allow you to define the lifecycle of applications, including the container images they use, the number of pods and the manner of updating them.

**What Is Kubernetes StatefulSet?**

- a StatefulSet is a workload API object for managing stateful applications.

- usually, Kubernetes users are not concerned with how pods are scheduled, although they do require pods to be deployed in order, to be attached to persistent storage volumes, and to have unique, persistent network IDs that are retained through rescheduling. 

- statefulSets can help achieve these objectives.



**There are three types of probes in Kubernetes**

- **Liveness Probe** indicates whether the container is running.
  - the kubelet uses a liveness probe to know when to restart the container. 
  
  - many applications running for long periods of time eventually transition to broken states, and cannot recover except by being restarted.
  
  - for example, if you are running a web application and the web server is running but not able to serve any request. 
 
  - restarting a container in such a scenario can help to make the application more available despite bugs.
  
  - theinitialDelaySeconds field tells the kubelet that it should wait 3 seconds before performing the first probe.
  
  - the periodSeconds the field specifies that the kubelet should perform a liveness probe every 3 seconds.
 
  - there are some other fields as well which can be specified in the probes spec
  
  - **failureThreshold** : when a probe fails, Kubernetes will try failureThreshold times before giving up. 
 
  - giving up in case of a liveness probe means restarting the container. 
  
  - in case of readiness probe, the Pod will be marked Unready. Defaults to 3. The minimum value is 1.

- **Readiness Probe** indicates whether the container is ready to respond to requests.

  - the Kubelet uses a readiness probe to know when a container is ready to start accepting traffic. 
  
  - a pod is considered ready when all its containers are ready. 
 
  - it is used to control which pods can be used as backends for the Service.

    **For example** 
    - an application might need to load some data or configuration at or connect to some external services at startup. 
    
    - we don’t want to kill such applications or either start sending requests until that application’s Pod is not successfully loaded data or configurations at startup. 
    
    - Kubernetes provides readiness probes to detect and mitigate these situations
  
  - if the readiness probe fails, the endpoints controller removes the Pod’s IP address from the endpoints of all Services that match the Pod. 

  - the default state of readiness before the initial delay is Failure. 
 
  - if a container does not provide a readiness probe, the default state is Success.


- **Startup Probe** indicates whether the container is started. 
  - the kubelet uses this probe to know when a container application has started. 
 
  - if the startupProbe is enabled, it disables liveness and readiness probe until it succeeds. 
  
  - this is done to make sure that liveness and readiness probes do not interface with the application startup. 
 
  - this can be used to replace the liveness probe on a slow starting container which can be killed by kubelet before they are up and running.

  - There are different kinds of mechanisms that are used to check the container probes. 
  
  - all types of probes use one of these check mechanisms.
  
    **Exec**
  
  - this kind of check executes a specified command inside the container. 
 
  - the probe is considered successful if the command exits with a status code of 0.
------------------------------------

**General**
- **Liveness probes** are essentially health checks. They periodically run a command (or send an HTTP request to an endpoint) on a container and wait for a response. If a response doesn't arrive, or the container returns a failure, or fails to respond within a certain time frame, the probe triggers a restart of the container.

- **Startup probes** are used alongside liveness probes to protect slow-starting containers. If you have a container that takes a long time to start—longer than your liveness probe threshold—you can use a startup probe to delay the liveness probe until the container has fully started.

- **Readiness probes** are also alongside liveness probes for containers that have finished starting, but aren't yet ready to serve traffic. This is for containers that do some kind of initialization task, like loading data from a remote data store or waiting for a downstream dependency to become available. Readiness probes can detect this and prevent liveness probes from restarting the container, while also preventing requests from reaching the container.

![](./../img/12.Screenshot%202022-12-08%20184735.png)

**:two: Что такое K8s Service? Как работает? Какие есть варианты?**
- an abstract way to expose an application running on a set of Pods as a network service.
- since pods are ephemeral, 
  - a service enables a group of pods, 
 
  - which provide specific functions (web services, image processing, etc.) to be assigned a name and unique IP address (clusterIP). 
 
  - as long as the service is running that IP address, 
 
  - it will not change. Services also define policies for their access.
 
  - a service is responsible for exposing an interface to those pods, which enables network access from either within the cluster or between external processes and the service.