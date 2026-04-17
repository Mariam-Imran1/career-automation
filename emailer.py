#!/usr/bin/env python3
import smtplib, os, glob
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

EMAIL = "mariamimrancareers@gmail.com"
PASSWORD = "kcxd kzgb tvma cljv"
today = date.today().strftime("%Y-%m-%d")
today_pretty = date.today().strftime("%B %d, %Y")

def md_section(title, content, color):
    lines = []
    for line in content.split("\n"):
        if line.startswith("## "):
            lines.append(f'<h3 style="color:{color};margin:14px 0 6px">{line[3:]}</h3>')
        elif line.startswith("# "):
            lines.append(f'<h2 style="color:{color}">{line[2:]}</h2>')
        elif line.startswith("| "):
            lines.append(f'<code style="font-size:11px;display:block">{line}</code>')
        elif line.startswith("- ") or line.startswith("* "):
            lines.append(f"<li>{line[2:]}</li>")
        elif line.strip() == "---":
            lines.append('<hr style="border:none;border-top:1px solid #ddd;margin:10px 0"/>')
        elif line.strip():
            lines.append(f'<p style="margin:3px 0;line-height:1.5">{line}</p>')
    return f"""
<div style="background:#f9f9f9;padding:16px;border-radius:8px;margin:14px 0;border-left:4px solid {color}">
  <h3 style="color:{color};margin:0 0 12px 0">{title}</h3>
  {"".join(lines)}
</div>"""

# Collect files
summaries = sorted(glob.glob("reports/pipeline-summary-*.md"))
summary = open(summaries[-1]).read() if summaries else "No pipeline summary found. The scan may still be running."
cvs = sorted(glob.glob("output/*-cv.md"))
answers = sorted(glob.glob("output/*-answers.md"))
doc_count = len(cvs) + len(answers)

# Build HTML
body = f"""<html><body style="font-family:Arial,sans-serif;max-width:700px;margin:auto;padding:24px;color:#333">
<div style="background:#1a1a2e;color:white;padding:22px;border-radius:10px;margin-bottom:20px">
  <h1 style="margin:0;font-size:24px">Daily Job Pipeline</h1>
  <p style="opacity:.8;margin:6px 0 0">{today_pretty} &nbsp;·&nbsp; {len(cvs)} tailored CVs &nbsp;·&nbsp; {len(answers)} answer sheets ready</p>
</div>
<p style="font-size:15px">Everything is ready below. Tailored CVs and pre-filled answers are embedded in this email and attached as files. <strong>Your only job: open each job link, paste the answers, click Submit.</strong></p>
"""

body += md_section("📊 Pipeline Summary", summary, "#1a1a2e")

for cv in cvs:
    name = os.path.basename(cv).replace("-cv.md", "").replace("-", " ").title()
    body += md_section(f"📄 Tailored Resume — {name}", open(cv).read(), "#2d6a4f")

for ans in answers:
    name = os.path.basename(ans).replace("-answers.md", "").replace("-", " ").title()
    body += md_section(f"✍️ Application Answers — {name}", open(ans).read(), "#1565c0")

body += """
<div style="background:#fff8e1;padding:16px;border-radius:8px;margin:20px 0;border-left:4px solid #f9a825">
  <strong>⚡ Next steps:</strong> Each section above has a job URL. Open it, copy-paste the answers, attach the tailored resume, click Submit. Takes ~2 minutes per application.
</div>
<p style="font-size:12px;color:#aaa;margin-top:24px">
  career-ops · runs daily at 9am Chicago time<br/>
  All files: <a href="https://github.com/Mariam-Imran1/career-automation/tree/main/output">github.com/Mariam-Imran1/career-automation/output</a>
</p>
</body></html>"""

plain = f"Daily Job Pipeline — {today}\n\n{summary}\n\n"
for f in cvs + answers:
    plain += f"\n\n{'='*50}\n{os.path.basename(f)}\n{'='*50}\n" + open(f).read()

# Build message
msg = MIMEMultipart("mixed")
msg["Subject"] = f"[career-ops] {doc_count} docs ready — {today}"
msg["From"] = EMAIL
msg["To"] = EMAIL

alt = MIMEMultipart("alternative")
alt.attach(MIMEText(plain, "plain"))
alt.attach(MIMEText(body, "html"))
msg.attach(alt)

# Attach all docs as files
for f in cvs + answers:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(f, "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{os.path.basename(f)}"')
    msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(EMAIL, PASSWORD)
    s.sendmail(EMAIL, EMAIL, msg.as_string())

print(f"Email sent to {EMAIL}: {doc_count} docs ({len(cvs)} CVs, {len(answers)} answer sheets)")
