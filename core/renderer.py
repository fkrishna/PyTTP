class Renderer:

    """ HTML RENDERER """
    
    auxmeta = '''
        <style>
            body {
                width:100%;margin:0 auto;
            }
            .mui-col-md-6, iframe { 
                width:100%; 
            }
            .tutorial-content {
                margin-top:60px;padding:15px
            }
        </style>
    '''

    @classmethod
    def render(cls, document):
        return f'''
        <html>
            <head>
                { cls.auxmeta }
            </head>
            <body>
                <div>{ document.table_contents }</div>
                <div>{ ''.join(Renderer.__div_wrapper(document.contents)) }</div>
            </body>
        </html>
        '''

    @staticmethod
    def __div_wrapper(contents = []):
        divs = []
        for content in contents:
            divs.append(f'<div>{content}</div>')
        return divs

