from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIDTH = 1160

# SVGs render at roughly 800px on GitHub, so internal sizes account for the
# viewBox scale while keeping descriptive text readable.
DISPLAY = 44
SECTION_TITLE = 36
CARD_TITLE = 26
BODY = 24
SECONDARY = 23
METADATA = 21

THEMES = {
    "light": {
        "background": "#f7f8fa",
        "panel": "#ffffff",
        "ink": "#1f2328",
        "muted": "#57606a",
        "line": "#d9e1e7",
        "accent": "#007f8b",
        "accent_soft": "#d9f2f1",
    },
    "dark": {
        "background": "#10161c",
        "panel": "#17212a",
        "ink": "#f0f6fc",
        "muted": "#b1bac4",
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


def centered_text(value: str, x: int, y: int, size: int, fill: str, weight: int = 400) -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="middle" fill="{fill}" font-family="ui-monospace, '
        f'SFMono-Regular, Menlo, Monaco, Consolas, monospace" font-size="{size}px" font-weight="{weight}">'
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


def shell(theme: dict[str, str], label: str, number: str, title: str, readable: bool = True) -> str:
    label_size = METADATA if readable else 14
    title_size = SECTION_TITLE if readable else 22
    title_x = 430 if readable else 315
    return (
        rect(32, 24, WIDTH - 64, 56, theme["panel"], theme["line"], 8)
        + text(f"{number} / {label}", 56, 59, label_size, theme["accent"], 700)
        + text(title, title_x, 59, title_size, theme["ink"], 700)
    )


def header(theme: dict[str, str]) -> str:
    theme = {
        **theme,
        "ink": "#14202b" if theme["background"] == "#f7f8fa" else "#f0f5f7",
        "muted": "#5d6b77" if theme["background"] == "#f7f8fa" else "#a7b6bf",
    }
    content = shell(theme, "IDENTITY", "00", "AI SYSTEMS CONTROL PLANE", readable=False)
    content += text("ATHARVA AMBADE", 56, 145, 44, theme["ink"], 700)
    content += text("AI ENGINEER", 58, 181, 20, theme["accent"], 700)
    content += text("BACKEND & SYSTEMS ENGINEER", 58, 211, 20, theme["ink"], 700)
    content += text("Building reliable AI applications, backend platforms,", 58, 257, 18, theme["muted"])
    content += text("agentic workflows, and cloud infrastructure.", 58, 284, 18, theme["muted"])
    content += rect(56, 320, 1048, 118, theme["panel"], theme["line"], 8)
    content += text("SYSTEM FLOW", 82, 348, 13, theme["accent"], 700)
    nodes = ["INPUT", "API", "AGENT / MODEL", "DATA", "INFRA", "OBSERVE"]
    centers = [170, 334, 498, 662, 826, 990]
    for index, node in enumerate(nodes):
        center = centers[index]
        x = center - 66
        content += rect(x, 365, 132, 64, theme["accent_soft"], "none", 6)
        if node == "AGENT / MODEL":
            content += centered_text("AGENT", center, 391, 14, theme["ink"], 700)
            content += centered_text("/ MODEL", center, 410, 14, theme["ink"], 700)
        else:
            content += centered_text(node, center, 401, 14, theme["ink"], 700)
        if index < len(nodes) - 1:
            content += line(center + 66, 397, centers[index + 1] - 66, 397, theme["accent"], 2)
    content += text("SAN FRANCISCO BAY AREA", 58, 476, 13, theme["muted"], 700)
    content += text("OPEN TO AI / SOFTWARE ENGINEERING OPPORTUNITIES", 315, 476, 13, theme["muted"], 700)
    content += text("PYTHON  /  TYPESCRIPT  /  RUST  /  GO", 770, 476, 13, theme["muted"], 700)
    content += line(56, 507, WIDTH - 56, 507, theme["line"])
    return svg(theme, 540, content)


def whoami(theme: dict[str, str]) -> str:
    content = shell(theme, "WHOAMI", "01", "ENGINEERING IDENTITY")
    blocks = [
        ("WHAT I BUILD", "Production AI applications, backend services,", "distributed workflows, and cloud automation."),
        ("HOW I WORK", "Measure bottlenecks, design reliable interfaces,", "automate delivery, and validate results."),
        ("CURRENT INTERESTS", "Agentic systems, inference infrastructure,", "developer tools, performance, and observability."),
    ]
    for index, block in enumerate(blocks):
        y = 116 + index * 104
        content += rect(56, y, 1048, 84, theme["panel"], theme["line"], 8)
        content += text(f"0{index + 1}", 82, y + 34, METADATA, theme["accent"], 700)
        content += text(block[0], 150, y + 34, CARD_TITLE, theme["ink"], 700)
        content += text(block[1], 440, y + 34, BODY, theme["muted"])
        content += text(block[2], 440, y + 64, BODY, theme["muted"])
    return svg(theme, 454, content)


def system_map(theme: dict[str, str]) -> str:
    content = shell(theme, "SYSTEM MAP", "02", "FROM MODEL TO OPERATING SYSTEM")
    layers = [
        ("AI + AGENTS", "LLM applications · MCP integrations · RAG and retrieval · Evaluation"),
        ("BACKEND + SYSTEMS", "APIs and services · Distributed processing · Concurrency and caching · Databases"),
        ("INFRASTRUCTURE", "AWS · Azure · GCP · Docker · Kubernetes · Terraform · CI/CD · Observability"),
    ]
    for index, (title, capabilities) in enumerate(layers):
        y = 116 + index * 128
        content += rect(56, y, 1048, 88, theme["panel"], theme["line"], 8)
        content += text(title, 82, y + 40, CARD_TITLE, theme["accent"], 700)
        if index == 0:
            content += text("LLM applications · MCP integrations · RAG and", 420, y + 34, SECONDARY, theme["ink"])
            content += text("retrieval · Evaluation", 420, y + 64, SECONDARY, theme["ink"])
        elif index == 1:
            content += text("APIs and services · Distributed processing ·", 420, y + 34, SECONDARY, theme["ink"])
            content += text("Concurrency and caching · Databases", 420, y + 64, SECONDARY, theme["ink"])
        else:
            content += text("AWS · Azure · GCP · Docker · Kubernetes ·", 420, y + 34, SECONDARY, theme["ink"])
            content += text("Terraform · CI/CD · Observability", 420, y + 64, SECONDARY, theme["ink"])
        if index < 2:
            content += text("↓", 570, y + 116, 28, theme["accent"], 700)
            content += text(("interfaces" if index == 0 else "delivery"), 612, y + 116, METADATA, theme["muted"], 700)
    return svg(theme, 500, content)


def projects(theme: dict[str, str]) -> str:
    content = shell(theme, "BUILD INDEX", "03", "FEATURED ENGINEERING WORK")
    featured = [
        ("01", "CONCURRENT DOCUMENT PROCESSOR", "Rust / Rayon / JSONL", "Measured local benchmark: 3.88x throughput at 8 workers."),
        ("02", "GPU INFERENCE ENGINE", "C++ / CUDA / ROCm / HIP", "Cross-platform kernel and benchmarking study."),
    ]
    for index, (number, title, stack, result) in enumerate(featured):
        x = 56 + index * 530
        content += rect(x, 118, 498, 156, theme["panel"], theme["line"], 8)
        content += text(number, x + 22, 153, METADATA, theme["accent"], 700)
        content += text(title, x + 62, 153, CARD_TITLE, theme["ink"], 700)
        content += text(stack, x + 22, 198, SECONDARY, theme["muted"])
        content += text(result, x + 22, 240, SECONDARY, theme["muted"])
    smaller = [
        ("03", "MULTI-AGENT DEVELOPMENT SYSTEM", "Five-agent plan / code / deploy / test / fix loop."),
        ("04", "JIRA SLACK MCP", "Async MCP server for Jira and Confluence workflows."),
        ("05", "MARKET-AI-AGENT", "ReAct agent with FastMCP tools for market intelligence."),
        ("06", "PORTFOLIO", "TypeScript / React / Vite personal engineering site."),
    ]
    for index, (number, title, result) in enumerate(smaller):
        x = 56 + (index % 2) * 530
        y = 318 + (index // 2) * 88
        content += text(number, x, y, METADATA, theme["accent"], 700)
        content += text(title, x + 40, y, CARD_TITLE, theme["ink"], 700)
        content += text(result, x + 40, y + 30, SECONDARY, theme["muted"])
        if index % 2 == 0:
            content += line(56, y + 53, 1104, y + 53, theme["line"])
    return svg(theme, 500, content)


def experience(theme: dict[str, str]) -> str:
    content = shell(theme, "EXPERIENCE ROUTE", "04", "RECENT SYSTEMS SHIPPED")
    entries = [
        ("2026—NOW", "OATMEAL AI", "AI ENGINEER", "Production multi-agent advisory workflows with", "LangGraph, FastAPI, RAG, and Azure Container Apps."),
        ("2025—2026", "BERKSHIRE HATHAWAY", "AI/ML ENGINEER", "AI and cloud infrastructure for educational", "applications using Gemini, Vertex AI, GCP, and Firebase."),
        ("2024—2026", "CAL STATE EAST BAY", "SOFTWARE ENGINEER / AI-ML RESEARCH", "Student systems engineering alongside PyTorch", "research and AI evaluation pipelines."),
        ("2022—2024", "ACCENTURE", "SOFTWARE ENGINEER (BACKEND)", "Enterprise data and delivery infrastructure with", "Python, Spark, Airflow, AWS, and Kubernetes."),
    ]
    for index, (dates, company, role, impact, impact_continued) in enumerate(entries):
        y = 124 + index * 140
        content += text(dates, 58, y + 6, METADATA, theme["accent"], 700)
        content += line(188, y - 8, 188, y + 100, theme["line"], 2)
        content += text(company, 218, y, CARD_TITLE, theme["ink"], 700)
        content += text(role, 600, y, METADATA, theme["accent"], 700)
        content += text(impact, 218, y + 40, SECONDARY, theme["muted"])
        content += text(impact_continued, 218, y + 70, SECONDARY, theme["muted"])
    return svg(theme, 700, content)


def stack(theme: dict[str, str]) -> str:
    content = shell(theme, "STACK", "05", "ENGINEERING TOOLKIT")
    groups = [
        ("LANGUAGES", "Python  ·  TypeScript  ·  Rust  ·  Go  ·", "C++  ·  SQL"),
        ("AI + MODEL SYSTEMS", "LangGraph  ·  RAG  ·  MCP  ·  PyTorch  ·", "Vertex AI"),
        ("BACKEND + DISTRIBUTED", "FastAPI  ·  REST  ·  gRPC  ·  Redis  ·", "Kafka"),
        ("CLOUD + INFRASTRUCTURE", "AWS  ·  Docker  ·  Kubernetes  ·", "Terraform  ·  CI/CD"),
        ("DATA + PERSISTENCE", "PostgreSQL  ·  Firestore  ·  Pinecone  ·", "ChromaDB"),
        ("OBSERVABILITY + DELIVERY", "MLflow  ·  Datadog  ·  Splunk  ·", "CloudWatch"),
    ]
    for index, (label, values, values_continued) in enumerate(groups):
        x = 56 + (index % 2) * 530
        y = 124 + (index // 2) * 92
        content += rect(x, y, 498, 84, theme["panel"], theme["line"], 6)
        content += text(label, x + 18, y + 25, METADATA, theme["accent"], 700)
        content += text(values, x + 18, y + 53, SECONDARY, theme["ink"])
        if values_continued:
            content += text(values_continued, x + 18, y + 78, SECONDARY, theme["ink"])
    return svg(theme, 470, content)


def current_focus(theme: dict[str, str]) -> str:
    content = shell(theme, "BUILD LOG", "06", "CURRENTLY BUILDING")
    content += rect(56, 124, 1048, 144, theme["panel"], theme["line"], 8)
    content += rect(80, 154, 14, 14, theme["accent"], "none", 7)
    content += text("ACTIVE", 112, 168, METADATA, theme["accent"], 700)
    content += text("Production agentic workflows  ·  GPU inference performance", 80, 213, BODY, theme["ink"], 700)
    content += text("Reliable backend platforms  ·  Developer automation", 80, 247, SECONDARY, theme["muted"])
    content += text("OPEN TO AI ENGINEERING, BACKEND, AND SYSTEMS OPPORTUNITIES", 80, 312, METADATA, theme["accent"], 700)
    return svg(theme, 360, content)


def telemetry(theme: dict[str, str]) -> str:
    content = shell(theme, "TELEMETRY", "04", "PUBLIC GITHUB SIGNALS")
    stats = [("27", "PUBLIC REPOSITORIES"), ("1", "FOLLOWER"), ("0", "PUBLIC GISTS")]
    for index, (value, label) in enumerate(stats):
        x = 56 + index * 190
        content += rect(x, 124, 164, 78, theme["panel"], theme["line"], 8)
        content += text(value, x + 18, 163, DISPLAY, theme["accent"], 700)
        content += text(label, x + 18, 190, METADATA, theme["muted"], 700)
    content += rect(646, 124, 458, 78, theme["panel"], theme["line"], 8)
    content += text("REPOSITORY LANGUAGE SUMMARY", 668, 151, METADATA, theme["accent"], 700)
    content += text("Python 10  ·  HTML 2  ·  Jupyter 2  ·  JavaScript 1", 668, 178, SECONDARY, theme["ink"])
    content += text("Rust 1  ·  TypeScript 1", 668, 202, SECONDARY, theme["ink"])
    content += text("LIVE CONTRIBUTION CALENDAR", 56, 254, METADATA, theme["accent"], 700)
    content += text("Contribution calendar — click through for the current GitHub view.", 56, 283, SECONDARY, theme["muted"])
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
