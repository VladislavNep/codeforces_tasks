from collections import deque


def person_is_seller(person):
    pass


def search(name):
    graph = {}
    search_queue = deque()
    search_queue += graph["my"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("yes!")
                return True
            else:
                search_queue += graph[person]
    return False
