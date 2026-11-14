# Original project scripts

`website/` contains the original Django application copied from `D:\Silpskorn University (2020 - 2024)\2 term 2\Web Technology\project\webtech2 final\webtech2\demo\project`. Its Python files remain unchanged. The About Us HTML now uses anonymous placeholders, and the three original photo panels showing people were removed from the base HTML. `db.sqlite3` is the original database with 10 saved listings. The included Bootstrap files are the copies referenced by the original template.

The original home page is `website/templates/base.html`; the listings and About Us pages are `website/internship/templates/internship/main.html` and `user_info.html`. The three retained JPGs in `../result/` are original 2022 browser screenshots of this Django site. Screenshots showing contributor identities or people were removed. The earlier portfolio preview and redesigned templates were removed because they did not represent the submitted work.

`web_scrapping/scrap_other_2.ipynb` is the unmodified original scraping notebook. Its original output path is `scrap_other_p2.csv`; the corresponding CSV is retained in `../dataset/` under a descriptive portfolio filename.

The original `website/scripts/load_internship.py` points to `internship/scrap_other3.csv`, a file absent from the recovered final project. The saved database already contains 10 records, so running that loader is unnecessary for viewing the original site.

The separate `wix/html/` directory in the university source contains Wix-generated page snapshots. The Django templates do not extend or import those pages. The Django site uses W3.CSS and Bootstrap instead.

To run the original Django site, install its dependencies (`django` and `django-extensions`), then run `python manage.py runserver` from `website/`. Open `http://127.0.0.1:8000/` for Home, `/internship/` for All Internship, and `/internship/user_info/` for About Us. The original home template references external CSS and a cityscape image URL, so some styling or the background may depend on those sites remaining available.

