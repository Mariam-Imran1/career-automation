# Obsidian Updater Instructions

Update Mariam Imran's Obsidian vault with today's job search activity.

The Obsidian repo is checked out at ../Obsidian/ (cloned alongside this repo).
The vault files are inside ../Obsidian/My Files/

## 1. Update Job Search Tracker
Read data/applications.md from this repo.
Rewrite ../Obsidian/My\ Files/Job\ Search\ Tracker.md with all current applications as a clean markdown table.

## 2. Update Claude Conversation Log
Read the latest reports/pipeline-summary-*.md from this repo.
Append to ../Obsidian/My\ Files/Claude\ Conversation\ Log.md:
- Today date and time
- Pipeline summary: how many roles scanned, matched, docs generated
- Top matches today: company, role, score, URL

## 3. Create Company Research Notes
For each role scoring 3.5+ in today's pipeline reports:
- Create or update ../Obsidian/My\ Files/Companies/{Company-Name}.md
- Include: company name, role, score, why it fits Mariam, apply URL, current status
- If file exists, update status only, preserve existing notes

## 4. Commit and push Obsidian repo
Run:
cd ../Obsidian
git config user.email mariamimrancareers@gmail.com
git config user.name "Mariam Imran"
git add "My Files/"
git commit -m "Daily job search update {date}" || echo "Nothing to commit"
git push origin main

Report what was created and updated.
