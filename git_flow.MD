# <span style="color:forestgreen">Git & GitHub Workflow</span>


*****
<span style="color:forestgreen; background-color:lightyellow">__<-- Back to [README](README.md#contact-and-collaboration)__</span>
*****


## Table of Contents

- [Git \& GitHub Workflow](#git--github-workflow)
          - [__\<-- Back to README__](#---back-to-readme)
  - [Table of Contents](#table-of-contents)
  - [In the Terminal](#in-the-terminal)
    - [Start with the latest main branch:](#start-with-the-latest-main-branch)
    - [Create a new branch (and switch to it):](#create-a-new-branch-and-switch-to-it)
    - [Make changes and work on the feature.](#make-changes-and-work-on-the-feature)
    - [Then add and commit the changes:](#then-add-and-commit-the-changes)
    - [Push the new branch to GitHub:](#push-the-new-branch-to-github)
  - [On GitHub:](#on-github)
    - [Open a Pull Request (PR) on GitHub:](#open-a-pull-request-pr-on-github)
  - [In the Terminal:](#in-the-terminal-1)
    - [Sync your local main after merging:](#sync-your-local-main-after-merging)
    - [Delete old branch (local):](#delete-old-branch-local)
    - [Delete old branch (remote):](#delete-old-branch-remote)
    - [Start a new feature:](#start-a-new-feature)
    - [Return to top and start again!](#return-to-top-and-start-again)
- [Additional Information](#additional-information)
    - [Staying in sync:](#staying-in-sync)
    - [Use descriptive branch names:](#use-descriptive-branch-names)

*****

## In the Terminal

### Start with the latest main branch:

`git checkout main`

`git pull origin main`

<br>

### Create a new branch (and switch to it):

`git checkout -b {branch}`

*****

    If you created a branch after deleting your last one, start with making your changes:

<br>

### Make changes and work on the feature.

Do whatever you want and need to do in this branch.

<br>

### Then add and commit the changes:

__Add__

`git add .`

  - You can also add by file name:
    - `git add {file name}`
    - `git add {file name} {file name} {file name}`

__Commit__

`git commit -m "{commit message}"`

  - Example:
    - `git commit -m "Implement results screen with value totals."`

<br>

### Push the new branch to GitHub:

`git push origin {branch}`

*******

## On GitHub:

### Open a Pull Request (PR) on GitHub:

- Go to your __[GitHub](https://github.com/dashboard)__ dashboard
  - _You may or may not need to navigate into the repository_
- Find the prompt "__Compare & pull request__"
- Open the PR into __main__ branch

- Add a good title and description

- Click "__Merge Pull Request__"

- After, click on the button to delete the branch (if available).

<span style="color:firebrick">** Please Note ** _If branch is deleted now, skip the __[Delete old branch (remote)](#delete-old-branch-remote)__ instruction._</span>


*******


## In the Terminal:

### Sync your local main after merging:
`git checkout main`

`git pull origin main`

<br>

### Delete old branch (local):

`git branch -d {branch}`

<br>

### Delete old branch (remote):

__<span style="color:firebrick">** Please Note **</span>__

_<span style="color:firebrick">Branch may be auto or manually deleted after merging pull request on GitHub. If you deleted on GitHub, please skip this instruction.</span>_ 

`git push origin --delete {branch}`

<br>

*** START HERE NEXT TIME ***
### Start a new feature:

`git checkout -b {next_branch}`

<br>

### <span style="color:firebrick">Return to __[Make changes and work on the feature](#make-changes-and-work-on-the-feature)__ and start working on your new branch!</span>

*****

## Additional Information

### Staying in sync:

- If you switch between branches often, sync with main:
  - `git fetch origin`
  - `git pull origin main`
<br>
- You can update your current branch with the latest main (Before a PR):
  - `git merge main`

<br>

### Use descriptive branch names:

- Good:
  - add-export-button
  - fix-overlapping-layout
  - refactor-results-logic

- Bad:
  - stuff
  - test
  - X