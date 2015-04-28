"""
Analyze complexity results output in JSON form by radon.
"""
import json

def analyze_complexity_report(filename):

    with open(filename) as f:
        data = json.loads(f.read())

    min_file_complexity = 1000
    max_file_complexity = 0
    min_block_complexity = 1000
    max_block_complexity = 0
    total_file_complexity = 0
    total_block_complexity = 0
    num_blocks = 0

    least_complex_file = None
    most_complex_file = None

    for filename in data:
        file_complexity = 0
        for block in data[filename]:
            num_blocks += 1
            block_complexity = block['complexity']
            total_block_complexity += block_complexity
            file_complexity += block_complexity
            
            max_block_complexity = max(max_block_complexity, block_complexity)
            min_block_complexity = min(min_block_complexity, block_complexity)

        # Store all file-level complexity data for mean later
        total_file_complexity += file_complexity

        # Update min/max if necessary
        if file_complexity > max_file_complexity:
            max_file_complexity = file_complexity
            most_complex_file = filename
        if file_complexity < min_file_complexity:
            min_file_complexity = file_complexity
            least_complex_file = filename

    return {
        'max_file_complexity': max_file_complexity,
        'min_file_complexity': min_file_complexity,
        'max_block_complexity': max_block_complexity,
        'min_block_complexity': min_block_complexity,
        'mean_file_complexity': total_file_complexity / float(len(data)),
        'mean_block_complexity': total_block_complexity / float(num_blocks),
        'most_complex_file': most_complex_file,
        'least_complex_file': least_complex_file
    }

if __name__ == '__main__':
    import sys, pprint
    pprint.pprint(analyze_complexity_report(sys.argv[1]))
