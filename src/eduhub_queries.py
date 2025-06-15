# Import required libraries
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
from faker import Faker
import json

# Initialize Faker for generating sample data
fake = Faker()

# Establish MongoDB connection
client = MongoClient('mongodb+srv://maleagava:RadFame@eduhub-mongodb-project.coocld6.mongodb.net/')
db = client['eduhub_db']

# Drop existing database for a clean start
client.drop_database('eduhub_db')

# Create collections with validation rules
db.create_collection('users', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['userId', 'email', 'firstName', 'lastName', 'role', 'dateJoined', 'isActive'],
        'properties': {
            'userId': {'bsonType': 'string'},
            'email': {'bsonType': 'string', 'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'},
            'firstName': {'bsonType': 'string'},
            'lastName': {'bsonType': 'string'},
            'role': {'enum': ['student', 'instructor']},
            'dateJoined': {'bsonType': 'date'},
            'profile': {
                'bsonType': 'object',
                'properties': {
                    'bio': {'bsonType': 'string'},
                    'avatar': {'bsonType': 'string'},
                    'skills': {'bsonType': 'array', 'items': {'bsonType': 'string'}}
                }
            },
            'isActive': {'bsonType': 'bool'}
        }
    }
})

db.create_collection('courses', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['courseId', 'title', 'instructorId', 'category', 'level', 'duration', 'price', 'createdAt', 'isPublished'],
        'properties': {
            'courseId': {'bsonType': 'string'},
            'title': {'bsonType': 'string'},
            'description': {'bsonType': 'string'},
            'instructorId': {'bsonType': 'string'},
            'category': {'bsonType': 'string'},
            'level': {'enum': ['beginner', 'intermediate', 'advanced']},
            'duration': {'bsonType': 'double'},
            'price': {'bsonType': 'double'},
            'tags': {'bsonType': 'array', 'items': {'bsonType': 'string'}},
            'createdAt': {'bsonType': 'date'},
            'updatedAt': {'bsonType': 'date'},
            'isPublished': {'bsonType': 'bool'}
        }
    }
})

db.create_collection('enrollments', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['enrollmentId', 'studentId', 'courseId', 'enrollmentDate', 'progress'],
        'properties': {
            'enrollmentId': {'bsonType': 'string'},
            'studentId': {'bsonType': 'string'},
            'courseId': {'bsonType': 'string'},
            'enrollmentDate': {'bsonType': 'date'},
            'progress': {'bsonType': 'double'},
            'completionDate': {'bsonType': 'date'}
        }
    }
})

db.create_collection('lessons', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['lessonId', 'courseId', 'title', 'content'],
        'properties': {
            'lessonId': {'bsonType': 'string'},
            'courseId': {'bsonType': 'string'},
            'title': {'bsonType': 'string'},
            'content': {'bsonType': 'string'},
            'duration': {'bsonType': 'double'}
        }
    }
})

db.create_collection('assignments', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['assignmentId', 'courseId', 'title', 'dueDate'],
        'properties': {
            'assignmentId': {'bsonType': 'string'},
            'courseId': {'bsonType': 'string'},
            'title': {'bsonType': 'string'},
            'description': {'bsonType': 'string'},
            'dueDate': {'bsonType': 'date'}
        }
    }
})

db.create_collection('submissions', validator={
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['submissionId', 'assignmentId', 'studentId', 'submissionDate'],
        'properties': {
            'submissionId': {'bsonType': 'string'},
            'assignmentId': {'bsonType': 'string'},
            'studentId': {'bsonType': 'string'},
            'submissionDate': {'bsonType': 'date'},
            'content': {'bsonType': 'string'},
            'grade': {'bsonType': 'double'},
            'feedback': {'bsonType': 'string'}
        }
    }
})

print("Database and collections created successfully!")
import random
import uuid
from datetime import timedelta

client.drop_database('eduhub_db')

