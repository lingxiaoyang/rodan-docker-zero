from mirrored_rodan_settings import *  # noqa


TEST_JOB_PACKAGES = [
    "rodan.jobs.helloworld",
]

# Run Celery task synchronously, instead of sending into queue
CELERY_ALWAYS_EAGER = True
# Propagate exceptions in synchronous task running by default
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# We won't install gm or kdu_compress in dev environment
ENABLE_DIVA = False


# STOP: don't edit further
##############################

# Append TEST_JOB_PACKAGES to RODAN_JOB_PACKAGES
for job_package in TEST_JOB_PACKAGES:
    if job_package not in RODAN_JOB_PACKAGES:
        RODAN_JOB_PACKAGES.append(job_package)

# Monkey-patch django.setup() so that we won't run into hanging issues with
# the setup() call in rodan/__init__.py => rodan/celery.py
import django  # noqa
import traceback  # noqa

_orig_django_setup = django.setup


def _setup_except_celery(*a, **k):
    """monkey-patch"""
    stack = traceback.extract_stack()
    if len(stack) >= 2 and stack[-2][0] == '/srv/Rodan/rodan/celery.py':
        print("MONKEY-PATCH: called from rodan/celery.py, do nothing")
        return None
    else:
        return _orig_django_setup(*a, **k)


# Avoid monkey-patching more than once
if django.setup.__doc__ != 'monkey-patch':
    django.setup = _setup_except_celery
