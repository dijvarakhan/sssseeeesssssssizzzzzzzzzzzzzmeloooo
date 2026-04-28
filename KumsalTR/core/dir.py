# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of KumsalTR


import shutil
from pathlib import Path

from KumsalTR import logger


def ensure_dirs():
    """
    Ensure that the necessary directories exist.
    """
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is not installed or not in the system PATH. It is required for media processing.")
    
    if not shutil.which("deno"):
        logger.warning("Deno is not installed. Some YouTube extractors may not work correctly, but the bot will attempt to start.")

    for dir in ["cache", "downloads", "KumsalTR/cookies"]:
        Path(dir).mkdir(parents=True, exist_ok=True)
    logger.info("Cache directories updated.")
