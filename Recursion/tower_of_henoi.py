def tower_of_hanoi(source, dest, help, n):
    if n==1:
        print(f"Plate {n} from {source} to {dest}")
        return
    tower_of_hanoi(source,help,dest,n-1)
    print(f"Plate {n} from {source} to {dest}")
    tower_of_hanoi(help,dest,'s',n-1)

tower_of_hanoi('s','d','h',3)