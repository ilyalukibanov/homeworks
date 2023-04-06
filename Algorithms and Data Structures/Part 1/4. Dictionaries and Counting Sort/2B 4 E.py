n = int(input())
topics_connections = {}
topics = {}
counter = 1

for i in range(n):
    s = int(input())
    if s == 0:
        topics[counter] = input()
        _ = input()
        topics_connections[counter] = [counter]
    else:
        _ = input()
        for key in topics_connections.keys():
            if s in topics_connections[key]:
                # print(s, 's')
                # print(key, 'key')
                topics_connections[key].append(counter)
    # print(counter)
    # print(topics_connections)
    counter += 1

max_messages = 0
topic = ''
for key in sorted(topics_connections.keys()):
    if len(topics_connections[key]) > max_messages:
        max_messages = len(topics_connections[key])
        topic = topics[key]
print(topic)
