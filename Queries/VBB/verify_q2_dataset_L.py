#Compare Q2's (timestamp, vehicle ID) results with Dataset L references
#Before running this file deploy Q2 -> nes-cli -t Queries/VBB/Q2.yaml start

import csv
from collections import Counter


def reference_pairs(path):
    pairs = Counter()
    with open(path, newline='') as reference_matches:
        csvreader = csv.reader(reference_matches)
        next(csvreader)  # header
        for row in csvreader:
            if row[2] == "R1_center":
                pairs[(int(row[1]), int(row[3]))] += 1
    return pairs


def query_pairs(path):
    pairs = Counter()
    with open(path, newline='') as query_results:
        csvreader = csv.reader(query_results)
        next(csvreader)  #  header
        for row in csvreader:
            if len(row) < 2:
                raise ValueError("Q2 output must contain both ID and TS columns")
            pairs[(int(row[1]), int(row[0]))] += 1  # key is (TS, ID)
    return pairs


if __name__ == '__main__':
    reference = reference_pairs(
        'Queries/VBB/data/TestDatasets-BerlinMobility/L/reference_matches.csv'
    )
    actual = query_pairs('Output/vbb/q2.csv')

    missing = reference - actual
    unexpected = actual - reference
    print(f"Expected vehicles: {reference.total()}")
    print(f"Actual vehicles: {actual.total()}")

    if missing or unexpected:
        print(f"missing: {sum(missing.values())}")
        print(f"not wanted in the output: {sum(unexpected.values())}")
        if missing:
            print(f"Examples missing (TS, ID): {list(missing.items())[:10]}")
        if unexpected:
            print(f"Examples not wanted (TS, ID): {list(unexpected.items())[:10]}")
        raise SystemExit(1)

    print("[PASS] Alle Acutal-Treffer stimmen für R1_center mit der Referenz überein.")
