import sqlite3 as sql
import pandas as pd
import logging
import os

def _create_db(db_name: str):
    if os.path.isfile(f"./database/{db_name}.db"):
        raise NameError(f'Db "{db_name}.db" is already created')

    connection = sql.connect(f"./database/{db_name}.db")
    print(f"{db_name}.db created")
    connection.close()


def _delete_db(db_name: str):
    if os.path.isfile(f"./database/{db_name}.db") == False:
        raise NameError(f'no such file "{db_name}.db"')

    os.remove(f"./database/{db_name}.db")
    print(f"{db_name}.db deleted")


def _create_standart_table(db_name: str, table_name: str):
    if os.path.isfile(f"./database/{db_name}.db") == False:
        raise NameError(f'no such file "{db_name}.db"')

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    CREATE TABLE IF NOT EXISTS {table_name}(
    id INTEGER,
    username TEXT,
    lvl INTEGER,
    task_1 INTEGER,
    task_2 INTEGER,
    task_3 INTEGER,
    task_4 INTEGER
    )
    """
    )
    print(f"standart table {table_name} created")
    connection.close()


def _get_db_list() -> list:
    return [
        name.replace(".db", "")
        for name in os.listdir("./database/")
        if name.endswith(".db")
    ]


def _get_table_list(db_name: str):
    if os.path.isfile(f"./database/{db_name}.db") == False:
        raise NameError(f'no such file "{db_name}.db"')

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    names = []
    for table in tables:
        names.append(table[0])
    connection.close()

    return names


def _convert_table2xlsx(db_name: str, table_name: str):
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')

    connection = sql.connect(f"./database/{db_name}.db")
    table = pd.read_sql_query(f"SELECT * FROM {table_name}", connection)
    table.to_excel(f"./database/{db_name}_{table_name}.xlsx", index_label="index")
    connection.close()


def _contains(db_name: str, table_name: str, user_id: int) -> bool:
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    SELECT id FROM {table_name}
    """
    )
    ids = cursor.fetchall()
    connection.close()
    id_list = []
    for id in ids:
        id_list.append(id[0])

    if user_id in id_list:
        return True
    else:
        return False


def add_user(db_name: str, table_name: str, user_id: int, user_name: str):
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id):
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    INSERT INTO {table_name} (id, username, lvl, task_1, task_2, task_3, task_4) VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (user_id, user_name, 1, 0, 0, 0, 0),
    )
    connection.commit()
    connection.close()
    logging.info(
        f"Added user with id: {user_id}, name: {user_name}. LVL assigned: {1}:"
    )


def set_user_lvl(db_name: str, table_name: str, user_id: int, user_lvl: int):
    """
    use only if table contains user
    """
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id) == False:
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    UPDATE {table_name} SET lvl = ? WHERE id = ?
    """,
        (user_lvl, user_id),
    )
    connection.commit()
    connection.close()
    logging.info(f"Users {user_id} LVL is set to: {user_lvl}")


def get_user_lvl(db_name: str, table_name: str, user_id: int) -> int:
    """
    use only if table contains user
    """
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id) == False:
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    SELECT lvl FROM {table_name} WHERE id = ?
    """,
        (user_id,),
    )
    lvl = cursor.fetchone()
    connection.close()

    logging.info(f"User LVL received: user: {user_id}, LVL: {lvl[0]}")
    return lvl[0]


def delete_user(db_name: str, table_name: str, user_id: int):
    """
    use only if table contains user
    """
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id) == False:
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    DELETE FROM {table_name} WHERE id = ?
    """,
        (user_id,),
    )
    connection.commit()
    connection.close()
    logging.info(f"Deleted user {user_id}")


def show_table(db_name: str, table_name: str):
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()
    cursor.execute(
        f"""
    SELECT * FROM {table_name}
    """
    )
    table = cursor.fetchall()
    connection.close()

    if len(table) == 0:
        print("table is empty")
        return

    for line in table:
        print(
            f"{line[0]}\t{line[2]}\t{line[1]}\t{line[3]}\t{line[4]}\t{line[5]}\t{line[6]}"
        )


def is_task_complete(
    db_name: str, table_name: str, user_id: int, task_name: str
) -> bool:
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id) == False:
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()

    cursor.execute(
        f"""
    SELECT {task_name} FROM {table_name} WHERE id = ?
    """,
        (user_id,),
    )
    task = cursor.fetchone()[0]
    complete = bool(task)
    connection.close()

    return complete


def task_complete(db_name: str, table_name: str, user_id: str, task_name: str):
    if table_name not in _get_table_list(db_name):
        raise NameError(f'no such table "{db_name}"')
    if _contains(db_name, table_name, user_id) == False:
        return

    connection = sql.connect(f"./database/{db_name}.db")
    cursor = connection.cursor()

    user_lvl = get_user_lvl(db_name, table_name, user_id)
    user_lvl += 1
    set_user_lvl(db_name, table_name, user_id, user_lvl)

    cursor.execute(
        f"""
    UPDATE {table_name} SET {task_name} = ? WHERE id = ?
    """,
        (1, user_id),
    )
    connection.commit()
    connection.close()
    logging.info(f"Users {user_id} {task_name} is set to: 1")
