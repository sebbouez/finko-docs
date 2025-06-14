import re

import re

def define_env(env):

    def on_page_markdown(markdown, page, config, **kwargs):
        # Rechercher toutes les balises <!-- md:version v="..." -->
        def replace_note(match):
            # Extraire le contenu de l'attribut text
            text = match.group(1)
            return f'<div><a class="note-apply-version" href="/finko-docs/updates/{text}/">Applies to {text}</a></div>'
    
        # Remplace toutes les balises personnalisées
        markdown = re.sub(r'<!--\s*md:version\s+v="([^"]+)"\s*-->', replace_note, markdown)
    
        return markdown

    env.on_page_markdown(on_page_markdown, page, config)
