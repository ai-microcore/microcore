from microcore.config import Config


def test_config(monkeypatch):
    monkeypatch.setenv("PROMPT_TEMPLATES_PATH", "mypath")
    assert Config().PROMPT_TEMPLATES_PATH == "mypath"
    monkeypatch.delenv("PROMPT_TEMPLATES_PATH", raising=False)
    assert Config().PROMPT_TEMPLATES_PATH == "tpl"
