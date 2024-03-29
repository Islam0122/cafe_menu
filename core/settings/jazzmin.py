JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel",
    "site_header": "Admin Panel",
    "site_brand": "Admin Panel",
    "site_logo_classes": "Admin Panel",
    "welcome_sign": "Добро пожаловать в панель администратора  Admin Panel!",
    "copyright": "IntermetalPlus",
    # "search_model": "src.services",
    "topmenu_links": [
        {"name": "Админ панель", "url": "http://127.0.0.1:8000/admin/", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"name": "О нас", "url": "/admin/About_us/"},
        {"name": "Контакт", "url": "/admin/Contact/"},

    ],
    "usermenu_links": [

    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": ['auth.group'],
    "icons": {
        # src icons

    },

    "order_with_respect_to": [

            ],

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-thumbtack",
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-warning",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": False,
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"

    },

    "actions_sticky_top": False
}
