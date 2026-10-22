
"""Track telecom tower maintenance and identify overdue or high-risk towers."""

import sqlite3


def initialize_database():
    """Create the in-memory database and towers table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE towers (
            id INTEGER PRIMARY KEY,
            site TEXT,
            last_service INTEGER,
            faults INTEGER
        )
        """
    )
    return connection


def add_tower(connection, site, last_service, faults=0):
    """Add a tower to the database."""
    connection.execute(
        """
        INSERT INTO towers (site, last_service, faults)
        VALUES (?, ?, ?)
        """,
        (site, last_service, faults),
    )
    connection.commit()


def service_tower(connection, tower_id, year):
    """Record tower servicing and reset its fault count."""
    try:
        cursor = connection.execute(
            """
            UPDATE towers
            SET last_service = ?, faults = 0
            WHERE id = ?
            """,
            (year, tower_id),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Service failed: {error}")
        return False

    return cursor.rowcount > 0


def overdue_towers(connection, year):
    """Return sites whose last service was at least two years ago."""
    rows = connection.execute(
        "SELECT site, last_service FROM towers"
    ).fetchall()

    return [
        site
        for site, last_service in rows
        if year - last_service >= 2
    ]


def risk_level(connection, tower_id):
    """Return the risk level of a tower based on its fault count."""
    row = connection.execute(
        "SELECT faults FROM towers WHERE id = ?",
        (tower_id,),
    ).fetchone()

    if row is None:
        return "unknown"

    if row[0] > 3:
        return "high"
    return "normal"


def snapshot(connection):
    """Return a snapshot of all tower records."""
    return connection.execute("SELECT * FROM towers").fetchall()


def main():
    """Run a demonstration of the tower maintenance tracker."""
    connection = initialize_database()

    try:
        add_tower(connection, "Ridge-A", 2021, 5)
        add_tower(connection, "Coast-B", 2024)
        service_tower(connection, 2, 2025)

        total = len(snapshot(connection))
        print(
            overdue_towers(connection, 2025),
            risk_level(connection, 1),
            total,
        )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
