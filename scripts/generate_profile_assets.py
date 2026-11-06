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
CHAR_WIDTH_FACTOR = 0.6

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


def vertically_centered_text(
    value: str,
    x: int,
    center_y: int,
    size: int,
    fill: str,
    weight: int = 400,
    anchor: str | None = None,
) -> str:
    text_anchor = f' text-anchor="{anchor}"' if anchor else ""
    return (
        f'<text x="{x}" y="{center_y}"{text_anchor} dominant-baseline="middle" fill="{fill}" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" '
        f'font-size="{size}px" font-weight="{weight}">{escape(value)}</text>'
    )


def multiline_text(
    lines: list[str],
    x: int,
    y: int,
    size: int,
    fill: str,
    weight: int = 400,
    line_height: int = 28,
    max_width: int | None = None,
    context: str = "text",
) -> str:
    if max_width is not None:
        widest = max((len(value) for value in lines), default=0) * size * CHAR_WIDTH_FACTOR
        if widest > max_width:
            raise ValueError(
                f"{context} line is too wide: estimated {widest:.1f}px exceeds {max_width}px"
            )
    tspans = "".join(
        f'<tspan x="{x}" dy="{0 if index == 0 else line_height}px">{escape(value)}</tspan>'
        for index, value in enumerate(lines)
    )
    return (
        f'<text x="{x}" y="{y}" fill="{fill}" font-family="ui-monospace, SFMono-Regular, '
        f'Menlo, Monaco, Consolas, monospace" font-size="{size}px" font-weight="{weight}">{tspans}</text>'
    )


def bounded_text(
    value: str,
    x: int,
    y: int,
    size: int,
    fill: str,
    max_width: int,
    weight: int = 400,
    context: str = "text",
) -> str:
    estimated_width = len(value) * size * CHAR_WIDTH_FACTOR
    if estimated_width > max_width:
        raise ValueError(
            f"{context} line is too wide: estimated {estimated_width:.1f}px exceeds {max_width}px"
        )
    return text(value, x, y, size, fill, weight)


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
    header_center_y = 24 + 56 / 2
    return (
        rect(32, 24, WIDTH - 64, 56, theme["panel"], theme["line"], 8)
        + vertically_centered_text(f"{number} / {label}", 56, header_center_y, label_size, theme["accent"], 700)
        + vertically_centered_text(title, title_x, header_center_y, title_size, theme["ink"], 700)
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
        ("WHAT I BUILD", "Production AI, backend services, and", "distributed workflows with cloud automation."),
        ("HOW I WORK", "Measure bottlenecks, design reliable systems,", "automate delivery, and validate results."),
        ("CURRENT INTERESTS", "Agentic systems, inference infrastructure,", "developer tooling, and observability."),
    ]
    for index, block in enumerate(blocks):
        y = 116 + index * 104
        content += rect(56, y, 1048, 84, theme["panel"], theme["line"], 8)
        content += text(f"0{index + 1}", 82, y + 34, METADATA, theme["accent"], 700)
        content += text(block[0], 150, y + 34, 22, theme["ink"], 700)
        content += multiline_text(
            [block[1], block[2]],
            400,
            y + 32,
            SECONDARY,
            theme["muted"],
            line_height=29,
            max_width=630,
            context=f"WHOAMI row {index + 1}",
        )
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
    builds = [
        ("01", "CONCURRENT DOCUMENT PROCESSOR", "Rust · Rayon · JSONL", "Measured local benchmark: 3.88x throughput at 8 workers."),
        ("02", "GPU INFERENCE ENGINE", "C++ · CUDA · ROCm/HIP", "Cross-platform kernel and benchmarking study."),
        ("03", "MULTI-AGENT DEVELOPMENT SYSTEM", None, "Five-agent plan / code / deploy / test / fix loop."),
        ("04", "JIRA SLACK MCP", None, "Async MCP server for Jira and Confluence workflows."),
        ("05", "MARKET-AI-AGENT", None, "ReAct agent with FastMCP tools for market intelligence."),
        ("06", "PORTFOLIO", None, "TypeScript / React / Vite personal engineering site."),
    ]
    card_x, card_width, card_height, row_gap = 56, 1048, 155, 170
    description_x = 100
    description_width = card_x + card_width - 80 - description_x
    for index, (number, title, stack, result) in enumerate(builds):
        y = 118 + index * row_gap
        content += rect(card_x, y, card_width, card_height, theme["panel"], theme["line"], 8)
        content += text(number, 100, y + 45, METADATA, theme["accent"], 700)
        content += bounded_text(
            title, 170, y + 45, CARD_TITLE, theme["ink"], 850, 700, f"project {number} title"
        )
        if stack:
            content += bounded_text(stack, description_x, y + 82, SECONDARY, theme["muted"], description_width, context=f"project {number} technology")
        content += bounded_text(
            result, description_x, y + 119, SECONDARY, theme["muted"], description_width, context=f"project {number} description"
            )
    return svg(theme, 1183, content)


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
        ("LANGUAGES", "Python · TypeScript · Rust", "Go · C++ · SQL"),
        ("AI + MODEL SYSTEMS", "LangGraph · RAG · MCP", "PyTorch · Vertex AI"),
        ("BACKEND + DISTRIBUTED", "FastAPI · REST · gRPC", "Redis · Kafka"),
        ("CLOUD + INFRASTRUCTURE", "AWS · Docker · Kubernetes", "Terraform · CI/CD"),
        ("DATA + PERSISTENCE", "PostgreSQL · Firestore", "Pinecone · ChromaDB"),
        ("OBSERVABILITY + DELIVERY", "MLflow · Datadog", "Splunk · CloudWatch"),
    ]
    heading_size, value_size = 28, 23
    for index, (label, values, values_continued) in enumerate(groups):
        x = 56 + (index % 2) * 530
        y = 124 + (index // 2) * 112
        content += rect(x, y, 498, 104, theme["panel"], theme["line"], 6)
        content += text(label, x + 18, y + 31, heading_size, theme["accent"], 700)
        content += bounded_text(values, x + 18, y + 68, value_size, theme["ink"], 450, context=f"{label} values")
        content += bounded_text(
            values_continued,
            x + 18,
            y + 96,
            value_size,
            theme["ink"],
            450,
            context=f"{label} continued values",
        )
    return svg(theme, 526, content)


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
    stats = [("27", "REPOSITORIES"), ("1", "FOLLOWER"), ("0", "GISTS")]
    stat_center_y = 124 + 78 / 2
    for index, (value, label) in enumerate(stats):
        x = 56 + index * 350
        content += rect(x, 124, 318, 78, theme["panel"], theme["line"], 8)
        content += vertically_centered_text(value, x + 40, stat_center_y, DISPLAY, theme["accent"], 700)
        content += vertically_centered_text(label, x + 150, stat_center_y, METADATA, theme["muted"], 700)
    content += rect(56, 230, 1048, 150, theme["panel"], theme["line"], 8)
    content += text("REPOSITORY LANGUAGE SUMMARY", 100, 268, METADATA, theme["accent"], 700)
    content += bounded_text(
        "Python 10 · HTML 2 · Jupyter 2 · JavaScript 1 · Rust 1 · TypeScript 1",
        100,
        310,
        22,
        theme["ink"],
        960,
        context="telemetry language summary",
    )
    content += text("LIVE CONTRIBUTION ACTIVITY", 56, 438, METADATA, theme["accent"], 700)
    content += text("Contribution graph links to the current GitHub view.", 56, 468, SECONDARY, theme["muted"])
    return svg(theme, 510, content)


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
