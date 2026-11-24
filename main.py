import argparse

import pdftoimage
import detect
import extract_cau

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a multiple-choice exam PDF into one image per question.")
    parser.add_argument("file", nargs="?", default="dethi/dethi1",
                        help="PDF path without the .pdf extension; output images "
                             "are written to a folder with this name (default: dethi/dethi1)")
    parser.add_argument("--num-pages", type=int, default=7,
                        help="number of question pages to process; pages after this "
                             "(e.g. the answer key) are ignored (default: 7)")
    # Tạo đường dẫn tới poppler (path to the poppler "bin" folder)
    parser.add_argument("--poppler-path", default=None,
                        help="folder containing pdftoppm; only needed if poppler is "
                             "not on PATH (e.g. on Windows)")
    args = parser.parse_args()

    file = args.file
    pdftoimage.creat_image(file=file, poppler_path=args.poppler_path)
    y1, y2, column = extract_cau.extract_cau_(file)
    pdftoimage.creat_image_full(file=file, num_pages=args.num_pages, y1=y1, y2=y2, column=column)
    detect.detect_cau(file, column=column)
