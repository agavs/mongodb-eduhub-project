# Mongodb Eduhub Project
## Project Overview
This project implements a MongoDB database for an e-learning platform called EduHub, supporting user management, course management, enrollments, lessons, assignments, and analytics.

## Setup Instructions
1. **Install MongoDB**: Ensure MongoDB is running locally (`mongodb+srv://maleagava:RadFame@eduhub-mongodb-project.coocld6.mongodb.net/`).
2. **Install Python Libraries**:
   pip install pymongo faker pandas
3. **Write Code**
4. **Run the notebook**:
   Open notebooks/eduhub_mongodb_project.ipynb in VS Code with the Jupyter extension.
   Execute all cells to set up the database, populate data, and run queries.
5. **Run the Python Script (optional)**:
   python src/eduhub_queries.py
6. **Database Schema**
   users: Stores student and instructor information.
   courses: Stores course details with references to instructors.
   enrollments: Tracks student course enrollments.
   lessons: Contains lesson content for courses.
   assignments: Stores assignment details.
   submissions: Tracks student assignment submissions.
7. **Queries Explained**
   CRUD Operations: Implemented in Part 3 for creating, reading, updating, and deleting documents.
   Advanced Queries: Part 4 includes complex queries and aggregation pipelines for analytics.
   Performance: Part 5 optimizes queries with indexes and analyzes performance.
8. **Performance Analysis**
   See docs/performance_analysis.md for detailed query performance results.
9. **Challenges and Solutions**:
   Challenge: Ensuring referential integrity without foreign key constraints.
   Solution: Used application-level checks and unique IDs for references.
   Challenge: Optimizing regex searches for course titles.
   Solution: Created a text index for efficient searches.
10. **Repository Structure**:
mongodb-eduhub-project/
├── README.md
├── notebooks/
│   └── eduhub_mongodb_project.ipynb
├── src/
│   └── eduhub_queries.py
├── data/
│   ├── sample_data.json
│   └── schema_validation.json
├── docs/
│   ├── performance_analysis.md
│   └── presentation.pptx
└── .gitignore
11. **License**:
    MIT License








