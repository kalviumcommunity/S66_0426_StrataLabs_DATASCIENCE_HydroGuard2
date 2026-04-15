"""DataFrame inspection helpers using head, info, and describe patterns."""

from __future__ import annotations

from io import StringIO

import pandas as pd


def inspection_snapshot(df: pd.DataFrame) -> dict[str, object]:
    info_buffer = StringIO()
    df.info(buf=info_buffer)
    return {
        "head": df.head().to_dict(orient="records"),
        "info": info_buffer.getvalue().strip(),
        "describe": df.describe(include="all").fillna("").to_dict(),
    }
