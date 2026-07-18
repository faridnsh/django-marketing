#!/usr/bin/env bash
set -euo pipefail

repo_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
audience_dir="$repo_dir/research/audiences"

required_headings=(
  "Audience definition and boundaries"
  "Important subsegments"
  "Primary job to be done"
  "Additional jobs to be done"
  "Functional, emotional, and social dimensions"
  "Triggering situations"
  "Desired outcomes"
  "Current behaviour or status quo"
  "Pushes"
  "Pulls"
  "Anxieties"
  "Habits and inertia"
  "Decision criteria"
  "Main concerns"
  "Objections and perceived risks"
  "Information needed to make progress"
  "Trusted content formats"
  "Discovery, evaluation, validation, and engagement channels"
  "Decision-makers and influencers"
  "Appropriate next actions for Django to encourage"
  "Overlaps with other audiences"
  "Possible segmentation problems"
  "Existing-analysis claim audit"
  "Evidence table"
  "Unanswered research questions"
)

expected_files=(
  "01-first-time-programmers.md"
  "02-python-developers-new-to-web.md"
  "03-experienced-backend-engineers.md"
  "04-full-stack-developers.md"
  "05-technical-leads-software-architects.md"
  "06-ctos-engineering-managers.md"
  "07-startups-technical-decision-makers.md"
  "08-large-organizations-stakeholders.md"
  "09-industry-contexts-government-education-media-healthcare-finance.md"
  "10-agencies-consultancies.md"
  "11-django-python-package-maintainers.md"
  "12-individual-educators-instructors-bootcamp-teachers.md"
  "13-existing-django-users.md"
  "14-former-django-users.md"
  "15-prospective-existing-django-contributors.md"
  "16-donors-sponsors-corporate-members.md"
  "17-educational-institutions-training-curriculum-decision-makers.md"
)

failed=0
for name in "${expected_files[@]}"; do
  file="$audience_dir/$name"
  if [[ ! -s "$file" ]]; then
    echo "MISSING $name"
    failed=1
    continue
  fi

  for heading in "${required_headings[@]}"; do
    if ! rg -q "^## ${heading}$" "$file"; then
      echo "MISSING HEADING $name: $heading"
      failed=1
    fi
  done

  if ! rg -q '^\| *Finding *\| *Source .*\| *Evidence type *\| *Direct evidence or inference *\| *Confidence *\| *Research notes *\|' "$file"; then
    echo "BAD EVIDENCE HEADER $name"
    failed=1
  fi

  url_count=$(rg -o 'https?://[^ )|]+' "$file" | sort -u | wc -l | tr -d ' ')
  if (( url_count < 6 )); then
    echo "LOW URL COUNT $name: $url_count"
    failed=1
  fi

  echo "OK $name ($(wc -w < "$file" | tr -d ' ') words; $url_count unique URLs)"
done

exit "$failed"
