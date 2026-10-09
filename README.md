# DSL homepage

Static site published with GitHub Pages: https://dankimuq.github.io/

## Where to edit

| What | File |
|---|---|
| Home | `index.html` |
| Dan Kim | `dan.html` |
| People | `members.html` |
| Publications | `publications.html` |
| Professional service | `services.html` |
| Join us | `pros-students.html` |
| News archive | `news.html` |
| Research overview | `research-summary.html` |
| Research projects | `<project>.html` and the `<project>/` folder (papers, codes, ...) |
| Menu, footer, search box | `assets/site.js` |
| Colours and layout | `assets/style.css` |

Each page is a normal HTML file. The content sits between `<article ...>` and `</article>`.

## After editing

Run `python3 tools/build_search.py` to refresh the site search, then commit and push.
The site updates about a minute after the push.

## Adding a page

Copy an existing page, change the title and content, and add a link in `assets/site.js` (menu) or in another page.
