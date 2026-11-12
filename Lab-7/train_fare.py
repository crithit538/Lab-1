BERTHS = ["SU", "LB", "MB", "UB", "LB", "MB", "UB", "SL"]


def parse_pnr(pnr):
    if not isinstance(pnr, str):
        return None
    if len(pnr) != 10 or not pnr.isdigit():
        return None
    return int(pnr[0]), int(pnr[1:])


def journey_distance(distances_csv):
    if not isinstance(distances_csv, str):
        return None
    if not distances_csv.strip():
        return None
    try:
        parts = distances_csv.split(',')
        if any(not part.strip() for part in parts):
            return None
        distances = [int(part.strip()) for part in parts]
        return distances[-1] - distances[0]
    except ValueError:
        return None


def berth_type(seat):
    if not isinstance(seat, str):
        return None
    if seat.count('-') != 1:
        return None
    coach, number = seat.split('-')
    coach = coach.strip()
    number = number.strip()
    if not coach or not number.isdigit():
        return None
    return coach.upper(), BERTHS[int(number) % 8]


def main():
    print("==== Running parse_pnr ====")
    user_input = input("Enter a 10 digit PNR (e.g. 4521367890): ")
    result = parse_pnr(user_input)
    print("Zone and Number:", result)

    print("\n==== Running journey_distance ====")
    user_input = input("Enter station distances as CSV (e.g. 0,120,340): ")
    result = journey_distance(user_input)
    print("Total Distance:", result)

    print("\n==== Running berth_type ====")
    user_input = input("Enter coach and seat (e.g. S3-45): ")
    result = berth_type(user_input)
    print("Coach and Berth:", result)


if __name__ == "__main__":
    main()
