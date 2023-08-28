# Introduction to GitHub and Version Control – the WorldFAIR cookbook worked example

About this tutorial:
Topics: Github, version control
Learning outcomes: After working through this tutorial you should understand:
-	The key concepts of version control
-	How to work with an existing code repository
-	How to contribute code to the WorldFAIR repository. 
Whether you're a software developer or an organic chemist, version control can be a really useful tool for organising, storing and documenting your work, whether this is on a collaborative project or working on your own. This tutorial will introduce the world of version control and the widely-used platform GitHub, through a worked example of the WorldFAIR cookbook. 
Examples in this tutorial use the windows GitHub desktop app, although it is possible to work with GitHub on other operating systems, directly through the command line, or through some code editing programs. 

## What is Version Control?
Version control is a system that tracks changes made to files over time. It allows multiple people to collaborate on a project simultaneously, keeping track of who made what changes and when. Additionally, it maintains a history of changes, making it easy to revert to previous versions if needed. An element of version control is now included in many products such as google docs, dropbox or Microsoft office, where you can see version history of a document or track changes that are made in a document. There are multiple different complete version control systems (VCS), in this tutorial we will only be working with GitHub.

## Key Benefits of Version Control
1.	**History Tracking:** Every change is tracked, allowing you to see who made the change and why.
2.	**Collaboration:** Multiple developers can work on the same project simultaneously without conflicts while working. 
3.	**Branching:** Create separate branches to work on new features or fixes without affecting the main codebase.
4.	**Backup and Recovery:** Easily revert to a previous working version in case of errors or issues.

## Introducing GitHub
GitHub is a web-based platform built around the concept of version control using Git, a distributed version control system. It provides a user-friendly interface for managing repositories (collections of files and their history) and collaborating with others. It's particularly popular among developers for hosting their code repositories and collaborating with others but can be used by anyone. We will work through an example using the WorldFAIR cookbook repository, but if you want more information about GitHub then check out their [GitHub Docs](https://docs.github.com/en) and [learning resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources).

### Key GitHub Concepts:
1.	**Repository (Repo)**: This is where your project lives, it contains code, other files, folders, and their history. Repositories can be public (visible to everyone) or private (restricted access).
2.	**Clone**: Creating a copy of a repository on your local machine is called "cloning". This allows you to work on the code locally and then sync your changes back to the GitHub repository.
3.	**Branch**: A branch is a separate line in the repository. It allows you to work on features or fixes without affecting the main codebase. The "main" branch typically represents the stable version of the project, and other branches can be used for development.
4.	**Fork**: Forking a repository creates a copy of the repository in your GitHub account. It allows you to experiment with changes without affecting the original project.
5.	**Commit**: A commit is a saved change to your project's files. Each commit has a unique identifier and is accompanied by a message describing the changes. A commit can include edits to more than one file. 
6.	**Pull Request (PR)**: When you've made changes in a branch and want to merge them into the main codebase, you create a pull request. Others can review the changes before merging.
7.	**Merge**: Merging combines changes from one branch into another. Pull requests are often merged after review.
8.	**Markdown**: Markdown is a simple text formatting language used to style documents and web content. It uses symbols (such as '#'. '*', '-') for basic formatting of text. 

![A GitHub flow diagram showing the process of making a branch from a repoistory](/book/images/github-flow.png)

## GitHub Worked Example:
1.	**Create a GitHub Account:** 
First, you need to create a GitHub account (or log in if you already have an account). Go to https://github.com and click on the "Sign Up" button. Follow the steps to create your account, choose a username, and set a strong password. Once you have completed the sign-up process, you will have your own GitHub profile.
2.	**Find Repositories:** You can browse public repositories to see how projects are organized and structured, many public repositories will also allow contributions to be made to them. If the repository you want to work on is private you will need to be invited to join it. In this example we will be looking at the public WorldFAIR cookbook repository https://github.com/IUPAC/WFChemCookbook
-	When you open the repo you will see the structure of the files / folders in the repo and a README file for the repo (if present) which should explain a bit about the project and how to work with it. 
-	You can navigate through the files to see the content present in the cookbook repository. Many of the files are .md which is the Markdown format. 
-	The Cookbook website is the best place to interact with the actual content, but if you want to contribute to the content or suggest an edit then this would be done through GitHub. Note: if you aren’t confident with GitHub / markdown but want to highlight an issue then you can submit an issue to the repository. 

![A screenshot of the WFChemCookbook GitHub repository](../images/github-repo.png)

