def ping_pong(pingArray, playerWins):
    print(f"\nStarting array: {pingArray}")
    i = 0
    while i < len(pingArray):
        # print(i)
        if pingArray[i] == "Ping" and i != 0:
            print(f"The insert i: {i}")
            pingArray.insert(i, "Pong")
            print(f"The array after insert: {pingArray}")
            i += 1
        i += 1
    if playerWins:
        pingArray.append("Pong")
    print(f"Ending array: {pingArray}")
    return pingArray

# Test Cases
pingPong1 = ["Ping"]
pingPong2 = ["Ping", "Ping", "Ping", "Ping", "Ping"]
pingPong3 = ["Ping", "Ping", "Ping"]
pingPong4 = ["Ping", "Ping", "Ping", "Ping", "Ping", "Ping", "Ping", "Ping", "Ping", "Ping"]

ping_pong(pingPong1, True)
ping_pong(pingPong2, False)
ping_pong(pingPong3, True)
ping_pong(pingPong4, False)