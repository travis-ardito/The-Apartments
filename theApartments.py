import random

def main():
    floor1:int = random.randint(1, 7)
    floor2:int = random.randint(1, 6)
    floor3:int = random.randint(1, 5)
    currentFloor = 1

    # floor rotations:
    # lower: -1
    # upper: +1

    loop = True
    doors = "neutral"

    while loop:
        val = True

        floor_list = [[floor1, "1"], [floor2, "2"], [floor3, "3"]]
        print(f"\nCurrent: Floor {currentFloor}, Room {floor_list[currentFloor - 1][0]}")
        del floor_list[currentFloor - 1]
        print(f"Other: Floor {floor_list[0][1]}: {floor_list[0][0]}, Floor {floor_list[1][1]}: {floor_list[1][0]}")

        if doors == "lr" or doors == "neutral":
            if mystery_int := random.randint(1, 8) == 8:
                print("Mystery Hallway appears")

        if doors == "lr":
            door_int = random.randint(1, 6)
            if  door_int == 1:
                print("Doors: Dead end\n")
            elif door_int == 5 or door_int == 6:
                print("Doors: Entrance blocked\n")
            else:
                print("Doors: Both open\n")
        elif doors == "neutral":
            door_int = random.randint(1, 4)
            if door_int == 1:
                print("Doors: Left open\n")
            elif door_int == 2:
                print("Doors: Right open\n")
            else:
                print("Doors: Both open\n")

        while val:
            command = input("Left, right, up, down, shift, mystery, or end? ").lower()
            if command == "l" or command == "left":
                val = False
                doors = "lr"
                if currentFloor == 1:
                    floor1 -= 1
                    floor2 -= 2
                elif currentFloor == 2:
                    floor1 -= 2
                    floor2 -= 1
                else:
                    floor1 -= 2
                    floor3 -= 1

            elif command == "r" or command == "right":
                val = False
                doors = "lr"
                if currentFloor == 1:
                    floor1 += 1
                    floor3 += 2
                elif currentFloor == 2:
                    floor2 += 1
                    floor3 += 2
                else:
                    floor2 += 2
                    floor3 += 1

            elif command == "u" or command == "up":
                if currentFloor != 3:
                    val = False
                    doors = "neutral"
                    currentFloor += 1
            elif command == "d" or command == "down":
                if currentFloor != 1:
                    val = False
                    doors = "neutral"
                    currentFloor -= 1
            elif command == "s" or command == "shift":
                val = False
                doors = "none"
                if currentFloor == 1:
                    floor2 -= 1
                    floor3 += 1
                elif currentFloor == 2:
                    floor1 -= 1
                    floor3 += 1
                else:
                    floor1 -= 1
                    floor2 += 1
            elif command == "m" or command == "mystery":
                val = False
                doors = "neutral"
                currentFloor = random.randint(1, 3)
                floor1 = random.randint(1, 7)
                floor2 = random.randint(1, 6)
                floor3 = random.randint(1, 5)
            elif command == "e" or command == "end":
                loop = False
                break
            elif command == "man" or command == "manual":
                val = False
                doors = "none"
                floor1 = int(input("Floor 1: "))
                floor2 = int(input("Floor 2: "))
                floor3 = int(input("Floor 3: "))
            if val:
                print("Invalid command. Please try again.\n")

        if loop:
            floor1 = circ(floor1, 7)
            floor2 = circ(floor2, 6)
            floor3 = circ(floor3, 5)
        #
        #     floor_list = [[floor1, "1"], [floor2, "2"], [floor3, "3"]]
        #     print(f"Current: Floor {currentFloor}, Room {floor_list[currentFloor - 1][0]}")
        #     del floor_list[currentFloor - 1]
        #     print(f"Other: Floor {floor_list[0][1]}: {floor_list[0][0]}, Floor {floor_list[1][1]}: {floor_list[1][0]}\n")




def circ(value, top):
    if value > top:
        return 0 + (value - top)
    elif value < 1:
        return top - (0 - value)
    else:
        return value

main()