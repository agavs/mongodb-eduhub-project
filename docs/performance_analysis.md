# Performance Analysis
# Query Optimization 
## Course Title Search
- **Query**: `{'title': {'$regex': 'learn', '$options': 'i'}}`
- **Execution Time**: <0.1764 seconds>
- **Result**: Uses index on `title` for efficient regex search.

## Enrollment Query
- **Query**: `{'studentId': <id>, 'courseId': <id>}`
- **Execution Time**: <0.2512 seconds>
- **Result**: Uses compound index on `studentId` and `courseId`.

## Assignment Due Date Query
- **Query**: `{'dueDate': {'$gte': <datetime>}}`
- **Execution Time**: <0.2039 seconds>
- **Result**: Uses index on `dueDate` for range queries.
## Course title search performance (with index):
Execution time: 0.1764 seconds
Explain result: {'executionSuccess': True, 'nReturned': 3, 'executionTimeMillis': 1, 'totalKeysExamined': 10, 'totalDocsExamined': 3, 'executionStages': {'isCached': False, 'stage': 'FETCH', 'nReturned': 3, 'executionTimeMillisEstimate': 1, 'works': 11, 'advanced': 3, 'needTime': 7, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'docsExamined': 3, 'alreadyHasObj': 0, 'inputStage': {'stage': 'IXSCAN', 'filter': {'title': {'$regex': 'learn', '$options': 'i'}}, 'nReturned': 3, 'executionTimeMillisEstimate': 1, 'works': 11, 'advanced': 3, 'needTime': 7, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'keyPattern': {'title': 1, 'category': 1}, 'indexName': 'title_1_category_1', 'isMultiKey': False, 'multiKeyPaths': {'title': [], 'category': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'indexVersion': 2, 'direction': 'forward', 'indexBounds': {'title': ['["", {})', '[/learn/i, /learn/i]'], 'category': ['[MinKey, MaxKey]']}, 'keysExamined': 10, 'seeks': 1, 'dupsTested': 0, 'dupsDropped': 0}}, 'allPlansExecution': []}

## Enrollment query performance (with index):
Execution time: 0.2512 seconds
Explain result: {'executionSuccess': True, 'nReturned': 1, 'executionTimeMillis': 0, 'totalKeysExamined': 1, 'totalDocsExamined': 1, 'executionStages': {'isCached': False, 'stage': 'FETCH', 'nReturned': 1, 'executionTimeMillisEstimate': 1, 'works': 2, 'advanced': 1, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'docsExamined': 1, 'alreadyHasObj': 0, 'inputStage': {'stage': 'IXSCAN', 'nReturned': 1, 'executionTimeMillisEstimate': 1, 'works': 2, 'advanced': 1, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'keyPattern': {'studentId': 1, 'courseId': 1}, 'indexName': 'studentId_1_courseId_1', 'isMultiKey': False, 'multiKeyPaths': {'studentId': [], 'courseId': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'indexVersion': 2, 'direction': 'forward', 'indexBounds': {'studentId': ['["5848c3bc-dbe7-41b5-be98-908cdd9e4f68", "5848c3bc-dbe7-41b5-be98-908cdd9e4f68"]'], 'courseId': ['["49dd82df-af24-4d97-934d-df31eb9b5780", "49dd82df-af24-4d97-934d-df31eb9b5780"]']}, 'keysExamined': 1, 'seeks': 1, 'dupsTested': 0, 'dupsDropped': 0}}, 'allPlansExecution': []}

## Assignment due date query performance (with index):
Execution time: 0.2039 seconds
Explain result: {'executionSuccess': True, 'nReturned': 0, 'executionTimeMillis': 0, 'totalKeysExamined': 0, 'totalDocsExamined': 0, 'executionStages': {'isCached': False, 'stage': 'FETCH', 'nReturned': 0, 'executionTimeMillisEstimate': 0, 'works': 1, 'advanced': 0, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'docsExamined': 0, 'alreadyHasObj': 0, 'inputStage': {'stage': 'IXSCAN', 'nReturned': 0, 'executionTimeMillisEstimate': 0, 'works': 1, 'advanced': 0, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'keyPattern': {'dueDate': 1}, 'indexName': 'dueDate_1', 'isMultiKey': False, 'multiKeyPaths': {'dueDate': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'indexVersion': 2, 'direction': 'forward', 'indexBounds': {'dueDate': ['[new Date(1750005685217), new Date(9223372036854775807)]']}, 'keysExamined': 0, 'seeks': 1, 'dupsTested': 0, 'dupsDropped': 0}}, 'allPlansExecution': []}