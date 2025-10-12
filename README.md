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
| Command | Description |
| :--- | :--- |
| git checkout -b feature/logger | Create new branch |
| git push origin feature/logger| Push Changes and Create PR|
| git checkout main | Change to the branch main |
| git pull --rebase origin main | Update main before deleting branches (Rebase workflow) |
| git branch -d feature/logger | Delete branch |
---

## 🧱 Applied Design Principles
* __Factory Method:__ Creates objects without exposing the instantiation logic to the client.
* __Single Responsability Principle (SRP):__ Each module and class has a clear, defined responsibility.
* __Open/Closed Principle (OCP):__ The system is open for extension (new game types) but closed for modification (client code remains unchanged).
---

Educational and practical project demonstrating clean architecture and design patterns in Python.


















