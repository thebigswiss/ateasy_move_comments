import logging
import os
import re

logger: logging.Logger = logging.getLogger(__name__)


def main() -> None:
    file_content: str

    for file_name in os.listdir(r"./input/"):
        if not file_name.endswith(r".drt"):
            logger.info(f"file {file_name} was not converted")
            continue

        with open(f"input/{file_name}", "r") as file:
            file_content = file.read()
        # Use regex101.com, or trust me.
        # TODO: when no var are present, is the { indented. This should be removed
        regex: str = r"(?:-*)(?P<values>(?:(?:\t.*)\n)*(?:{\n))(?P<comment>(?:\t!-+\n)((?:\t!.*)\n)+(?:\t!-+))"
        subst: str = r"\g<comment>\n\g<values>"
        file_content = re.sub(regex, subst, file_content, 0, re.MULTILINE)

        regex: str = r"(!-+\n\t?)"
        subst: str = ""
        file_content = re.sub(regex, subst, file_content, 0, re.MULTILINE)

        with open(f"./output/{file_name}", "w") as file:
            file.write(file_content)
            logger.info(f"file {file_name} was converted and saved in output/")


if __name__ == "__main__":
    main()
