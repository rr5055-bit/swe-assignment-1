# Site-wide template values (footer owner and year)
from datetime import date

from .loader import load_cv


def site_wide(request):
    return {
        "site_owner": load_cv()["header"]["name"],
        "current_year": date.today().year,
    }
