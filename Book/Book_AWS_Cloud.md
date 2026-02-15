# Cloud computing

## AWS-Terms

- Cloud platform V/S Cloud Service Provider (CSP) :

  - A company that provides Cloud services. It is a company or organization. Ex., Amazon, Google, and Micorosofte are CSP.
  - Services provided by Cloud service provider. It is a product which is consumed by users. Ex., Amazon's AWS, Google's GCP and Microsoft's Azure.

- Kondratiev Waves (K-waves) : Descibes Economical & technological cycle which repeats always. It is common pattern of a wave of change in supply and demand.

- Burning platform : It is used when a company abandons old technology for new with the uncertainty of success and can be motivated by some fear. Latest trend of companies adoptation to AI is example of burning platform.

- Solutions Architect : A role in organization which delivers technical solution using multiple systems to meet business needs. He makes sure Security (How secure the solution is?) and Cost (How much is it going to cost?). He does his researcha & experiments to deliver solution.

- Cloud Architect : It is a solution architect but he finds the technical solution using just cloud services. He architects the cloud solution by providing High availability, scalability, elasticity, fault tolerance & disaster recovery.

- Business Continuity Plan (BCP) : It is a document that outlines how a business will continue operating during an unplanned incident. It is basically telling how much business is willing to loss data and is going to take time to recover from an incident. Diaster recovery plans are expensive as you move toward faster recovery plan. Hence BCP tracks RPO and RTO to make for a recovery plan.

- Recovery Point Objective (RPO) : The maximum amount of data loss expected after an incident. More like it answers the question like "How much are you willing to lose data?".

- Recovery Time Objective (RTO) : The maximum amount of downtime your business can tolerate without any financial loss. It answers the question like "How much time are you willing to go down?".

- Global Service V/S Regional Service: In simple words, `AWS Billing`, `IAM`, `Route53` services are Global services as you don't need to set region to use them. However, for Regional Services (`AWS EC2`), you need to determine which region's service do you wish to use.

- Data center : It is a secured building that contains millions of computers. Data centers will be isolated from each other but they have a low-latency of (< 10ms).
- Availability Zone (AZ) : It is a physical location made up of one or more datacenter. 
- AZ identifier : For `us-east-1`, there are different AZ subnets which are like `us-east-1a`, `us-east-1b`, `us-east-1c` ... `us-east-1f`.
- Region : They're geographiucally distinct locations consisting of multiple AZs.

## Benefits of clouds

- Earlier "6 Benefits of cloud" terms was common but list got upgrade.

  - Agility

    - It is ability to move fast and adapt quickly to the change.
    - Earlier a company has to spend many hours to build a new server. But with AWS, it can be achieved by few minutes.
    - Ealier, companies tooks months to build new feature -> make a release -> recieve feedback. Now, companies make new snapshot and test with beta users to get earliest feedback.
  
  - Pay-as-you-go pricing
  - Economy of scale

    - The bigger you are, the cheaper each unit becomes. In AWS pricing, you'll notice the more instance of process you consume, the cheaper it will get.
    - In real world, Bulk prices are always relatively cheaper than the fraction.

  - Global Reach

    - Ability to deploy your application worldwide in minutes.
    - Enter new markets faster with the help of AWS.

  - Security
  - Reliability
  - Scalability

    - Ability to increase or decrease resources to handle workload changes.

  - Elasticity

    - It is automatic ability to adapt scalability. It is an ability to increase or decrease number of servers to handle the traffic.
    - Example, ASG (Auto Scaling Groups) allows automatic Horizontal scaling (scale-in or scale-out) behaviour.

  - High Availability

    - System remains available with minimal downtime.
    - It ensures no point failure and provides a certain level of performance.
    - Example, ELB (Elastic Load Balancer) is being used to re-route traffic to healthy servers if a server becomes unavailble or unhealthy. It ensures your application remains available.

  - Fault Tolerance

    - Fault tolerance.= Stronger form of High availability.
    - An ability to ensure preventing change of failure or no single point of failure. ZERO downtime.
    - Example, Failover in database, when all the traffic is moved to secondary/ redundant server to handle requests. The secondary system is not in use until fail over occurs.

### Diaster Recovery

- An ability to recover from a disaster and to prevent the loss of data solutions that recovers from a disater. It is a strategy to restore systems after a major failure or catastrophy.
- Disaster recovery apporach should answer these question: Do you have a backup? How fast can you restore? Does it even work? How do you ensure it is not corrupted?
- Example, AWS's CloudEndure Disaster Recovery continuously replicates machine for fast and relible recovery in case of failure.

#### Disaster Recovery Options

There are 4 recovery options:

- Backup & Restore
- Pilot light
- Warm standby
- Multi-site active-active

Application Stack:
Frontend + Backend + Database + EC2 + ELB

