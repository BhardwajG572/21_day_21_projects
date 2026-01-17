---
title: "Git for Beginners: Basics and Essential Commands"
datePublished: Sat Jan 17 2026 14:57:44 GMT+0000 (Coordinated Universal Time)
cuid: cmkiflwpz000w02l5b1g5fzdj
slug: git-for-beginners-basics-and-essential-commands
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/KPAQpJYzH0Y/upload/cfa54042f0f317cdbcdcc97fd2a869ab.jpeg
tags: blogging, beginners, gitcommands, hiteshchaudhary, chaiaurcode, chaicode, chaicohort, piyushgarag

---

## **1\. Introduction**

Have you ever made a big change or struggled to remember what you changed last week? That’s where Git comes in.

**Git** is a distributed version control system that helps developers track changes in their code and collaborate efficiently. A key benefit is that every developer keeps a full copy of the project history. This decentralization ensures code recovery even if the central server crashes.

With Git, we can undo mistakes, work offline, and merge our work with teammates smoothly.

In this blog, we’ll cover the basics of Git and go through the essential commands every beginner should know.

Unlike traditional systems, every developer has a full copy of the project history. This means your code is safe even if a central server crashes.

**Why do we use Git?**

Git is used because it allows us to:

* Track every change made to the code
    
* Revert mistakes safely
    
* Work in teams without overwriting each other’s work
    
* Experiment with new features without breaking stable code
    
* Maintain a complete project history
    

## **2\. Core Git Terminologies**

So  let’s first understand the  Basics of Git and the Core Terminologies

* **Working Directory:** Folder of our computer where we are currently writing code and making changes(our active workspace)
    
* **Repository (repo):** The project folder that Git tracks.
    
* **Commit:** A specific snapshot of our code at a given moment.
    
* **Branch:** A parallel line used for development.
    
* **HEAD:** A pointer that indicates our current location in history. We can think of it like the “where am i right now on the map”.
    
* \*\*Staging area (index):\*\*Area where changes are prepared before committing
    

Now that we understand the terminology, let’s look at the actual workflow. The diagram below visualizes how our code moves through these stages using specific Git commands.

## **3\. The Git Workflow**

***Working Directory → Staging Area → Local Repository → Remote Repository/(GitHub)***

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768500832630/16b02464-aebd-4090-85af-2b9614b36261.png align="center")

*Figure 1: The Git Workflow Lifecycle*

So let's understand how this workflow happens. Initially, we are in the working directory (the place where we are writing our code/project folder). To save the files in Git, we first have to add those files. Using `git add <file name>`, we can add the file that we want to save. If we have many files and want to add them all, we can use `git add .`.

