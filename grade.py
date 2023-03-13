import os
import re
from glob import glob
import zipfile
import shutil
import subprocess
import argparse
from config import SOLUTIONS_DIR, SOLUTION_DIR, TESTER_PATH


def matching_solutions(pattern: str):
    solutions = os.listdir(SOLUTIONS_DIR)
    cpattern = re.compile(pattern)
    return [os.path.join(SOLUTIONS_DIR, solution) for solution in solutions if cpattern.match(solution)]


def select_solution(keywords: list[str]):
    solutions = matching_solutions(".*" + ".*".join(keywords) + ".*")
    assert len(solutions) == 1, ("Expected one matching solution found:", solutions)
    return solutions[0]


def zip_solution(path: str):
    zip_paths = glob(os.path.join(path, "*.zip"))
    if len(zip_paths) != 1:
        return False
    zip_path = zip_paths[0]
    os.mkdir(SOLUTION_DIR)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(SOLUTION_DIR)
    return True


def direct_solution(path: str):
    if len(glob(os.path.join(path, '**/*.htm*'), recursive=True)) < 1:
        return False
    if len(glob(os.path.join(path, '**/*.css'), recursive=True)) < 1:
        return False
    shutil.copytree(path, SOLUTION_DIR)
    return True


def prep_clear_solution():
    if os.path.exists(SOLUTION_DIR):
        shutil.rmtree(SOLUTION_DIR)


def focus(keywords: list[str]):
    prep_clear_solution()
    solution = select_solution(keywords)
    # trying different solutions schema
    assert zip_solution(solution) or direct_solution(solution)


def run_tester():
    subprocess.run(f"PROJECT_PATH={os.path.abspath(SOLUTION_DIR)} ./test.sh", shell=True, cwd=TESTER_PATH)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", nargs="*", type=str, help="specifies pattern with which solution folder is searched for")
    parser.add_argument("-n", "--no_tests", help="dont run tests after extracting solution", action="store_true")

    args = parser.parse_args()
    focus(args.keyword)
    if not args.no_tests:
        run_tester()