Primary Region:

- Running at full production scale
- Handles 100% of traffic

| Strategy | RTO (Recovery Time) | RPO (Data Loss) | Cost | What’s Running in Secondary Region | What Happens During Disaster |
|-----------|---------------------|-----------------|------|-----------------------------------|------------------------------|
| Backup & Restore | High (Hours) | Medium (depends on backup frequency) | $ | Nothing running. Only snapshots, backups, and database backups stored. | Launch new EC2, restore DB from backup, configure ELB, update DNS. Full rebuild required. |
| Pilot Light | Medium (Tens of Minutes) | Low (DB replication active) | $$ | Only core components running (e.g., database replica). No frontend/backend servers running. | Launch EC2 (frontend/backend), attach to running DB, configure ELB, update DNS. |
| Warm Standby | Low (Minutes) | Very Low | $$$ | Full application stack running but at smaller scale (minimal EC2, smaller DB). | Scale up EC2 instances and DB to production capacity. Switch traffic. |
| Multi-Site Active-Active | Near Zero | Near Zero | $$$$ | Full production-scale stack running and actively serving traffic. | Traffic automatically shifts to healthy region. No rebuild or scaling needed. |

## Hosting Types Comparison

| Feature           | Shared Hosting | VPS        | Dedicated Server | Cloud Hosting  |
|-----------------  |----------------|------------|------------------|--------------- |
| Physical server   | Shared         | Shared     | Single tenant    | Pooled         |
| OS isolation      | ❌ No          | ✅ Yes     | ✅ Yes           | ✅ Yes         |
| Root access       | ❌ No          | ✅ Yes     | ✅ Yes           | ✅ Yes         |
| Vertical Scaling. | ❌ No          | ⚠️ Limited | ⚠️ Limited       | ✅ Yes         |
| Horizontal Scaling| ❌ No          | ⚠️ Limited | ⚠️ Very slow     | ✅ Yes         |
| Auto scaling      | ❌ No          | ❌ No      | ❌ No            | ✅ Yes         |
| Fault tolerance   | ❌ No          | ❌ No      | ❌ No            | ✅ Yes         |
| Cost              | Very low       | Low        | High             | Variable       |
| Maintenance       | Provider       | You        | You              | Mostly provider|
| Performance       | Low            | Medium     | High             | Variable       |
| Compliance        | ❌ No          | ⚠️ Partial | ✅ Yes           | ✅ Yes         |

### Dedicated Hosting

- A physical server that is being used by a single client or an application.
  - Companies who wants High performance, and low-stable latency prefers `Dedicated hosting` like Gaming, Trading, and High Data processing companies. Also, Government, HealthCare, and Banking prefer this server since it provides full control, security and compliance.
  - Disadantages:
    - Expensive  
    - No auto-scaling since it is one fixed machine. Hence, performance of application is impacted when number of requests are increased by a lot.
    - Less fault tolerence. Hardware, disk or CPU fault affect whole system.
    - Less portability: To create new instance, it requires new machine, resources and manual efforts for setup.
    - Engineers need to setup CPU+RAM, If overestimated --> Charge more else underestimated --> Performance issue.

### VPS (Virtual Private Server)

- A virtual machine created by dividing one physical server into multiple isolated virtual servers using Virtulization.

  - An Individual business is using this type of hosting because it is more cost effective and easy to manage than Dedicated hosting server. Additionally, It provides isolation and security through Virtualization.
  - Disadvantages:

    - Still shared Hardware result in `noisy neighbour problem`. Sudden traffic to an app will affect performance of other apps.
    - Limited scaling, fixed resources, and no support for auo-scaling.
    - Single point of failure means all apps are affected if main server is down.

### Shared Hosting

- A single physical machine shared by multiple hosts to host multiple applications.

  - Individuals and small businesses, who have limited budgets to host portfolios or websites. Additionally, Maintability of server is taken care by Hosts hence it requires less maintanence.
  - Disadvantages:

    - Poor performance. (Noisy neighbour problem exist)
    - No control. Can't install new softwares to virtual machine.
    - Security risk and weak isolation
    - Not scalable

### Cloud Hosting

- Multiple physical servers creates one server to maintain and host multiple application.

  - Industries, Enterprise, and startups prefers because it provides High availablility, elastic scaling, Pay-as-you-go service, and multiple cloud native services like load balancer, monitoring, logging etc.
  - Disadvantages:

    - High Complexity
    - Cost can grow rapidly
    - Less physical control

## Scaling

- Scaling is the process of adjusting resources (RAM, ROM, CPU, Storage) to handle system workload.

  - Scale up = Increasing resources when workload increased
  - Scale down = Decreasing resources when workload decreased

### Vertical scaling (Scale up)

