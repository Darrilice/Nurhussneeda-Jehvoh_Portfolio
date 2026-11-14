# Internship listings with web scraping and Django

**Year 2 · Web Technology · Python, scraping, Django, HTML/CSS**

## Primary evidence and code status

`script/website/` is the recovered final Django application. `script/web_scrapping/scrap_other_2.ipynb` is an original scraper notebook. The saved database and three 2022 screenshots show the site; some source names and IDs were anonymised in this portfolio. Separate Wix snapshots were not used by the Django templates.

## Dataset and workflow

`dataset/` holds **15 scraping CSVs** from เด็กฝึกงาน.com and JobBKK, plus the saved SQLite database. [`dataset/README.md`](dataset/README.md) maps current filenames to their originals. Only `web_scrapping_other_page1.csv` matches the **10 listings** in the final database table; the other CSVs are collected outputs, not verified database inputs.

## End-to-end workflow

Scrape internship listings → save CSVs → store ten records in SQLite → render Home, All Internship and About Us with Django. The recovered loader points to a missing CSV, so the original import step cannot be rerun as-is.

## Results and outcome

The original Django site displays **10 internship listings**. [Open a clickable copy](result/original_site_preview/index.html) rendered from its templates and database; it retains the original layout. External CSS, fonts and the background image depend on their original URLs.

## Saved historical results

`result/` contains three original 2022 screenshots and the clickable HTML export. The HTML is a later rendering of the original site, not an original 2022 screenshot.

## Files

[`dataset/`](dataset/) · [`script/website/`](script/website/) · [`script/web_scrapping/`](script/web_scrapping/) · [`result/`](result/) · [`script/README.md`](script/README.md). No report was recovered.
