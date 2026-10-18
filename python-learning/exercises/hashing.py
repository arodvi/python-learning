"""Explore hash() and dictionary insertion order."""


if __name__ == "__main__":
    first_name = "Alan"
    second_name = "Maya"

    print("Hash of Alan:", hash(first_name))
    print("Hash of Maya:", hash(second_name))
    print("Same key, same hash in this process:", hash(first_name) == hash("Alan"))

    # A string's hash may be different on the next Python run.
    # Hash values are NOT fixed list positions or dictionary order.
    students = {"Alan": 7, "Maya": 9}
    students["Sam"] = 4
    print("Dictionary insertion order:", list(students))
