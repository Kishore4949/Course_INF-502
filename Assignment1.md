**On your local machine:** Using the command line, find and access the "handson/" directory (if you didn't download and unzip the file, go back to the beginning of Part 1's instructions). Then, answer the following questions (on your *Assigment1.md* file):

1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.
```
There are two branches in the repository they are :
master and math

commits in Master Branch are:
commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)
     
commits in math branch are:
commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)


```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
 git log --graph --all
 commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)
       
here we can see some commits which are made on Aug 14 
first commit message is "Creating all files (all empty)
In second commit Author added a draft A.py 
In Third Commit Head is pointed to math and Author is added some more knowledge to the function
In fourth commit Author Added small changes in master branch 

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
the difference between master and math branch is shown below:

diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.

We can see clearly above that, in A.py(math branch) if-else loop are present in function(calculate_this) whereas there is no if statement in A.py(master branch)
the other difference is: there is a comment line in B.py (master branch) whereas B.py (math branch) is empty.


```

4. Write a command sequence to merge the non-master branch into `master`.

```
for merging non-master branch in Master, intial step is we need to point head to the master branch and we need to use below command to merge the non master branch into master branch
git merge math

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
(i) git branch math
(ii) git checkout math --> Now Head will point to math branch 

```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes.
```
git commit -a -m "two lines of code is added to math branch"

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
command: git merge math
Automatic merge is failed, it says merge conflict in B.py fix conflicts and commit the results    


```
   
10. Write a set of commands to abort the merge.
```
command: git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
command: git merge math

in B.py it shows like:
<<<<<<< HEAD
# Another file that will receive a line of code... at least.
=======
print 'I know math, look:'
print 2+2
>>>>>>> math

Here I am just deleting some lines in B.py, manualy editing and commiting changes to master branch.

I used git commit -a -m "merged successfully" to commit the changes that I made.

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
command is "git merge math" and Now master is branch is upto date.

```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
I used none of the commands. I directly edited a file in a remote repository.
After editing a file, there will be a commit changes option at the bottom of the file; I chose that, then I went directly to the pull request option.
After clicking the new pull request option,it shows a list of the files you modified will appear; select the file you want to submit a pull request for,
and it will be accomplished.

```
