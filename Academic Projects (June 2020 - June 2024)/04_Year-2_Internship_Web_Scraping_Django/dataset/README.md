# Scraped internship data

These CSVs are outputs collected for the internship-site project. Filenames identify the source and category. A page number appears only where the source filename or scraper recorded one. `web_scrapping` follows the naming requested for the เด็กฝึกงาน.com data. The `jobbkk` grouping follows the original JobBKK filenames and the salary-style fields in those CSVs.

| Current file | Original file | Records | Role |
|---|---|---:|---|
| `web_scrapping_accounting_page1.csv` | `scrap_accounting_p1.csv` | 10 | Collected accounting listings |
| `web_scrapping_designer_page1.csv` | `scrap_designer_p1.csv` | 10 | Collected design listings |
| `web_scrapping_engineer_page1.csv` | `scrap_engineer_p1.csv` | 10 | Collected engineering listings |
| `web_scrapping_it_page1.csv` | `scrap_IT_p1.csv` | 10 | Collected IT listings |
| `web_scrapping_marketing_page1.csv` | `ver2-scrap_marketing_p1.csv` | 10 | Marketing listings with image field |
| `web_scrapping_marketing_page2.csv` | `scrap_marketing_p2.csv` | 10 | Collected marketing listings |
| `web_scrapping_other_page1.csv` | `script/website/internship/scrap_other1.csv` | 10 | Source of all 10 rows in the saved Django database |
| `web_scrapping_other_page2.csv` | `scrap_other_p2.csv` | 10 | Output of `script/web_scrapping/scrap_other_2.ipynb` |
| `web_scrapping_other_page3.csv` | `scrap_other_p3.csv` | 10 | Collected other listings |
| `jobbkk_accounting.csv` | `scrap_accounting2.csv` | 16 | Collected accounting listings |
| `jobbkk_engineer.csv` | `scrap_engineer2.csv` | 2 | Collected engineering listings |
| `jobbkk_it.csv` | `scrap_IT2.csv` | 15 | Collected IT listings |
| `jobbkk_marketing_page1.csv` | `ver2-scrap_marketting2_p1.csv` | 17 | Updated marketing scrape with image field |
| `jobbkk_other_page1.csv` | `jobbkk_other2_p1.csv` | 25 | Collected other listings |
| `jobbkk_other_page2.csv` | `jobbkk_other2_p2.csv` | 25 | Collected other listings |

`db.sqlite3` is the saved Django database. Only `web_scrapping_other_page1.csv` matches the ten records in its `internship_intern_other` table. The other CSVs are distinct scraping outputs retained for the broader project, rather than proven inputs to that final database table.

Two older portfolio copies were removed during cleanup. `scrap_other_p1.csv` was superseded for the final Django data by the matching `script/website/internship/scrap_other1.csv`. `scrap_marketting2_p1.csv` was replaced by the later `ver2-scrap_marketting2_p1.csv`, which includes an image field and overlaps substantially with the older version. The original university source folders still contain the old files.

