#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py collectstatic --noinput --verbosity 0
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='$DEFAULT_EMAIL').exists() or  User.objects.create_superuser('$DEFAULT_EMAIL', '$DEFAULT_PASS')"
python manage.py runserver_plus 0.0.0.0:8000
