# Pipeline Instructions

Run the full automated job search pipeline for Mariam Imran. USA-ONLY roles.

## STEP 1 - Install and scan
Run: npm install
Run: npx playwright install chromium
Run: node scan.mjs
Collect all NEW job URLs. SKIP any role not in USA, Remote-US, or unspecified location.

## STEP 2 - Evaluate each role (USA only, score 3.5+)
For each new USA job URL:
1. Fetch the job posting
2. Read cv.md and config/profile.yml
3. Read modes/oferta.md for scoring framework
4. Score A-F. Skip anything below 3.5/5 or outside USA.
5. Save report to reports/{###}-{company-slug}-{date}.md
6. Write TSV to batch/tracker-additions/{###}-{company-slug}.tsv

## STEP 3 - Generate tailored CV as PDF for each 3.5+ role
For each passing role:
1. Read modes/pdf.md for instructions
2. Read cv.md and the job description
3. Extract 15-20 keywords from the JD
4. Rewrite Professional Summary with keywords injected
5. Build full HTML from templates/cv-template.html
6. Save HTML to /tmp/cv-mariam-imran-{company-slug}.html
7. Run: node generate-pdf.mjs /tmp/cv-mariam-imran-{company-slug}.html output/{###}-{company-slug}-cv.pdf --format=letter
8. Save markdown version to output/{###}-{company-slug}-cv.md

## STEP 4 - Pre-fill application answers
For each passing role:
1. Read modes/apply.md
2. Draft: cover letter (200 words), why this company (150 words), relevant experience summary
3. Save to output/{###}-{company-slug}-answers.md

## STEP 5 - Merge tracker
Run: node merge-tracker.mjs

## STEP 6 - Pipeline summary
Create reports/pipeline-summary-{date}.md with:
- Total scanned, evaluated, passed (3.5+), skipped
- Table: Company, Role, Score, Location, Apply URL
- Files generated (CVs as PDF, answer sheets)
- Next steps for Mariam

## STEP 7 - Commit and push
Run these commands:
git config user.email mariamimrancareers@gmail.com
git config user.name "Mariam Imran"
git add reports/ output/ data/applications.md batch/tracker-additions/
git commit -m "Pipeline {date}: USA PM/PMM roles evaluated"
git push origin main

## Candidate Profile
- Name: Mariam Imran, Chicago IL
- Target: PM, PMM, Associate PM, Intern roles - USA ONLY
- Experience: 7+ years GTM + AI products (Coca-Cola EMEA, Mingora)
- Education: MS DePaul Marketing Analysis + AI (STEM OPT March 2027)
- Skills: Python, SQL, multi-agent AI, Power BI
- Salary: $60K-110K full-time / $18-30/hr internship
- RULE: USA and Remote-US roles only. Never submit applications.
