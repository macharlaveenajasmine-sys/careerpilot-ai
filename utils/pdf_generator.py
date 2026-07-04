from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report):

    doc = SimpleDocTemplate("Career_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>CareerPilot AI Report</b>", styles["Title"]))

    story.append(Paragraph("<br/><br/>", styles["BodyText"]))

    for title, content in report.items():

        story.append(
            Paragraph(f"<b>{title.upper()}</b>", styles["Heading2"])
        )

        story.append(
            Paragraph(
                str(content).replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

        story.append(
            Paragraph("<br/>", styles["BodyText"])
        )

    doc.build(story)

    return "Career_Report.pdf"