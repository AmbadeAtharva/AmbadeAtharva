from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIDTH = 1160

THEMES = {
    "light": {
        "background": "#f7f8fa",
        "panel": "#ffffff",
        "ink": "#14202b",
        "muted": "#5d6b77",
        "line": "#d9e1e7",
        "accent": "#007f8b",
        "accent_soft": "#d9f2f1",
    },
    "dark": {
        "background": "#10161c",
        "panel": "#17212a",
        "ink": "#f0f5f7",
        "muted": "#a7b6bf",
        "line": "#31404a",
        "accent": "#62d9d4",
        "accent_soft": "#1b4144",
    },
}


def text(value: str, x: int, y: int, size: int, fill: str, weight: int = 400) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="ui-monospace, SFMono-Regular, '
        f'Menlo, Monaco, Consolas, monospace" font-size="{size}px" font-weight="{weight}">'
        f"{escape(value)}</text>"
    )


def rect(x: int, y: int, width: int, height: int, fill: str, stroke: str = "none", radius: int = 0) -> str:
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def line(x1: int, y1: int, x2: int, y2: int, stroke: str, width: int = 1) -> str:
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{stroke}" stroke-width="{width}" fill="none"/>'


def svg(theme: dict[str, str], height: int, content: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" role="img">'
        f"{rect(0, 0, WIDTH, height, theme['background'])}{content}</svg>\n"
    )


def shell(theme: dict[str, str], label: str, number: str, title: str) -> str:
    return (
        rect(32, 24, WIDTH - 64, 56, theme["panel"], theme["line"], 8)
        + text(f"{number} / {label}", 56, 59, 14, theme["accent"], 700)
        + text(title, 315, 59, 22, theme["ink"], 700)
    )


def header(theme: dict[str, str]) -> str:
    content = shell(theme, "IDENTITY", "00", "AI SYSTEMS CONTROL PLANE")
    content += text("ATHARVA AMBADE", 56, 145, 44, theme["ink"], 700)
    content += text("AI ENGINEER", 58, 181, 20, theme["accent"], 700)
    content += text("BACKEND & SYSTEMS ENGINEER", 58, 211, 20, theme["ink"], 700)
    content += text("Building reliable AI applications, backend platforms,", 58, 257, 18, theme["muted"])
    content += text("agentic workflows, and cloud infrastructure.", 58, 284, 18, theme["muted"])
    content += rect(690, 130, 414, 168, theme["panel"], theme["line"], 8)
    content += text("SYSTEM FLOW", 720, 161, 13, theme["accent"], 700)
    nodes = ["INPUT", "API", "AGENT / MODEL", "DATA", "INFRA", "OBSERVE"]
    for index, node in enumerate(nodes):
        x = 720 + index * 62
        content += rect(x, 202, 48, 34, theme["accent_soft"], "none", 5)
        content += text(node, x + 24 - (len(node) * 3), 223, 8, theme["ink"], 700)
        if index < len(nodes) - 1:
            content += line(x + 48, 219, x + 59, 219, theme["accent"], 2)
    content += text("SAN FRANCISCO BAY AREA", 58, 348, 13, theme["muted"], 700)
    content += text("OPEN TO AI / SOFTWARE ENGINEERING OPPORTUNITIES", 315, 348, 13, theme["muted"], 700)
    content += text("PYTHON  /  TYPESCRIPT  /  RUST  /  GO", 770, 348, 13, theme["muted"], 700)
    content += line(56, 379, WIDTH - 56, 379, theme["line"])
    return svg(theme, 412, content)


def whoami(theme: dict[str, str]) -> str:
    content = shell(theme, "WHOAMI", "01", "ENGINEERING IDENTITY")
    blocks = [
        ("WHAT I BUILD", "Production AI applications,", "backend services, distributed workflows,", "and cloud automation."),
        ("HOW I WORK", "Measure bottlenecks, design", "reliable interfaces, automate delivery,", "and validate results."),
        ("CURRENT INTERESTS", "Agentic systems, inference", "infrastructure, developer tools,", "backend performance, observability."),
    ]
    for index, block in enumerate(blocks):
        x = 56 + index * 350
        content += rect(x, 122, 318, 156, theme["panel"], theme["line"], 8)
        content += text(f"0{index + 1}", x + 22, 153, 14, theme["accent"], 700)
        content += text(block[0], x + 22, 184, 14, theme["ink"], 700)
        content += text(block[1], x + 22, 220, 14, theme["muted"])
        content += text(block[2], x + 22, 244, 14, theme["muted"])
        content += text(block[3], x + 22, 268, 14, theme["muted"])
    return svg(theme, 318, content)


