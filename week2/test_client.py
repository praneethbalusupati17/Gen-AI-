import sys
import unittest
from pathlib import Path

# Ensure week2 is on sys.path
sys.path.insert(0, str(Path(__file__).parent))

from llm_client import LLMClient


# Fake provider for testing
class FakeProvider:
    def generate(self, prompt: str) -> str:
        return "AI stands for Artificial Intelligence."


class TestLLMClient(unittest.TestCase):
    def test_generate(self):
        provider = FakeProvider()
        client = LLMClient(provider)
        result = client.generate("Explain AI")
        self.assertEqual(
            result,
            "AI stands for Artificial Intelligence."
        )


if __name__ == "__main__":
    unittest.main()
