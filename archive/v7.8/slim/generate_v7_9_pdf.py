#!/usr/bin/env python3
"""Generate metatime_paper_v7_9.pdf from HTML using WeasyPrint (v7.9)."""
import weasyprint

weasyprint.HTML(filename='metatime_paper_v7_9.html').write_pdf('metatime_paper_v7_9.pdf')

print("-> metatime_paper_v7_9.pdf")
