from main import main


def test1_main() -> None:
    main()
    with open(r"./output/test1.drt", "r") as file:
        file_content_output: str = file.read()
    with open("./target/test1.drt", "r") as file:
        file_content_target: str = file.read()

    assert file_content_output == file_content_target


def test2_main() -> None:
    main()
    with open(r"./output/test2.drt", "r") as file:
        file_content_output: str = file.read()
    with open("./target/test2.drt", "r") as file:
        file_content_target: str = file.read()

    assert file_content_output == file_content_target


def test3_main() -> None:
    main()
    with open("./target/test3.drv", "r") as file:
        file_content_target: str = file.read()

    assert "BLANK\n" == file_content_target
