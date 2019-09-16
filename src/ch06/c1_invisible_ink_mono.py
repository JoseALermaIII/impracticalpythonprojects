"""Use stenography to hide messages in a word processor document.

Use :py:obj:`docx.Document` to hide encrypted messages in a word processor
document by embedding the encrypted message in a fake message's whitespace,
then changing the encrypted message's font color to white.

Note:
    Using LibreOffice version 6.0.7.3

Warning:
    There are many ways this method of stenography can fail. Please don't use
    for actual covert operations (covered in MIT License).

"""
import docx
from docx.shared import RGBColor

from src.ch06.p1_invisible_ink import get_text


def check_fit(plaintext: list, ciphertext: list) -> int:
    """Check if ciphertext can fit in plaintext's whitespace.

    Sum number of blanks in **plaintext** and compare to number of characters
    in **ciphertext** to see if it can fit.

    Args:
        plaintext (list): Paragraphs of a fake message in a list of strings
            (likely from :func:`get_text`).
        ciphertext (list): Paragraphs of an encrypted message in a list of
            strings (likely from :func:`get_text`).

    Returns:
        Integer representing the number of needed blanks to fit
        **ciphertext** in **plaintext**. ``0`` would mean that **ciphertext**
        can fit in **plaintext**.

    Note:
        To separate words, the blanks in **ciphertext** count toward the
        needed length of **plaintext**. By contrast, blank lines in
        **plaintext** do not count.

    """
    blanks = sum(line.count(' ') for line in plaintext if line != '')
    letters = sum(len(line) for line in ciphertext if line != '')
    if blanks >= letters:
        return 0
    return letters - blanks


def write_invisible(plaintext: list, ciphertext: list,
                    template_path: str = None,
                    filename: str = 'output.docx') -> None:
    """Embed ciphertext in plaintext's letter whitespace.

    Open a template file, **template_path**, with the needed fonts, styles,
    and margins. Write each line in **plaintext** to the template file
    and add each line in **ciphertext** to **plaintext**'s space between
    letters by using a monospace font.
    Save the new file as **filename**.

    Args:
        plaintext (list): Lines of a fake message in a list of strings
            (likely from :func:`get_text`).
        ciphertext (list): Lines of an encrypted message in a list of
            strings (likely from :func:`get_text`).
        template_path (str): Absolute path to .docx file with predefined
            fonts, styles, and margins. Defaults to :py:obj:`None`. If not
            provided, defaults will be created.
        filename (str): File name to use for output file. Defaults to
            ``output.docx``.

    Returns:
        :py:obj:`None`. **plaintext** is written to the file at
        **template_path** with **ciphertext** embedded in the blank space.

    Raises:
        ValueError: If the number of spaces in **plaintext** aren't
            enough to embed **ciphertext** based on output of
            :func:`check_fit`.

    Note:
        As of python-docx v0.8.10, creating custom styles isn't well
        supported. More info `here`_.

        As a result, if a template isn't provided, the default template is
        modified to use a font named ``Courier New`` on Windows and
        ``Liberation Mono`` on other operating systems in the ``Normal``
        style.

    .. _here:
        https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html

    """


def main():
    """Demonstrate the invisible ink writer."""


if __name__ == '__main__':
    main()
