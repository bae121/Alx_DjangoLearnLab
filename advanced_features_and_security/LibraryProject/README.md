# 🔐 Permissions and Groups Setup

## Custom Permissions
Defined in `Article` model:
- `can_view`: View articles
- `can_create`: Create articles
- `can_edit`: Edit articles
- `can_delete`: Delete articles

## Groups
Configured via Django Admin:
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Views
Each view is protected using `@permission_required` decorators to enforce access control.

## Testing
Create users and assign them to groups. Log in and verify access to each view.

# Django Security Measures

## Configured Settings
- `DEBUG=False`: Prevents sensitive error info from being exposed.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Enforce HTTPS-only cookies.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`: Add browser-level protections.
- `SECURE_HSTS_*`: Enforce HTTPS with HSTS.

## CSRF Protection
All forms include `{% csrf_token %}` to prevent CSRF attacks.

## SQL Injection Prevention
User input is validated using Django forms and ORM filters are used instead of raw SQL.

## Content Security Policy
Configured using `django-csp` to limit external content sources and mitigate XSS.

## Testing
- Manually tested form submissions with and without CSRF tokens.
- Verified that invalid input is rejected.
- Confirmed that CSP headers are present in HTTP responses.
