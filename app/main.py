def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": "passed" if not errors else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    # [{"errors": [], "path": "./test_source_code_2.py", "status": "passed"}, format_single_linter_file(file_path, errors) for file in linter_report]
    return [format_single_linter_file(file_path, linter_report[file_path]) for file_path in linter_report]
