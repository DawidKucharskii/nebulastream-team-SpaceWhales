#For the Dataset L (Full Scan)

import csv

#R1 - defined in rectangles.csv R1_center,13.375,13.43,52.485,52.54
#befor running this file deploy Q2 -> nes-cli -t Queries/VBB/Q2.yaml start
def vehicles_in_r1_reference (path):
    total = 0
    with open(path, newline="") as referenceCounts:
        csvreader = csv.reader(referenceCounts)
        next(csvreader)
        for row in csvreader:
            if row[2] == "R1_center":
                total += int(row[3])

        return (total)

def vehicles_in_r1_Query2(path):
    total_rows = 0
    with open(path, newline="") as realCounts:
        csvreader = csv.reader(realCounts)
        next(csvreader)
        for row in csvreader:
           total_rows += 1
        return (total_rows)

if __name__ == '__main__':
    if __name__ == '__main__':
        expected = vehicles_in_r1_reference(
            'Queries/VBB/data/TestDatasets-BerlinMobility/L/reference_counts.csv'
        )
        actual = vehicles_in_r1_Query2('Output/vbb/q2.csv')

        print(f'Erwartet (Referenz): {expected}')
        print(f'Tatsächlich (NES Q2): {actual}')

        assert (
                expected == actual
        ), f'Abweichung! Erwartet: {expected}, erhalten: {actual}'
        print('[PASS] Q2 stimmt zu 100% mit der Ground Truth überein.')



