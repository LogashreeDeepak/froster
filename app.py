git commit --amend -m "Correct commit message"
git diff --staged / --cached - to see the staged changes
git restore --staged database.py - accidently staged the changes by git add database.py but u dont want it to be staged
git show <commitid> - This shows the commit information and its changes.
git rm old-config.yaml - remove files from the working directory and stages the deletion
git mv old-name.txt new-name.txt - rename /move File     
git Add -A - adition, modification and deletion accrosss the repository
git branch
git switch
git switch -c feature-login - create and switch to the new branch 
git branch -d - safe deletion
git branch -D - force deletion
branch naming conventions - feature/user-authentication, feature/payment-api,bugfix/login-error
hotfix/payment-production,release/v2.1.0
merge conflict - A conflict occurs when Git cannot automatically determine how to combine changes.
git merge --abort - Suppose you're in the middle of a complicated merge and decide you don't want to continue.
origin - when you clone a remote repo git normally givea the remote repo this name origin
git fetch - downloads the latest objects and references from the remote repository without merging those changes into my current local branch.
git pull - git fetch + git merge
