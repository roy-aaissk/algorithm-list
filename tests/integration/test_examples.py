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


def test_linear_example():
    script = os.path.join(ROOT, 'search', 'linear.py')
    example = os.path.join(ROOT, 'examples', 'linear.txt')
    assert run_script(script, example) == '2'


def test_binary_example():
    script = os.path.join(ROOT, 'search', 'binary.py')
    example = os.path.join(ROOT, 'examples', 'binary.txt')
    assert run_script(script, example) == '3'


def test_quick_sort_example():
    script = os.path.join(ROOT, 'sort', 'quick_sort.py')
    example = os.path.join(ROOT, 'examples', 'quick_sort.txt')
    assert run_script(script, example) == '1 2 3 5 7 8'


def test_dijkstra_example():
    script = os.path.join(ROOT, 'graph', 'dijkstra.py')
    example = os.path.join(ROOT, 'examples', 'dijkstra.txt')
    assert run_script(script, example) == '0 1 3 4'


def test_knapsack_example():
    script = os.path.join(ROOT, 'dp', 'knapsack_01.py')
    example = os.path.join(ROOT, 'examples', 'knapsack.txt')
    assert run_script(script, example) == '220'


def test_kmp_example():
    script = os.path.join(ROOT, 'strings', 'kmp.py')
    example = os.path.join(ROOT, 'examples', 'kmp.txt')
    assert run_script(script, example) == '6'
