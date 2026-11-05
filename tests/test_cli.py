from ecotrack.cli import main


def test_cli_prints_summary(tmp_path, capsys):
    csv_file = tmp_path / "laps.csv"
    csv_file.write_text("lap,time_s\n1,80.00\n2,70.50\n")

    assert main([str(csv_file)]) == 0

    out = capsys.readouterr().out
    assert "Best lap:     1:10.50" in out


def test_cli_without_file_shows_usage(capsys):
    assert main([]) == 1
    assert "Usage" in capsys.readouterr().out