# Education-specific data
course_titles = [
    "Introduction to Python Programming",
    "Advanced Machine Learning",
    "Web Development with JavaScript",
    "Data Structures and Algorithms",
    "Graphic Design Fundamentals",
    "Business Analytics",
    "Database Management Systems",
    "Mobile App Development"
]
course_categories = ["Programming", "Data Science", "Web Development", "Algorithms", "Design", "Business", "Databases", "Mobile Development"]
assignment_titles = [
    "Python Functions Homework",
    "Machine Learning Model Project",
    "Build a Responsive Website",
    "Implement Sorting Algorithms",
    "Create a Logo Design",
    "Business Case Study",
    "SQL Query Assignment",
    "Mobile App Prototype"
]
lesson_titles = [
    "Variables and Data Types",
    "Supervised Learning Basics",
    "HTML and CSS Foundations",
    "Binary Search Trees",
    "Color Theory in Design",
    "Market Analysis Techniques",
    "Relational Database Design",
    "UI/UX for Mobile Apps"
]
description_templates = [
    "Write a program to {task}.",
    "Analyze a dataset using {tool}.",
    "Design a {item} for a client.",
    "Implement a {algorithm} in {language}.",
    "Create a {deliverable} based on {concept}.",
    "Solve a business problem using {method}.",
    "Query a database to retrieve {data}.",
    "Build a prototype for a {feature}."
]
tools_concepts = ["pandas", "scikit-learn", "React", "Python", "Figma", "Excel", "SQL", "Flutter"]
deliverables = ["web page", "machine learning model", "logo", "algorithm", "report", "query set", "app interface"]

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Drop database for clean start
client.drop_database('eduhub_db')
print("Dropped eduhub_db for clean start")

# Generate Users (15 students, 5 instructors)
db.users.delete_many({})
users = []
for _ in range(15):  # Students
    users.append({
        'userId': generate_id(),
        'email': fake.email(),
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'role': 'student',
        'dateJoined': fake.date_time_this_year(),
        'profile': {
            'bio': f"Student interested in {random.choice(course_categories)}.",
            'avatar': fake.image_url(),
            'skills': random.sample(course_categories, 3)
        },
        'isActive': True
    })
for _ in range(5):  # Instructors
    users.append({
        'userId': generate_id(),
        'email': fake.email(),
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'role': 'instructor',
        'dateJoined': fake.date_time_this_year(),
        'profile': {
            'bio': f"Instructor specializing in {random.choice(course_categories)}.",
            'avatar': fake.image_url(),
            'skills': random.sample(course_categories, 5)
        },
        'isActive': True
    })
db.users.insert_many(users)
print("Inserted users:", db.users.count_documents({}))

# Generate Courses
db.courses.delete_many({})
levels = ['beginner', 'intermediate', 'advanced']
instructor_ids = [u['userId'] for u in db.users.find({'role': 'instructor'})]
courses = []
for i in range(8):
    course_id = generate_id()
    courses.append({
        'courseId': course_id,
        'title': course_titles[i],
        'description': f"Learn the fundamentals of {course_titles[i].lower()} through hands-on projects and expert guidance.",
        'instructorId': fake.random_element(instructor_ids),
        'category': course_categories[i],
        'level': fake.random_element(levels),
        'duration': float(fake.random_int(min=5, max=50)),
        'price': float(round(fake.random_number(digits=2) + fake.random.random(), 2)),
        'tags': random.sample(course_categories, 4),
        'createdAt': fake.date_time_this_year(),
        'updatedAt': fake.date_time_this_year(),
        'isPublished': fake.boolean()
    })
db.courses.insert_many(courses)
print("Inserted courses:", db.courses.count_documents({}))

# Generate Enrollments
db.enrollments.delete_many({})
student_ids = [u['userId'] for u in db.users.find({'role': 'student'})]
course_ids = [c['courseId'] for c in db.courses.find()]
enrollments = []
for _ in range(15):
    enrollment = {
        'enrollmentId': generate_id(),
        'studentId': fake.random_element(student_ids),
        'courseId': fake.random_element(course_ids),
        'enrollmentDate': fake.date_time_this_year(),
        'progress': float(round(fake.random.random() * 100, 2)),
        'completionDate': fake.date_time_this_year() if fake.boolean() else None
    }
    enrollments.append(enrollment)

