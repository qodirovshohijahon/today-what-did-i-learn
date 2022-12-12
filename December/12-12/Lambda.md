AWS Lambda is 
- a serverless,
- event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers. 


You can trigger Lambda from over 200 AWS services and software as a service (SaaS) applications, and only pay for what you use.


**AWS Lambda** is a compute service that lets you run code without provisioning or managing servers. 
 
**Lambda** runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including 
 - server and operating system maintenance, 
 - capacity provisioning 
 - automatic scaling, and logging



**When to use Lambda**

- **File processing:** 
  - use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload.

- **Stream processing:** 
  - use Lambda and Amazon Kinesis to process real-time streaming data for application activity tracking, 
    - transaction order processing,
    - clickstream analysis, 
    - data cleansing, 
    - log filtering, 
    - indexing, 
    - social media analysis, 
    - Internet of Things (IoT) device data telemetry, 
    - metering.

- **Web applications:** 
  - combine Lambda with other AWS services to build powerful web applications that automatically scale up and down and run in a highly available configuration across multiple data centers.

- **IoT backends:** 
  - build serverless backends using Lambda to handle web, 
    - mobile, 
    - IoT, 
    - third-party API requests.

- **Mobile backends:** 
  - build backends using Lambda and Amazon API Gateway to authenticate and process API requests. 
  - Use AWS Amplify to easily integrate your backend with your iOS, Android, Web, and React Native frontends.



**1. How does Lambda handle failure during event processing?**
- In Lambda, a function is run in either synchronous or asynchronous mode. 
- If a function fails in synchronous mode, then it just gives an exception to the calling application. 
- If a function fails in asynchronous mode, then it is retried at least three times.


**2. Some of the limitations of AWS Lambda are as follows:**

- The default deployment package size is 50 MB.
- The ephemeral disk space is limited to 512 MB as the Lambda function will take longer time to execute with a larger package size.
- The execution time is more when the memory allocation is less.
- The memory range is from 128 MB to 10,240 MB.
- The maximum execution timeout for a function is 15 minutes.


**3. What is serverless computing?**
- Serverless computing is a cutting-edge computing execution model wherein a cloud provider runs the virtual server and dynamically manages the allocation of machine resources. 
- Serverless computing helps build and run applications and services without being concerned about servers. 
- With the prowess of serverless computing, applications run on servers, but the servers are managed by AWS. 
- This gives developers a lot of flexibility and freedom to focus on app development. 
- AWS Lambda is at the core of serverless computing as it helps to run code without servers.

**4. What is the role of the handler when working with Lambda functions via SDK?**

Before executing your lambda function, AWS Lambda calls a handler function. It can process the triggering event's data and execute other functions or methods.

Here is an example handler function written in Node.js.
```js
exports.myHandler = function(event, context, callback) {
     console.log("value = " + event.key);
     console.log("functionName = ", context.functionName);
     callback(null, "Demo tested successfully");				
}; 
```
- The first line prints the event object's key attribute to show the trigger event.
- The second line shows the name of your lambda function that it will call.
- Lastly, we have a callback that can return information about errors or results of successful execution back to AWS Lambda.



**5. Can you briefly tell why there is a need for a serverless.yml file to support Lambda functions?**

- A YML configuration file contains all the information about the services, functions, and resources you want to run. The file describes the exact configuration of all the resources you want to use. In the case of AWS Lambda, the serverless.yml file holds the configuration for the Serverless framework.

- This framework provides you with a CLI that makes developing serverless functions easier. You can use the Serverless framework and create independent pieces of code (functions). The framework will organize and take care of their execution. Additionally, it will create resources to run the events you define and configure your function to catch these events.

- With serverless.yml, AWS Lambda will know how you want to use the framework, which functions to call, which events to look out for, and much more. A serverless.yml for a demo project is given below for better clarity.



**6. What is the context object in a Lambda function?**
- The context object given to the handler function contains essential information about the function and its execution. For example, the function's name, how much time remains before your function times out, and the stream related to your function. It also comes with helpful methods which you can use within your function like context.succeed() or context.fail().

**Some helpful properties and methods of the context object are as follows:**

- `context.functionVersion:` This method returns which version of the function is getting executed.
- `context.awsRequestID:` This method returns the request ID attached to a certain function and its execution.
- `context.callbackWaitsForEmptyEventLoop:` This property controls the behavior of the callback() function. If you set it to false, its won't process other tasks in the event loop. Its default value is true, and it only returns to the caller when the event loop closes.
Note: Commonly asked AWS Lambda interview question


**7. What is the time limit for execution in Lambda when you perform DDOS?**
- The time limit is 5 minutes.


**8. What are the Final Variables and Effectively final variables in Lambda?**
- Final Variables are those which cannot be modified once assigned. When they are in an earlier stage where it is possible to make any form of change, they are called effectively variable. The value is yet to be assigned to them. The outcome is required without restriction in many cases and that is the reason to use effective variables. They can also play a role in testing. If final variables are to be equipped with several additional features, this can be done through effective Variables. Most local expressions in Lambda are final