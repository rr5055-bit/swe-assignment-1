# Views that render the full CV page or a single section partial
from django.http import Http404
from django.shortcuts import render

from .loader import load_cv


def cv_view(request):
    return render(request, "cv_assignment/cv.html", {"cv": load_cv()})


def section_view(request, name):
    cv = load_cv()
    if name not in cv["sections"]:
        raise Http404(f"Unknown section: {name}")
    return render(request, f"cv_assignment/cv.html#{name}_section", {"cv": cv})
