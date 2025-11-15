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
