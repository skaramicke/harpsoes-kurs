import json


def data():
    return [
        {
            "name": "robot 1",
            "installation date": "2020-09-16 08:00:00",
            "event log": [
                {
                    "type": "process event",
                    "time-of-start": 12952315,
                    "product": "70086cad-ksr35",
                    "event-length": 175000,
                    "id": "487be270"
                },
                {
                    "type": "process event",
                    "time-of-start": 7047255,
                    "product": "93d3bf71-plt55",
                    "event-length": 155000,
                    "id": "4fec1a27"
                },
                {
                    "type": "process event",
                    "time-of-start": 13908392,
                    "product": "cb81cb46-plt55",
                    "event-length": 155000,
                    "id": "5be66821"
                },
                {
                    "type": "process event",
                    "time-of-start": 21986420,
                    "product": "d65386b5-plt55",
                    "event-length": 127000,
                    "id": "ad2653a3"
                }
            ],
            "next inspection": "2023-10-10 14:40:00",
            "active": True
        },
        {
            "name": "robot 2",
            "installation date": "2020-01-11 08:00:00",
            "event log": [
                {
                    "type": "process event",
                    "time-of-start": 3420510,
                    "product": "2dc98276-ksr35",
                    "event-length": 181000,
                    "id": "1576211b"
                },
                {
                    "type": "process event",
                    "time-of-start": 21764844,
                    "product": "ed196d4a-plt55",
                    "event-length": 169000,
                    "id": "70540cd4"
                },
                {
                    "type": "process event",
                    "time-of-start": 13398860,
                    "product": "14705d35-plt55",
                    "event-length": 165000,
                    "id": "3b72fec0"
                }
            ],
            "next inspection": "2023-10-14 10:40:00",
            "active": False
        },
        {
            "name": "robot 4",
            "installation date": "2021-08-15 08:00:00",
            "event log": [
                {
                    "type": "process event",
                    "time-of-start": 4687736,
                    "product": "09d57d9d-ksr35",
                    "event-length": 171000,
                    "id": "c8545b72"
                },
                {
                    "type": "process event",
                    "time-of-start": 9705159,
                    "product": "55810e65-ksr35",
                    "event-length": 193000,
                    "id": "fc892004"
                },
                {
                    "type": "process event",
                    "time-of-start": 15667650,
                    "product": "6b111460-plt55",
                    "event-length": 170000,
                    "id": "f3f5f1dd"
                },
                {
                    "type": "process event",
                    "time-of-start": 2664399,
                    "product": "04b3a2cf-plt55",
                    "event-length": 171000,
                    "id": "57179705"
                },
                {
                    "type": "process event",
                    "time-of-start": 8366721,
                    "product": "8c7129c8-ksr35",
                    "event-length": 189000,
                    "id": "8da48a6e"
                }
            ],
            "next inspection": "2023-10-13 13:20:00",
            "active": False
        },
        {
            "name": "robot 3",
            "installation date": "2020-05-06 08:00:00",
            "event log": [
                {
                    "type": "process event",
                    "time-of-start": 1516433,
                    "product": "9142d18f-ksr35",
                    "event-length": 174000,
                    "id": "48e321c0"
                },
                {
                    "type": "process event",
                    "time-of-start": 27754570,
                    "product": "7b2c178f-plt55",
                    "event-length": 140000,
                    "id": "6ef6737b"
                },
                {
                    "type": "process event",
                    "time-of-start": 27812562,
                    "product": "a15c58cd-ksr35",
                    "event-length": 184000,
                    "id": "beeadf5a"
                },
                {
                    "type": "process event",
                    "time-of-start": 8183557,
                    "product": "3c06b533-plt55",
                    "event-length": 158000,
                    "id": "18a9df37"
                }
            ],
            "next inspection": "2023-10-12 08:40:00",
            "active": True
        }
    ]


def extractEvent(index, data):
    return data[index]["event log"]


def getAverageEventLength(eventLog):
    sum = 0
    for event in eventLog:
        sum += event["event-length"]

    return sum / len(eventLog)


def filterEventLogByStartTimeMatching(eventLog, start, stop):
    filteredEvents = []
    for event in eventLog:
        if event["time-of-start"] >= start and event["time-of-start"] <= stop:
            filteredEvents.append(event)

    return filteredEvents


def filterEventLogByProductSuffix(eventLog, suffix):
    filteredEvents = []
    for event in eventLog:
        if event["product"].endswith(suffix):
            filteredEvents.append(event)

    return filteredEvents


if __name__ == '__main__':

    # read the list
    data = data()

    print("Uppgift 0A")
    print(data[0])

    print("Uppgift 0B")
    print(data[0]["event log"])

    print("Uppgift 1")
    print(extractEvent(0, data))

    print("Uppgift 2a")

    print("Uppgift 2b")
    averageEventLength = getAverageEventLength(extractEvent(0, data))
    print(averageEventLength)

    print("Uppgift 3a")

    print("Uppgift 3b")

    # Get start time from user
    start = int(input("Start time: "))

    # Get stop time from user
    stop = int(input("Stop time: "))

    combinedEventLog = []
    for robot in data:
        filteredEventLog = filterEventLogByStartTimeMatching(
            robot["event log"], start, stop)
        combinedEventLog.extend(filteredEventLog)
    averageEventLength = getAverageEventLength(combinedEventLog)
    print("Combined Average event length: " + str(averageEventLength))

    print("Uppgift 4")
    combinedEventLog = []
    for robot in data:
        filteredEventLog = filterEventLogByProductSuffix(
            robot["event log"], "plt55")
        combinedEventLog.extend(filteredEventLog)

    averageEventLength = getAverageEventLength(combinedEventLog)
    print("Combined Average event length, plt55: " + str(averageEventLength))
