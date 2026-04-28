from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image as RLImage,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "paper_pdf"
FIG = OUT / "figures"
PDF = OUT / "the_plural_of_anecdote_is_data.pdf"
SOURCE_APPENDIX = ROOT / "source_appendix.md"

AUTHOR = "Birger Moëll"
TITLE = "The Plural of Anecdote Is Data"
SUBTITLE = "How Patients Describe Using Large Language Models for Health"


PAL = {
    "ink": "#1f2933",
    "muted": "#66747f",
    "hair": "#dfe5ea",
    "paper": "#fffdf8",
    "white": "#ffffff",
    "blue": "#315f7d",
    "blue2": "#9fb8c8",
    "teal": "#3d7c75",
    "green": "#6f8150",
    "gold": "#a77d32",
    "red": "#a95b5e",
    "plum": "#76617f",
    "slate": "#6d7880",
    "mist": "#f4f6f7",
    "soft_blue": "#edf4f7",
    "soft_gold": "#f6f0e4",
    "soft_red": "#f7eceb",
}


def rgb(hex_color: str) -> tuple[int, int, int]:
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgba(hex_color: str, alpha: int = 255) -> tuple[int, int, int, int]:
    r, g, b = rgb(hex_color)
    return r, g, b, alpha


def font(size: int, weight: str = "regular") -> ImageFont.ImageFont:
    candidates = {
        "regular": [
            "/System/Library/Fonts/Supplemental/Avenir Next.ttc",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
        ],
        "bold": [
            "/System/Library/Fonts/Supplemental/Avenir Next.ttc",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        ],
        "serif": [
            "/System/Library/Fonts/Supplemental/Georgia.ttf",
            "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
        ],
        "serif_bold": [
            "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
            "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        ],
    }[weight]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(d: ImageDraw.ImageDraw, text: str, f: ImageFont.ImageFont, max_width: int) -> list[str]:
    out: list[str] = []
    words = text.split()
    line: list[str] = []
    for word in words:
        candidate = " ".join(line + [word])
        if d.textbbox((0, 0), candidate, font=f)[2] <= max_width or not line:
            line.append(word)
        else:
            out.append(" ".join(line))
            line = [word]
    if line:
        out.append(" ".join(line))
    return out


def shadow_box(draw: ImageDraw.ImageDraw, xy, radius: int = 18, fill: str = PAL["white"], outline: str = PAL["hair"]):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle((x0 + 7, y0 + 8, x1 + 7, y1 + 8), radius=radius, fill=rgb("#e6ebef"))
    draw.rounded_rectangle(xy, radius=radius, fill=rgb(fill), outline=rgb(outline), width=2)


def draw_title(draw: ImageDraw.ImageDraw, fig_no: str, title: str, subtitle: str):
    draw.text((110, 82), f"Figure {fig_no}.", fill=rgb(PAL["blue"]), font=font(34, "bold"))
    draw.text((280, 77), title, fill=rgb(PAL["ink"]), font=font(56, "serif_bold"))
    draw.text((112, 152), subtitle, fill=rgb(PAL["muted"]), font=font(28))
    draw.line((112, 205, 2288, 205), fill=rgb(PAL["hair"]), width=3)


def draw_plate_title(draw: ImageDraw.ImageDraw, label: str, title: str, subtitle: str):
    draw.text((110, 82), label, fill=rgb(PAL["blue"]), font=font(34, "bold"))
    label_w = draw.textbbox((0, 0), label, font=font(34, "bold"))[2]
    draw.text((135 + label_w, 77), title, fill=rgb(PAL["ink"]), font=font(54, "serif_bold"))
    draw.text((112, 152), subtitle, fill=rgb(PAL["muted"]), font=font(27))
    draw.line((112, 205, 2288, 205), fill=rgb(PAL["hair"]), width=3)


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def normalize_source(row: dict[str, str]) -> str:
    st = row["source_type"]
    platform = row["platform"]
    if "Reddit" in platform or st.startswith("public"):
        return "Reddit / public posts"
    if st == "patient forum":
        return "Patient forums"
    if "news" in st:
        return "News-mediated"
    if "essay" in st or "column" in st:
        return "Personal essays"
    return "Other"


def normalize_valence(row: dict[str, str]) -> str:
    v = row["valence"]
    if v == "helpful":
        return "Helpful"
    if v == "unhelpful_or_insufficient":
        return "No resolution"
    if "harm" in v or "unhelpful" in v:
        return "Harm / unhelpful"
    if "mixed" in v or "risk" in v:
        return "Mixed / uncertain"
    return "No resolution"


def make_fig1(path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(
        d,
        "1",
        "Anecdotes as Early Signal",
        "Patient stories locate LLMs in the work that surrounds formal care.",
    )

    columns = [
        ("System gap", "Where formal care feels absent", ["Rushed visits", "Portal jargon", "Delayed referrals", "Therapy access", "Night uncertainty"], PAL["gold"]),
        ("LLM function", "What the model is asked to do", ["Translate", "Synthesize", "Prepare", "Comfort", "Track"], PAL["blue"]),
        ("Patient action", "What changes after the chat", ["Seek care", "Ask questions", "Request tests", "Change routines", "Upload records"], PAL["teal"]),
        ("Boundary risk", "Where usefulness can flip", ["Wrong triage", "Unsafe advice", "Reassurance loops", "Psychosis/mania", "Privacy exposure"], PAL["red"]),
    ]

    top = 330
    lefts = [110, 680, 1250, 1820]
    for idx, (heading, kicker, items, color) in enumerate(columns):
        x = lefts[idx]
        shadow_box(d, (x, top, x + 445, top + 820), radius=20)
        d.rounded_rectangle((x, top, x + 445, top + 94), radius=20, fill=rgb(color))
        d.text((x + 30, top + 24), heading, fill="white", font=font(31, "bold"))
        d.text((x + 30, top + 124), kicker, fill=rgb(PAL["muted"]), font=font(20))
        y = top + 205
        for item in items:
            d.ellipse((x + 34, y + 11, x + 55, y + 32), fill=rgb(color))
            for line in wrap(d, item, font(29), 320):
                d.text((x + 82, y), line, fill=rgb(PAL["ink"]), font=font(29))
                y += 41
            y += 34
        if idx < 3:
            ax = x + 474
            ay = top + 410
            d.line((ax, ay, ax + 92, ay), fill=rgb(PAL["slate"]), width=8)
            d.polygon([(ax + 108, ay), (ax + 80, ay - 22), (ax + 80, ay + 22)], fill=rgb(PAL["slate"]))

    d.rounded_rectangle((160, 1240, 2240, 1358), radius=18, fill=rgb("#eef5f7"), outline=rgb(PAL["hair"]), width=2)
    d.text((205, 1268), "Interpretive claim", fill=rgb(PAL["blue"]), font=font(25, "bold"))
    claim = "The corpus is not mainly a story of patients replacing clinicians; it is a map of unpaid sensemaking work around care."
    for i, line in enumerate(wrap(d, claim, font(28), 1780)):
        d.text((470, 1264 + i * 38), line, fill=rgb(PAL["ink"]), font=font(28))
    img.convert("RGB").save(path, quality=96)


def make_fig2(seed: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "2", "Corpus Architecture", "A 100-record seed corpus organized by provenance, valence, and readiness for analysis.")

    source_counts = Counter(normalize_source(r) for r in seed)
    valence_counts = Counter(normalize_valence(r) for r in seed)
    status_counts = Counter(r["inclusion_status"] for r in seed)

    # Source bars
    x, y = 120, 340
    d.text((x, y - 65), "Source provenance", fill=rgb(PAL["ink"]), font=font(30, "bold"))
    order = ["Reddit / public posts", "Patient forums", "News-mediated", "Personal essays", "Other"]
    cols = [PAL["blue"], PAL["teal"], PAL["gold"], PAL["plum"], PAL["slate"]]
    max_v = max(source_counts.values())
    for i, name in enumerate(order):
        yy = y + i * 92
        d.text((x, yy + 6), name, fill=rgb(PAL["ink"]), font=font(25))
        d.rounded_rectangle((x + 320, yy, x + 1050, yy + 48), radius=24, fill=rgb("#e7edf1"))
        w = int(730 * source_counts[name] / max_v)
        d.rounded_rectangle((x + 320, yy, x + 320 + w, yy + 48), radius=24, fill=rgb(cols[i]))
        d.text((x + 1080, yy + 4), str(source_counts[name]), fill=rgb(PAL["ink"]), font=font(26, "bold"))

    # Donut
    cx, cy, radius = 1710, 650, 310
    d.text((1390, 275), "Reported valence", fill=rgb(PAL["ink"]), font=font(30, "bold"))
    v_order = [("Helpful", PAL["green"]), ("Harm / unhelpful", PAL["red"]), ("Mixed / uncertain", PAL["gold"]), ("No resolution", PAL["slate"])]
    total = sum(valence_counts.values())
    start = -90
    for label, color in v_order:
        angle = 360 * valence_counts[label] / total
        d.pieslice((cx - radius, cy - radius, cx + radius, cy + radius), start, start + angle, fill=rgb(color))
        start += angle
    d.ellipse((cx - 175, cy - 175, cx + 175, cy + 175), fill=rgb(PAL["paper"]))
    d.text((cx - 78, cy - 74), "100", fill=rgb(PAL["ink"]), font=font(82, "bold"))
    d.text((cx - 82, cy + 24), "records", fill=rgb(PAL["muted"]), font=font(27))
    ly = 1000
    for i, (label, color) in enumerate(v_order):
        xx = 1330 + (i % 2) * 430
        yy = ly + (i // 2) * 70
        d.rounded_rectangle((xx, yy, xx + 42, yy + 42), radius=10, fill=rgb(color))
        d.text((xx + 58, yy + 3), f"{label}: {valence_counts[label]}", fill=rgb(PAL["ink"]), font=font(23))

    # Readiness strip
    d.text((120, 955), "Analysis readiness", fill=rgb(PAL["ink"]), font=font(30, "bold"))
    status_order = [("include", "Ready-ish include", PAL["green"]), ("include_with_caution", "Use with caution", PAL["gold"]), ("candidate", "Needs cleanup", PAL["red"]), ("duplicate_context", "Duplicate context", PAL["slate"])]
    sx, sy, sw, sh = 120, 1025, 1060, 64
    cur = sx
    for key, label, color in status_order:
        seg = int(sw * status_counts[key] / len(seed))
        d.rectangle((cur, sy, cur + seg, sy + sh), fill=rgb(color))
        cur += seg
    d.rounded_rectangle((sx, sy, sx + sw, sy + sh), radius=12, outline=rgb(PAL["ink"]), width=2)
    yy = 1120
    for key, label, color in status_order:
        d.rounded_rectangle((120, yy, 150, yy + 30), radius=7, fill=rgb(color))
        d.text((168, yy - 1), f"{label}: {status_counts[key]}", fill=rgb(PAL["ink"]), font=font(22))
        yy += 48

    d.text((120, 1365), "Counts describe an exploratory corpus; they are not prevalence estimates.", fill=rgb(PAL["muted"]), font=font(21))
    img.convert("RGB").save(path, quality=96)


def make_fig3(coded: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "3", "Taxonomy of LLM-Mediated Patient Work", "Pilot coding shows six recurring functions and one cross-cutting boundary problem.")

    themes = [
        ("Translator", "Makes medical language usable", ["Labs", "Pathology", "Imaging"], PAL["blue"], ["lab_translation", "medical_translation", "report_interpretation"]),
        ("Pattern finder", "Connects fragments across time", ["Records", "Symptoms", "Triggers"], PAL["teal"], ["record_synthesis", "differential_generation"]),
        ("Appointment amplifier", "Turns confusion into action", ["Questions", "Summaries", "Triage"], PAL["green"], ["urgent_triage", "care_escalation"]),
        ("Companion", "Provides presence between encounters", ["Grounding", "Disclosure", "Recovery"], PAL["plum"], ["emotional_support", "addiction_support", "disclosure", "creative_coping"]),
        ("Behavior scaffold", "Reduces friction of daily change", ["Meal logging", "Routines", "Rehab"], PAL["gold"], ["diet_weight_tracking", "symptom_tracking"]),
        ("Risky validator", "Makes unsafe loops feel coherent", ["OCD", "Psychosis", "Medication"], PAL["red"], ["ai_as_therapy", "reassurance_seeking", "medication_timing"]),
    ]
    use_counts = Counter(r["primary_use_case"] for r in coded)
    max_count = max(sum(use_counts[u] for u in uses) for *_, uses in themes)

    positions = [(135, 330), (855, 330), (1575, 330), (135, 840), (855, 840), (1575, 840)]
    for (name, desc, items, color, uses), (x, y) in zip(themes, positions):
        count = sum(use_counts[u] for u in uses)
        shadow_box(d, (x, y, x + 610, y + 390), radius=18)
        d.rectangle((x, y, x + 14, y + 390), fill=rgb(color))
        d.text((x + 45, y + 38), name, fill=rgb(color), font=font(35, "bold"))
        d.text((x + 45, y + 88), desc, fill=rgb(PAL["muted"]), font=font(23))
        yy = y + 150
        for item in items:
            d.rounded_rectangle((x + 45, yy, x + 240, yy + 42), radius=21, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]))
            d.text((x + 66, yy + 8), item, fill=rgb(PAL["ink"]), font=font(20))
            yy += 55
        d.text((x + 340, y + 165), str(count), fill=rgb(PAL["ink"]), font=font(68, "bold"))
        d.text((x + 337, y + 245), "pilot-coded\nrecords", fill=rgb(PAL["muted"]), font=font(22))
        d.rounded_rectangle((x + 45, y + 334, x + 565, y + 358), radius=12, fill=rgb("#e7edf1"))
        d.rounded_rectangle((x + 45, y + 334, x + 45 + int(520 * count / max_count), y + 358), radius=12, fill=rgb(color))

    d.text((120, 1370), "Counts come from a 35-record pilot-coded subset and support theme development, not prevalence claims.", fill=rgb(PAL["muted"]), font=font(21))
    img.convert("RGB").save(path, quality=96)


def make_fig4(path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "4", "Boundary Conditions for Safer Use", "Usefulness rises when LLMs support sensemaking; risk rises when they assume clinical accountability.")

    x0, y0, x1, y1 = 260, 350, 2140, 1190
    shadow_box(d, (x0, y0, x1, y1), radius=22)
    midx, midy = (x0 + x1) // 2, (y0 + y1) // 2
    d.line((midx, y0, midx, y1), fill=rgb(PAL["hair"]), width=5)
    d.line((x0, midy, x1, midy), fill=rgb(PAL["hair"]), width=5)

    d.text((x0, y0 - 70), "Lower clinical stakes", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    d.text((x1 - 255, y0 - 70), "Higher clinical stakes", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    d.text((85, y0 + 25), "More decisive", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    d.text((85, y1 - 35), "More supportive", fill=rgb(PAL["muted"]), font=font(22, "bold"))

    quads = [
        (x0 + 60, y0 + 55, "Useful translator", "Best fit: explain, summarize, prepare", ["Explain jargon", "Summarize reports", "Prepare questions"], PAL["blue"]),
        (midx + 60, y0 + 55, "Clinical judgment required", "High-stakes decisions need escalation", ["Urgency", "Medication changes", "Treatment timing"], PAL["red"]),
        (x0 + 60, midy + 55, "Supportive scaffold", "Helpful when bounded by daily routines", ["Meal logging", "Grounding", "Recovery routines"], PAL["green"]),
        (midx + 60, midy + 55, "Safeguarding required", "Risky when friction and reality testing are needed", ["OCD reassurance", "Psychosis / mania", "Suicidality"], PAL["gold"]),
    ]
    for x, y, title, subtitle, items, color in quads:
        d.text((x, y), title, fill=rgb(color), font=font(35, "bold"))
        d.text((x, y + 50), subtitle, fill=rgb(PAL["muted"]), font=font(22))
        yy = y + 130
        for item in items:
            d.ellipse((x, yy + 11, x + 18, yy + 29), fill=rgb(color))
            d.text((x + 36, yy), item, fill=rgb(PAL["ink"]), font=font(27))
            yy += 54

    d.rounded_rectangle((445, 1280, 1955, 1364), radius=18, fill=rgb("#eef5f7"), outline=rgb(PAL["hair"]), width=2)
    d.text((490, 1301), "Design implication:", fill=rgb(PAL["blue"]), font=font(25, "bold"))
    d.text((730, 1301), "shift from confident answers toward explanation, uncertainty, questions, and escalation.", fill=rgb(PAL["ink"]), font=font(25))
    img.convert("RGB").save(path, quality=96)


def theme_for_use_case(use_case: str) -> str:
    if use_case in {"lab_translation", "medical_translation", "report_interpretation"}:
        return "Translator"
    if use_case in {"record_synthesis", "differential_generation"}:
        return "Pattern finder"
    if use_case in {"urgent_triage", "care_escalation"}:
        return "Appointment amplifier"
    if use_case in {"emotional_support", "addiction_support", "disclosure", "creative_coping", "ai_as_therapy"}:
        return "Companion"
    if use_case in {"diet_weight_tracking", "symptom_tracking"}:
        return "Behavior scaffold"
    if use_case in {"reassurance_seeking", "medication_timing", "medication_or_substance_decision"}:
        return "Risk boundary"
    return "Other"


def domain_label(domain: str) -> str:
    mapping = {
        "mental_health": "Mental health",
        "acute_triage": "Acute triage",
        "chronic_illness": "Chronic illness",
        "oncology": "Oncology",
        "records_labs": "Records / labs",
        "behavior_change": "Behavior change",
    }
    return mapping.get(domain, "Other")


def intensity_color(base_hex: str, value: int, max_value: int) -> tuple[int, int, int]:
    if value <= 0:
        return rgb("#f4f6f7")
    base = rgb(base_hex)
    white = rgb("#ffffff")
    t = 0.22 + 0.62 * (value / max_value)
    return tuple(int(white[i] * (1 - t) + base[i] * t) for i in range(3))


def make_fig5_heatmap(coded: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "5", "Evidence Landscape", "Where health domains and LLM functions intersect in the pilot-coded subset.")

    domains = ["Mental health", "Acute triage", "Chronic illness", "Oncology", "Records / labs", "Behavior change", "Other"]
    themes = ["Translator", "Pattern finder", "Appointment amplifier", "Companion", "Behavior scaffold", "Risk boundary"]
    matrix = {domain: Counter() for domain in domains}
    for row in coded:
        dom = domain_label(row["domain_group"])
        if dom not in matrix:
            dom = "Other"
        matrix[dom][theme_for_use_case(row["primary_use_case"])] += 1
    max_value = max(max(counter.values() or [0]) for counter in matrix.values())

    x0, y0 = 360, 345
    cell_w, cell_h = 285, 122
    d.text((120, y0 + 12), "Health domain", fill=rgb(PAL["muted"]), font=font(23, "bold"))
    for j, theme in enumerate(themes):
        lines = wrap(d, theme, font(21, "bold"), cell_w - 18)
        for k, line in enumerate(lines):
            d.text((x0 + j * cell_w + 12, y0 - 72 + k * 26), line, fill=rgb(PAL["muted"]), font=font(21, "bold"))

    for i, domain in enumerate(domains):
        y = y0 + i * cell_h
        d.text((120, y + 42), domain, fill=rgb(PAL["ink"]), font=font(24, "bold"))
        for j, theme in enumerate(themes):
            x = x0 + j * cell_w
            value = matrix[domain][theme]
            fill = intensity_color(PAL["blue"], value, max_value)
            d.rounded_rectangle((x, y, x + cell_w - 16, y + cell_h - 16), radius=18, fill=fill, outline=rgb(PAL["hair"]), width=2)
            if value:
                d.text((x + cell_w // 2 - 12, y + 39), str(value), fill=rgb(PAL["ink"]), font=font(34, "bold"))
            else:
                d.text((x + cell_w // 2 - 7, y + 43), "–", fill=rgb(PAL["muted"]), font=font(28))

    # Legend
    lx, ly = 360, 1265
    d.text((120, ly + 8), "Cell intensity", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    for k in range(6):
        val = int(round(k * max_value / 5))
        d.rounded_rectangle((lx + k * 92, ly, lx + k * 92 + 70, ly + 40), radius=10, fill=intensity_color(PAL["blue"], val, max_value), outline=rgb(PAL["hair"]))
    d.text((lx + 585, ly + 7), f"0 to {max_value} pilot-coded records", fill=rgb(PAL["muted"]), font=font(21))
    d.text((120, 1372), "Interpretation: concentration marks where anecdotes are analytically dense, not where use is most prevalent.", fill=rgb(PAL["muted"]), font=font(21))
    img.convert("RGB").save(path, quality=96)


def make_fig6_terrain(coded: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "6", "Benefit–Risk Terrain", "LLM use cases cluster by clinical stakes and need for psychological or behavioral safeguarding.")

    theme_counts = Counter(theme_for_use_case(row["primary_use_case"]) for row in coded)
    points = [
        ("Translator", 0.22, 0.27, PAL["blue"]),
        ("Pattern finder", 0.46, 0.38, PAL["teal"]),
        ("Appointment amplifier", 0.74, 0.32, PAL["green"]),
        ("Behavior scaffold", 0.38, 0.64, PAL["gold"]),
        ("Companion", 0.27, 0.80, PAL["plum"]),
        ("Risk boundary", 0.78, 0.78, PAL["red"]),
    ]

    x0, y0, w, h = 300, 315, 1750, 930
    shadow_box(d, (x0, y0, x0 + w, y0 + h), radius=22)
    # Subtle quadrant washes
    d.rectangle((x0, y0, x0 + w // 2, y0 + h // 2), fill=rgb("#f8fafb"))
    d.rectangle((x0 + w // 2, y0, x0 + w, y0 + h // 2), fill=rgb("#fbf4f3"))
    d.rectangle((x0, y0 + h // 2, x0 + w // 2, y0 + h), fill=rgb("#f5f7ef"))
    d.rectangle((x0 + w // 2, y0 + h // 2, x0 + w, y0 + h), fill=rgb("#f8f2e8"))
    d.line((x0 + w // 2, y0, x0 + w // 2, y0 + h), fill=rgb(PAL["hair"]), width=4)
    d.line((x0, y0 + h // 2, x0 + w, y0 + h // 2), fill=rgb(PAL["hair"]), width=4)
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=22, outline=rgb(PAL["hair"]), width=3)

    d.text((x0, y0 - 65), "Lower clinical accountability", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    d.text((x0 + w - 350, y0 - 65), "Higher clinical accountability", fill=rgb(PAL["muted"]), font=font(22, "bold"))
    d.text((65, y0 + 35), "More psychological /\nbehavioral intensity", fill=rgb(PAL["muted"]), font=font(21, "bold"))
    d.text((82, y0 + h - 80), "More informational", fill=rgb(PAL["muted"]), font=font(21, "bold"))

    for name, xp, yp, color in points:
        count = theme_counts[name]
        cx = int(x0 + xp * w)
        cy = int(y0 + yp * h)
        r = 44 + int(count * 4.5)
        d.ellipse((cx - r - 6, cy - r + 8, cx + r - 6, cy + r + 8), fill=rgb("#e3e8ec"))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=rgb(color), outline=rgb(PAL["white"]), width=5)
        d.text((cx - 15 * len(str(count)), cy - 30), str(count), fill="white", font=font(54, "bold"))
        label_y = cy + r + 20
        d.text((cx - d.textbbox((0, 0), name, font=font(24, "bold"))[2] // 2, label_y), name, fill=rgb(PAL["ink"]), font=font(24, "bold"))

    d.rounded_rectangle((430, 1288, 1970, 1368), radius=18, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]), width=2)
    d.text((470, 1310), "Reading the map:", fill=rgb(PAL["blue"]), font=font(23, "bold"))
    d.text((690, 1310), "movement upward/right means the model needs more friction, escalation, and accountability.", fill=rgb(PAL["ink"]), font=font(23))
    img.convert("RGB").save(path, quality=96)


def make_fig7_pipeline(path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "7", "From Anecdote to Research Agenda", "A structured corpus turns public stories into testable hypotheses and safety requirements.")

    stages = [
        ("Public narratives", "Posts, forums,\nessays, media", PAL["slate"]),
        ("Qualitative coding", "Task, domain,\nvalence, risk", PAL["blue"]),
        ("Use taxonomy", "Translator, pattern finder,\ncompanion, scaffold", PAL["teal"]),
        ("Risk mechanisms", "Triage, medication,\nOCD, psychosis, privacy", PAL["red"]),
        ("Formal studies", "Benchmarks, audits,\nclinical workflows", PAL["green"]),
    ]
    x_positions = [150, 610, 1070, 1530, 1990]
    y = 560
    for i, ((title, body, color), x) in enumerate(zip(stages, x_positions)):
        d.ellipse((x - 110, y - 110, x + 110, y + 110), fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]), width=3)
        d.ellipse((x - 84, y - 84, x + 84, y + 84), fill=rgb(color), outline=rgb(PAL["white"]), width=5)
        d.text((x - d.textbbox((0, 0), str(i + 1), font=font(58, "bold"))[2] // 2, y - 42), str(i + 1), fill="white", font=font(58, "bold"))
        d.text((x - d.textbbox((0, 0), title, font=font(25, "bold"))[2] // 2, y + 140), title, fill=rgb(PAL["ink"]), font=font(25, "bold"))
        yy = y + 184
        for line in body.split("\n"):
            d.text((x - d.textbbox((0, 0), line, font=font(20))[2] // 2, yy), line, fill=rgb(PAL["muted"]), font=font(20))
            yy += 28
        if i < len(stages) - 1:
            ax = x + 125
            bx = x_positions[i + 1] - 125
            d.line((ax, y, bx, y), fill=rgb(PAL["hair"]), width=9)
            d.polygon([(bx + 20, y), (bx - 10, y - 24), (bx - 10, y + 24)], fill=rgb(PAL["hair"]))

    lower_cards = [
        ("What anecdotes are good for", ["Finding real workflows", "Detecting unmet needs", "Generating safety hypotheses"], PAL["blue"]),
        ("What anecdotes are not for", ["Estimating prevalence", "Proving efficacy", "Verifying diagnoses"], PAL["red"]),
        ("What to build next", ["Direct-permalink corpus", "Double coding", "Prospective patient studies"], PAL["green"]),
    ]
    for i, (head, bullets, color) in enumerate(lower_cards):
        x = 180 + i * 740
        shadow_box(d, (x, 1015, x + 620, 1288), radius=18)
        d.rectangle((x, 1015, x + 12, 1288), fill=rgb(color))
        d.text((x + 38, 1050), head, fill=rgb(color), font=font(25, "bold"))
        yy = 1110
        for bullet in bullets:
            d.ellipse((x + 42, yy + 8, x + 56, yy + 22), fill=rgb(color))
            d.text((x + 76, yy), bullet, fill=rgb(PAL["ink"]), font=font(22))
            yy += 45

    d.text((120, 1380), "Scientific value comes from making the anecdotal layer traceable, coded, and explicitly limited.", fill=rgb(PAL["muted"]), font=font(22))
    img.convert("RGB").save(path, quality=96)


def corpus_text(seed: list[dict[str, str]]) -> str:
    fields = ["health_domain", "use_case", "outcome_claim", "evidentiary_notes", "initial_codes"]
    return " ".join(row.get(field, "") for row in seed for field in fields).lower()


def phrase_count(text: str, patterns: list[str]) -> int:
    total = 0
    for pattern in patterns:
        total += len(re.findall(pattern, text))
    return total


def term_regex(term: str) -> str:
    escaped = re.escape(term)
    if " " in term or "-" in term:
        return escaped
    if len(term) <= 3:
        return rf"\b{escaped}\b"
    return rf"\b{escaped}\w*\b"


def draw_node(
    d: ImageDraw.ImageDraw,
    label: str,
    count: int,
    x: int,
    y: int,
    color: str,
    scale: tuple[int, int],
):
    min_count, max_count = scale
    if max_count == min_count:
        t = 0.5
    else:
        t = (count - min_count) / (max_count - min_count)
    label_font = font(int(22 + 12 * t), "bold")
    count_font = font(16)
    label_box = d.textbbox((0, 0), label, font=label_font)
    count_text = f"n={count}"
    count_box = d.textbbox((0, 0), count_text, font=count_font)
    w = max(label_box[2], count_box[2]) + 58
    h = 68 + int(20 * t)
    x0, y0 = x - w // 2, y - h // 2
    d.rounded_rectangle((x0 + 4, y0 + 6, x0 + w + 4, y0 + h + 6), radius=26, fill=rgb("#e1e7eb"))
    d.rounded_rectangle((x0, y0, x0 + w, y0 + h), radius=26, fill=rgb("#ffffff"), outline=rgb(color), width=3)
    d.ellipse((x0 + 18, y0 + h // 2 - 9, x0 + 36, y0 + h // 2 + 9), fill=rgb(color))
    d.text((x0 + 48, y0 + 13), label, fill=rgb(PAL["ink"]), font=label_font)
    d.text((x0 + 50, y0 + h - 29), count_text, fill=rgb(PAL["muted"]), font=count_font)


def make_fig8_word_map(seed: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "8", "The Language of Patient Work", "A corpus-derived word map of how patients describe LLMs around care.")

    text = corpus_text(seed)
    terms = [
        ("reports", ["report", "pathology", "imaging", "scan", "mri", "ultrasound", "sleep study"], PAL["blue"], 520, 420),
        ("labs", ["lab", "blood work", "ck", "psa", "antibody", "biopsy"], PAL["blue"], 620, 640),
        ("symptoms", ["symptom", "pain", "rash", "fatigue", "cough", "soreness"], PAL["teal"], 870, 460),
        ("questions", ["question", "ask", "prepare", "appointment", "oncologist"], PAL["green"], 1120, 620),
        ("urgent care", ["urgent", "er", "emergency", "hospital", "red flag"], PAL["green"], 1410, 450),
        ("cancer", ["cancer", "oncology", "tumor", "chemotherapy", "radiation"], PAL["plum"], 1590, 665),
        ("caregiver", ["caregiver", "family", "son", "father", "spouse", "partner"], PAL["teal"], 900, 820),
        ("therapy", ["therapy", "therapeutic", "ground", "trauma", "depression", "anxiety"], PAL["plum"], 1215, 900),
        ("cravings", ["craving", "withdrawal", "cannabis", "weed", "sober", "quit"], PAL["gold"], 875, 1080),
        ("meal logging", ["meal", "diet", "calorie", "weight loss", "logging"], PAL["gold"], 590, 1020),
        ("medication", ["medication", "drug", "dose", "levothyroxine", "iron", "ivermectin"], PAL["red"], 1670, 930),
        ("reassurance", ["reassurance", "rumination", "ocd", "compulsion", "spiral"], PAL["red"], 1370, 1110),
        ("psychosis", ["psychosis", "mania", "delusion", "sycophancy", "hallucination"], PAL["red"], 1775, 1130),
        ("privacy", ["privacy", "upload", "records", "diaries", "family-member", "genomics"], PAL["slate"], 650, 1125),
    ]
    scored = []
    for label, patterns, color, x, y in terms:
        count = phrase_count(text, [term_regex(pattern) for pattern in patterns])
        scored.append((label, max(1, count), color, x, y))
    counts = [item[1] for item in scored]
    scale = (min(counts), max(counts))

    # Analytic field.
    x0, y0, x1, y1 = 320, 310, 2050, 1260
    shadow_box(d, (x0, y0, x1, y1), radius=26, fill="#fbfcfd")
    for cx, cy, rx, ry, color in [
        (650, 580, 520, 330, PAL["soft_blue"]),
        (1260, 650, 540, 330, "#eef6f1"),
        (1560, 1030, 520, 310, PAL["soft_red"]),
        (720, 1080, 480, 250, PAL["soft_gold"]),
    ]:
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        od.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=rgba(color, 150))
        img.alpha_composite(overlay)
        d = ImageDraw.Draw(img)

    d.line((x0 + 60, y1 - 80, x1 - 60, y1 - 80), fill=rgb(PAL["hair"]), width=4)
    d.polygon([(x1 - 45, y1 - 80), (x1 - 80, y1 - 103), (x1 - 80, y1 - 57)], fill=rgb(PAL["hair"]))
    d.line((x0 + 70, y1 - 70, x0 + 70, y0 + 60), fill=rgb(PAL["hair"]), width=4)
    d.polygon([(x0 + 70, y0 + 44), (x0 + 47, y0 + 82), (x0 + 93, y0 + 82)], fill=rgb(PAL["hair"]))
    d.text((x0 + 115, y1 - 55), "from understanding", fill=rgb(PAL["muted"]), font=font(20, "bold"))
    d.text((x1 - 300, y1 - 55), "toward action", fill=rgb(PAL["muted"]), font=font(20, "bold"))

    # Soft thematic labels behind nodes.
    for label, x, y, color in [
        ("translation", 650, 350, PAL["blue"]),
        ("care navigation", 1200, 350, PAL["green"]),
        ("daily scaffolding", 500, 910, PAL["gold"]),
        ("boundary risk", 1540, 830, PAL["red"]),
    ]:
        d.text((x, y), label.upper(), fill=rgb(color), font=font(21, "bold"))

    # Draw connecting curves as restrained relationship hints.
    links = [
        ("reports", "questions"), ("labs", "questions"), ("symptoms", "urgent care"),
        ("therapy", "reassurance"), ("medication", "urgent care"), ("cancer", "questions"),
        ("meal logging", "cravings"), ("privacy", "reports"), ("psychosis", "reassurance"),
    ]
    pos = {label: (x, y) for label, _, _, x, y in scored}
    for a, b in links:
        ax, ay = pos[a]
        bx, by = pos[b]
        midx = (ax + bx) // 2
        d.line((ax, ay, midx, ay, midx, by, bx, by), fill=rgb("#cdd8df"), width=3, joint="curve")

    for label, count, color, x, y in sorted(scored, key=lambda item: item[1]):
        draw_node(d, label, count, x, y, color, scale)

    d.rounded_rectangle((165, 1315, 2235, 1390), radius=18, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]), width=2)
    d.text((205, 1336), "Reading the map:", fill=rgb(PAL["blue"]), font=font(23, "bold"))
    d.text((425, 1336), "terms are counted from corpus fields and placed by analytic role, not by dimensional modeling.", fill=rgb(PAL["ink"]), font=font(23))
    img.convert("RGB").save(path, quality=96)


def category_count(text: str, patterns: list[str]) -> int:
    return max(1, phrase_count(text, [term_regex(pattern) for pattern in patterns]))


def draw_stream(d: ImageDraw.ImageDraw, x0: int, y0: int, x1: int, y1: int, width: int, color: str):
    steps = 24
    top = []
    bottom = []
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * (3 * t * t - 2 * t * t * t)
        taper = width * (0.88 + 0.12 * (1 - abs(2 * t - 1)))
        top.append((x, y - taper / 2))
        bottom.append((x, y + taper / 2))
    d.polygon(top + bottom[::-1], fill=rgba(color, 155))


def flow_card(
    d: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    label: str,
    count: int,
    color: str,
):
    shadow_box(d, (x, y, x + w, y + h), radius=20, fill="#ffffff")
    d.rectangle((x, y, x + 10, y + h), fill=rgb(color))
    label_lines = wrap(d, label, font(21, "bold"), w - 185)
    for i, line in enumerate(label_lines[:2]):
        d.text((x + 32, y + 22 + i * 27), line, fill=rgb(PAL["ink"]), font=font(21, "bold"))
    signal_y = y + 72 if len(label_lines) > 1 else y + 62
    d.text((x + 32, signal_y), f"term signal: {count}", fill=rgb(PAL["muted"]), font=font(17, "bold"))
    d.rounded_rectangle((x + w - 115, y + 36, x + w - 42, y + 78), radius=21, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]))
    count_text = str(count)
    count_w = d.textbbox((0, 0), count_text, font=font(23, "bold"))[2]
    d.text((x + w - 78 - count_w // 2, y + 46), count_text, fill=rgb(color), font=font(23, "bold"))


def make_fig9_narrative_grammar(seed: list[dict[str, str]], path: Path) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_title(d, "9", "The Narrative Grammar of LLM Health Use", "A flow model of what patient anecdotes tend to contain.")

    text = corpus_text(seed)
    columns = [
        (
            "System gap",
            [
                ("opaque records", ["report", "pathology", "lab", "imaging", "portal"], PAL["blue"]),
                ("fragmented care", ["doctor", "specialist", "referral", "years", "unrevealing"], PAL["teal"]),
                ("unavailable support", ["therapy", "night", "craving", "anxiety", "withdrawal"], PAL["plum"]),
                ("high-stakes uncertainty", ["urgent", "cancer", "medication", "psychosis", "pregnancy"], PAL["red"]),
            ],
        ),
        (
            "LLM function",
            [
                ("translate", ["explain", "summarize", "translate", "jargon", "interpret"], PAL["blue"]),
                ("synthesize", ["connect", "pattern", "history", "records", "longitudinal"], PAL["teal"]),
                ("prepare", ["question", "appointment", "oncologist", "visit", "doctor"], PAL["green"]),
                ("contain", ["support", "ground", "vent", "reflect", "craving"], PAL["plum"]),
            ],
        ),
        (
            "Patient action",
            [
                ("asks better questions", ["question", "prepare", "follow-up", "discussion"], PAL["green"]),
                ("seeks care or tests", ["er", "urgent", "test", "doctor", "hospital"], PAL["green"]),
                ("changes routine", ["meal", "diet", "exercise", "quit", "rehab"], PAL["gold"]),
                ("relies or loops", ["reassurance", "spiral", "dependency", "rumination"], PAL["red"]),
            ],
        ),
        (
            "Boundary condition",
            [
                ("bridge to clinician", ["clinician", "doctor", "oncologist", "pharmacist"], PAL["green"]),
                ("verify claims", ["verify", "source", "caution", "uncertain"], PAL["slate"]),
                ("add friction", ["red flag", "urgent", "medication", "unsafe"], PAL["red"]),
                ("protect privacy", ["privacy", "upload", "records", "family", "genomics"], PAL["blue"]),
            ],
        ),
    ]

    x_positions = [190, 765, 1340, 1915]
    card_w = 392
    y_top = 330
    item_gap = 188
    centers: list[list[tuple[int, int, int, str]]] = []
    for col_idx, (heading, items) in enumerate(columns):
        x = x_positions[col_idx]
        d.text((x, 255), heading, fill=rgb(PAL["ink"]), font=font(31, "serif_bold"))
        col_centers = []
        for item_idx, (label, patterns, color) in enumerate(items):
            count = category_count(text, patterns)
            y = y_top + item_idx * item_gap
            h = 112 + min(42, count // 2)
            flow_card(d, x, y, card_w, h, label, count, color)
            col_centers.append((x + card_w, y + h // 2, count, color))
        centers.append(col_centers)

    stream_overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(stream_overlay)
    routes = [
        (0, 0, 1, 0, 26, PAL["blue"]),
        (0, 1, 1, 1, 22, PAL["teal"]),
        (0, 2, 1, 3, 20, PAL["plum"]),
        (0, 3, 1, 2, 18, PAL["red"]),
        (1, 0, 2, 0, 24, PAL["blue"]),
        (1, 1, 2, 1, 22, PAL["teal"]),
        (1, 2, 2, 0, 20, PAL["green"]),
        (1, 3, 2, 2, 20, PAL["plum"]),
        (2, 0, 3, 0, 22, PAL["green"]),
        (2, 1, 3, 0, 24, PAL["green"]),
        (2, 2, 3, 1, 18, PAL["gold"]),
        (2, 3, 3, 2, 22, PAL["red"]),
    ]
    for c0, i0, c1, i1, width, color in routes:
        x0, y0, _, _ = centers[c0][i0]
        x1 = x_positions[c1]
        y1 = centers[c1][i1][1]
        draw_stream(sd, x0 + 18, y0, x1 - 18, y1, width, color)
    img.alpha_composite(stream_overlay)
    d = ImageDraw.Draw(img)

    # Redraw cards on top of streams for crispness.
    for col_idx, (heading, items) in enumerate(columns):
        x = x_positions[col_idx]
        for item_idx, (label, patterns, color) in enumerate(items):
            count = category_count(text, patterns)
            y = y_top + item_idx * item_gap
            h = 112 + min(42, count // 2)
            flow_card(d, x, y, card_w, h, label, count, color)

    d.rounded_rectangle((250, 1268, 2150, 1370), radius=20, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]), width=2)
    d.text((292, 1294), "Central story:", fill=rgb(PAL["blue"]), font=font(25, "bold"))
    story = "LLMs appear most valuable when they turn opacity into questions and next steps; risk rises when the loop closes without accountable care."
    for i, line in enumerate(wrap(d, story, font(24), 1540)):
        d.text((500, 1294 + i * 32), line, fill=rgb(PAL["ink"]), font=font(24))

    img.convert("RGB").save(path, quality=96)


def make_figures(seed: list[dict[str, str]], coded: list[dict[str, str]]) -> list[Path]:
    FIG.mkdir(parents=True, exist_ok=True)
    paths = [
        FIG / "figure_1_signal.png",
        FIG / "figure_2_corpus_architecture.png",
        FIG / "figure_3_taxonomy.png",
        FIG / "figure_4_boundary_conditions.png",
        FIG / "figure_5_evidence_landscape.png",
        FIG / "figure_6_benefit_risk_terrain.png",
        FIG / "figure_7_research_agenda.png",
        FIG / "figure_8_language_map.png",
        FIG / "figure_9_narrative_grammar.png",
    ]
    make_fig1(paths[0])
    make_fig2(seed, paths[1])
    make_fig3(coded, paths[2])
    make_fig4(paths[3])
    make_fig5_heatmap(coded, paths[4])
    make_fig6_terrain(coded, paths[5])
    make_fig7_pipeline(paths[6])
    make_fig8_word_map(seed, paths[7])
    make_fig9_narrative_grammar(seed, paths[8])
    return paths


def draw_wrapped_cell(
    d: ImageDraw.ImageDraw,
    text: str,
    x: int,
    y: int,
    width: int,
    f: ImageFont.ImageFont,
    fill: str,
    line_gap: int = 30,
    max_lines: int | None = None,
) -> int:
    lines = wrap(d, text, f, width)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(".") + "..."
    for i, line in enumerate(lines):
        d.text((x, y + i * line_gap), line, fill=rgb(fill), font=f)
    return len(lines) * line_gap


def table_plate(
    path: Path,
    label: str,
    title: str,
    subtitle: str,
    columns: list[str],
    widths: list[int],
    rows: list[list[str]],
    accent: str,
    note: str,
) -> None:
    img = Image.new("RGBA", (2400, 1500), rgb(PAL["paper"]) + (255,))
    d = ImageDraw.Draw(img)
    draw_plate_title(d, label, title, subtitle)

    x0, y0 = 120, 300
    table_w = sum(widths)
    header_h = 72
    head_font = font(22, "bold")
    body_font = font(22)
    body_bold = font(22, "bold")
    small_font = font(20)
    line_gap = 30

    # Compute row heights from wrapped line counts.
    row_heights: list[int] = []
    for row in rows:
        max_lines = 1
        for text, col_w in zip(row, widths):
            lines = wrap(d, text, body_font, col_w - 46)
            max_lines = max(max_lines, len(lines))
        row_heights.append(max(86, 38 + max_lines * line_gap))

    total_h = header_h + sum(row_heights)
    shadow_box(d, (x0, y0, x0 + table_w, y0 + total_h), radius=18)
    d.rounded_rectangle((x0, y0, x0 + table_w, y0 + header_h), radius=18, fill=rgb(accent))
    d.rectangle((x0, y0 + 34, x0 + table_w, y0 + header_h), fill=rgb(accent))

    x = x0
    for col, w in zip(columns, widths):
        d.text((x + 22, y0 + 23), col, fill="white", font=head_font)
        x += w

    y = y0 + header_h
    for r_idx, (row, rh) in enumerate(zip(rows, row_heights)):
        fill = "#fbfcfd" if r_idx % 2 == 0 else "#ffffff"
        d.rectangle((x0, y, x0 + table_w, y + rh), fill=rgb(fill))
        d.line((x0, y, x0 + table_w, y), fill=rgb(PAL["hair"]), width=2)
        x = x0
        for c_idx, (text, w) in enumerate(zip(row, widths)):
            f = body_bold if c_idx == 0 else body_font
            col_fill = PAL["ink"] if c_idx != 1 or text.isdigit() else PAL["blue"]
            if c_idx == 1 and text.isdigit():
                d.rounded_rectangle((x + 24, y + 22, x + 94, y + 62), radius=20, fill=rgb("#edf3f5"), outline=rgb(PAL["hair"]))
                d.text((x + 47 - 6 * len(text), y + 29), text, fill=rgb(PAL["ink"]), font=body_bold)
            else:
                draw_wrapped_cell(d, text, x + 22, y + 22, w - 46, f, col_fill, line_gap=line_gap)
            x += w
            if c_idx < len(widths) - 1:
                d.line((x, y, x, y + rh), fill=rgb(PAL["hair"]), width=2)
        y += rh
    d.line((x0, y0 + total_h, x0 + table_w, y0 + total_h), fill=rgb(PAL["hair"]), width=2)

    # Note strip.
    note_y = min(1365, y0 + total_h + 44)
    d.rounded_rectangle((x0, note_y, x0 + table_w, note_y + 74), radius=18, fill=rgb("#eef3f5"), outline=rgb(PAL["hair"]), width=2)
    d.text((x0 + 28, note_y + 22), "Note", fill=rgb(PAL["blue"]), font=font(21, "bold"))
    draw_wrapped_cell(d, note, x0 + 110, note_y + 22, table_w - 150, small_font, PAL["muted"], line_gap=27)
    img.convert("RGB").save(path, quality=96)


def make_table_plates() -> list[Path]:
    FIG.mkdir(parents=True, exist_ok=True)
    paths = [
        FIG / "table_1_corpus_characteristics.png",
        FIG / "table_2_use_case_taxonomy.png",
        FIG / "table_3_safety_mechanisms.png",
    ]
    table_plate(
        paths[0],
        "Table 1.",
        "Corpus Characteristics",
        "What the 100-record seed corpus can and cannot support.",
        ["Characteristic", "n", "Interpretation for analysis"],
        [640, 140, 1400],
        [
            ["Seed corpus", "100", "Exploratory archive of public online accounts; not a prevalence sample."],
            ["Helpful or perceived-helpful", "78", "Poster-reported benefit, not verified clinical efficacy."],
            ["Harmful or unhelpful", "13", "Includes near misses, worsening, unsafe advice, and model failures."],
            ["Mixed, uncertain, or risk-bearing", "8", "Useful experiences with unresolved clinical or methodological caveats."],
            ["No resolution", "1", "AI increased information but did not overcome access or referral bottlenecks."],
            ["Ready-ish include", "46", "Stable enough for thematic analysis after routine source checking."],
            ["Needs cleanup", "31", "Mostly comment-level records that need direct permalinks before being featured."],
        ],
        PAL["blue"],
        "Counts describe the exploratory corpus assembled for this paper, not population prevalence or verified clinical effect.",
    )
    table_plate(
        paths[1],
        "Table 2.",
        "Use-Case Taxonomy",
        "How public accounts describe the work LLMs perform around care.",
        ["Theme", "Patient work described", "Representative records"],
        [500, 1180, 500],
        [
            ["Translator", "Explains labs, pathology, imaging, notes, diagnoses, portal language, and medical jargon.", "LHA-031, LHA-033, LHA-036, LHA-086"],
            ["Pattern finder", "Synthesizes longitudinal symptoms, records, food triggers, wearable data, and specialist notes.", "LHA-008, LHA-058, LHA-078, LHA-082, LHA-084"],
            ["Appointment amplifier", "Generates questions, visit summaries, care-seeking prompts, and clinician-facing discussion lists.", "LHA-001, LHA-002, LHA-033, LHA-094"],
            ["Always-on companion", "Provides grounding, disclosure, reflection, recovery support, and late-night emotional presence.", "LHA-022, LHA-048, LHA-052, LHA-075"],
            ["Behavior scaffold", "Reduces friction in meal logging, tracking, rehabilitation, routines, and habit change.", "LHA-020, LHA-021, LHA-022, LHA-083"],
            ["Risky validator", "Can reinforce rumination, unsafe certainty, delusional loops, reassurance seeking, or medication mistakes.", "LHA-014, LHA-049, LHA-055, LHA-056"],
        ],
        PAL["teal"],
        "Themes were developed from a pilot-coded subset of 35 records and should be treated as analytic categories, not frequencies.",
    )
    table_plate(
        paths[2],
        "Table 3.",
        "Safety Mechanisms and Design Responses",
        "Where the same properties that help users can create clinical or psychological risk.",
        ["Risk mechanism", "What the anecdote shows", "Design response"],
        [590, 910, 680],
        [
            ["Wrong triage", "A fluent answer can delay care when symptoms need examination, severity assessment, or time-sensitive treatment.", "Escalate red flags; ask severity questions; avoid narrow reassurance."],
            ["Unsafe medication or diet advice", "Mundane questions can carry toxicology, interaction, pregnancy, oncology, or comorbidity risks.", "Avoid dosing changes; bridge to pharmacist or clinician; state uncertainty."],
            ["Compulsive reassurance", "Always-available support can become part of OCD or anxiety maintenance loops.", "Limit repetitive reassurance; redirect to coping plans and human care."],
            ["Psychosis or mania amplification", "Symbolic, grandiose, or paranoid interpretations can be mirrored instead of interrupted.", "Preserve reality testing; avoid sycophancy; escalate crisis patterns."],
            ["Privacy exposure", "Users upload labs, imaging, pathology, genomics, diaries, and family-member records.", "Offer redaction, local processing options, and explicit data-handling cues."],
            ["System bottleneck", "AI can make patients more informed without making referrals, insurance, or specialists respond.", "Produce concise escalation summaries, referral scripts, and question lists."],
        ],
        PAL["red"],
        "The design responses are implications generated from the corpus; they are not validated safety interventions.",
    )
    return paths


def styles():
    base = getSampleStyleSheet()
    base.add(ParagraphStyle("TitleJournal", parent=base["Title"], fontName="Times-Bold", fontSize=30, leading=35, textColor=colors.HexColor(PAL["ink"]), alignment=TA_CENTER, spaceAfter=6))
    base.add(ParagraphStyle("SubtitleJournal", parent=base["Normal"], fontName="Helvetica", fontSize=13, leading=17, textColor=colors.HexColor(PAL["muted"]), alignment=TA_CENTER, spaceAfter=7))
    base.add(ParagraphStyle("Author", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=colors.HexColor(PAL["ink"]), alignment=TA_CENTER, spaceAfter=18))
    base.add(ParagraphStyle("H1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=15.5, leading=19, textColor=colors.HexColor(PAL["blue"]), spaceBefore=13, spaceAfter=5))
    base.add(ParagraphStyle("H2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=11.2, leading=14, textColor=colors.HexColor(PAL["ink"]), spaceBefore=9, spaceAfter=4))
    base.add(ParagraphStyle("Body", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.4, leading=12.2, textColor=colors.HexColor(PAL["ink"]), spaceAfter=5))
    base.add(ParagraphStyle("Abstract", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.2, leading=12.2, textColor=colors.HexColor(PAL["ink"]), leftIndent=12, rightIndent=12, borderColor=colors.HexColor(PAL["hair"]), borderWidth=0.8, borderPadding=8, backColor=colors.HexColor("#f8fafb"), spaceAfter=8))
    base.add(ParagraphStyle("Caption", parent=base["BodyText"], fontName="Helvetica-Oblique", fontSize=8.2, leading=10.2, textColor=colors.HexColor(PAL["muted"]), spaceBefore=2, spaceAfter=8))
    base.add(ParagraphStyle("BulletJournal", parent=base["BodyText"], fontName="Times-Roman", fontSize=9.2, leading=12, textColor=colors.HexColor(PAL["ink"])))
    base.add(ParagraphStyle("Kicker", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=colors.HexColor(PAL["blue"]), alignment=TA_CENTER, spaceAfter=5))
    base.add(ParagraphStyle("AppendixCell", parent=base["BodyText"], fontName="Helvetica", fontSize=6.7, leading=8.0, textColor=colors.HexColor(PAL["ink"])))
    base.add(ParagraphStyle("AppendixHead", parent=base["BodyText"], fontName="Helvetica-Bold", fontSize=6.8, leading=8.0, textColor=colors.white))
    return base


def p(text: str, style) -> Paragraph:
    text = text.replace("&", "&amp;")
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    return Paragraph(text, style)


def link_p(label: str, url: str, style) -> Paragraph:
    safe_label = label.replace("&", "&amp;")
    safe_url = url.replace("&", "&amp;")
    return Paragraph(f'<a href="{safe_url}" color="{PAL["blue"]}">{safe_label}</a>', style)


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def write_source_appendix(seed: list[dict[str, str]]) -> None:
    lines = [
        "# Appendix A. Corpus Source Index",
        "",
        "Each `LHA-###` identifier maps to one public source used in the exploratory corpus. "
        "The links support auditability and source review; they do not independently verify clinical claims.",
        "",
        "| Record ID | Source type | Platform | Date | Health domain | Valence | Inclusion status | URL |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in seed:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(row["id"]),
                    md_escape(row["source_type"]),
                    md_escape(row["platform"]),
                    md_escape(row["date_observed_or_published"]),
                    md_escape(row["health_domain"]),
                    md_escape(row["valence"]),
                    md_escape(row["inclusion_status"]),
                    md_escape(row["url"]),
                ]
            )
            + " |"
        )
    SOURCE_APPENDIX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def extract_body(md: str) -> tuple[str, str, str, list[str]]:
    lines = md.splitlines()
    title = TITLE
    subtitle = SUBTITLE
    author = AUTHOR
    body: list[str] = []
    title_seen = False
    subtitle_seen = False
    for line in lines:
        if line.startswith("# ") and not title_seen:
            title = line[2:].strip()
            title_seen = True
            continue
        if line.startswith("## ") and not subtitle_seen:
            subtitle = line[3:].strip()
            subtitle_seen = True
            continue
        if line.strip().startswith("**Birger"):
            author = line.strip().strip("*")
            continue
        body.append(line)
    return title, subtitle, author, body


def markdown_story(md: str, fig_paths: list[Path], s) -> list:
    title, subtitle, author, body_lines = extract_body(md)
    story: list = []
    story.append(p("EXPLORATORY QUALITATIVE EVIDENCE MAP", s["Kicker"]))
    story.append(p(title, s["TitleJournal"]))
    story.append(p(subtitle, s["SubtitleJournal"]))
    story.append(p(author, s["Author"]))

    fig_done = set()
    current: list[str] = []
    i = 0

    def flush():
        nonlocal current
        if current:
            story.append(p(" ".join(current), s["Body"]))
            current = []

    while i < len(body_lines):
        line = body_lines[i].rstrip()
        if not line:
            flush()
            i += 1
            continue
        if line.startswith("### Abstract"):
            flush()
            story.append(p("Abstract", s["H1"]))
            i += 1
            parts = []
            while i < len(body_lines) and not body_lines[i].startswith("### "):
                if body_lines[i].strip():
                    parts.append(body_lines[i].strip())
                i += 1
            story.append(p(" ".join(parts), s["Abstract"]))
            continue
        if line.startswith("### Keywords"):
            flush()
            story.append(p("Keywords", s["H1"]))
            i += 1
            if i < len(body_lines):
                story.append(p(body_lines[i].strip(), s["Body"]))
            i += 1
            continue
        if line.startswith("## "):
            flush()
            story.append(p(line[3:], s["H1"]))
            i += 1
            continue
        if line.startswith("### "):
            flush()
            heading = line[4:]
            story.append(p(heading, s["H2"]))
            if heading == "Corpus Characteristics" and "fig2" not in fig_done:
                story.append(RLImage(str(fig_paths[1]), width=6.55 * inch, height=4.09 * inch))
                story.append(p("Figure 2. Corpus architecture by source provenance, reported valence, and readiness for analysis.", s["Caption"]))
                fig_done.add("fig2")
            elif heading == "Theme 1: The LLM as Translator" and "fig1" not in fig_done:
                story.append(RLImage(str(fig_paths[0]), width=6.55 * inch, height=4.09 * inch))
                story.append(p("Figure 1. Anecdotes as early signal: how system gaps, LLM functions, patient actions, and boundary risks connect.", s["Caption"]))
                fig_done.add("fig1")
            elif heading == "Theme 6: The LLM as Risky Validator" and "fig3" not in fig_done:
                story.append(RLImage(str(fig_paths[2]), width=6.55 * inch, height=4.09 * inch))
                story.append(p("Figure 3. Taxonomy of LLM-mediated patient work from the pilot-coded subset.", s["Caption"]))
                fig_done.add("fig3")
            elif heading == "Design and Clinical Implications" and "fig4" not in fig_done:
                story.append(RLImage(str(fig_paths[3]), width=6.55 * inch, height=4.09 * inch))
                story.append(p("Figure 4. Boundary conditions for safer use.", s["Caption"]))
                fig_done.add("fig4")
            i += 1
            continue
        if re.match(r"^\d+\. ", line):
            flush()
            items = []
            while i < len(body_lines) and re.match(r"^\d+\. ", body_lines[i].strip()):
                items.append(ListItem(p(re.sub(r"^\d+\. ", "", body_lines[i].strip()), s["BulletJournal"])))
                i += 1
            story.append(ListFlowable(items, bulletType="1", leftIndent=18))
            continue
        if line.startswith("- "):
            flush()
            items = []
            while i < len(body_lines) and body_lines[i].strip().startswith("- "):
                items.append(ListItem(p(body_lines[i].strip()[2:], s["BulletJournal"])))
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=18))
            continue
        if line.startswith("# "):
            i += 1
            continue
        current.append(line)
        i += 1
    flush()
    return story


def add_helpful_tables(story: list, s, table_paths: list[Path]) -> None:
    story.append(PageBreak())
    story.append(p("Helpful Tables", s["H1"]))
    story.append(p("The tables below are designed as publication plates so the long qualitative labels remain readable rather than compressed into dense grid cells.", s["Body"]))
    for idx, table_path in enumerate(table_paths):
        if idx > 0:
            story.append(PageBreak())
        story.append(RLImage(str(table_path), width=6.55 * inch, height=4.09 * inch))
        story.append(p(f"{table_path.stem.replace('_', ' ').title()}.", s["Caption"]))


def add_visual_atlas(story: list, s, fig_paths: list[Path]) -> None:
    story.append(PageBreak())
    story.append(p("Visual Findings Atlas", s["H1"]))
    story.append(p("These additional figures summarize the corpus as an evidence landscape, a benefit-risk terrain, a research pipeline, a corpus-derived language map, and a narrative flow model. They are intended to make the qualitative findings inspectable without implying prevalence or clinical efficacy.", s["Body"]))
    captions = [
        "Figure 5. Evidence landscape: health domains by patient-described LLM function.",
        "Figure 6. Benefit-risk terrain: use cases positioned by clinical accountability and psychological or behavioral safeguarding needs.",
        "Figure 7. From anecdote to research agenda: how a traceable corpus generates hypotheses and design requirements.",
        "Figure 8. Language of patient work: corpus-derived terms placed by analytic role and boundary condition.",
        "Figure 9. Narrative grammar of LLM health use: how system gaps, model functions, patient actions, and safety boundaries connect.",
    ]
    for i, path in enumerate(fig_paths[4:]):
        if i > 0:
            story.append(PageBreak())
        story.append(RLImage(str(path), width=6.55 * inch, height=4.09 * inch))
        story.append(p(captions[i], s["Caption"]))


def add_source_appendix(story: list, s, seed: list[dict[str, str]]) -> None:
    story.append(PageBreak())
    story.append(p("Appendix A. Corpus Source Index", s["H1"]))
    story.append(
        p(
            "The source index maps each LHA corpus identifier to a public source URL. "
            "These links are included for auditability and source review; they do not verify diagnoses, outcomes, or causality.",
            s["Body"],
        )
    )
    story.append(
        p(
            "Comment-level and media-mediated entries should be rechecked before direct quotation in a submission version.",
            s["Caption"],
        )
    )

    header = [
        p("ID", s["AppendixHead"]),
        p("Source / platform", s["AppendixHead"]),
        p("Health domain", s["AppendixHead"]),
        p("Status", s["AppendixHead"]),
        p("URL", s["AppendixHead"]),
    ]
    rows = [header]
    for row in seed:
        source_platform = f'{row["source_type"]}<br/>{row["platform"]}<br/>{row["date_observed_or_published"]}'
        rows.append(
            [
                p(row["id"], s["AppendixCell"]),
                p(source_platform, s["AppendixCell"]),
                p(row["health_domain"], s["AppendixCell"]),
                p(row["inclusion_status"].replace("_", " "), s["AppendixCell"]),
                link_p("open source", row["url"], s["AppendixCell"]),
            ]
        )

    table = Table(
        rows,
        colWidths=[0.52 * inch, 1.86 * inch, 1.35 * inch, 1.02 * inch, 1.0 * inch],
        repeatRows=1,
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(PAL["blue"])),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor(PAL["hair"])),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafb")]),
            ]
        )
    )
    story.append(table)


def page_decor(canvas, doc):
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(colors.HexColor(PAL["hair"]))
    canvas.setLineWidth(0.6)
    canvas.line(doc.leftMargin, 0.54 * inch, width - doc.rightMargin, 0.54 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor(PAL["muted"]))
    canvas.drawString(doc.leftMargin, 0.34 * inch, f"{TITLE} · {AUTHOR}")
    canvas.drawRightString(width - doc.rightMargin, 0.34 * inch, str(doc.page))
    canvas.restoreState()


def build_pdf(fig_paths: list[Path], table_paths: list[Path], seed: list[dict[str, str]]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    s = styles()
    md = (ROOT / "manuscript_draft.md").read_text(encoding="utf-8")
    md = md.split("## References to Add")[0].strip()
    story = markdown_story(md, fig_paths, s)
    add_visual_atlas(story, s, fig_paths)
    add_helpful_tables(story, s, table_paths)
    add_source_appendix(story, s, seed)
    doc = SimpleDocTemplate(
        str(PDF),
        pagesize=letter,
        rightMargin=0.68 * inch,
        leftMargin=0.68 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.72 * inch,
        title=TITLE,
        author=AUTHOR,
    )
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)


def main() -> None:
    seed = read_csv("seed_corpus.csv")
    coded = read_csv("coded_corpus.csv")
    fig_paths = make_figures(seed, coded)
    table_paths = make_table_plates()
    write_source_appendix(seed)
    build_pdf(fig_paths, table_paths, seed)
    print(PDF)
    print(SOURCE_APPENDIX)
    for path in fig_paths:
        print(path)
    for path in table_paths:
        print(path)


if __name__ == "__main__":
    main()
