def test_core_imports():
    """Smoke test: importa as dependências principais usadas nas demos.

    Se esse teste falhar, o CI deve reportar quais pacotes não foram importados.
    """
    import importlib

    pkgs = ["streamlit", "pandas", "numpy", "altair", "pydeck"]
    missing = []
    for p in pkgs:
        try:
            importlib.import_module(p)
        except Exception as e:
            missing.append(f"{p}: {e}")

    assert not missing, "Missing or failing imports: " + "; ".join(missing)
