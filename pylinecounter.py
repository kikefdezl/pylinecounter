from argparse import ArgumentParser
from pathlib import Path
from dataclasses import dataclass
import bisect


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "directory",
        help="Path to the directory containing a python project.",
        type=str,
    )
    parser.add_argument(
        "--top_k",
        help="How many 'top number of lines' files to show.",
        default=3,
        type=int,
    )
    args = parser.parse_args()
    return args


@dataclass
class File:
    name: str
    n_lines: int


def main():
    args = parse_args()
    directory = Path(args.directory)
    python_files = [f for f in Path(directory).rglob("*") if f.suffix.lower() == ".py"]

    top_files = [File(name="dummy", n_lines=-1)]
    total_lines, total_test_lines = 0, 0
    for file in python_files:
        with open(file, "r") as pyfile:
            n_lines = len(pyfile.readlines())

        filename = file.relative_to(directory)

        if n_lines > top_files[0].n_lines:
            f = File(name=filename, n_lines=n_lines)
            bisect.insort(top_files, f, key=lambda x: x.n_lines)
            if len(top_files) > args.top_k:
                top_files = top_files[len(top_files) - args.top_k:]

        total_lines += n_lines
        if "test" in filename.as_posix():
            total_test_lines += n_lines

        print(f"{filename}: {n_lines} lines.")

    print()
    print("---")
    print()
    print(f"Total lines: {total_lines}")
    print(f"Test lines: {total_test_lines}")
    print()
    print(f"Total files: {len(python_files)}")
    print("Top files:")
    for file in top_files[::-1]:
        print(f" - {file.name}: {file.n_lines} lines.")
    print()
    print("---")


if __name__ == "__main__":
    main()
