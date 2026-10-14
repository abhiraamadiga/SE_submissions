"""Animal shelter adoption register module.

Manages pet records, adoptions, and shelter status using SQLite.
"""

import logging
import secrets
import sqlite3

logger = logging.getLogger(__name__)

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE pets (id INTEGER PRIMARY KEY, name TEXT, species TEXT, age INTEGER, adopted INTEGER)")
adoption_stats = {"count": 0}


def register_pet(name, species, age, tags=None):
    """Register a new pet in the shelter database.

    Args:
        name: Name of the pet.
        species: Species of the pet.
        age: Age of the pet in years.
        tags: Optional list of tags associated with the pet.

    Returns:
        list: The updated list of tags including the pet's species.
    """
    if tags is None:
        tags = []
    conn.execute(
        "INSERT INTO pets (name, species, age, adopted) VALUES (?, ?, ?, 0)",
        (name, species, age),
    )
    tags.append(species)
    return tags


def adopt(pet_id):
    """Process an adoption for a pet by ID.

    Args:
        pet_id: Unique identifier of the pet to adopt.

    Returns:
        bool: True if pet was successfully adopted, False if not found or already adopted.
    """
    cur = conn.execute(
        "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
        (pet_id,),
    )
    if cur.rowcount > 0:
        adoption_stats["count"] += 1
        return True
    return False


def adoption_code():
    """Generate a unique adoption confirmation code.

    Returns:
        str: Adoption code prefixed with 'PET-'.
    """
    code_num = secrets.SystemRandom().randint(1000, 9999)
    return f"PET-{code_num}"


def oldest_available():
    """Find the name of the oldest pet currently available for adoption.

    Returns:
        str or None: Name of the oldest unadopted pet, or None if no pets are available.
    """
    try:
        cur = conn.execute("SELECT name, age FROM pets WHERE adopted = 0 ORDER BY age DESC")
        row = cur.fetchone()
        if row is not None:
            return row[0]
        return None
    except sqlite3.Error as err:
        logger.error("Database query failed: %s", err)
        return None


def clear_unadopted():
    """Remove records of all unadopted pets from the database.

    Returns:
        int: Number of deleted unadopted records.
    """
    try:
        cur = conn.execute("DELETE FROM pets WHERE adopted = 0")
        return cur.rowcount
    except sqlite3.Error as err:
        logger.error("Failed to clear unadopted pets: %s", err)
        return 0


def shelter_status():
    """Determine shelter status based on recorded adoptions.

    Returns:
        str: 'active' if any pets were adopted, otherwise 'quiet'.
    """
    if adoption_stats["count"] > 0: return "active"
    return "quiet"


def main():
    """Run shelter demonstration workflow."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)
    adopt(1)
    print(oldest_available(), adoption_code(), shelter_status())
    clear_unadopted()


if __name__ == "__main__":
    main()
