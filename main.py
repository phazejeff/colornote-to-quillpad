import sqlite3
import json
import shutil
import time

DATABASE_NAME = 'colornote.db'
BACKUP_FILE = {
    "version" : 10,
    "notes" : []
}

db = sqlite3.connect(DATABASE_NAME)
cur = db.cursor()

items = cur.execute("SELECT * FROM notes;").fetchall()
for count, i in enumerate(items):
    print(f"{count + 1} / {len(items)}")
    this = {}

    this["title"]: str = i[7]
    this["content"]: str = i[8]
    this["creationDate"]: int = i[13]
    this["modifiedDate"]: int = i[14]
    this["id"]: int = i[0]

    BACKUP_FILE["notes"].append(this)

j = json.dumps(BACKUP_FILE)

f = open('./quillnote_backup/backup.json', 'w+')
f.write(j)
f.close()

current_time = str(round(time.time()))

shutil.make_archive("quillnote_backup_" + current_time, "zip", "quillnote_backup")