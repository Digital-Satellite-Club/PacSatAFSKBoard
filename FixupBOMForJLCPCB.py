#!/usr/bin/python3

# This program read a Kicad BOM output from stdin or from a file
# supplied on the command line and generates a BOM suitable for JLCPCB
# on standard output.  This involves rearranging the columns and
# changing the column names and renaming some footprints.

import sys
import csv

if len(sys.argv) > 1:
    f = open(sys.argv[1])
else:
    f = sys.stdin

cf = csv.reader(f, delimiter=';')
line = cf.__next__()
if len(line) != 7:
    sys.stderr.write("First line doesn't have 6 values, doesn't appear to be"
                     + " a Kicad BOM output")
    sys.exit(1)
    pass

ocf = csv.writer(sys.stdout)

expected_first_line = 'Id;Designator;Footprint;Quantity;Designation;Supplier and ref;'.split(";")
for i in range(0, len(expected_first_line)):
    if line[i] != expected_first_line[i]:
        sys.stderr.write("First line pos %d: Expected %s, got %s" %
                         (i, expected_first_line[i], line[i]))
        sys.exit(1)
        pass
    pass
ocf.writerow(('Comment', 'Designator', 'Footprint'))

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
}
def xlat_footprint(s):
    if s in footprint_xlats:
        return footprint_xlats[s]
    return s

comment_xlats = {
    '78n,2%,Q=28': 'LQW18AN78NG8ZD',
    '18n,2%,Q=58': 'AISC-Q0402HQ-18NG-T',
    '22n 2% Q=67': '0402DC-22NXGRW',
    '6.9n 2% Q=69': '0402DC-6N9XGRW',
    '36n Q>40 I>1A': '0603DC-36NXGRW',
    '180n 2% Q=50': 'LQW2BANR18G00L',
    '91n 2% Q=64': '0603DC-91NXGRW',
    '47n 2% Q=73': '0603DC-47NXGRW',
    '27n 2% Q=82': '0603DC-27NXGRW',
    '43n 2% Q=82': '0603DC-43NXGRW',
    '78n 2% Q=28': '0603DC-43NXGRW',
    '1n Q=77': '0402CS-1N0XJRW',
    '': '',
    '': '',
    '': '',
}
def clat_comment(s):
    if s in comment_xlats:
        return comment_xlats[s]
    return s

lineno = 1
for line in cf:
    lineno += 1
    if len(line) != 8:
        sys.stderr.write("Line %s doesn't have 8 values, it has %d" %
                         (lineno, len(line)));
        sys.exit(1)
        pass
    comment = xlat_comment(line[4])
    comment = cmoment.replace(' ', ',')
    comment = comment.replace('Ω', 'ohm')
    footprint = xlat_footprint(line[2]).strip('"')
    ocf.writerow((comment, line[1], footprint))
    pass
