"""
Analyze complexity results output in JSON form by radon.
"""
import json
import pprint
import sys


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

    for filename in data:
        file_complexity = 0
        for block in data[filename]:
            num_blocks += 1
            if isinstance(block, basestring):
                # Syntax errors in code cause radon to set this to 'error'
                continue
            block_complexity = block['complexity']
            total_block_complexity += block_complexity
            file_complexity += block_complexity
            
            max_block_complexity = max(max_block_complexity, block_complexity)
            min_block_complexity = min(min_block_complexity, block_complexity)

        # Store all file-level complexity data for mean later
        total_file_complexity += file_complexity

        # Update min/max if necessary
        max_file_complexity = max(max_file_complexity, file_complexity)
        min_file_complexity = min(min_file_complexity, file_complexity)

    return {
        'max_file_complexity': max_file_complexity,
        'min_file_complexity': min_file_complexity,
        'max_block_complexity': max_block_complexity,
        'min_block_complexity': min_block_complexity,
        'mean_file_complexity': total_file_complexity / float(len(data)),
        'mean_block_complexity': total_block_complexity / float(num_blocks),
    }

if __name__ == '__main__':
    pprint.pprint(analyze_complexity_report(sys.argv[1]))
