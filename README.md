# 🧩 Factory Method Pattern in Python
This project implements the Factory Method design pattern in Python, demonstrating how to create objects of various game types (Chess, Solitaire) without tightly coupling the client code to concrete classes.

## 🚀 Objective
To apply the Factory Method pattern to:
* Create games in a flexible and decoupled manner.
* Incorporate new functionalities (e.g., new game types) without modifying existing client code.
* Practice good Git workflow (branching, Pull Requests, rebase, merges, logging).

## 🏗️ Project Structure

factory_method/
  * audit/   | Module for logging functionality
      * Logger.py
  * client/  | Main client (entry point)
      * FactoryMethodClient.py
  * factory/ | Base and concrete Factory classes
      * Board.py
      * ChessBoard.py
      * SolitaireBoard.py
  * products/ | Product classes (specific game types)
      * ChessGame.py
      * Game.py
      * SolitaireGame.py
  * README.md

## 🧠 Core Features
    
| Feature | Description |  
| :--- | :--- |  
| Dynamic Game Creation | Instances are created without the client knowing the concrete class (Factory Method implementation). |  
| Game Types Supported | Supports ChessGame, SolitaireGame |  
| Configurable Difficulty | Allows selection between easy, normal, and hard difficulties. | 
| Timer/Duration Tracking | Records game duration and move counts. | 
| Logger Integration | Logs activity and results to audit/factory_logs.txt. | 

## 🧰 Technologies and Standards
* Python 3.10+
* Factory Method Design Pattern
* PEP8 (Code conventions)
* File handling (os, datetime modules)
* Git and GitHub (Professional branching and PR workflow)
---

## 🔀 Git Development Workflow
 |No.|Command/Action|Action/Description |
| :--- | :--- |:--- |
|1|Git checkout main|Switch to the main branch (the stable branch of the project).|
|2|Git fetch --prune|Download changes from the remote repository and remove local references to branches that no longer exist on the remote.|
|3|Git pull --rebase origin main|Synchronize the local main branch with the remote, downloading the latest changes and rebase local commits, if any, to maintain a clean, linear history.|
|4|Git status|Show the status of the working tree and the staging area (modified, added files, etc.).|
|5|Git checkout -b nueva-rama|Create a new branch called nueva-rama (new-branch) and switch to it immediately.|
|**6**|**Code**|**Perform changes, implement new features, or fix bugs in the files.**|
|7|Git add .|Add all modified and new files in the current working directory to the staging area for the next commit.|
|8|Git commit -m Message|Save the changes from the staging area to the history of the current branch with a descriptive message.|
|9|Git pull --rebase origin main|Update the working branch (nueva-rama) with the latest changes from main before pushing, using rebase so that your own commits come after main's commits.|
|10|Git push origin nueva-rama|Upload the local nueva-rama branch and all its commits to the remote repository.|
|**11**|**Create Pull Request**|**Formally request the merge of nueva-rama into main through the repository interface (GitHub, GitLab, etc.).**|
|12|Git branch|Verify that you are on the newly created branch.|
|13|Git status|Check the status of the branch.|
|14|Git pull --rebase origin main|Update the working branch with the latest changes from main (in case main was updated while waiting for approval).|
|**15**|**Pull Request approved**|**The PR has been approved and the merge of nueva-rama into main has been performed on the remote repository. The new branch is also deleted from the remote repository.**|
|16|Git checkout main|Return to the main branch to synchronize.|
|17|Git branch|Verify the branches.|
|18|Git status|Check the status of the branch.|
|19|Git fetch --prune|Update the list of remote branches and remove the local reference to nueva-rama if it was deleted on the remote after the merge.|
|20|Git pull --rebase origin main|Download the merge commit (or the rebased commits) that was performed on the remote.|
|21|Git status|Verify that the working tree is clean.|
|22|Git branch -d nueva-rama|Delete the nueva-rama branch locally (this only works if the branch has already been merged).|







## 🧱 Applied Design Principles
* __Factory Method:__ Creates objects without exposing the instantiation logic to the client.
* __Single Responsability Principle (SRP):__ Each module and class has a clear, defined responsibility.
* __Open/Closed Principle (OCP):__ The system is open for extension (new game types) but closed for modification (client code remains unchanged).
---

Educational and practical project demonstrating clean architecture and design patterns in Python.


















