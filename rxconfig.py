import reflex as rx

config = rx.Config(
    app_name="E_Learning_JCB_Reflex",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)