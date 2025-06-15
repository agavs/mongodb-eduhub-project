# Performance Analysis

## Course Title Search
- **Query**: `{'title': {'$regex': 'learn', '$options': 'i'}}`
- **Execution Time**: <insert time from output>
- **Explain Result**: Uses index on `title` for efficient regex search.

## Enrollment Query
- **Query**: `{'studentId': <id>, 'courseId': <id>}`
- **Execution Time**: <insert time from output>
- **Explain Result**: Uses compound index on `studentId` and `courseId`.

## Assignment Due Date Query
- **Query**: `{'dueDate': {'$gte': <datetime>}}`
- **Execution Time**: <insert time from output>
- **Explain Result**: Uses index on `dueDate` for range queries.