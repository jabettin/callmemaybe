import json
from pathlib import Path

from pydantic import BaseModel, ValidationError

class PromptSpec(BaseModel):
    prompt: str


def prompt_loader(path: Path) -> list[PromptSpec]:
    try:
        raw_text = path.read_text()
    except OSError as exc:
        raise RuntimeError(f"Could not read definition file at {path}: {exc}") from exc

    try:
        raw_data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

    try:
        return [PromptSpec.model_validate(item) for item in raw_data]
    except ValidationError as exc:
        raise RuntimeError(f"Prompts in {path} do not match expected schema: {exc}") from exc
