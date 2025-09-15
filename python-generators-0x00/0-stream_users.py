
---

## `0-stream_users.py`

```python
#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator function that streams rows from user_data table one by one."""
    try:
        # 1. Connect to ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",           # <-- change if using another MySQL user
            password="your_password",  # <-- change to your MySQL password
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)  # dictionary=True returns rows as dicts
        cursor.execute("SELECT * FROM user_data")

        # 2. Single loop yielding one row at a time
        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
```

---

### 🔑 Key Points:

✅ **Generator Function**

* `yield row` makes this a generator — rows are returned lazily, one at a time.
* Uses **only one loop** as required.

✅ **Memory Efficient**

* This doesn’t load the entire table into memory (good for large datasets).

✅ **Dictionary Cursor**

* Returns each row as a dictionary (`{'user_id': ..., 'name': ..., ...}`)
  — exactly like in your example output.

---

### Test with `1-main.py`

You already have:

```python
#!/usr/bin/python3
from itertools import islice
stream_users = __import__('0-stream_users')

for user in islice(stream_users.stream_users(), 6):
    print(user)
```

Output should look like:

```
{'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67}
{'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119}
...
```

---
