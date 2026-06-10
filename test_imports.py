import os
import sys

def test_imports():
    modules = [
        "config",
        "database.mongo",
        "database.models",
        "database.redis_db",
        "core.downloader",
        "core.call",
        "core.queue",
        "core.thumbnail",
        "core.decorators",
        "handlers.start",
        "handlers.help",
        "handlers.play",
        "handlers.controls",
        "handlers.queue_handler",
        "handlers.settings",
        "handlers.group_tools",
        "handlers.admin",
        "handlers.owner_panel",
        "handlers.broadcast",
        "handlers.clone",
        "handlers.callbacks",
        "utils.logger",
        "utils.formatter",
        "utils.startup_check",
    ]

    for module in modules:
        try:
            __import__(module)
            print(f"✅ Successfully imported {module}")
        except Exception as e:
            print(f"❌ Failed to import {module}: {e}")

if __name__ == "__main__":
    test_imports()
