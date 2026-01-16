---
title: "Why Version Control Exists: The Pendrive Problem"
slug: why-version-control-exists-the-pendrive-problem
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1768582537095/50199d09-1f0c-44ed-b908-77fcc7dbac01.png

---

## Introduction: The “Dark Ages” of Coding

Imagine this: It’s 2:00 AM. You and two friends are working on your final year project. You just finished a critical feature. You zip the folder, name it `Project_Final_v1`, copy it to a pendrive, and hand it to your friend, Rahul.

"Don't change the database file!" you warn him.

Three hours later, Rahul hands the drive back. You plug it in, copy the files to your laptop, and hit run.

**CRASH**

Your code is broken. The database file was overwritten. And worst of all? You have no idea *what* Rahul changed, and your previous working version is gone forever because you pasted over it.

Before tools like Git and GitHub existed, this wasn't just a nightmare—it was the standard workflow.

In this article, we’re going to explore **why** Version Control Systems (VCS) exist, using the "Pendrive Analogy" to understand the chaos developers faced before the modern era.

## The Pendrive Analogy: How We Used to Struggle

Before we had sophisticated tools, "version control" was entirely manual. It relied on human memory, strict discipline, and a lot of luck.

### The "Folder" Strategy

If you looked at a developer's desktop in 2005 (or a student's desktop today who hasn't learned Git), you’d see this:

```javascript
/My_Project
    ├── code.py
    ├── code_backup.py
    ├── code_final.py
    ├── code_final_v2.py
    └── code_final_REALLY_FINAL_DO_NOT_TOUCH.py
```

### The Collaboration Chaos

When working in a team, the "Pendrive Workflow" looked like this:

1. **Dev A** writes code on their machine.
    
2. **Dev A** copies code to a pendrive.
    
3. **Dev A** physically walks to **Dev B** and gives them the pendrive.
    
4. **Dev B** copies the code, edits it, and hopes they didn't overwrite Dev A's latest bug fix.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768573249487/c271df6f-8c48-4a3b-930c-e772e3e531eb.png align="center")

Diagram 1: The Pendrive Bottleneck

so we can analyze from the above diagram, that how developer A is completely blocked while the pendrive is in transit. This highlights the fatal flaw of the ‘Pendrive Workflow’: it creates a single point of failure.

## The 3 Major Problems Before VCS

This manual approach led to three devasting problem that plagued the software industry.

1. The "Overwriting" Disaster
    
    Considering the pendrive era, code didn’t vanish magically—it was overwritten. Each developer worked on their own local copy of the same file, made changes independently, and later copied the file back to the shared pendrive or folder.
    
    When the second developer copied their version, the system simply replaced the existing file because it only recognized the filename, not the changes inside it. Since there was no merge, no warning, and no history, the first developer’s work was silently erased. To the team, it felt like the code “disappeared,” but in reality, it was blindly overwritten by another valid change.
    
2. No History(The “Ctrl+Z” Limit)
    
    we know that when we save a file and close the editor, our “Undo” history gone. if we realized that the code we wrote last week was actually better than the code we wrote today, there is no option of going back and retrieving back , either we have to make backup of the file locally by putting names “back\_up\_version1\_on\_some\_date” in some backup folder , again searching about the changes in backup folder is very cumbersome. it may work in some small project ,but on large team or working on complex/big project and retrieving the backup is very hard.
    
3. The “Blame Game”(Lack of Accountability).
    
    In this pendrive world, When the application crashed, nobody knew who wrote the bad code , and sometime teammates start fighting with each other and saying that “I didn’t touch that function” , or “well, it was working fine before you took the pendrive !! “.
    
    So here, there was no log, no author signature, and no timestamps.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768579388875/425cc970-ac84-4e32-b0db-43e21dc3bb79.png align="center")

Diagram 2 : The Silent Overwrite

## The Origin Story: How Linus Torvalds Created Git

If managing a 3-person college project is hard without tools, imagine managing the **Linux Kernel**—an open-source project with thousands of contributors and millions of lines of code.

The “BitKeeper” Crisis (2005)

For a long time, the Linux community used a proprietary tool called *BitKeeper*. It was powerful, but it wasn't open source. In 2005, the relationship between the Linux community and BitKeeper fell apart, and the free license was revoked. The Linux community was suddenly left without a collaboration tool.

“I’II Do it Myself”

**Linus Torvalds**, the creator of Linux, needed a replacement immediately. He looked at existing options (like CVS or Subversion) and hated them. He felt they were too slow and centralized.

So what he did , he disapperard for a weekend(literally about 10 days to a working prototype) and wrote his own. He named it Git.

What Makes Git Different ?

Git was designed with a clear philosophy: it had to be distributed so every developer owned the full project history, fast enough to handle Linux kernel development, and secure through cryptographic hashing to guarantee data integrity.

As Linus later joked, “I’m an egotistical bastard, and I name all my projects after myself. First Linux, now Git”—with “git” being British slang for an unpleasant person.

## Version Control System : The Time Machine

We can think VCS not as “backup tool” , but as a Time Machine for our project. It records changes to a file or set of files over time so that we can recall specific versions later.

### Difference between Old way (Pendrive) vs New way (VCS/Git)

| Old Way (Pendrive) | New Way (VCS/Git) |
| --- | --- |
| Overwriting: Last one to save wins | **Merging:** The system detects conflicts and asks us to combine both changes intelligently. |
| History: final\_v2.zip (saved in file) | Log: A detailed history of every character changed, who changed it, and why. |
| Fear: Scared to delete code in case we need it | Confidence: Delete anything. we can always revert to yesterday’s state. |

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768581947221/476120e9-cd03-443f-8b59-5e462327bbf7.png align="center")

Diagram 3:The Parallel Workflow (Branching & Merging)

You can see in the above diagram, how two features(Login and Payment) were built separately and then combined. No pendrives required.

## Conclusion: Why This Matters for Your Career

If you are a student aiming for industry placements or building "Proof of Work" projects, using Version Control isn't optional—it is mandatory.

It is the difference between an amateur hobbyist and a professional engineer. It allows teams of hundreds of developers to work on massive codebases (like Facebook or Google) without stepping on each other's toes