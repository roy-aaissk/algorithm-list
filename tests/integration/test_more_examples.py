import os
import sys
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def run_script(script_path, example_path):
    proc = subprocess.run([sys.executable, script_path], stdin=open(example_path, 'rb'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=ROOT)
    out = proc.stdout.decode().strip()
    if proc.returncode != 0:
        raise RuntimeError(f"Script {script_path} failed: {proc.stderr.decode()}")
    return out


def test_lower_bound_example():
    script = os.path.join(ROOT, 'search', 'lower_bound.py')
    example = os.path.join(ROOT, 'examples', 'lower_bound.txt')
    assert run_script(script, example) == '3'


def test_merge_sort_example():
    script = os.path.join(ROOT, 'sort', 'merge_sort.py')
    example = os.path.join(ROOT, 'examples', 'merge_sort.txt')
    assert run_script(script, example) == '1 2 3 5 7 8'


def test_heap_sort_example():
    script = os.path.join(ROOT, 'sort', 'heap_sort.py')
    example = os.path.join(ROOT, 'examples', 'heap_sort.txt')
    assert run_script(script, example) == '1 2 3 5 7 8'


def test_bubble_sort_example():
    script = os.path.join(ROOT, 'sort', 'bubble_sort.py')
    example = os.path.join(ROOT, 'examples', 'bubble_sort.txt')
    assert run_script(script, example) == '1 2 3 5 7 8'


def test_bfs_example():
    script = os.path.join(ROOT, 'graph', 'bfs.py')
    example = os.path.join(ROOT, 'examples', 'bfs.txt')
    assert run_script(script, example) == '0 1 2 3'


def test_sieve_example():
    script = os.path.join(ROOT, 'number', 'sieve.py')
    example = os.path.join(ROOT, 'examples', 'sieve.txt')
    assert run_script(script, example) == '2 3 5 7 11 13 17 19'


def test_lis_example():
    script = os.path.join(ROOT, 'dp', 'lis.py')
    example = os.path.join(ROOT, 'examples', 'lis.txt')
    assert run_script(script, example) == '3'
