# CI-CD_Piplines

### Why Do We Need a CI/CD Pipeline?

- **Modern software delivery** involves:
    
    - Code writing
        
    - Testing
        
    - Building
        
    - Deployment
        
    - Repeated again and again (cycle)
        
- Doing this **manually** is:
    
    - Slow
        
    - Error-prone
        
    - Inconsistent
        
- Solution → **Automation using CI/CD tools**

---

## Structure
![](a.png)

---

### Putting it All Together (The CI/CD Loop)


`Idea → Write Code → Push to GitHub → Jenkins gets triggered →  Run tests → Build Docker Image → Deploy → Monitor → Repeat`

---

This is part of the **Software Development Life Cycle (SDLC)**:

- A circular flow where:
    
    - New features are added
        
    - Code is improved or debugged
        
    - New tests are run
        
    - New versions are deployed
 
---

### Automation Best Practice

- **If you do it often** → Automate it.
    
- **If it’s one-time setup** → Manual is okay.
    
    - Example: Installing `pytest` once manually is fine.
 
---

### What Is a Jenkins Trigger?

- **Trigger**: An automated condition to run a Jenkins job **without manual click**.
    
- Allows jobs to be executed:
    
    - On a schedule (like a cron job)
        
    - On a GitHub push
        
    - When another job completes
        
    - On build failure or success
        
- Purpose: **Pure automation**.

You know the flow of:

`GitHub → Jenkins → Test → Build → Deploy`

---

### Final CI/CD Pipeline Summary

#### Full Flow:


`Developer writes code → Pushes to GitHub → Jenkins detects change (trigger) → Pulls code → Runs tests (pytest) → Builds Docker image → (Optional) Push to Docker Hub → Deploys container → Pipeline complete`

