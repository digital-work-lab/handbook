---
layout: default
title: OCR
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# OCR

## Single PDF

Replace the `filename.pdf`:

```
in="filename.pdf"
tmp="${in%.pdf}_ocr.pdf"

docker run --rm -u $(id -u):$(id -g) \
  -v "$(pwd)":/mnt jbarlow83/ocrmypdf \
  --language eng+deu \
  "/mnt/$in" "/mnt/$tmp"
```

## PDF Batches

To OCR all PDFs in a folder using Docker and [`ocrmypdf`](https://github.com/ocrmypdf/OCRmyPDF){: target="_blank"}:

1. Place your input files in a `pdfs/` directory.
2. Run the following shell script to OCR each file using English and German (`eng+deu`) language support:

```
#!/bin/bash

# Directory containing PDFs
PDF_DIR="./pdfs"
# Output directory
OUTPUT_DIR="./ocr_output"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over all PDF files in the directory
for pdf_file in "$PDF_DIR"/*.pdf; do
    # Get the base filename (without path)
    base_name=$(basename "$pdf_file")
    output_file="$OUTPUT_DIR/$base_name"

    echo "Processing: $pdf_file"
    
    docker run --rm -u $(id -u):$(id -g) \
        -v "$(pwd)":/mnt jbarlow83/ocrmypdf \
        --language eng+deu \
        "/mnt/${pdf_file}" "/mnt/${output_file}"

    echo "Saved OCR'd file to: $output_file"
done
```
