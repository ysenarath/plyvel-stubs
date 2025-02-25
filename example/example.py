import plyvel


def main():
    db = plyvel.DB("/tmp/testdb/", create_if_missing=True)
    db.put(b"key", b"value")
    print(db.get(b"key"))
    db.close()


if __name__ == "__main__":
    main()
