"""
Analyze raw results output in JSON form by radon.
"""
import json
import pprint
import sys


def analyze_raw_results(filename):

    with open(filename) as f:
        data = json.loads(f.read())

    loc = 0
    lloc = 0
    sloc = 0
    comments = 0
    multi = 0
    blank = 0

    for filename in data:
        loc += data[filename]['loc']
        lloc += data[filename]['lloc']
        sloc += data[filename]['sloc']
        comments += data[filename]['comments']
        multi += data[filename]['multi']
        blank += data[filename]['blank']

    return {
        'loc': loc,
        'lloc': lloc,
        'sloc': sloc,
        'comments': comments,
        'multi': multi,
        'blank': blank,
        'num_files': len(data),
    }

if __name__ == '__main__':
    pprint.pprint(analyze_raw_results(sys.argv[1]))
