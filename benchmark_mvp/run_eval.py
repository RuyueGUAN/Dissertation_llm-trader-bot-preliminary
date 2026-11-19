"""
Lightweight Evaluation Runner for LLM Trader Bot (Direction A)
Supports OpenAI and DeepSeek (OpenAI-compatible API).
Usage:
  export API_KEY="your_api_key"
  export BASE_URL="https://api.deepseek.com"   # Omit or set to OpenAI URL for GPT models
  export MODEL_NAME="deepseek-chat"            # e.g., deepseek-chat, gpt-4o
  python run_eval.py
"""

import json
import os
import time
from pathlib import Path
from openai import OpenAI

BASE_DIR = Path(__file__).parent
PROMPT_PATH = BASE_DIR / "system_prompt_v1.md"
CASES_PATH = BASE_DIR / "test_cases.json"
OUTPUT_DIR = BASE_DIR / "results"


def run_benchmark():
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL", "https://api.openai.com/v1")
    model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")

    if not api_key:
        raise ValueError("Please set the API_KEY environment variable before running.")

    client = OpenAI(api_key=api_key, base_url=base_url)
    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    benchmark = json.loads(CASES_PATH.read_text(encoding="utf-8"))

    OUTPUT_DIR.mkdir(exist_ok=True)
    records = []

    for case in benchmark["test_cases"]:
        print(f"Running {case['id']} ({case['category']}) on {model_name}...")
        start_time = time.perf_counter()

        response = client.chat.completions.create(
            model=model_name,
            temperature=0.0,  # Deterministic setting for reproducible benchmarking
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": case["user_input"]},
            ],
        )

        latency_sec = round(time.perf_counter() - start_time, 2)
        raw_content = response.choices[0].message.content

        try:
            parsed_json = json.loads(raw_content)
            valid_json = True
        except json.JSONDecodeError:
            parsed_json = None
            valid_json = False

        records.append({
            "case_id": case["id"],
            "model": model_name,
            "latency_sec": latency_sec,
            "valid_json": valid_json,
            "usage": response.usage.model_dump() if response.usage else {},
            "output": parsed_json if valid_json else raw_content,
        })

    out_file = OUTPUT_DIR / f"eval_{model_name.replace('/', '_')}.json"
    out_file.write_text(json.dumps(
