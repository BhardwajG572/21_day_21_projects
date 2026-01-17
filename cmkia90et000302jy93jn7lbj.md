---
title: "Inside Git: How It Works and the Role of the .git Folder"
datePublished: Sat Jan 17 2026 12:27:44 GMT+0000 (Coordinated Universal Time)
cuid: cmkia90et000302jy93jn7lbj
slug: inside-git-how-it-works-and-the-role-of-the-git-folder
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1768651691794/4a35b123-d6f1-4ffc-bdda-2476220f83b5.png
tags: blogging, git, beginners, chaiaurcode, chaicode

---

Well, we know that Git is the most important thing in the journey of any developer. We often use commands such as `git init`, `git add .`, `git add <file name>`, `git commit`, and `git push`, right? And yes, our tasks are completed properly.

Have we ever wondered how these things actually happen? In the current working directory, a hidden folder is created when we initialize Git (using the command `git init`). In this hidden file (.git folder), all the operations occur. It seems like a black box, but if we go inside and examine it, it won’t be surprising.

Most of us treat Git like a black box. We put files in, and it usually saves them. But I thought to look inside that black box (wanted to see under the hood).

So if we open the .git folder and spend some time with it, we’ll see it is not magic; in fact, it is a simple database. And honestly, once we see how it works, it stops being scary.

If we delete our code or files but keep the .git folder intact, we can get everything back. If we delete the .git folder, well, we just have a regular folder with no history.

Inside the .git folder, we have:

```powershell
.git/
├── objects/    <-- The Hard Disk (Where data lives)
├── refs/       <-- The Bookmarks (Tags & Branches)
├── HEAD        <-- The "we Are Here" sign
└── index       <-- The Staging Area
```

Let’s crack open the objects folder, because that’s where the cool stuff is.

## The Big Three: Blob, Tree, and Commit

Git uses a fancy term called "content-addressed filesystem." All that means is: **Git doesn't care about filenames; it cares about content.**

Inside that `objects` folder, Git stores three main things. Each one gets a unique ID (a long string of numbers and letters called a "hash").

Here is the mental model we need:

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768649156608/092109ab-8954-4b58-853c-770018db1f8b.png align="center")

1. The Blob:
    
    When we give Git a file, it removes the filename. It just takes the file content, compresses it, and saves it.
    
    Think of it like this: we write a letter, discard the envelope, and keep the sheet of paper. (Blob = just the text/data/content)
    
2. The Tree:
    
    A blob has data but no name. That's not helpful if we want to organize a project. So, Git uses a tree. A tree is simply a list that says, "Hey, the file named `app.js` matches the data in Blob XYZ."
    
    Think of it like this: a table of contents (Tree = folder structure)
    
3. The Commit:
    
    This is the part we all know, but a commit doesn't actually store our files. It's just a wrapper. It stores a pointer to the main tree (our root folder), plus some info like who we are, what time it is, and a note about what we changed.
    
    Think of it like this: a Polaroid photo with a date and a caption written on the back. (Commit = Snapshot of the Tree)
    

## Watching it Happen

So let's see practically what happens when we add a file to Git.

Step 1: The git add moment

I made a file called `a.txt` and typed "hello git" inside. Then I ran:

```powershell
git add a.txt
```

I used to think this just "marked" the file. **Wrong.** Git actually took the text "hello git," turned it into a Blob, and saved it in the `.git/objects` folder immediately.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768649967646/92343638-9fa3-4e89-90af-1b45f47e277f.png align="center")

I checked the folder myself, and boom—there was a new file with a weird hash name. When I opened it, it said "hello git." **Mind-blown:** Git saves your data *before* you even commit.

Step 2: The git commit Moment

```powershell
git commit -m "first commit"
```

Basically Git did three things internally , it created a Tree to link the name a.txt to that Blob , it also created a Commit object pointing to that Tree, it moved the HEAD pointer to this new commit.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768650217284/a966ad42-f493-497a-9235-d241b20eb4f0.png align="center")

We can see the strange numbers (Hashes).

We might wonder, “Why use these long, strange strings like 9f4d96…?” Well, Git doesn’t trust filenames; it trusts math. If I change even one letter in my file, the content changes. If the content changes, the hash ID changes.

* New content = New Blob ID.
    
* New Blob = New Tree ID.
    
* New Tree = New Commit ID.
    

This is why Git is so reliable. We can't accidentally change history without the IDs changing.

How does Git know where we are (HEAD)?

Finally, how does Git know which branch we are on?

I opened the `.git/HEAD` file. It's very small. It simply says: `ref: refs/heads/main`.

If we check `refs/heads/main`, it's just a text file with the **Commit ID** of the latest commit.

* **Branch:** It's like a sticky note with a Commit ID written on it.
    
* **HEAD:** It's a pointer that says, "This is the sticky note I'm looking at right now."
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1768650540591/0e9aaba2-dd50-4e9e-b64b-33c4afef452f.png align="center")

When we switch branches with, we aren't moving files; we're just pointing HEAD to a different sticky note. Git sees that and updates our files to match.

Let's summarize what we've learned. Initially, it seemed like a black box, but now we understand it as a simple graph.

* Blobs hold data.
    
* Trees hold a folder structure.
    
* Commits hold history.
    
* Refs hold our place.
    

Git is not just a version control tool — it's a content-addressed database that happens to track code. Once we see this, Git stops being magic and starts being logic.