def system_map(theme: dict[str, str]) -> str:
    content = shell(theme, "SYSTEM MAP", "02", "FROM MODEL TO OPERATING SYSTEM")
    columns = [
        ("AI + AGENTS", ["LLM applications", "MCP integrations", "RAG + retrieval", "Evaluation"]),
        ("BACKEND + SYSTEMS", ["APIs + services", "Distributed processing", "Concurrency + caching", "Databases"]),
        ("INFRASTRUCTURE", ["AWS + Azure + GCP", "Docker + Kubernetes", "Terraform + CI/CD", "Observability"]),
    ]
    for index, (title, items) in enumerate(columns):
        x = 68 + index * 354
        content += rect(x, 124, 292, 168, theme["panel"], theme["line"], 8)
        content += text(title, x + 22, 155, 14, theme["accent"], 700)
        for item_index, item in enumerate(items):
            y = 190 + item_index * 24
            content += rect(x + 22, y - 14, 8, 8, theme["accent"], "none", 2)
            content += text(item, x + 42, y - 5, 14, theme["ink"])
        if index < 2:
            content += line(x + 292, 208, x + 342, 208, theme["accent"], 2)
    content += text("interfaces", 344, 194, 11, theme["muted"])
    content += text("delivery", 698, 194, 11, theme["muted"])
    return svg(theme, 332, content)


