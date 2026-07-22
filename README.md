# EdMo Grows — consultancy website

One-page site, no build step. `index.html` is the whole thing — all styles are inlined in the `<style>` block in its `<head>`, so the file renders correctly however you open it.

## Photos & videos

Web-ready copies live in `images/` (resized JPEGs) and `videos/` (compressed MP4s) — these are what the site uses. The original folders (`Me (Ed)`, `Q Homes`, `Festivals Speaker Slots`) are untouched source material and aren't referenced by the site.

Still using placeholder boxes (swap in a photo when you have one):
- **I Feel Good Pilates Club** — a screenshot of the site or a studio shot
- **Cob Courses** — a build-in-progress or course photo

To add a new photo: convert/resize it first (`sips -s format jpeg -s formatOptions 80 --resampleHeightWidthMax 1600 in.heic --out images/name.jpg`), then reference it in `index.html`.

## Editing content

- All copy lives in `index.html` — it's plain text, just edit and save.
- Colours and fonts are defined near the top of the `<style>` block under `:root`.

## Previewing locally

```sh
python3 -m http.server 4173
```
Then open http://localhost:4173

## Going live (free options)

- **Netlify Drop** — drag the folder onto https://app.netlify.com/drop
- **Cloudflare Pages** or **GitHub Pages** — connect this git repo, no build command needed.

Then point your domain (e.g. edmogrows.com) at it from your registrar.
