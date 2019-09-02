class Renderer:

    """ HTML RENDERER """

    @staticmethod
    def render(document = ''):

        add_styles = '''
            <style>
                body {
                    width:100%; margin:0 auto;
                }
                .mui-col-md-6, iframe { 
                    width: 100%; 
                }
            </style>
        '''

        return f'''
        <html>
            <head>
                { document.head }
                { add_styles }
            </head>
            <body>
                <div>{ document.table_contents }</div>
                <div>{ ''.join(document.contents) }</div>
            </body>
        </html>
        '''

    

                
