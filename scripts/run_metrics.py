import os
import subprocess
import sys


def gather_metrics(commit, project_dir, data_dir):
    filename = '{}.json'.format(commit)

    # Check out commit
    subprocess.call(['git', 'checkout', commit], cwd=project_dir)
    excluded_filenames = subprocess.check_output(['find', '.', '-type', 'f', '-empty'], cwd=project_dir).replace('\n', ',')

    # Execute radon cc
    target_filename = os.path.join(os.path.join(data_dir, 'complexity'), filename)
    with open(target_filename, 'w') as f:
        print "Gathering complexity metrics for commit {}...".format(commit)
        subprocess.call(['radon', 'cc', '-s', '-j', '--total-average', '-e',
                         excluded_filenames, '.'], cwd=project_dir, stdout=f)
        print "Done."

    # Execute radon mi
    target_filename = os.path.join(os.path.join(data_dir, 'maintainability_index'), filename)
    with open(target_filename, 'w') as f:
        print "Gathering MI metrics for commit {}...".format(commit)
        subprocess.call(['radon', 'mi', '-s', '-j', '-e',
                         excluded_filenames, '.'], cwd=project_dir, stdout=f)
        print "Done."

    # Execute radon raw
    target_filename = os.path.join(os.path.join(data_dir, 'raw_metrics'), filename)
    with open(target_filename, 'w') as f:
        print "Gathering raw metrics for commit {}...".format(commit)
        subprocess.call(['radon', 'raw', '-s', '-j', '-e',
                         excluded_filenames, '.'], cwd=project_dir, stdout=f)
        print "Done."

    sys.stdout.flush()

if __name__ == '__main__':
    EXAMPLE_COMMITS = {  # These are from Flask
        '2010-04-01 00:00:00': '33850c0ebd23ae615e6823993d441f46d80b1ff0',
        '2010-07-01 00:00:00': 'bc662a546ed9028d93482f79314e64beae19a1d6',
        '2011-01-01 00:00:00': '4c76607553e92f6e1b03930e053cc7078fc32f8d',
        '2011-04-01 00:00:00': 'a06cd0a64418f2aafafb0a574c64c2ea5f3e9239',
        '2011-07-01 00:00:00': '15372661af2974577d5c1d15fdaf88452661c2a9',
        '2011-10-01 00:00:00': '3765cc2e9e6ea2d227f898d5b176aa50680e491c',
        '2012-01-01 00:00:00': '065afe53a6f72e42428c4373ed10d082868f25d6',
        '2012-04-01 00:00:00': 'c2698416a835dfb5d0e52e8c291ea43eaa3d1757',
        '2012-07-01 00:00:00': 'd5218997d927be869dd55ef04542e1bbc1e69653',
        '2012-10-01 00:00:00': 'ee76129812419d473eb62434051e81d5855255b6',
        '2013-01-01 00:00:00': 'ff2e8449ffbb37cb8ebf4d7575c0e9102c78e772',
        '2013-04-01 00:00:00': '6309987dca72ebe62539ce7b851a072f4e4e9173',
        '2013-07-01 00:00:00': '4028e2395c3b559ca65db13fb1407c79ca79a4c7',
        '2013-10-01 00:00:00': '3e485009a8ca606c742c88c92cfd178547b708cd',
        '2014-01-01 00:00:00': 'dbc40961913381ecf1513fa2467aefeef6d4d41b',
        '2014-04-01 00:00:00': 'b2b531a36bab939f76df51b7ae88f87e60eea8f6',
        '2014-07-01 00:00:00': '0ce47a365f4618f19b5b5c59c33f70c4f69157c0',
        '2014-10-01 00:00:00': 'b9237121ec94558a95fcb117d84f40c853930a74',
        '2015-01-01 00:00:00': '4fde65eb7a9cb2495c2ffd0eb86a3c3cbba98628',
    }

    for date in EXAMPLE_COMMITS:
        gather_metrics(EXAMPLE_COMMITS[date], sys.argv[1], sys.argv[2])
