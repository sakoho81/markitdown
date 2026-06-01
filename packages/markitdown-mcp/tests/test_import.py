def test_import():
    import markitdown_mcp  # noqa: F401
    from markitdown_mcp import __version__

    assert __version__
