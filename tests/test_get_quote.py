import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "get-quote.py"
QUOTES = (REPO / "quotes.txt").read_text(encoding="utf-8").splitlines()


def run_script(cwd):
    return subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


class GetQuoteTest(unittest.TestCase):
    def test_prints_a_quote_from_quotes_file(self):
        result = run_script(REPO)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(result.stdout.strip(), QUOTES)

    def test_works_when_run_from_another_directory(self):
        with tempfile.TemporaryDirectory() as elsewhere:
            result = run_script(elsewhere)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(result.stdout.strip(), QUOTES)


if __name__ == "__main__":
    unittest.main()
