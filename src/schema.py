import json
from pathlib import Path

from pydantic import BaseModel, ValidationError


class ParameterSpec(BaseModel):
    type: str


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, ParameterSpec]
    returns: ParameterSpec


def load_function_definitions(path: Path) -> list[FunctionDefinition]:
    try:
        raw_text = path.read_text()
    except OSError as exc:
        raise RuntimeError(f"Could not read functions definition file at {path}: {exc}") from exc

    try:
        raw_data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

    try:
        return [FunctionDefinition.model_validate(item) for item in raw_data]
    except ValidationError as exc:
        raise RuntimeError(f"Function definitions in {path} do not match expected schema: {exc}") from exc
