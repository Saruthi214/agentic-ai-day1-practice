import ast
import operator

from academic_config import SUBJECT_CREDITS


def get_subject_credits(subject_code: str) -> str:
    """Get the credit value of a subject."""
    credits = SUBJECT_CREDITS.get(subject_code.strip().upper())

    if credits is None:
        return f"Unknown subject code: {subject_code}"

    return str(credits)


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(
        node.value, (int, float)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](
            evaluate(node.left),
            evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](
            evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Perform basic arithmetic safely."""
    try:
        return str(
            evaluate(
                ast.parse(expression, mode="eval").body
            )
        )
    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_subject_credits": get_subject_credits,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_subject_credits",
            "description": (
                "Get the credit value for one subject code, "
                "such as CS501."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "subject_code": {
                        "type": "string"
                    }
                },
                "required": ["subject_code"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Calculate arithmetic expressions using "
                "+, -, *, / and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"],
            },
        },
    },
]