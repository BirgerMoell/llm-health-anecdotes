from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image as RLImage,
    KeepTogether,
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


PALETTE = {
    "ink": "#1f2933",
    "muted": "#5f6f7a",
    "light": "#f4f6f8",
    "line": "#d7dee4",
    "blue": "#2f6f9f",
    "teal": "#2a9d8f",
    "green": "#6a994e",
    "gold": "#d19a2a",
    "coral": "#d65f5f",
    "plum": "#7c5c8f",
    "paper": "#fffdf8",
}


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            pass
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        test = " ".join(current + [word])
        if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def rounded_box(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=24, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def read_seed() -> list[dict[str, str]]:
    with (ROOT / "seed_corpus.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_coded() -> list[dict[str, str]]:
    with (ROOT / "coded_corpus.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def figure_1_ecology(path: Path) -> None:
    w, h = 1800, 1120
    img = Image.new("RGB", (w, h), hex_to_rgb(PALETTE["paper"]))
    d = ImageDraw.Draw(img)
    title_f = font(54, True)
    sub_f = font(28)
    head_f = font(28, True)
    body_f = font(24)
    small_f = font(21)

    d.text((90, 70), "Figure 1. Where LLMs Enter Patient Work", fill=hex_to_rgb(PALETTE["ink"]), font=title_f)
    d.text(
        (92, 135),
        "Public anecdotes place chatbots between system gaps, patient sensemaking, and clinical action.",
        fill=hex_to_rgb(PALETTE["muted"]),
        font=sub_f,
    )

    columns = [
        ("Healthcare gaps", ["Rushed visits", "Portal jargon", "Delayed referrals", "Specialist silos", "Therapy access", "Nighttime uncertainty"], PALETTE["gold"]),
        ("LLM roles", ["Translator", "Pattern finder", "Appointment amplifier", "Always-on companion", "Behavior-change scaffold", "Risky validator"], PALETTE["blue"]),
        ("Patient actions", ["Seek urgent care", "Ask better questions", "Request tests", "Track symptoms", "Change routines", "Upload records"], PALETTE["teal"]),
        ("Failure modes", ["Wrong triage", "Unsafe advice", "Reassurance loops", "Psychosis amplification", "Privacy exposure", "System bottlenecks"], PALETTE["coral"]),
    ]
    x0s = [90, 525, 960, 1395]
    top = 240
    card_w, card_h = 320, 650
    for i, (head, items, color) in enumerate(columns):
        x = x0s[i]
        rounded_box(d, (x, top, x + card_w, top + card_h), "#ffffff", PALETTE["line"], 26, 3)
        d.rounded_rectangle((x, top, x + card_w, top + 86), radius=26, fill=hex_to_rgb(color))
        d.text((x + 24, top + 25), head, fill="white", font=head_f)
        y = top + 125
        for item in items:
            d.ellipse((x + 25, y + 8, x + 39, y + 22), fill=hex_to_rgb(color))
            for line in wrap_text(d, item, body_f, card_w - 82):
                d.text((x + 55, y), line, fill=hex_to_rgb(PALETTE["ink"]), font=body_f)
                y += 31
            y += 22
        if i < 3:
            ax = x + card_w + 24
            ay = top + card_h // 2
            d.line((ax, ay, ax + 95, ay), fill=hex_to_rgb(PALETTE["muted"]), width=7)
            d.polygon([(ax + 95, ay), (ax + 72, ay - 17), (ax + 72, ay + 17)], fill=hex_to_rgb(PALETTE["muted"]))

    d.text(
        (100, 955),
        "Interpretation: the corpus is less a story of patients replacing clinicians than of patients doing unpaid interpretive work around care.",
        fill=hex_to_rgb(PALETTE["ink"]),
        font=small_f,
    )
    img.save(path, quality=95)


def figure_2_corpus(seed: list[dict[str, str]], path: Path) -> None:
    w, h = 1800, 1120
    img = Image.new("RGB", (w, h), hex_to_rgb(PALETTE["paper"]))
    d = ImageDraw.Draw(img)
    title_f = font(54, True)
    sub_f = font(27)
    label_f = font(26, True)
    small_f = font(22)
    tiny_f = font(19)

    d.text((90, 70), "Figure 2. Corpus Composition", fill=hex_to_rgb(PALETTE["ink"]), font=title_f)
    d.text((92, 135), "A 100-record seed corpus, stratified by source and reported valence.", fill=hex_to_rgb(PALETTE["muted"]), font=sub_f)

    source_counts = Counter()
    for r in seed:
        st = r["source_type"]
        if "Reddit" in r["platform"] or st.startswith("public"):
            group = "Reddit / public posts"
        elif st == "patient forum":
            group = "Patient forums"
        elif "news" in st:
            group = "News-mediated"
        elif "essay" in st or "column" in st:
            group = "Personal essays"
        else:
            group = "Other"
        source_counts[group] += 1

    source_order = ["Reddit / public posts", "Patient forums", "News-mediated", "Personal essays", "Other"]
    colors_order = [PALETTE["blue"], PALETTE["teal"], PALETTE["gold"], PALETTE["plum"], PALETTE["muted"]]
    x, y = 100, 265
    d.text((x, y - 60), "Source mix", fill=hex_to_rgb(PALETTE["ink"]), font=label_f)
    max_v = max(source_counts.values())
    for i, name in enumerate(source_order):
        count = source_counts[name]
        bw = int(720 * count / max_v)
        yy = y + i * 80
        d.text((x, yy + 5), name, fill=hex_to_rgb(PALETTE["ink"]), font=small_f)
        d.rounded_rectangle((x + 260, yy, x + 260 + 740, yy + 40), radius=20, fill=hex_to_rgb("#e7ecef"))
        d.rounded_rectangle((x + 260, yy, x + 260 + bw, yy + 40), radius=20, fill=hex_to_rgb(colors_order[i]))
        d.text((x + 1025, yy + 4), str(count), fill=hex_to_rgb(PALETTE["ink"]), font=small_f)

    valence_counts = Counter()
    for r in seed:
        v = r["valence"]
        if v == "helpful":
            group = "Helpful"
        elif v == "unhelpful_or_insufficient":
            group = "No resolution"
        elif "harm" in v or "unhelpful" in v:
            group = "Harm / unhelpful"
        elif "mixed" in v or "risk" in v:
            group = "Mixed / uncertain"
        else:
            group = "No resolution"
        valence_counts[group] += 1

    cx, cy, radius = 1260, 570, 265
    d.text((1040, 205), "Reported valence", fill=hex_to_rgb(PALETTE["ink"]), font=label_f)
    total = sum(valence_counts.values())
    start = -90
    valence_order = [
        ("Helpful", PALETTE["green"]),
        ("Harm / unhelpful", PALETTE["coral"]),
        ("Mixed / uncertain", PALETTE["gold"]),
        ("No resolution", PALETTE["muted"]),
    ]
    for name, color in valence_order:
        angle = 360 * valence_counts[name] / total
        d.pieslice((cx - radius, cy - radius, cx + radius, cy + radius), start, start + angle, fill=hex_to_rgb(color))
        start += angle
    d.ellipse((cx - 145, cy - 145, cx + 145, cy + 145), fill=hex_to_rgb(PALETTE["paper"]))
    d.text((cx - 54, cy - 54), "100", fill=hex_to_rgb(PALETTE["ink"]), font=font(68, True))
    d.text((cx - 76, cy + 22), "records", fill=hex_to_rgb(PALETTE["muted"]), font=small_f)

    ly = 875
    for i, (name, color) in enumerate(valence_order):
        xx = 1010 + (i % 2) * 350
        yy = ly + (i // 2) * 58
        d.rounded_rectangle((xx, yy, xx + 34, yy + 34), radius=8, fill=hex_to_rgb(color))
        d.text((xx + 48, yy + 1), f"{name}: {valence_counts[name]}", fill=hex_to_rgb(PALETTE["ink"]), font=tiny_f)

    d.text((100, 1010), "Note: valence reflects the poster's reported experience, not verified clinical effect.", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f)
    img.save(path, quality=95)


def figure_3_taxonomy(coded: list[dict[str, str]], path: Path) -> None:
    w, h = 1800, 1120
    img = Image.new("RGB", (w, h), hex_to_rgb(PALETTE["paper"]))
    d = ImageDraw.Draw(img)
    title_f = font(54, True)
    sub_f = font(27)
    head_f = font(26, True)
    body_f = font(22)
    tiny_f = font(18)

    d.text((90, 70), "Figure 3. A Taxonomy of Patient-Described LLM Use", fill=hex_to_rgb(PALETTE["ink"]), font=title_f)
    d.text((92, 135), "Pilot coding organizes anecdotes by the kind of patient work the model performs.", fill=hex_to_rgb(PALETTE["muted"]), font=sub_f)

    themes = [
        ("Translator", "Explains labs, reports, jargon, and portal results.", ["lab_translation", "medical_translation", "report_interpretation"], PALETTE["blue"]),
        ("Pattern finder", "Synthesizes long histories, records, symptoms, triggers, and tests.", ["record_synthesis", "differential_generation"], PALETTE["teal"]),
        ("Appointment amplifier", "Turns confusion into questions, summaries, and escalation decisions.", ["urgent_triage", "care_escalation"], PALETTE["green"]),
        ("Companion", "Provides disclosure, grounding, reflection, addiction support, and late-night presence.", ["emotional_support", "addiction_support", "disclosure", "creative_coping"], PALETTE["plum"]),
        ("Behavior scaffold", "Supports tracking, routines, meal logging, rehabilitation, and self-management.", ["diet_weight_tracking", "symptom_tracking"], PALETTE["gold"]),
        ("Risky validator", "May reinforce reassurance loops, psychosis, unsafe certainty, or medication mistakes.", ["ai_as_therapy", "reassurance_seeking", "medication_timing"], PALETTE["coral"]),
    ]
    use_counts = Counter(r["primary_use_case"] for r in coded)
    max_count = max(sum(use_counts[u] for u in uses) for _, _, uses, _ in themes)

    for i, (name, desc, uses, color) in enumerate(themes):
        col = i % 3
        row = i // 3
        x = 90 + col * 560
        y = 255 + row * 385
        rounded_box(d, (x, y, x + 500, y + 305), "#ffffff", PALETTE["line"], 28, 3)
        d.rounded_rectangle((x, y, x + 500, y + 68), radius=28, fill=hex_to_rgb(color))
        d.text((x + 26, y + 17), name, fill="white", font=head_f)
        yy = y + 95
        for line in wrap_text(d, desc, body_f, 430):
            d.text((x + 26, yy), line, fill=hex_to_rgb(PALETTE["ink"]), font=body_f)
            yy += 29
        count = sum(use_counts[u] for u in uses)
        d.text((x + 26, y + 210), f"Pilot-coded records: {count}", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f)
        d.rounded_rectangle((x + 26, y + 244, x + 454, y + 272), radius=14, fill=hex_to_rgb("#e7ecef"))
        d.rounded_rectangle((x + 26, y + 244, x + 26 + int(428 * count / max_count), y + 272), radius=14, fill=hex_to_rgb(color))

    d.text((100, 1030), "Counts come from a 35-record pilot-coded subset and are used for theme development, not prevalence.", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f)
    img.save(path, quality=95)


def figure_4_boundary(path: Path) -> None:
    w, h = 1800, 1120
    img = Image.new("RGB", (w, h), hex_to_rgb(PALETTE["paper"]))
    d = ImageDraw.Draw(img)
    title_f = font(54, True)
    sub_f = font(27)
    head_f = font(29, True)
    body_f = font(22)
    tiny_f = font(18)

    d.text((90, 70), "Figure 4. Boundary Conditions for Safer Use", fill=hex_to_rgb(PALETTE["ink"]), font=title_f)
    d.text((92, 135), "The corpus suggests LLMs are most useful for sensemaking and riskiest when accountability is required.", fill=hex_to_rgb(PALETTE["muted"]), font=sub_f)

    x0, y0, x1, y1 = 190, 265, 1610, 920
    d.rounded_rectangle((x0, y0, x1, y1), radius=26, fill="#ffffff", outline=hex_to_rgb(PALETTE["line"]), width=3)
    midx, midy = (x0 + x1) // 2, (y0 + y1) // 2
    d.line((midx, y0, midx, y1), fill=hex_to_rgb(PALETTE["line"]), width=4)
    d.line((x0, midy, x1, midy), fill=hex_to_rgb(PALETTE["line"]), width=4)
    d.text((x0 + 20, y0 - 50), "Lower clinical stakes", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f)
    d.text((x1 - 220, y0 - 50), "Higher clinical stakes", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f)
    d.text((x0 - 105, y1 - 20), "More\nsupportive", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f, align="center")
    d.text((x0 - 105, y0 + 20), "More\ndecisive", fill=hex_to_rgb(PALETTE["muted"]), font=tiny_f, align="center")

    quadrants = [
        (x0 + 40, y0 + 40, "Useful translator", ["Explain jargon", "Summarize reports", "Prepare questions"], PALETTE["blue"]),
        (midx + 40, y0 + 40, "Clinical judgment required", ["Urgency", "Medication changes", "Treatment timing"], PALETTE["coral"]),
        (x0 + 40, midy + 40, "Supportive scaffold", ["Meal logging", "Grounding", "Recovery routines"], PALETTE["green"]),
        (midx + 40, midy + 40, "Safeguarding required", ["OCD reassurance", "Psychosis/mania", "Suicidality"], PALETTE["gold"]),
    ]
    for x, y, head, items, color in quadrants:
        d.text((x, y), head, fill=hex_to_rgb(color), font=head_f)
        yy = y + 58
        for item in items:
            d.ellipse((x, yy + 9, x + 13, yy + 22), fill=hex_to_rgb(color))
            d.text((x + 28, yy), item, fill=hex_to_rgb(PALETTE["ink"]), font=body_f)
            yy += 42

    d.line((300, 980, 1500, 980), fill=hex_to_rgb(PALETTE["ink"]), width=3)
    d.text((470, 1008), "Safer design shifts from answers toward explanation, questions, uncertainty, and escalation.", fill=hex_to_rgb(PALETTE["ink"]), font=body_f)
    img.save(path, quality=95)


def make_figures(seed, coded) -> list[Path]:
    FIG.mkdir(parents=True, exist_ok=True)
    paths = [
        FIG / "figure_1_ecology.png",
        FIG / "figure_2_corpus.png",
        FIG / "figure_3_taxonomy.png",
        FIG / "figure_4_boundary.png",
    ]
    figure_1_ecology(paths[0])
    figure_2_corpus(seed, paths[1])
    figure_3_taxonomy(coded, paths[2])
    figure_4_boundary(paths[3])
    return paths


def clean_inline(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = text.replace("&", "&amp;").replace("<font name='Courier'>", "<font name='Courier'>")
    return text


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle("TitleBig", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=28, leading=34, textColor=colors.HexColor(PALETTE["ink"]), alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle("Subtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=15, leading=19, textColor=colors.HexColor(PALETTE["muted"]), alignment=TA_CENTER, spaceAfter=22))
    styles.add(ParagraphStyle("Heading1X", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=colors.HexColor(PALETTE["blue"]), spaceBefore=14, spaceAfter=7))
    styles.add(ParagraphStyle("Heading2X", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=colors.HexColor(PALETTE["ink"]), spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle("BodyX", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.6, leading=13.2, textColor=colors.HexColor(PALETTE["ink"]), spaceAfter=6))
    styles.add(ParagraphStyle("AbstractX", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.4, leading=12.7, textColor=colors.HexColor(PALETTE["ink"]), leftIndent=16, rightIndent=16, backColor=colors.HexColor("#f7f9fa"), borderColor=colors.HexColor(PALETTE["line"]), borderWidth=0.8, borderPadding=9, spaceAfter=10))
    styles.add(ParagraphStyle("CaptionX", parent=styles["BodyText"], fontName="Helvetica-Oblique", fontSize=8.5, leading=11, textColor=colors.HexColor(PALETTE["muted"]), spaceBefore=3, spaceAfter=10))
    styles.add(ParagraphStyle("BulletX", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12, textColor=colors.HexColor(PALETTE["ink"])))
    return styles


def para(text: str, style) -> Paragraph:
    return Paragraph(text.replace("&", "&amp;"), style)


def markdown_to_flowables(md: str, styles, fig_paths: list[Path]):
    story = []
    lines = md.splitlines()
    i = 0
    current_para: list[str] = []
    fig_inserted = set()
    title_used = False
    subtitle_used = False

    def flush():
        nonlocal current_para
        if current_para:
            story.append(para(" ".join(current_para), styles["BodyX"]))
            current_para = []

    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            flush()
            i += 1
            continue
        if line.startswith("# "):
            flush()
            if not title_used:
                story.append(para(line[2:], styles["TitleBig"]))
                title_used = True
            i += 1
            continue
        if line.startswith("## "):
            flush()
            if not subtitle_used:
                story.append(para(line[3:], styles["Subtitle"]))
                subtitle_used = True
            else:
                story.append(para(line[3:], styles["Heading1X"]))
            i += 1
            continue
        if line.startswith("### Abstract"):
            flush()
            story.append(para("Abstract", styles["Heading1X"]))
            i += 1
            abs_parts = []
            while i < len(lines) and not lines[i].startswith("### "):
                if lines[i].strip():
                    abs_parts.append(lines[i].strip())
                i += 1
            story.append(para(" ".join(abs_parts), styles["AbstractX"]))
            continue
        if line.startswith("### Keywords"):
            flush()
            story.append(para("Keywords", styles["Heading1X"]))
            i += 1
            if i < len(lines):
                story.append(para(lines[i].strip(), styles["BodyX"]))
            i += 1
            continue
        if line.startswith("### "):
            flush()
            heading = line[4:]
            story.append(para(heading, styles["Heading2X"]))
            if heading == "Corpus Characteristics" and 0 not in fig_inserted:
                story.append(RLImage(str(fig_paths[1]), width=6.5 * inch, height=4.04 * inch))
                story.append(para("Figure 2. Corpus composition by source and reported valence.", styles["CaptionX"]))
                fig_inserted.add(0)
            if heading == "Theme 1: The LLM as Translator" and 1 not in fig_inserted:
                story.append(RLImage(str(fig_paths[0]), width=6.5 * inch, height=4.04 * inch))
                story.append(para("Figure 1. Where LLMs enter patient work.", styles["CaptionX"]))
                fig_inserted.add(1)
            if heading == "Theme 6: The LLM as Risky Validator" and 2 not in fig_inserted:
                story.append(RLImage(str(fig_paths[2]), width=6.5 * inch, height=4.04 * inch))
                story.append(para("Figure 3. Taxonomy of patient-described LLM use.", styles["CaptionX"]))
                fig_inserted.add(2)
            if heading == "Design and Clinical Implications" and 3 not in fig_inserted:
                story.append(RLImage(str(fig_paths[3]), width=6.5 * inch, height=4.04 * inch))
                story.append(para("Figure 4. Boundary conditions for safer use.", styles["CaptionX"]))
                fig_inserted.add(3)
            i += 1
            continue
        if re.match(r"^\d+\. ", line):
            flush()
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(ListItem(para(re.sub(r"^\d+\. ", "", lines[i].strip()), styles["BulletX"])))
                i += 1
            story.append(ListFlowable(items, bulletType="1", leftIndent=18))
            continue
        if line.startswith("- "):
            flush()
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(ListItem(para(lines[i].strip()[2:], styles["BulletX"])))
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", leftIndent=18))
            continue
        current_para.append(line)
        i += 1
    flush()
    return story


def add_tables(story, styles):
    story.append(PageBreak())
    story.append(para("Key Tables", styles["Heading1X"]))
    table1 = [
        ["Characteristic", "Count"],
        ["Total seed records", "100"],
        ["Helpful or perceived-helpful", "78"],
        ["Harmful or unhelpful", "13"],
        ["Mixed, uncertain, or helpful-with-risk", "8"],
        ["No resolution / system-insufficient", "1"],
        ["Reddit posts or comments", "67"],
        ["Patient forum records", "12"],
        ["News reports", "10"],
    ]
    t = Table(table1, colWidths=[4.7 * inch, 1.0 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(PALETTE["blue"])),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 12),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor(PALETTE["line"])),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#fbfcfd")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#fbfcfd"), colors.white]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("RIGHTPADDING", (1, 1), (1, -1), 8),
        ("ALIGN", (1, 1), (1, -1), "RIGHT"),
    ]))
    story.append(t)
    story.append(Spacer(1, 14))
    story.append(para("Note: Counts describe the exploratory seed corpus, not prevalence among all LLM health users.", styles["CaptionX"]))


def page_decor(canvas, doc):
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(colors.HexColor(PALETTE["line"]))
    canvas.line(doc.leftMargin, 0.55 * inch, width - doc.rightMargin, 0.55 * inch)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor(PALETTE["muted"]))
    canvas.drawString(doc.leftMargin, 0.34 * inch, "The Plural of Anecdote Is Data")
    canvas.drawRightString(width - doc.rightMargin, 0.34 * inch, str(doc.page))
    canvas.restoreState()


def build_pdf(fig_paths):
    OUT.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    md = (ROOT / "manuscript_draft.md").read_text(encoding="utf-8")
    # Keep the PDF focused; references checklist remains separate.
    md = md.split("## References to Add")[0].strip()
    story = markdown_to_flowables(md, styles, fig_paths)
    add_tables(story, styles)
    doc = SimpleDocTemplate(
        str(PDF),
        pagesize=letter,
        rightMargin=0.72 * inch,
        leftMargin=0.72 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.72 * inch,
        title="The Plural of Anecdote Is Data",
        author="Draft manuscript",
    )
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)


def main():
    seed = read_seed()
    coded = read_coded()
    fig_paths = make_figures(seed, coded)
    build_pdf(fig_paths)
    print(PDF)
    for p in fig_paths:
        print(p)


if __name__ == "__main__":
    main()
