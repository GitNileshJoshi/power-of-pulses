# Deploying Power of Pulses with Google Sites

## Recommended architecture
Google Sites is the public shell. Host this folder as a static site with GitHub Pages, Cloudflare Pages, or Firebase Hosting, then embed the published URL in Google Sites using **Insert > Embed > By URL**. This preserves search, filtering, local meal-planning, and calendar export.

## Publish with GitHub Pages
1. Create a repository named `power-of-pulses`.
2. Upload everything in this folder.
3. In **Settings > Pages**, choose **Deploy from a branch**, `main`, `/root`.
4. Copy the published URL.
5. In Google Sites choose **Insert > Embed**, paste the URL, and resize the embed.

## Add or edit recipes
- Edit `recipes.json` and the embedded `baseRecipes` data in `index.html`, then republish.
- The easiest no-code workflow is to maintain `recipes.csv` in Google Sheets, export it as CSV, and run the included `update_from_csv.py` script before publishing.
- New image files belong in `assets/recipes/`. Use WebP or JPG, ideally under 250 KB each.

## Calendar and privacy
The meal planner stores preparation date, made date, and notes only in the visitor's browser using localStorage. **Add to calendar** downloads an `.ics` event that works with Google Calendar, Outlook, and Apple Calendar. No personal data is sent to a server.

## Important
The recipe pages are preserved as images from the supplied PDF. Verify accessibility text and recipe details before public release. Keep the source/funding disclaimer visible on the Google Sites home page.