- Make existing server more powerful by adding more resources (RAM, ROM, CPU, Storage).

  - ```text
    Before Scaling:  Server → handles 1,000 users
    After Scaling:   Server → handles 2,000 users
    ```

- Simple to implement. No code change needed.
- Disadvantages:

  - Has limit to add resources (Can't add RAM forever) and expensive.
  - Single point of failure (System dies then everything dies)
  - Downtime expected during scaling.

### Horizontal scaling (Scale out)

- Adding more servers instead of upgrading current one.

  - ```text
    Before Scaling:  1 server  → handles 1,000 users
    After Scaling:   5 servers → handles 5,000 users
    ```

- Complex architecture to implement but It is more cost effective, no downtime expected and no single point of failure.

- Disadvantages:

  - Complex architecture (Need load balancer) and planning needed.

### Auto-scaling

- Auto-scaling only performs Horizontal scaling (Scale out) approach. More practical in daily life since traffic is highly volitile.

- Set of rules are created to add more servers and to remove newly added servers.

- Advantages:

  - Cost effective
  - High availability and Fault tolerance (if one server dies, it adds one more to handle traffic automatically)
  - Better performance
  - No manual monitoring requries

- Disadvantages:

  - Complex to implement
  - Configuration overhead
  - Hard to debug while unexpected prodution issue rises
  - Not applicable for all application (like local storage systems, database and log-running batch jobs). It is useful for web servers and APIs.

## Cloud Service Model

- Responsibility Comparison

| Component            | Examples                         | On-Prem | IaaS | PaaS | SaaS |
|----------------------|----------------------------------|---------|------|------|------|
| Applications & Data  | Data + Apps                      | You     | You  | You  | CSP  |
| Runtime              | Docker                           | You     | You  | CSP  | CSP  |
| Middleware           | Additional Softwares             | You     | You  | CSP  | CSP  |
| Operating System     | Linux + Windows                  | You     | You  | CSP  | CSP  |
| Virtualization       | Virtual Machine                  | You     | CSP  | CSP  | CSP  |
| Servers              | Memory + Motherboard + CPU       | You     | CSP  | CSP  | CSP  |
| Networking           | Routers + Switch + Internet      | You     | CSP  | CSP  | CSP  |
| Storage              | HDD + SSD                        | You     | CSP  | CSP  | CSP  |

### On-premises

- You manage everything (Infrastructure, Platform & Software).

- Use case:

  - Private Enterprise
  - Government
  - University
  - A bank creating their private setup.

### SaaS (Software as a Service)

- Cloud Service Provider manages Software, Platform and Infrastructure.

  - Infrastructure: Storage, networking, hardware, virtulization
  - Platform: OS, middleware & runtime
  - Software: Data & application

- You do not manage anything. You will use the application.

- Use case:

  - AWS EC2
  - Azure's Virtual Machines

- Use case:

  - Google's Gmail, youtube etc
  - Microsoft office and their applications.

### PaaS (Platform as a Service)

- Cloud Service Provider manages Infrastructure & Platform

  - Infrastructure: Storage, networking, hardware and virtulization
  - Platform: OS, middleware & runtime

- You manage software.

  - Software: Data & application

- Use case:

  - AWS EC2
  - Azure's Virtual Machines

### IaaS (Infrastructure as a Service)

- Cloud provider manages Infrastructure.

  - Infrastructure: Networking, hardware, storage and virtualization

- You manage Platform and Software.

  - Platform: Os, middleware, runtime
  - Software: data & application

- Use Case:

  - Migration of workload
  - backup & recovery
  - test & development

## Cloud Deployment Models

| Model      | Cost   | Control | Security | Complexity | Real-World Examples |
|------------|--------|---------|----------|------------|--------------------|
| Public     | Low    | Low     | Medium   | Low        | AWS, Azure, Google Cloud |
| Private    | High   | High    | High     | High       | VMware-based internal data center |
| Hybrid     | Medium | Medium  | High     | High       | On-Prem + AWS integration |
| Community  | Medium | Medium  | Medium   | Medium     | Government shared cloud infrastructure |

### Public Cloud

- Pay-as-you-go approach where third-party (google, amazon) provides cloud services.
- Small business, startups, web-application uses Public cloud services.

### Private Cloud

- Dedicated cloud service for a single organization to use.
- Govenment, HealthCare, Large enterprises, financial institutions etc

### Hybrid Cloud

- Keeeps sensitive informations to Private cloud while using Public clouds for other tasks.

### Cross Cloud

- Using multiple public cloud providers simultaneously.
- Ex., Spotify uses Google cloud for Data analytics while AWS for infrastructure.

### Community Cloud

- Shared Infrastructure among organizations which shares similar requirements.
- Government agencies, research institutions, healthcare networks

# 03:12:40 Management and Developer Tools
