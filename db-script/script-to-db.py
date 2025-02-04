import sqlite3

with open('exercises.txt', 'r') as f1:
    conn = sqlite3.connect('../sweeft/db.sqlite3')
    cursor = conn.cursor()
    txt = f1.readlines()
    for e in txt:
        if e == "\n":
            txt.remove(e)
    d = {}
    uid = 1
    for i in range(0, 80, 4):
        name = txt[i]
        desc = txt[i + 1]
        instruction = txt[i + 2]
        muscles = txt[i + 3]
        d[uid] = {'name': name.strip(),
                  'desc': desc.split(":")[1].strip(),
                  'instruction': instruction.split(':')[1].strip(),
                  'muscles': muscles.split(':')[1].strip()}
        uid += 1

    for v in d.values():
        name = v['name']
        desc = v['desc']
        instruction = v['instruction']
        muscles = v['muscles']

        cursor.execute(
            """INSERT INTO
            workoutExercise_exercise(name, description, instruction)
             VALUES (?, ?, ?)""",
            (name, desc, instruction))

        cursor.execute("SELECT last_insert_rowid()")
        last_inserted_id = cursor.fetchone()[0]

        for muscle in muscles.split(","):
            cursor.execute(
                """INSERT INTO
                workoutExercise_muscle(muscle, exercise_id)
                 VALUES (?, ?)""",
                (muscle.strip(), last_inserted_id))
            conn.commit()


print("Successfully inserted")
