"""
Analyze complexity results output in JSON form by radon.
"""
import json

def analyze_mi_results(filename):

    with open(filename) as f:
        data = json.loads(f.read())

    min_mi = 1000
    max_mi = 0
    total_mi = 0

    for filename in data:
        min_mi = min(min_mi, data[filename]['mi'])
        max_mi = max(max_mi, data[filename]['mi'])
        total_mi += data[filename]['mi']

    return {
        'min_mi': min_mi,
        'max_mi': max_mi,
        'mean_mi': total_mi / len(data),
    }

if __name__ == '__main__':
    import sys, pprint
    pprint.pprint(analyze_mi_results(sys.argv[1]))
