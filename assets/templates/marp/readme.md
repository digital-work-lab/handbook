To create slides, run:

```
docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=$LANG -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli slides.md --theme-set theme.css --html --allow-local-files

# instead of marp-pdf export: print the PDF from the browser (html)
# instead of pptx export: export to PDF/via Adobe to pptx (and add the background)
# docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=$LANG -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli slides.md  --theme-set theme.css --pdf --allow-local-files
```