import csv
import os
import flask_project, django_project, ansible_project, tornado_project, requests_project

import gather_metrics
from summarize_complexity import analyze_complexity_report
from summarize_mi import analyze_mi_results
from summarize_raw import analyze_raw_results

CSV_HEADERS = [
    'start_date',
    'commit',
    'num_files',
    'max_block_complexity',
    'min_block_complexity',
    'mean_block_complexity',
    'max_file_complexity',
    'min_file_complexity',
    'mean_file_complexity',
    'loc',
    'lloc',
    'sloc',
    'comments',
    'multi',
    'blank',
    'min_mi',
    'max_mi',
    'mean_mi'
]

if __name__ == '__main__':
    projects = requests_project,

    for project in projects:
        project_dir = os.path.join(gather_metrics.DATA_ROOT_DIR, project.DIR)
        commits = gather_metrics.gather_commits(project)

        lines = {}
        for date in commits:
            lines[date] = {'start_date': date, 'commit': commits[date]}
            file_name = '{}.json'.format(commits[date])

            dir_name = os.path.join(project_dir, 'complexity')
            print 'Summarizing complexity data for commit', commits[date]
            complexity_summary = analyze_complexity_report(
                os.path.join(dir_name, file_name))
            lines[date].update(complexity_summary)

            dir_name = os.path.join(project_dir, 'maintainability_index')
            print 'Summarizing MI data for commit', commits[date]
            mi_summary = analyze_mi_results(os.path.join(dir_name, file_name))
            lines[date].update(mi_summary)

            dir_name = os.path.join(project_dir, 'raw_metrics')
            print 'Summarizing raw data for commit', commits[date]
            raw_summary = analyze_raw_results(os.path.join(dir_name, file_name))
            lines[date].update(raw_summary)

        with open(os.path.join(project_dir, 'metrics_summary.csv'), 'w') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)

            writer.writeheader()
            for date in sorted(lines.keys()):
                writer.writerow(lines[date])
