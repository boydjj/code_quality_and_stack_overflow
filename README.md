Analyzing Python Project Code Metrics vs. Stack Overflow Activity
=================================================================
Data collection
---------------

 1. Each project folder under `data/` contains a file, `commits.txt`, which 
 documents the commit hashes explored for this analysis. These were gathered via 
 `gather_metrics.py`'s `gather_commits`.

 1. Inside each project are three folders, `complexity`, 
 `maintainability_index`, and `raw_metrics`, containing the JSON output of 
 `radon` for each of these commits. These were generated by having 
 `gather_metrics.py` operate on each project.

 1. These individual metric files were summarized via 
 `scripts/write_metric_summaries.py` into each project folder's 
 `metrics_summary.csv`.

 1. Each folder's `answered_vs_unanswered.csv` (which contains the total number 
 of questions as well as a breakdown of answered/unanswered questions) and 
 `answers.csv` (containing all answers, accepted or not) comes from the Stack
  Overflow data explorer via [parametrized][1] [queries][2].

 1. Finally, `data/concatenated_summaries.csv` is a combined CSV with all data 
 from each project's `answered_vs_unanswered.csv`, `answers.csv`, and
 `metrics_summary.csv`, slightly modified to include the project's name. This 
 was put together manually.

[1]: http://data.stackexchange.com/stackoverflow/query/296434/get-quarterly-breakdown-of-answered-unanswered-questions-for-a-tag
[2]: http://data.stackexchange.com/stackoverflow/query/296447/quarterly-number-of-answers-for-a-tag
