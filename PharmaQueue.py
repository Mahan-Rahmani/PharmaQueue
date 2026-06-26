import sqlite3

print("Welcome to PharmaQueue")
print('*' * 35, '\n')

def get_priorities(status):
    if status.lower() == 'emergency':
        return 1
    elif status.lower() == 'prescription':
        return 2
    else:
        return 3

# Connect to SQLite database
conn = sqlite3.connect("pharma_queue.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS queue (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    status TEXT
)
""")
conn.commit()

while True:
    print('What do you want to do?\n\t1) Add a person to queue\n\t2) Show the list\n\t'
          '3) Serve first in queue\n\t4) Search for a patient\n\t5) Exit')
    try:
        choice = int(input('Your choice: '))
        if choice not in [1, 2, 3, 4, 5]:
            print("❗ Invalid choice. Please select a number between 1 and 5.\n")
            continue
    except ValueError:
        print("❗ Please enter a valid number.\n")
        continue

    if choice == 1:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        status = input('Enter status (General or Emergency or Prescription): ')
        cursor.execute("INSERT INTO queue (name, age, status) VALUES (?, ?, ?)", (name, age, status))
        conn.commit()
        print('✅ The person added to queue successfully.\n')
        print('*' * 40, '\n')

    elif choice == 2:
        cursor.execute("SELECT * FROM queue")
        rows = cursor.fetchall()
        if not rows:
            print("❗ Queue is empty.\n")
        else:
            sorted_queue = sorted(rows, key=lambda person: get_priorities(person[3]))
            for i, person in enumerate(sorted_queue):
                print(f"{i + 1}. [ID: {person[0]}] Name: {person[1]}, Age: {person[2]}, Status: {person[3]}")
            print()
        print('*' * 40, '\n')

    elif choice == 3:
        cursor.execute("SELECT * FROM queue")
        rows = cursor.fetchall()

        if not rows:
            print("❗ Queue is empty.\n")
        else:
            sorted_queue = sorted(rows, key=lambda person: get_priorities(person[3]))
            served_person = sorted_queue[0]

            print(f"✅ Served: {served_person[1]} | Age: {served_person[2]} | Status: {served_person[3]}")


            patient_id = served_person[0]
            cursor.execute("DELETE FROM queue WHERE id = ?", (patient_id,))
            conn.commit()
            print()
        print('*' * 40, '\n')

    elif choice == 4:
        name = input("Enter the name to search: ")
        cursor.execute("SELECT * FROM queue WHERE LOWER(name) = LOWER(?)", (name,))
        results = cursor.fetchall()

        if results:
            print(f"\n🔍 Found {len(results)} patient(s) with name '{name}':")
            for person in results:
                print(f"[ID: {person[0]}] Name: {person[1]}, Age: {person[2]}, Status: {person[3]}")
            print()
        else:
            print("❗ No patient found with that name.\n")
        print('*' * 40, '\n')

    elif choice == 5:
        print('Thank you for using PharmaQueue')
        conn.close()
        break