When we add the files, they all reach the staging area (it's like a rocket ready for launch). When we commit at stage 3, we put the files into the .git folder (local repository) at stage 4.

Finally, we push into the cloud/server, such as GitHub, at stage 5, so that other people can also see my code and pull it to their personal computers.

## **4\. Essential Git Commands for Beginners**

### 4.1 . Install Git (Just a Link)

Link to download:  [https://git-scm.com/downloads](https://git-scm.com/downloads) ( Pick OS and then follow the setup)

### 4.2 . Configure Git Identity

Input

```plaintext
git config --global user.name "Your_Name"
git config --global user.email "your@mail.com"
```

For example: just replace "Your\_Name" with gaurav and "your@mail.com" with gaurav@abc.com.

We can verify if the above code snippet is configured properly or not.

```plaintext
git config --list
```

**Output**

```plaintext
user.name = gaurav
user.email = gaurav@abc.com
```

### 4.3. Initialize a Repository

Suppose we have to create a project and then want to put the folder into git.

**Input**

```plaintext
mkdir my_project
cd my_project
git init
```

**Output**

```plaintext
Initialized empty Git repository in 
/path/to/my_project/.git/
```

The above code snippet creates a .git folder (our local repository) in our folder.

### 4.4. Create our First File and Track it

**Input**

```plaintext
echo "# My Project" > README.md
git status
```

Using git status, we can see that the file is untracked; we need to add it to staging.

We can see the output of git status below :

**Output**

```plaintext
On branch master

No commits yet

Untracked files:
  (use "git add <file> . . ." to include in what
will be committed)
        README.md
```

```plaintext
git add README.md
```

To stage multiple files, use the following code: ( “. “ means everything in the current directory)

```plaintext
git add .
```

### 4.5. Commit Changes

**Input**

```plaintext
git commit -m "Initial commit: added README"
```

**Output**

```plaintext
[master (root-commit) a1b2c3d] Initial commit:
added README
1 file changed, 1 insertion(+)
create mode 100644 README.md
```

Now our file is officially saved in Git History. Use:

**Input**

```plaintext
git log
```

**Output**

```plaintext
commit a1b2c3d4e5f6g7h8
Author: gaurav<Gaurav@abc.com>
Date:
Inital commit: added README
```

It displays the history of commits.

### 4.6. Check Status and Differences

**Input**

```plaintext
git status  # shows what's staged/unstaged/untracked
git diff    # Shows what's changed but not yet staged
git diff --staged  # shows changes that are staged
```

**Output**

```plaintext
diff --git a/README.md b/README.md
index e69de29 ..3b18313 100644
--- a/README.md
+++ b/README.md
@@ -0,0 +1 @@
+# My Project
```

We can see above exactly what changed, line by line.

### 4.7. Connect to GitHub

We can establish a connection between a local repository and a remote repository, such as one hosted on GitHub or another cloud service.

We must ensure that we are within the Project Folder.

**Input**

```plaintext
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -U origin main
```

**Output**

```plaintext
enumerating objects: 3, done.
Counting objects: 100% (3/3) , done.
Writing objects: 100% (3/3) , done.
Branch 'main' set up to track remote branch
 'main' from 'origin' .
```

Now our Project is live on GitHub.

## **5.** Branching and Merging in Git

### 5.1 The Problem: Breaking Stable Code

Suppose we are working on a project, and everything is running perfectly. The code is stable, and we’ve already pushed it to GitHub. Now our manager asks me to add a new feature.

I start working on it directly in the project, but unfortunately, halfway through, things break.  The feature is incomplete, the test fails, and suddenly our working code(stable code) is no longer reliable.

At this point, our main project is messy — and the feature isn’t even finished.

### 5.2 Why This is a Problem

Ideally, we want our main codebase to remain stable at all times. And we want the freedom to experiment, try new ideas, and break things without fear.

So we need a way to do this safely without touching the stable version of the code.

### 5.3 The Solution: Git Branches

This is where Git branches come into action.

**5.3.1 What is a Branch?**

A **branch** is a separate line of development created from the main codebase. The main branch holds code that is stable and ready for production, whereas a feature branch is used for experimentation and developing new features.

Changes made inside a branch remain isolated and do not impact the main branch until you explicitly choose to merge them.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768581947221/476120e9-cd03-443f-8b59-5e462327bbf7.png align="center")

*Diagram 2: Visualizing Branching in Git*

This diagram shows how multiple features can be developed in parallel without disturbing the main branch.  
Once a feature is completed and tested, it is safely merged back into the main branch.

**5.3.2 Why do we need merging?**

Once you finish working on your feature (and whatever experiments you want to do) and everything looks good, you will want to bring those changes back into the main branch. This process is called merging.

Merging in Git serves the following key purposes:

* **Integrates Changes:** It combines modifications from a source branch into a target branch.
    
* **Maintains History:** It helps keep the project's history clean and well-structured.
    
* **Ensures Quality:** It guarantees that only finished and tested work is incorporated into the main codebase.
    

In summary, we can say **Branching** acts as a safety net for isolated work—such as experimenting or developing new features—while **Merging** is the process through which completed work is integrated into the main codebase.

### **5.4 Working with Branches: Commands and Outputs**

**5.4.1. Check Current Branch**

**Input**

```plaintext
git branch
```

**Output**

```plaintext
* main
```

The \* indicates the **current branch**. We can see that we are on the main branch.

**5.4.2. Create a New Branch**

Now we create a new branch where we will work on a feature safely.

As discussed earlier, we are creating a separate line of development without changing the main branch.

**Input**

```plaintext
git branch feature-login
```

Git creates the branch but we are still on the main branch. The new branch exists, but it is not active yet.

**5.4.3. Switch to the New Branch**

Next, we move into the newly created branch.

We are switching our working context from main to feature-login.

**Input**

```plaintext
git checkout feature-login
```

**Output**

```plaintext
Switched to branch 'feature-login'
```

From now on, any changes we make will be saved in the **feature-login** branch instead of **main**.

**5.4.4. Confirm the Active Branch**

We are double-checking that we are on the correct branch.

We are verifying that Git is pointing to the new branch.

**Input**

```plaintext
git branch
```

**Output**

```plaintext
* feature-login
main
```

The \* now appears next to feature-login, confirming that this branch is active.\*

**5.4.5: Make Changes on the Branch**

Now we make a small change to simulate working on a feature, so we modify a file while staying inside the feature branch.

**Input**

```plaintext
echo "Login feature added" >> README.md
```

We can check the status using git status (that we have discussed earlier)

**Input**

```plaintext
git status
```

**Output**

```plaintext
On branch feature-login
Changes not staged for commit:
    modified: README.md
```

Git detects that the file has changed, but the change is not yet staged or committed.

**5.4.6. Stage and Commit the Changes**

As discussed earlier, we are preparing the file for commit and then creating a snapshot of the changes.

**Input**

```plaintext
git add README.md
git commit -m "Added login feature description"
```

**Output**

```plaintext
[feature-login a7b8c9d] Added login feature
description
1 file changed, 1 insertion(+)
```

This commit is stored **only in the feature-login branch**. The main branch remains unchanged.

**5.4.7 Switch Back to the Main Branch**

Once the feature is complete, we return to the main branch (we are moving back to the stable version of the project)

**Input**

```plaintext
git checkout main
```

At this point, the changes made in feature-login are not yet part of the main branch.

**Output**

```plaintext
Switched to branch 'main'
```

**5.4.8. Merge the Feature Branch into Main**

Now we combine the completed feature with the main codebase We are integrating changes from **feature-login** into **main**.

```plaintext
git merge feature-login
```

**Output**

```plaintext
Updating a1b2c3d....a7b89d
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

So what we did was simply move the main branch forward to include the new commit.

**5.4.9. Verify the Merge.**

In this step, we can check the commit history after merging and confirm that the branch changes are now part of the main branch.

**Input**

```plaintext
git log --oneline
```

**Output**

```plaintext
a7b8c9d Added login feature description
a1b2c3d Initial commit: added README
```

The commit from feature-login is now visible in the main branch history.

**5.4.10. Delete the Feature Branch**

This is the optional step. After merging, the branch is no longer needed, so we can clean up by deleting the branch locally.

**Input**

```plaintext
git branch -d feature-login
```

**Output**

```plaintext
Deleted branch feature-login (earlier a7b8c9d)
```

The output above shows that the branch has been removed.

With this workflow, we can safely develop new features without risking the stability of our main codebase. By using branches, we keep our work separate, and by merging, we only add tested and completed changes.

This branching strategy is a key part of professional Git workflows and is used in nearly every real-world project.

## 6\. Conclusion

By now, we have a clear understanding of how Git helps us track changes, collaborate efficiently, and work safely using branches.

These core Git concepts—committing, branching, and merging—are the foundation of almost every professional development workflow. Once we’re comfortable with them, using Git in real-world projects becomes much more intuitive.