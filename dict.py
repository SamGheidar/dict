import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="user",
   password="abc123"
)

# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: adds words and translation:
# argument: C - the database connection.
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: deletes words and translation by asking ID:
# argument: C - the database connection.
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: saves and close the program(stops the loop):
# argument: C - the database connection.
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

# while loop: creating commands for user
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "help":
        print("""available commands:
add - add a phone number
delete - delete a contact
list - list all phone numbers
quit - quit the program""")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