db.enrollments.insert_many(enrollments)
print("Inserted enrollments:", db.enrollments.count_documents({}))

# Generate Lessons
db.lessons.delete_many({})
lessons = []
for course in db.courses.find():
    for i in range(fake.random_int(min=2, max=5)):
        lessons.append({
            'lessonId': generate_id(),
            'courseId': course['courseId'],
            'title': lesson_titles[i % len(lesson_titles)],
            'content': f"This lesson covers {lesson_titles[i % len(lesson_titles)].lower()} with practical examples and exercises.",
            'duration': round(fake.random.random() * 2, 2)
        })
db.lessons.insert_many(lessons)
print("Inserted lessons:", db.lessons.count_documents({}))

# Generate Assignments
db.assignments.delete_many({})
assignments = []
for course in db.courses.find():
    for i in range(fake.random_int(min=1, max=3)):
        template = random.choice(description_templates)
        assignments.append({
            'assignmentId': generate_id(),
            'courseId': course['courseId'],
            'title': assignment_titles[i % len(assignment_titles)],
            'description': template.format(
                task=random.choice(assignment_titles).lower(),
                tool=random.choice(tools_concepts),
                item=random.choice(deliverables),
                algorithm=random.choice(["sorting", "searching", "graph traversal"]),
                language=random.choice(["Python", "JavaScript", "SQL"]),
                deliverable=random.choice(deliverables),
                concept=random.choice(tools_concepts),
                method=random.choice(["analysis", "design", "implementation"]),
                data=random.choice(["sales records", "user data", "student grades"]),
                feature=random.choice(["login system", "dashboard", "notification"])
            ),
            'dueDate': fake.date_time_this_month()
        })
db.assignments.insert_many(assignments)
print("Inserted assignments:", db.assignments.count_documents({}))

# Generate Submissions
db.submissions.delete_many({})
assignment_ids = [a['assignmentId'] for a in db.assignments.find()]
submissions = []
for _ in range(12):
    submissions.append({
        'submissionId': generate_id(),
        'assignmentId': fake.random_element(assignment_ids),
        'studentId': fake.random_element(student_ids),
        'submissionDate': fake.date_time_this_month(),
        'content': f"Submitted work for {random.choice(assignment_titles).lower()}.",
        'grade': float(round(fake.random.random() * 100, 2)),
        'feedback': f"Good work on {random.choice(assignment_titles).lower()}, improve {random.choice(tools_concepts)} usage."
    })
db.submissions.insert_many(submissions)
print("Inserted submissions:", db.submissions.count_documents({}))

print("Sample data inserted successfully!")
# Verify course instructor references
courses = db.courses.find()
for course in courses:
    instructor = db.users.find_one({'userId': course['instructorId'], 'role': 'instructor'})
    print(f"Course {course['title']} has valid instructor: {instructor is not None}")

# Verify enrollment references
enrollments = db.enrollments.find()
for enrollment in enrollments:
    student = db.users.find_one({'userId': enrollment['studentId'], 'role': 'student'})
    course = db.courses.find_one({'courseId': enrollment['courseId']})
    print(f"Enrollment {enrollment['enrollmentId']} has valid student: {student is not None}, course: {course is not None}")
    # Education-specific data
course_titles = [
    "Introduction to Python Programming",
    "Advanced Machine Learning",
    "Web Development with JavaScript",
    "Data Structures and Algorithms",
    "Graphic Design Fundamentals",
    "Business Analytics",
    "Database Management Systems",
    "Mobile App Development"
]
course_categories = ["Programming", "Data Science", "Web Development", "Algorithms", "Design", "Business", "Databases", "Mobile Development"]
assignment_titles = [
    "Python Functions Homework",
    "Machine Learning Model Project",
    "Build a Responsive Website",
    "Implement Sorting Algorithms",
    "Create a Logo Design",
    "Business Case Study",
    "SQL Query Assignment",
    "Mobile App Prototype"]

