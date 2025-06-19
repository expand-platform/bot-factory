from dataclasses import dataclass

DOMAIN = "https://expand-platform.notion.site/"

@dataclass
class NotionPages:
    """ index """
    home: str = DOMAIN
    about: str = f"{DOMAIN}about-platform"
    prices: str = f"{DOMAIN}prices"
    
    """ coding languages """
    html_css: str = f"{DOMAIN}html-css"
    javascript: str = f"{DOMAIN}javascript"
    python: str = f"{DOMAIN}python"
    php: str = f"{DOMAIN}php"
    vue: str = f"{DOMAIN}vue"
    node_js: str = f"{DOMAIN}node-js"
    full_stack: str = f"{DOMAIN}full-stack"
    
    """ tasks & projects """
    tasks: str = f"{DOMAIN}tasks"
    projects: str = f"{DOMAIN}project"
    

NOTION_PAGE = NotionPages()


