# Past Jobs photo uploads

Upload JPG, JPEG, PNG, WebP, AVIF or GIF files into this folder using GitHub's **Add file → Upload files**. You can select multiple files at once.

After you commit, GitHub Actions generates `public/past-jobs-gallery.json` and commits it automatically. Your hosting provider redeploys from `main` if connected to this repository. New images appear at the top. Images uploaded together are ordered by filename (descending). Removing an image removes it from the gallery on the next successful update.

For best results use descriptive filenames, e.g. `2026-10-30-backyard-tree-removal.jpg`. The filename is used as the photo caption.

Do not edit `past-jobs-gallery.json` manually. Check the **Actions** tab if photos do not appear.