# Add a new student
new_student = {
    'userId': generate_id(),
    'email': fake.email(),
    'firstName': fake.first_name(),
    'lastName': fake.last_name(),
    'role': 'student',
    'dateJoined': fake.date_time_this_year(),
    'profile': {
        'bio': f"Student interested in {random.choice(course_categories)}.",
        'avatar': fake.image_url(),
        'skills': random.sample(course_categories, 3)
    },
    'isActive': True
}
db.users.insert_one(new_student)
print("New student added:", new_student['userId'])

# Create a new course
new_course = {
    'courseId': course_id,
        'title': course_titles[i],
        'description': f"Learn the fundamentals of {course_titles[i].lower()} through hands-on projects and expert guidance.",
        'instructorId': fake.random_element(instructor_ids),
        'category': course_categories[i],
        'level': fake.random_element(levels),
        'duration': float(fake.random_int(min=5, max=50)),
        'price': float(round(fake.random_number(digits=2) + fake.random.random(), 2)),
        'tags': random.sample(course_categories, 4),
        'createdAt': fake.date_time_this_year(),
        'updatedAt': fake.date_time_this_year(),
        'isPublished': fake.boolean()
}
db.courses.insert_one(new_course)
print("New course added:", new_course['courseId'])
# Find all active students
active_students = list(db.users.find({'role': 'student', 'isActive': True}))
print("Active Students:")
display(pd.DataFrame(active_students))

# Retrieve course details with instructor information
course_with_instructor = list(db.courses.aggregate([
    {'$lookup': {
        'from': 'users',
        'localField': 'instructorId',
        'foreignField': 'userId',
        'as': 'instructor'
    }},
    {'$unwind': '$instructor'}
]))
print("Courses with Instructor Details:")
display(pd.DataFrame(course_with_instructor))

# Get all courses in a specific category
programming_courses = list(db.courses.find({'category': 'Programming'}))
print("Programming Courses:")
display(pd.DataFrame(programming_courses))

# Find students enrolled in a specific course
course_id = db.courses.find_one()['courseId']
enrolled_students = list(db.enrollments.aggregate([
    {'$match': {'courseId': course_id}},
    {'$lookup': {
        'from': 'users',
        'localField': 'studentId',
        'foreignField': 'userId',
        'as': 'student'
    }},
    {'$unwind': '$student'}
]))
print(f"Students enrolled in course {course_id}:")
display(pd.DataFrame(enrolled_students))

# Search courses by title (case-insensitive, partial match)
search_query = 'learn'
courses_by_title = list(db.courses.find({'title': {'$regex': search_query, '$options': 'i'}}))
print(f"Courses matching '{search_query}':")
display(pd.DataFrame(courses_by_title))
# Update a user's profile
user_id = db.users.find_one({'role': 'student'})['userId']
db.users.update_one(
    {'userId': user_id},
    {'$set': {'profile.bio': 'Updated bio', 'profile.skills': ['Python', 'SQL']}}
)
print("Updated user profile:", user_id)

# Mark a course as published
course_id = db.courses.find_one({'isPublished': False})['courseId']
db.courses.update_one(
    {'courseId': course_id},
    {'$set': {'isPublished': True, 'updatedAt': datetime.now()}}
)
print("Marked course as published:", course_id)

# Update assignment grades
submission_id = db.submissions.find_one()['submissionId']
db.submissions.update_one(
    {'submissionId': submission_id},
    {'$set': {'grade': 85.0, 'feedback': 'Great work!'}}
)
print("Updated submission grade:", submission_id)

# Add tags to an existing course
db.courses.update_one(
    {'courseId': course_id},
    {'$push': {'tags': {'$each': ['new', 'trending']}}}
)
print("Added tags to course:", course_id)
# Soft delete a user
user_id = db.users.find_one({'role': 'student', 'isActive': True})['userId']
db.users.update_one(
    {'userId': user_id},
    {'$set': {'isActive': False}}
)
print("Soft deleted user:", user_id)

