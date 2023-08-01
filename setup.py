from cx_Freeze import setup, Executable

settings = Executable( 
    script='app.py',
    icon='assets\\instagram.ico'
)

setup( 
    name='Bot de Curtidas no Instagram',
    version='2.0',
    description='Monitore cada nova postagem de uma página.',
    author='Jonatas Lopes de Sousa',
    options={'build_exe':{
        'include_msvcr': True
    }}, 
    executables=[settings]),
    