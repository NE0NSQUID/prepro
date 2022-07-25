"""drop drop"""
def main():
    """print"""
    sem1 = float(input())
    if sem1 < 1.00:
        print("I'm so sad.")
    elif sem1 < 2.00:
        print("%.2f"%(4.00 - sem1))
    elif sem1 >= 2.00:
        print("I'm so happy.")
main()