# Delete an enrollment
enrollment_id = db.enrollments.find_one()['enrollmentId']
db.enrollments.delete_one({'enrollmentId': enrollment_id})
print("Deleted enrollment:", enrollment_id)

# Remove a lesson from a course
lesson_id = db.lessons.find_one()['lessonId']
db.lessons.delete_one({'lessonId': lesson_id})
print("Deleted lesson:", lesson_id)
# Find courses with price between $50 and $200
price_range_courses = list(db.courses.find({
    'price': {'$gte': 50, '$lte': 200}
}))
print("Courses priced between $50 and $200:")
display(pd.DataFrame(price_range_courses))

# Get users who joined in the last 6 months
six_months_ago = datetime.now() - timedelta(days=180)
recent_users = list(db.users.find({
    'dateJoined': {'$gte': six_months_ago}
}))
print("Users joined in the last 6 months:")
display(pd.DataFrame(recent_users))

# Find courses with specific tags
courses_with_tags = list(db.courses.find({
    'tags': {'$in': ['python', 'coding']}
}))
print("Courses with tags 'python' or 'coding':")
display(pd.DataFrame(courses_with_tags))

# Retrieve assignments with due dates in the next week
next_week = datetime.now() + timedelta(days=7)
upcoming_assignments = list(db.assignments.find({
    'dueDate': {'$gte': datetime.now(), '$lte': next_week}
}))
print("Assignments due in the next week:")
display(pd.DataFrame(upcoming_assignments))
# Course Enrollment Statistics
enrollment_stats = list(db.enrollments.aggregate([
    {'$group': {
        '_id': '$courseId',
        'totalEnrollments': {'$sum': 1},
        'avgProgress': {'$avg': '$progress'}
    }},
    {'$lookup': {
        'from': 'courses',
        'localField': '_id',
        'foreignField': 'courseId',
        'as': 'course'
    }},
    {'$unwind': '$course'},
    {'$group': {
        '_id': '$course.category',
        'courses': {
            '$push': {
                'title': '$course.title',
                'totalEnrollments': '$totalEnrollments',
                'avgProgress': '$avgProgress'
            }
        }
    }}
]))
print("Course Enrollment Statistics by Category:")
display(pd.DataFrame(enrollment_stats))

# Student Performance Analysis
student_performance = list(db.submissions.aggregate([
    {'$group': {
        '_id': '$studentId',
        'avgGrade': {'$avg': '$grade'},
        'totalSubmissions': {'$sum': 1}
    }},
    {'$lookup': {
        'from': 'users',
        'localField': '_id',
        'foreignField': 'userId',
        'as': 'student'
    }},
    {'$unwind': '$student'},
    {'$sort': {'avgGrade': -1}},
    {'$limit': 5}
]))
print("Top 5 Students by Average Grade:")
display(pd.DataFrame(student_performance))

# Instructor Analytics
instructor_analytics = list(db.courses.aggregate([
    {'$lookup': {
        'from': 'enrollments',
        'localField': 'courseId',
        'foreignField': 'courseId',
        'as': 'enrollments'
    }},
    {'$unwind': {'path': '$enrollments', 'preserveNullAndEmptyArrays': True}},
    {'$group': {
        '_id': '$instructorId',
        'totalStudents': {'$sum': {'$cond': [{'$ifNull': ['$enrollments', False]}, 1, 0]}},
        'totalRevenue': {'$sum': {'$cond': [{'$ifNull': ['$enrollments', False]}, '$price', 0]}}
    }},
    {'$lookup': {
        'from': 'users',
        'localField': '_id',
        'foreignField': 'userId',
        'as': 'instructor'
    }},
    {'$unwind': '$instructor'}
]))
print("Instructor Analytics:")
display(pd.DataFrame(instructor_analytics))

