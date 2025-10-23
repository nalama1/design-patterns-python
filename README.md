# Factory Method Pattern in Python
This project implements the Factory Method design pattern in Python, demonstrating how to create objects of various game types (Chess, Solitaire) without tightly coupling the client code to concrete classes.

<img width="848" height="638" alt="image" src="https://github.com/user-attachments/assets/7af07b76-6caf-43d4-bdb3-37e984073cdb" />

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

### Factory Method Pattern
| To clearly represent the Factory Method pattern with the following classes:									|
| :--- |
|  🧍‍♂️ Client (FactoryMethodClient)|                                                                          |
|  🧱 Abstract factory (Board)|                                                                               |
|  🧩 Concrete factories (ChessBoard, SolitaireBoard)                                                         |
|  🎮 Abstract product (Game)                                                                                 |
|  🕹 Concrete products (ChessGame, SolitaireGame)                                                            |
|                                                                                                               |
|   |
|  💡 **How to interpret it:**                                                                                    |
|  🧱 **Board** is abstract → it defines the create_game() method but does not implement it.                         |
|  🧩 **ChessBoard** and **SolitaireBoard** are concrete factories, which return instances of ChessGame or SolitaireGame.|
|  🎮 **Game** is the abstract base class for all games.|
|  🧍‍♂️ **FactoryMethodClient** represents the client that initiates the entire process.|
|     **ILogger** is an interface for logging (implemented by Logger).|

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

## 🚀 Objective
To apply the Factory Method pattern to:
* Create games in a flexible and decoupled manner.
* Incorporate new functionalities (e.g., new game types) without modifying existing client code.
* Practice good Git workflow (branching, Pull Requests, rebase, merges, logging).

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>


## 🏗️ Project Structure

* **factory_method/**
    * **audit/** (Module for logging functionality)
        * `ILogger.py`
        * `Logger.py`
    * **client/** (Main client / entry point)
        * `FactoryMethodClient.py`
    * **factory/** (Base and concrete Factory classes)
        * `Board.py` (Abstract Factory)
        * `ChessBoard.py` (Concrete Factory)
        * `SolitaireBoard.py` (Concrete Factory)
    * **products/** (Product classes / specific game types)
        * `ChessGame.py` (Concrete Product)
        * `Game.py` (Abstract Product)
        * `SolitaireGame.py` (Concrete Product)
    * `README.md`

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

## 🧠 Core Features
    
| Feature | Description |  
| :--- | :--- |  
| Dynamic Game Creation | Instances are created without the client knowing the concrete class (Factory Method implementation). |  
| Game Types Supported | Supports ChessGame, SolitaireGame |  
| Configurable Difficulty | Allows selection between easy, normal, and hard difficulties. | 
| Timer/Duration Tracking | Records game duration and move counts. | 
| Logger Integration | Logs activity and results to audit/factory_logs.txt. | 

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

## 🧰 Technologies and Standards
* Python 3.10+
* Factory Method Design Pattern
* PEP8 (Code conventions)
* File handling (os, datetime modules)
* Git and GitHub (Professional branching and PR workflow)
---

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

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

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>


## 🧱 Applied Design Principles
* __Factory Method:__ Creates objects without exposing the instantiation logic to the client.
* __Single Responsability Principle (SRP):__ Each module and class has a clear, defined responsibility.
* __Open/Closed Principle (OCP):__ The system is open for extension (new game types) but closed for modification (client code remains unchanged).

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>  
 
---

## 🚀 Getting Started

These instructions will help you set up and run the project on your local machine.

### 🧩 Prerequisites

Make sure you have the following installed on your system:

* **Python 3.10+** (or your exact project version)
* **Git** (for cloning the repository)
* **Poetry** (recommended Python dependency manager).
  If you don’t have Poetry, install it globally:

```bash
pip install poetry
```

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>  

---

### ⚙️ Installation & Setup

Follow these steps to set up the environment and install dependencies:

#### 1️⃣ Clone the Repository

Replace the URL with your GitHub project link:

```bash
git clone [YOUR_GITHUB_REPOSITORY_URL]
```

#### 2️⃣ Change Directory

```bash
cd [your-project-folder-name]
```

#### 3️⃣ Install Dependencies

This command creates a virtual environment and installs all required libraries:

```bash
poetry install
```

#### 4️⃣ Activate the Virtual Environment

```bash
poetry shell
```
<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>  

---

### ▶️ Usage

Once the environment is active, run the main client file to see the **Factory Method Pattern** in action:

```bash
python -m client.FactoryMethodClient
```
<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>  

---



### 🛠️ Built With

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-60A5FA?logo=poetry)](https://python-poetry.org/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)](https://github.com/)
[![PyCharm](https://img.shields.io/badge/PyCharm-IDE-000000?logo=pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
[![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![PlantUML](https://img.shields.io/badge/PlantUML-Diagrams-F6921E?logo=plantuml&logoColor=black)](https://plantuml.com/)
[![Markdown](https://img.shields.io/badge/Markdown-Docs-000000?logo=markdown)](https://www.markdownguide.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>

---  

## 📷 Capture images of program from console (Terminal PyCharm)

<img width="566" height="279" alt="image" src="https://github.com/user-attachments/assets/db2895e0-87fc-4f43-bd54-4eaac88a700d" />  

**Selecting the option one:**  

<img width="565" height="418" alt="image" src="https://github.com/user-attachments/assets/b24c8e1c-7ed1-45fe-95cc-061d3e95245a" />

**Selecting the option two:**  

<img width="527" height="282" alt="image" src="https://github.com/user-attachments/assets/07186fb8-7fe2-4714-902e-e8168e2d4e07" />

**Selecting the option three:**  

<img width="568" height="659" alt="image" src="https://github.com/user-attachments/assets/8cd4d2cc-4e3a-40e9-b897-9d2f7b81e0c9" />

**Selecting the option zero:**  

<img width="363" height="178" alt="image" src="https://github.com/user-attachments/assets/60478b41-1e74-40f1-bcb9-241e7a616ad5" />


---  

<p align="right">
<a href="#factory-method-pattern-in-python">:arrow_up: Back to top</a>
</p>  


Educational and practical project demonstrating clean architecture and design patterns in Python.


















