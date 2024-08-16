# Incident Postmortem: Website Downtime Due to Deployment and Configuration Issues

## Incident Summary:
**Date**: August 31, 2024
**Duration**: 3 hours 30 minutes (02:30 AM GMT - 06:00 AM GMT)

### Impact:
- Service Affected: Website
- User Experience: Slow responses and unavailability
- Percentage of Users Affected: 100%

### Root Cause:
- **Misconfigured Firewall**: A misconfigured firewall on the new servers, which rejected all incoming non-SSH traffic, including traffic from the load balancer.
- **Performance Bottleneck**: A performance bottleneck introduced by a new feature, which caused increased load and slowed responses from the existing servers.

## Timeline:
- 02:30 AM GMT: Issue detected via automated monitoring alerts indicating slow response times.
- 02:35 AM GMT: On-call technician verifies and confirms the alert by checking website performance and user reports.
- 02:45 AM GMT: On-call technician investigates server load and network connectivity, suspecting a DDoS attack, but finds normal behavior.
- 03:00 AM GMT: The issue is escalated to the DevOps team, who began investigating the load balancer and server configurations.
- 03:15 AM GMT: The team investigated a misleading path, suspecting a problem with the load balancer's SSL certificates, but found no issues.
- 03:30 AM GMT: Team investigates network infrastructure, identifies firewall misconfiguration on new servers as the root cause.
- 03:45 AM GMT: New feature deployment is reviewed, revealing a performance bottleneck contributing to the issue.
- 04:00 AM GMT: The team implemented a temporary fix by adding the load balancer's IP address to the firewall's whitelist, allowing traffic flow to new servers.
- 04:30 AM GMT: Decision made to rollback to previous stable code version.
- 04:45 AM GMT: Emergency rollback to a previous stable version initiated.
- 05:00 AM GMT: Website partially restored.
- 06:00 AM GMT: Website fully restored, and the incident was resolved.

## Root Cause and Resolution
### Root Cause Analysis
- **Primary Cause**: The firewall configuration fault on the new servers, which rejected all incoming non-SSH traffic, including web traffic from the load balancer.
- **Contributing Cause**: The new feature introduced a significant performance bottleneck, exhausting server resources.
- **Underlying Cause**: Inadequate testing and validation of the new deployment, including the firewall configuration and the new feature.

### Resolution
- **Initial Response**: The on-call technician attempted to restart the newer servers and adjust the load balancer to distribute traffic more evenly, but were unsuccessful.
- **Temporary Fix**: The team implemented a temporary fix by adding the load balancer's IP address to the firewall's whitelist, allowing traffic to flow to the new servers.
- **Mitigation**: The team rolled back the new deployment, disabled the problematic feature, and corrected the firewall rules to allow only necessary traffic from the load balancer.

## Corrective and Preventative Measures
### Preventive Measures
- **Improve Firewall Configuration and Testing**: Develop a more robust firewall configuration and testing process to prevent similar issues in the future.
- **Enhance Testing and Validation**: Increase testing and validation efforts for new features and deployments to detect performance bottlenecks and other issues before they reach production.
- **Implement Automated Rollbacks**: Develop a process for automated rollbacks in case of deployment failures to minimize downtime and impact.
- **Improve Monitoring and Alerting**: Enhance monitoring and alerting to detect issues like this earlier, reducing the time to detect and respond to incidents.

### Action Items
- [ ] Create a firewall configuration checklist including port rules, IP whitelisting, and service accounts.
- [ ] Enhance monitoring systems to detect configuration issues and server performance anomalies.
- [ ] Implement a mandatory code review process for all new features.
- [ ] Develop automated scripts for routine system checks and performance testing.
- [ ] Establish a dedicated rollback environment for testing and implementation.