def projects(theme: dict[str, str]) -> str:
    content = shell(theme, "BUILD INDEX", "03", "FEATURED ENGINEERING WORK")
    featured = [
        ("01", "CONCURRENT DOCUMENT PROCESSOR", "Rust / Rayon / JSONL", "Measured local benchmark: 3.88x throughput at 8 workers."),
        ("02", "GPU INFERENCE ENGINE", "C++ / CUDA / ROCm / HIP", "Cross-platform kernel and benchmarking study."),
    ]
    for index, (number, title, stack, result) in enumerate(featured):
        x = 56 + index * 530
        content += rect(x, 118, 498, 132, theme["panel"], theme["line"], 8)
        content += text(number, x + 22, 148, 14, theme["accent"], 700)
        content += text(title, x + 62, 148, 14, theme["ink"], 700)
        content += text(stack, x + 22, 181, 12, theme["muted"])
        content += text(result, x + 22, 216, 12, theme["muted"])
    smaller = [
        ("03", "MULTI-AGENT DEVELOPMENT SYSTEM", "Five-agent plan / code / deploy / test / fix loop."),
        ("04", "JIRA SLACK MCP", "Async MCP server for Jira and Confluence workflows."),
        ("05", "MARKET-AI-AGENT", "ReAct agent with FastMCP tools for market intelligence."),
        ("06", "PORTFOLIO", "TypeScript / React / Vite personal engineering site."),
    ]
    for index, (number, title, result) in enumerate(smaller):
        x = 56 + (index % 2) * 530
        y = 282 + (index // 2) * 64
        content += text(number, x, y, 13, theme["accent"], 700)
        content += text(title, x + 40, y, 13, theme["ink"], 700)
        content += text(result, x + 40, y + 22, 11, theme["muted"])
        if index % 2 == 0:
            content += line(56, y + 39, 1104, y + 39, theme["line"])
    return svg(theme, 450, content)


def experience(theme: dict[str, str]) -> str:
    content = shell(theme, "EXPERIENCE ROUTE", "04", "RECENT SYSTEMS SHIPPED")
    entries = [
        ("2026—NOW", "OATMEAL AI", "AI ENGINEER", "Production multi-agent advisory workflows with LangGraph, FastAPI, RAG, and Azure Container Apps."),
        ("2025—2026", "BERKSHIRE HATHAWAY", "AI/ML ENGINEER", "AI and cloud infrastructure for educational applications using Gemini, Vertex AI, GCP, and Firebase."),
        ("2024—2026", "CAL STATE EAST BAY", "SOFTWARE ENGINEER / AI-ML RESEARCH", "Student systems engineering alongside PyTorch research and AI evaluation pipelines."),
        ("2022—2024", "ACCENTURE", "SOFTWARE ENGINEER (BACKEND)", "Enterprise data and delivery infrastructure with Python, Spark, Airflow, AWS, and Kubernetes."),
    ]
    for index, (dates, company, role, impact) in enumerate(entries):
        y = 123 + index * 54
        content += text(dates, 58, y + 4, 12, theme["accent"], 700)
        content += line(188, y - 8, 188, y + 25, theme["accent"], 2)
        content += text(company, 218, y, 14, theme["ink"], 700)
        content += text(role, 430, y, 12, theme["accent"], 700)
        content += text(impact, 218, y + 22, 12, theme["muted"])
    return svg(theme, 370, content)


def stack(theme: dict[str, str]) -> str:
    content = shell(theme, "STACK", "05", "ENGINEERING TOOLKIT")
    groups = [
        ("LANGUAGES", "Python  ·  TypeScript  ·  Rust  ·  Go  ·  C++  ·  SQL"),
        ("AI + MODEL SYSTEMS", "LangGraph  ·  RAG  ·  MCP  ·  PyTorch  ·  Vertex AI"),
        ("BACKEND + DISTRIBUTED", "FastAPI  ·  REST  ·  gRPC  ·  Redis  ·  Kafka"),
        ("CLOUD + INFRASTRUCTURE", "AWS  ·  Docker  ·  Kubernetes  ·  Terraform  ·  CI/CD"),
        ("DATA + PERSISTENCE", "PostgreSQL  ·  Firestore  ·  Pinecone  ·  ChromaDB"),
        ("OBSERVABILITY + DELIVERY", "MLflow  ·  Datadog  ·  Splunk  ·  CloudWatch"),
    ]
    for index, (label, values) in enumerate(groups):
        x = 56 + (index % 2) * 530
        y = 124 + (index // 2) * 64
        content += rect(x, y, 498, 46, theme["panel"], theme["line"], 6)
        content += text(label, x + 16, y + 19, 11, theme["accent"], 700)
        content += text(values, x + 16, y + 37, 12, theme["ink"])
    return svg(theme, 350, content)


def current_focus(theme: dict[str, str]) -> str:
    content = shell(theme, "BUILD LOG", "06", "CURRENTLY BUILDING")
    content += rect(56, 124, 1048, 118, theme["panel"], theme["line"], 8)
    content += rect(80, 152, 12, 12, theme["accent"], "none", 6)
    content += text("ACTIVE", 108, 163, 12, theme["accent"], 700)
    content += text("Production agentic workflows  ·  GPU inference performance", 80, 199, 18, theme["ink"], 700)
    content += text("Reliable backend platforms  ·  Developer automation", 80, 225, 15, theme["muted"])
    content += text("OPEN TO AI ENGINEERING, BACKEND, AND SYSTEMS OPPORTUNITIES", 80, 278, 13, theme["accent"], 700)
    return svg(theme, 326, content)


def telemetry(theme: dict[str, str]) -> str:
    content = shell(theme, "TELEMETRY", "04", "PUBLIC GITHUB SIGNALS")
    stats = [("27", "PUBLIC REPOSITORIES"), ("1", "FOLLOWER"), ("0", "PUBLIC GISTS")]
    for index, (value, label) in enumerate(stats):
        x = 56 + index * 190
        content += rect(x, 124, 164, 78, theme["panel"], theme["line"], 8)
        content += text(value, x + 18, 163, 28, theme["accent"], 700)
        content += text(label, x + 18, 184, 10, theme["muted"], 700)
    content += rect(646, 124, 458, 78, theme["panel"], theme["line"], 8)
    content += text("REPOSITORY LANGUAGE SUMMARY", 668, 151, 11, theme["accent"], 700)
    content += text("Python 10  ·  HTML 2  ·  Jupyter 2  ·  JavaScript 1", 668, 176, 12, theme["ink"])
    content += text("Rust 1  ·  TypeScript 1", 668, 194, 12, theme["ink"])
    content += text("LIVE CONTRIBUTION CALENDAR", 56, 254, 12, theme["accent"], 700)
    content += text("Contribution calendar — click through for the current GitHub view.", 56, 279, 13, theme["muted"])
    return svg(theme, 318, content)


GENERATORS = {
    "header": header,
    "whoami": whoami,
    "system-map": system_map,
    "projects": projects,
    "experience": experience,
    "stack": stack,
    "telemetry": telemetry,
    "current-focus": current_focus,
}


def main() -> None:
    for theme_name, theme in THEMES.items():
        output_dir = ROOT / "assets" / theme_name
        output_dir.mkdir(parents=True, exist_ok=True)
        for name, generator in GENERATORS.items():
            (output_dir / f"{name}.svg").write_text(generator(theme), encoding="utf-8")


if __name__ == "__main__":
    main()
