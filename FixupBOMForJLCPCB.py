#!/usr/bin/python3

# This program read a Kicad BOM CSV output from stdin or from a file
# supplied on the command line and generates a BOM in XLS format
# suitable for JLCPCB on standard output.  This involves rearranging
# the columns and changing the column names and renaming some
# footprints.

import sys
import csv
from openpyxl import Workbook

if len(sys.argv) < 3:
    sys.stderr.write("No CSV BOM file and XLS output file given\n")
    sys.exit(1)

if not sys.argv[1].endswith(".csv"):
    sys.stderr.write("First file doesn't end in '.csv': " + sys.argv[1] + "\n")
    sys.exit(1)

if not sys.argv[2].endswith(".xls"):
    sys.stderr.write("Second file doesn't end in '.xls': " + sys.argv[2] + "\n")
    sys.exit(1)

f = open(sys.argv[1])

cf = csv.reader(f, delimiter=';')
line = cf.__next__()
if len(line) != 7:
    sys.stderr.write("First line doesn't have 6 values, doesn't appear to be"
                     + " a Kicad BOM output")
    sys.exit(1)
    pass

expected_first_line = 'Id;Designator;Footprint;Quantity;Designation;Supplier and ref;'.split(";")
for i in range(0, len(expected_first_line)):
    if line[i] != expected_first_line[i]:
        sys.stderr.write("First line pos %d: Expected %s, got %s" %
                         (i, expected_first_line[i], line[i]))
        sys.exit(1)
        pass
    pass

footprint_xlats = {
    'R_0402_1005Metric': '0402',
    'R_0603_1608Metric': '0603',
    'R_0805_2012Metric': '0805',
    'R_1206_3216Metric': '1206',
    'C_0402_1005Metric': '0402',
    'C_0603_1608Metric': '0603',
    'C_0805_2012Metric': '0805',
    'C_1206_3216Metric': '1206',
    'L_0402_1005Metric': '0402',
    'L_0603_1608Metric': '0603',
    'L_0805_2012Metric': '0805',
    'L_1206_3216Metric': '1206',
    'D_0603_1608Metric': '0603',
    'D_SOD_323':         'SOD-323',
    'D_SOD_882':         'SOD-882',

    'C_0603_1608Metric_Pad1.08x0.95mm_HandSolder': '0603',
    'C_0805_2012Metric_Pad1.18x1.45mm_HandSolder': '0805',
    'R_0603_1608Metric_Pad0.98x0.95mm_HandSolder': '0603',
    'R_1206_3216Metric_Pad1.30x1.75mm_HandSolder': '1206',
    'L_0603_1608Metric_Pad1.05x0.95mm_HandSolder': '0603',
    'C_0402_1005Metric_Pad0.74x0.62mm_HandSolder': '0402',
    'LED_0603_1608Metric_Pad1.05x0.95mm_HandSolder': '0603',
    'L_1210_3225Metric_Pad1.42x2.65mm_HandSolder': '1210',
    'L_0402_1005Metric_Pad0.77x0.64mm_HandSolder': '0402',
    'R_0402_1005Metric_Pad0.72x0.64mm_HandSolder': '0402',
    'L_0805_2012Metric_Pad1.05x1.20mm_HandSolder': '0805',

    'SOT-23-5_HandSoldering': 'SOT-23-5',
    'SOT-23-6_HandSoldering': 'SOT-23-6',

    'TE_2118714-2': 'TE_2118714-2',
    'TE_2118718-2': 'TE_2118718-2',
}
def xlat_footprint(s):
    if s in footprint_xlats:
        return footprint_xlats[s]
    return s

comment_xlats = {
    '1nH': '0402CS-1N0XJRW',
    '3.3nH 2%': '0603DC-3N3XGRW',
    '6.9nH 2%': '0402DC-6N9XGRW',
    '11nH 2%': '0603DC-11NXGRW',
    '18nH 2%': '0603DC-18NXGRW',
    '18nH 2% 0402': '0402DC-18NXGRW',
    '22nH 2%': '0402DC-22NXGRW',
    '27nH 2%': '0603DC-27NXGRW',
    '36nH I>1A': '0603DC-36NXGRW',
    '43nH 2%': '0603DC-43NXGRW',
    '47nH 2%': '0603DC-47NXGRW',
    '78nH 2%': 'LQW18AN78NG8ZD',
    '91nH 2%': '0805CS-910XGRC',
    '180nH 2%': '0805CS-181XGRC',
    '': '',
}
def xlat_comment(s):
    if s in comment_xlats:
        return comment_xlats[s]
    return s

wb = Workbook()
ws = wb.active

lineno = 1
ws['A1'] = 'Comment'
ws['A2'] = 'Designator'
ws['A3'] = 'Footprint'

for line in cf:
    lineno += 1
    if len(line) != 8:
        sys.stderr.write("Line %s doesn't have 8 values, it has %d" %
                         (lineno, len(line)));
        sys.exit(1)
        pass
    comment = xlat_comment(line[4])
    comment = comment.replace(' ', ',')
    designator = line[1]
    footprint = xlat_footprint(line[2]).strip('"')
    ws.cell(lineno, 1, comment)
    ws.cell(lineno, 2, designator)
    ws.cell(lineno, 3, footprint)
    pass

wb.save(sys.argv[2])