# Advanced Analytics: Monthly Enrollment Trends
monthly_trends = list(db.enrollments.aggregate([
    {'$group': {
        '_id': {
            'year': {'$year': '$enrollmentDate'},
            'month': {'$month': '$enrollmentDate'}
        },
        'totalEnrollments': {'$sum': 1}
    }},
    {'$sort': {'_id.year': 1, '_id.month': 1}}
]))
print("Monthly Enrollment Trends:")
display(pd.DataFrame(monthly_trends))
# User email lookup
db.users.create_index([('email', 1)], unique=True)
print("Created index on users.email")

# Course search by title and category
db.courses.create_index([('title', 1), ('category', 1)])
print("Created compound index on courses.title and courses.category")

# Assignment queries by due date
db.assignments.create_index([('dueDate', 1)])
print("Created index on assignments.dueDate")

# Enrollment queries by student and course
db.enrollments.create_index([('studentId', 1), ('courseId', 1)])
print("Created compound index on enrollments.studentId and enrollments.courseId")
import time

# Query 1: Course search by title (before and after index)
query = {'title': {'$regex': 'learn', '$options': 'i'}}
start_time = time.time()
explain_result = db.courses.find(query).explain()
end_time = time.time()
print("Course title search performance (with index):")
print(f"Execution time: {end_time - start_time:.4f} seconds")
print("Explain result:", explain_result['executionStats'])

# Query 2: Enrollment by student and course
query = {'studentId': db.enrollments.find_one()['studentId'], 'courseId': db.enrollments.find_one()['courseId']}
start_time = time.time()
explain_result = db.enrollments.find(query).explain()
end_time = time.time()
print("Enrollment query performance (with index):")
print(f"Execution time: {end_time - start_time:.4f} seconds")
print("Explain result:", explain_result['executionStats'])

# Query 3: Assignments by due date
query = {'dueDate': {'$gte': datetime.now()}}
start_time = time.time()
explain_result = db.assignments.find(query).explain()
end_time = time.time()
print("Assignment due date query performance (with index):")
print(f"Execution time: {end_time - start_time:.4f} seconds")
print("Explain result:", explain_result['executionStats'])
try:
    # Invalid user (missing required field)
    db.users.insert_one({
        'userId': generate_id(),
        'email': 'invalid-email',  # Invalid email format
        'firstName': 'Test',
        # Missing lastName
        'role': 'student',
        'dateJoined': datetime.now(),
        'isActive': True
    })
except Exception as e:
    print("Validation error (missing lastName):", str(e))

try:
    # Invalid course (invalid level)
    db.courses.insert_one({
        'courseId': generate_id(),
        'title': 'Test Course',
        'instructorId': db.users.find_one()['userId'],
        'category': 'Programming',
        'level': 'expert',  # Invalid enum value
        'duration': 10.0,
        'price': 50.0,
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        'isPublished': True
    })
except Exception as e:
    print("Validation error (invalid level):", str(e))
    from pymongo.errors import DuplicateKeyError

# Handle duplicate email
try:
    db.users.insert_one({
        'userId': generate_id(),
        'email': db.users.find_one()['email'],  # Duplicate email
        'firstName': fake.first_name(),
        'lastName': fake.last_name(),
        'role': 'student',
        'dateJoined': datetime.now(),
        'profile': {'bio': '', 'avatar': '', 'skills': []},
        'isActive': True
    })
except DuplicateKeyError as e:
    print("Duplicate key error:", str(e))

# Handle invalid data type
try:
    db.courses.insert_one({
        'courseId': generate_id(),
        'title': fake.catch_phrase(),
        'description': fake.text(),
        'instructorId': db.users.find_one()['userId'],
        'category': 'Programming',
        'level': 'beginner',
        'duration': '10',  # Invalid type (string instead of double)
        'price': 50.0,
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        'isPublished': True
    })
except Exception as e:
    print("Invalid data type error:", str(e))
    # Create text index on course title and description
db.courses.create_index([('title', 'text'), ('description', 'text')])
text_search_results = list(db.courses.find(
    {'$text': {'$search': 'programming learn'}},
    {'score': {'$meta': 'textScore'}}
).sort([('score', {'$meta': 'textScore'})]))
print("Text search results for 'programming learn':")
display(pd.DataFrame(text_search_results))